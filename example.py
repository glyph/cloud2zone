# Licensed to Tomaz Muraus under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# Tomaz muraus licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sys import argv
from getpass import getpass

from libcloud.dns.providers import get_driver as get_dns_driver
from libcloud.dns.base import DNSDriver
from libcloud.common.types import InvalidCredsError

from keyring import get_password, set_password
from cloud2zone import libcloud_zone_to_bind_zone_file


def get_authenticated_driver(driver_name: str, account_name: str) -> DNSDriver:
    secret_site = "libcloud/" + driver_name
    cls = get_dns_driver(driver_name)
    pw = get_password(secret_site, account_name)
    askuser = lambda prefix="": getpass(
        "{prefix}API key for {driver_name}/{account_name}:"
        .format(prefix=prefix, driver_name=driver_name,
                account_name=account_name)
    )

    if not pw:
        pw = askuser()

    while True:
        try:
            dns = cls(account_name, pw)
        except InvalidCredsError:
            pw = askuser("API key invalid; ")
        else:
            set_password(secret_site, account_name, pw)
            return dns


driver_name, account_name, domain_name = argv[1:3]  # todo: use click
driver = get_authenticated_driver(driver_name, account_name)

zones = driver.list_zones()
zone = next(z for z in zones if z.domain == domain_name)

result = libcloud_zone_to_bind_zone_file(zone=zone)
print(result)
