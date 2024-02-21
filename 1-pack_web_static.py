#!/usr/bin/python3
# afiletic.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
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
