from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

name = "weather"
default_task = "publish"


@init
def set_project_properties(project):
    project.depends_on('requests')
    project.depends_on('xmltodict')
