#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.26.57.162', '100.26.120.217']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""

    # Check if the archive exists
    if exists(archive_path) is False:
        return False

    try:
        # Extract necessary information from the archive path
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the server
        put(archive_path, '/tmp/')

        # Create directory for the extracted files
        run('mkdir -p {}{}/'.format(path, no_extension))

        # Extract the archive into the directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(file_name))

        # Move the contents of the extracted directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))

        # Remove the web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_extension))

        # Update the symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))

        return True
    except:
        return False
