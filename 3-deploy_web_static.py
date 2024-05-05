#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers

execute: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

# Define the list of hosts
env.hosts = ['100.26.57.162', '100.26.120.217']


def do_pack():
    """Generates a tgz archive"""
    try:
        # Get the current date and time
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Create a 'versions' directory if it doesn't exist
        if isdir("versions") is False:
            local("mkdir versions")
        
        # Define the file name for the archive
        file_name = "versions/web_static_{}.tgz".format(date)
        
        # Create the tgz archive
        local("tar -cvzf {} web_static".format(file_name))
        
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        # Extract necessary information from the archive path
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        
        # Upload the archive to /tmp/ on the remote server
        put(archive_path, '/tmp/')
        
        # Create necessary directory structure and extract the archive
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        
        # Clean up by removing the uploaded archive
        run('rm /tmp/{}'.format(file_n))
        
        # Move the extracted files to the correct location
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        
        # Remove the empty web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        
        # Update the symbolic link to the new release
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

