#!/usr/bin/python3
# le tocreatanserv.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]

def dp():
    """rec."""
    xs = datetime.utcnow()
    d = "versions/web_static_{}{}{}{}{}{}.tgz".format(xs.year,
                                                         xs.month,
                                                         xs.day,
                                                         xs.hour,
                                                         xs.minute,
                                                         xs.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(d)).failed is True:
        return None
    return d


def dd(b):
    """iivese.

    Args: archive_path (str): hestrbut.
    Returns: If.
    """
    if os.path.isfile(b) is False:
        return False
    d = b.split("/")[-1]
    c = d.split(".")[0]

    if put(b, "/tmp/{}".format(d)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(c)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(c)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(d, c)).failed is True:
        return False
    if run("rm /tmp/{}".format(d)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(c, c)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(c)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(c)).failed is True:
        return False
    return True


def deploy():
    """ateserve."""
    d = dp()
    if d is None:
        return False
    return dd(d)
