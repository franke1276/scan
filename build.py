from pybuilder.core import init, use_plugin, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("copy_resources")

name = "PyBarCodeScan"

authors = [Author('Christian Franke', 'chriss@frankeonline.net')]
description = "Scan tool"
license = 'APACHE LICENSE, VERSION 2.0'
summary = 'Scan tool'
url = 'https://github.com/cfranke/scan'
version = '0.0.13'

default_task = ['clean', 'package']


@init
def initialize(project):
  project.build_depends_on('mockito')
  project.depends_on("httplib2")
  project.depends_on("Flask")
  project.depends_on("gunicorn")
  project.depends_on("gevent")
  project.depends_on("flask-sse")
  project._package_data.setdefault('barcodescan', []).append('templates/*')
  project.install_file('/etc/systemd/system/', 'barcodescan/barcodescan_sse.service')
  project.install_file('/etc/systemd/system/', 'barcodescan/read_from_scanner.service')