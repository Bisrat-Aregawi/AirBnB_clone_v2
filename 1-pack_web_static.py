#!/usr/bin/python3
"""Directory packer fabric module"""
from fabric.api import local


def do_pack():
    """Pack `web_static` directory to .tgz inside versions.

    Returns:
        path of archive <class 'str'>, None <class 'NoneType'>
    """
    try:
        timestamp = local("date +%Y%m%d%H%M%S", capture=True)
        local("mkdir -p versions;", capture=True)
        local(
            "tar -cvzf versions/web_static_{}.tgz web_static"
            .format(timestamp)
        )
        return 'versions/{}'.format(timestamp)
    except Exception:
        return None
