# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import platform
import sys
import textwrap

from pip.utils import get_installed_distributions
from mirage.command import log


def create_readme_doc(name):

    return textwrap.dedent(
'''
# {name}

This is your first Django application.

# Info
Information of development environment.

## Environment
OS: {os}

## Versions
Django Version: `{django_version}`

Python Version: `{python_version}`

## Installed pip packages
{installed_pip_packages}

''').format(
    name = name,
    os = get_os_name(),
    django_version = get_django_version(),
    python_version = get_python_version(),
    installed_pip_packages = get_pip_list()
).strip()


def get_django_version():
    try:
        import django
        version = django.VERSION
        return str(version[0]) + "." + str(version[1]) + "." + str(version[2])
    except:
        log("Failed to import Django!", withError = True)
        return "FAILED TO IMPORT DJANGO!"


def get_python_version():
    version = sys.version_info
    return str(version[0]) + "." + str(version[1]) + "." + str(version[2])


def get_os_name():
    os = platform.system()

    if os == "Darwin":
        return "macOS"
    elif os == "Windows":
        return os
    else:
        return os


def get_pip_list():
    string = ""

    ignore_packages = ["setuptools", "pip", "python", "mirage"]
    
    packages = get_installed_distributions(local_only = True, skip = ignore_packages)
    
    for package in packages:
        string += "+ " + package.project_name + " " + package.version + "  \n"

    return string