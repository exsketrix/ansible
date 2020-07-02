import json
from urllib import request
from distutils.version import LooseVersion
import re

strictversion_regex = re.compile('^\\d+\\.\\d+\\.\\d+$')
strict_versions = []


def latest_version(package_name):
    url = "https://pypi.python.org/pypi/%s/json" % (package_name,)
    data = json.load(request.urlopen(request.Request(url)))
    versions = data["releases"].keys()
    for v in versions:
        if (strictversion_regex.match(v)):
            strict_versions.append(v)
    return sorted(strict_versions, key=LooseVersion)[-1]


print(latest_version("ansible"), end='')
