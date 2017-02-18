from pybuilder.core import init, use_plugin, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "scan"

authors = [Author('Christian Franke', 'chriss@frankeonline.net')]
description = "Scan tool"
license = 'APACHE LICENSE, VERSION 2.0'
summary = 'Scan tool'
url = 'https://github.com/cfranke/scan'
version = '0.0.1'

default_task = ['clean', 'package']


@init
def initialize(project):
  project.build_depends_on('mockito')
  project.depends_on("httplib2")
