import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from utilities.dir_creator import ProjectDirectoryManager
from utilities.tensorflow_installer import clone_tensorflow_models, install_tensorflow_object_detection
from utilities.other_tensorlow_installer import other_tensorflow_installer
from utilities.create_label_map import create_label_map


from utilities.update_config_transfer_learning import update_config_transfer_learning
from utilities.copy_model_config import copy_model_config_to_training_path
from utilities.clone_tf_record import generate_tf_records
from utilities.unzip_handler import unzip_handler
from utilities.detect import detect


def setup_tensorflow():
    ProjectDirectoryManager.create_project_directories()

    # clone_tensorflow_models()

    install_tensorflow_object_detection()


    # other_tensorflow_installer()

    #--------------unzip some files-------------
    # unzip_handler()


    #------------2. Create Label Map---------
    # create_label_map()

    #---------------clone tf-record---
    # generate_tf_records()

    #------------4. Copy Model Config to Training Folder
    # copy_model_config_to_training_path()

    #--------------5. Update Config For Transfer Learning---
    # update_config_transfer_learning()

    #-------------------------- detect---------------
    # detect()



if __name__ == "__main__":
    setup_tensorflow()