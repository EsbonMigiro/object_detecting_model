import os
import subprocess
from .dir_creator import ProjectDirectoryManager

# Paths dictionary from your main configuration file or hardcoded here
def clone_tensorflow_models():
    """Clones the TensorFlow models repository if not already present."""
    object_detection_path = os.path.join(ProjectDirectoryManager.paths['APIMODEL_PATH'], 'research', 'object_detection')
    
    if not os.path.exists(object_detection_path):
        print("TensorFlow models repository not found. Cloning...")
        try:
            # Increase Git buffer size
            subprocess.run(["git", "config", "--global", "http.postBuffer", "524288000"], check=True)
            
            subprocess.run(
                ["git", "clone", "https://github.com/tensorflow/models", ProjectDirectoryManager.paths['APIMODEL_PATH']],
                check=True
            )
            print("TensorFlow models repository successfully cloned.")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning TensorFlow models repository: {e}")
    else:
        print("TensorFlow models repository already exists.")




# Paths dictionary for consistency

def install_tensorflow_object_detection():
    """Installs TensorFlow Object Detection API dependencies."""
    try:
        if os.name == 'posix':  # Linux/MacOS
            print("Installing TensorFlow Object Detection API on POSIX system...")
            # subprocess.run(["sudo", "apt-get", "install", "-y", "protobuf-compiler"], check=True)
            import subprocess

            subprocess.run(["pip", "install", "protobuf"], check=True)

            subprocess.run(
                f"cd {os.path.join(ProjectDirectoryManager.paths['APIMODEL_PATH'], 'research')} && "
                "protoc object_detection/protos/*.proto --python_out=. && "
                "cp object_detection/packages/tf2/setup.py . && "
                "python -m pip install .",
                shell=True,
                check=True
            )
        print("TensorFlow Object Detection API installed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


