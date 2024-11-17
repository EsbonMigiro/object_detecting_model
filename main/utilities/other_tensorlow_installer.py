import os
import subprocess
from .dir_creator import ProjectDirectoryManager

def other_tensorflow_installer():

    # Install TensorFlow
    subprocess.run(["pip", "install", "tensorflow==2.13.0"], check=True)

    # Define the verification script path
    VERIFICATION_SCRIPT = os.path.join(ProjectDirectoryManager.paths['APIMODEL_PATH'], 'research', 'object_detection', 'builders', 'model_builder_tf2_test.py')

    # Run the verification script
    result = subprocess.run(["python", f"{VERIFICATION_SCRIPT}"], capture_output=True, text=True)

    # Check the result and handle potential errors
    if result.returncode != 0:
        print(f"Verification failed with error: {result.stderr}")
    else:
        try:
            import object_detection
            print("Object Detection API is installed correctly")
        except ImportError:
            print("Object Detection API installation failed")
