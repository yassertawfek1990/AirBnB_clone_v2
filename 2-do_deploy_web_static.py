#!/usr/bin/python3
# bfiler.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ['54.89.109.87', '100.25.190.21']


def do_deploy(archive_path):
    """Dist.

    Args:
        archive_path (str): Th
    Returns:
        If
    """
    if os.path.isfile(archive_path) is False:
        return False
    a = archive_path.split("/")[-1]
    c = a.split(".")[0]

    if put(archive_path, "/tmp/{}".format(a)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(c)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(c)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(a, c)).failed is True:
        return False
    if run("rm /tmp/{}".format(a)).failed is True:
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
