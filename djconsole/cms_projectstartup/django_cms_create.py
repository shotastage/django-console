import os

from djconsole.flow import Flow

from os import getcwd, chdir, path
from djconsole.command import log, command
from shutil import move
from djconsole.cms_projectstartup.readme import create_readme_doc



class DjangoCMSStartupFlow(Flow):

    def __init__(self, name = None):
        self._project_name = name

    def flow(self):

        if self._project_name == None:
            log("Please type your new Django CMS application name.")
            self._project_name = log("Django CMS name", withInput = True)

        try:
            self._check(self._project_name)
        except:
            log("Project {0} is already exists.".format(self._project_name), withError = True)

        
        self._create_new_django_app(self._project_name)

        current = getcwd()
        chdir("./" + self._project_name)
        self._create_template_git_project(self._project_name)
        self._create_docs(self._project_name)
        chdir("../")


    def _create_new_django_app(self, name):
        log("Creating Django CMS application...")
        log("Please wait for a moment.")
        command("djangocms " + name)


    def _create_template_git_project(self, name):
        command("curl -O https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore")
        move("Python.gitignore", ".gitignore")
        command("git init")

    def _create_docs(self, name):
        with open("README.md", "a") as readme:
            readme.write(create_readme_doc(name))


    def _check(self, name):
        if path.exists(name):
            raise FileExistsError