#!/usr/bin/python3
# Fabfiles.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Darcves.

    Args:
        number (int): Theep.

    etc.
    """
    x = 1 if int(x) == 0 else int(x)

    s = sorted(os.listdir("versions"))
    [s.pop() for f in range(x)]
    with lcd("versions"):
        [local("rm ./{}".format(t)) for t in s]

    with cd("/data/web_static/releases"):
        s = run("ls -tr").split()
        s = [t for t in s if "web_static_" in t]
        [s.pop() for f in range(x)]
        [run("rm -rf ./{}".format(t)) for t in s]
