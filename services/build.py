
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "services"
default_task = "publish"


@init
def set_project_properties(project):
    project.set_property("verbose", True)
