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

import datetime

from libcloud import __version__ as libcloud_version
from libcloud.dns.types import RecordType

from libcloud_to_bind.utils import get_record_id

__version__ = "0.1.0"
__all__ = ["__version__", "libcloud_zone_to_bind_zone_file"]


def libcloud_zone_to_bind_zone_file(zone) -> str:
    if zone.type != "master":
        raise ValueError("You can only generate BIND file for master zones")
    return "\n".join(
        [
            f"; Generated by Libcloud v{libcloud_version} on {datetime.datetime.now().isoformat()}",
            f"$ORIGIN {zone.domain}.",
            f"$TTL {zone.ttl}",
            "",
        ]
        + [
            " ".join(
                [
                    record.name or "@",
                    str(
                        record.extra["ttl"]
                        if "ttl" in record.extra
                        else record.zone.ttl
                    ),
                    "IN",
                    record.type,
                    *(
                        [str(record.extra["priority"])]
                        if record.type in [RecordType.MX, RecordType.SRV]
                        else ()
                    ),
                    '"' + it.replace('"', '\\"') + '"'
                    if (
                        (
                            " "
                            in (
                                it := (
                                    record.data
                                    + (
                                        "."
                                        if record.type
                                        in [
                                            RecordType.CNAME,
                                            RecordType.DNAME,
                                            RecordType.MX,
                                            RecordType.PTR,
                                            RecordType.SRV,
                                        ]
                                        and not record.data.endswith(".")
                                        else ""
                                    )
                                )
                            )
                        )
                        and record.type in [RecordType.TXT, RecordType.SPF]
                    )
                    else it
                ]
            )
            for record in sorted(zone.list_records(), key=get_record_id)
            # filter out apex NS records
            if not ((not record.name) and (record.type == RecordType.NS))
        ]
    )
