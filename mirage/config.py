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

import os
import yaml


def get_all_config():
    return load_miragefile()


def get_proj_config(conf_name):

    try:
        data = load_miragefile()

        if os.path.exists("Miragefile.addon"): additional = load_additional_conf()
        elif os.path.exists("Miragefile.secret"):   secret = load_secret_conf()
    except:
        return "Invalid Miragefile"

    if conf_name == "all":
        return data

    elif conf_name == "name":
        return data["project"]["name"]

    elif conf_name == "version":
        return data["project"]["version"]

    elif conf_name == "author":
        return data["project"]["author"]

    elif conf_name == "git":
        return data["project"]["git"]

    elif conf_name == "license":
        return data["project"]["license"]

    elif conf_name == "description":
        return data["project"]["description"]
        
    elif conf_name == "iyashi":
        try:
            return additional["additional_options"]["iyashi"]
        except:
            return False



def get_django_config(conf_name):

    try:
        data = load_miragefile()
    except:
        return "Invalid Miragefile"

    if conf_name == "path":
        if data["django"]["path"] == ".": return os.getcwd()
        else: return data["django"]["path"]

    elif conf_name == "package":
        return data["django"]["package"]

    elif conf_name == "database":
        return data["django"]["database"]




def get_node_config(conf_name):

    try:
        data = load_miragefile()
    except:
        return "Invalid Miragefile"

    if conf_name == "path":
        if data["frontend"]["path"] == ".": return os.getcwd()
        else: return data["frontend"]["path"]

    elif conf_name == "package":
        return data["frontend"]["package"]

    elif conf_name == "builder":
        return data["frontend"]["builder"]



def load_miragefile():
    with open("Miragefile", "r") as djfile:
        try:
            return yaml.load(djfile)
        except:
            raise Exception


def load_additional_conf():
    with open("Miragefile.addon", "r") as djfile:
        try:
            return yaml.load(djfile)
        except:
            raise Exception


def load_secret_conf():
    with open("Miragefile.secret", "r") as djfile:
        try:
            return yaml.load(djfile)
        except:
            raise Exception


"""
project:
    name: Sample Project
    version: 0.0.1
    author: Shota Shimazu
    git: https://github.com/shotastage/django-console.git
    license: restricted
    description: "This is template!"

    django:
        path: sample
        package: pipenv
        database: PostgreSQL

    frontend:
        path: shell
        package: yarn
        builder: webpack

    djworkspace:
        path: .mirage

    copyright:
        start_year: 2017
        copyrights:
            - Shota Shimazu
            - Aika Yamashita

clean:
    - rm -rf site/
    - rm -rf node_modules/

"""
