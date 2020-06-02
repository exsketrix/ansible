import json
from urllib import request
from distutils.version import LooseVersion


def latest_version(package_name):
    url = "https://pypi.python.org/pypi/%s/json" % (package_name,)
    data = json.load(request.urlopen(request.Request(url)))
    versions = data["releases"].keys()
    return sorted(versions, key=LooseVersion)[-1]
    return list(versions)[-1]


print(latest_version("ansible"), end='')
