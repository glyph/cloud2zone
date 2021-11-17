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

from setuptools import setup, find_packages


setup(
    name="cloud2zone",
    version="0.1.2",
    long_description=open("README.rst").read(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "apache-libcloud>=0.13.1",
        "keyring",
        "click",
    ],
    url="https://github.com/glyph/cloud2zone/",
    license="Apache License (2.0)",
    author="Tomaz Muraus",
    author_email="tomaz+pypi@tomaz.me",
    maintainer="Glyph Lefkowitz",
    maintainer_email="glyph@glyph.im",
    description="Python module which allows you to export Libcloud DNS "
    + "zone to the BIND zone file format",
    test_suite="tests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "console_scripts": [
            "cloud2zone = cloud2zone.cli:script",
        ],
    },
)
