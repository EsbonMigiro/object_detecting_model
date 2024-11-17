import os
import subprocess
from .dir_creator import ProjectDirectoryManager

def generate_tf_records():
    paths = ProjectDirectoryManager.paths
    files = ProjectDirectoryManager.files

    # Check if the TFRecord script exists
    if not os.path.exists(files['TF_RECORD_SCRIPT']):
        print("TFRecord script not found. Cloning repository...")
        # Clone the repository if the script doesn't exist
        subprocess.run(['git', 'clone', 'https://github.com/nicknochnack/GenerateTFRecord', paths['SCRIPTS_PATH']], check=True)
    
    # Run the TFRecord generation for training data
    train_cmd = [
        'python', files['TF_RECORD_SCRIPT'],
        '-x', os.path.join(paths['IMAGE_PATH'], 'train'),
        '-l', files['LABELMAP'],
        '-o', os.path.join(paths['ANNOTATION_PATH'], 'train.record')
    ]
    print("Generating train record...")
    subprocess.run(train_cmd, check=True)

    # Run the TFRecord generation for test data
    test_cmd = [
        'python', files['TF_RECORD_SCRIPT'],
        '-x', os.path.join(paths['IMAGE_PATH'], 'test'),
        '-l', files['LABELMAP'],
        '-o', os.path.join(paths['ANNOTATION_PATH'], 'test.record')
    ]
    print("Generating test record...")
    subprocess.run(test_cmd, check=True)

    print("TFRecords generated successfully.")

