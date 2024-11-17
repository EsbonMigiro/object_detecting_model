from .dir_creator import ProjectDirectoryManager
import os
import shutil
import tarfile
import urllib.request

def unzip_handler():
        
    if os.name == 'posix':
        # Download the pretrained model
        urllib.request.urlretrieve(ProjectDirectoryManager.PRETRAINED_MODEL_URL, ProjectDirectoryManager.PRETRAINED_MODEL_NAME+'.tar.gz')

        # Move the downloaded file
        shutil.move(ProjectDirectoryManager.PRETRAINED_MODEL_NAME+'.tar.gz', os.path.join(ProjectDirectoryManager.paths['PRETRAINED_MODEL_PATH'], ProjectDirectoryManager.PRETRAINED_MODEL_NAME+'.tar.gz'))

        # Extract the tar.gz file
        with tarfile.open(os.path.join(ProjectDirectoryManager.paths['PRETRAINED_MODEL_PATH'], ProjectDirectoryManager.PRETRAINED_MODEL_NAME+'.tar.gz'), 'r:gz') as tar:
            tar.extractall(path=ProjectDirectoryManager.paths['PRETRAINED_MODEL_PATH'])
