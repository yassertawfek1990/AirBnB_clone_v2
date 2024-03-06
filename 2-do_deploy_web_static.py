#!/usr/bin/python3
""" archive to the web servers """

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['<IP web-01>', 'IP web-02']


def do_deploy(archive_path):
    """d"""
    if exists(archive_path) is False:
        return False
    try:
        n = archive_path.split("/")[-1]
        t = n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, t))
        run('tar -xzf /tmp/{} -C {}{}/'.format(n, path, t))
        run('rm /tmp/{}'.format(n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, t))
        run('rm -rf {}{}/web_static'.format(path, t))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, t))
        return True
    except:
        return False
