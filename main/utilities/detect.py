from .detector import detector
import os
from .dir_creator import ProjectDirectoryManager


IMAGE_PATH = os.path.join(ProjectDirectoryManager.paths['IMAGE_PATH'], 'test', 'sample.png')
SAVE_PATH = os.path.join(ProjectDirectoryManager.paths['IMAGE_PATH'], 'test', 'detected_image.png')


def detect():
    detector(IMAGE_PATH, SAVE_PATH)