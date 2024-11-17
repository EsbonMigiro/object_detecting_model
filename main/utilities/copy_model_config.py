import os
from .dir_creator import ProjectDirectoryManager
import subprocess

def copy_model_config_to_training_path():
    from_path = os.path.join(ProjectDirectoryManager.paths['PRETRAINED_MODEL_PATH'], ProjectDirectoryManager.PRETRAINED_MODEL_NAME, 'pipeline.config') 
    to_path = os.path.join(ProjectDirectoryManager.paths['CHECKPOINT_PATH'])
    
    try:
        # Attempt to copy the file
        subprocess.run(["cp", from_path, to_path], check=True)
        print("Model config file copied successfully.")
    
    except subprocess.CalledProcessError as e:
        # Handle the error if the subprocess fails
        print(f"Error occurred while copying model config file: {e}")
    
    except Exception as e:
        # Catch any other general exceptions
        print(f"An unexpected error occurred: {e}")
