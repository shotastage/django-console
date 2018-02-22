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

from . import version

usage = """
Mirage v{0}

Usage:
    mi [action] option <--sub-option> <inputs>

    mi [action]:[subaction] option <--sub-option> <inputs>


Actions:
    newproject         new                      Create a new Django project.
    newproject:react   new:react                Create a new Django API project with React.js front-end.
    newproject:cms     new:cms                  Create a new Django CMS project. ( Django CMS is required. )
    backup             b            app         Backup exsiting app.
    configure          conf                     Generate miragefile or reconfig mirage.
    console            c                        Launch Django Python shell.
    console:db         c:db                     Launch databse shell.
    database:migrate   db:migrate               Make migrations and apply migrations.
    database:reset     db:reset                 Reset all database. ( Only debugging SQLite is supported. )
    generate           g            app         Create multiple Django apps at once.
    generate           g            model       Create Django model class.
    scaffold           ide                      Launch mirgae Web UI. (Now under development.)
    server             s                        Launch debugging server.
    file               f                        Create a new Python source file with copyrights doc string.

    help               h                        Show usage of Mirage.
    version            v                        Print version information.


""".format(version.text)

version = """
Mirage Version {0}

https://github.com/shotastage/django-mirage

Copyright (c) 2017-2018 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
""".format(version.text)