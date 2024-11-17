import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format
from .dir_creator import ProjectDirectoryManager
import os

def update_config_transfer_learning():

    labels = [{'name':'salmonella_typhi5', 'id':1}, {'name':'Vibrio_cholerae5', 'id':2}, {'name':'e.coli5', 'id':3}]

        # Load pipeline configuration
    config = config_util.get_configs_from_pipeline_file(ProjectDirectoryManager.files['PIPELINE_CONFIG'])
    print(config)

    # Read the pipeline config file and update it
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
    with tf.io.gfile.GFile(ProjectDirectoryManager.files['PIPELINE_CONFIG'], "r") as f:
        proto_str = f.read()
        text_format.Merge(proto_str, pipeline_config)

    # Update the pipeline config with necessary parameters
    pipeline_config.model.ssd.num_classes = len(labels)  # Set number of classes
    pipeline_config.train_config.batch_size = 4  # Set batch size
    pipeline_config.train_config.fine_tune_checkpoint = os.path.join(ProjectDirectoryManager.paths['PRETRAINED_MODEL_PATH'], 'PRETRAINED_MODEL_NAME', 'checkpoint', 'ckpt-0')
    pipeline_config.train_config.fine_tune_checkpoint_type = "detection"  # Fine-tune checkpoint type
    pipeline_config.train_input_reader.label_map_path = ProjectDirectoryManager.files['LABELMAP']  # Label map path
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [os.path.join(ProjectDirectoryManager.paths['ANNOTATION_PATH'], 'train.record')]  # Input path for train
    pipeline_config.eval_input_reader[0].label_map_path = ProjectDirectoryManager.files['LABELMAP']  # Label map path for evaluation
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [os.path.join(ProjectDirectoryManager.paths['ANNOTATION_PATH'], 'test.record')]  # Input path for test

    # Convert the updated config to a string and save it
    config_text = text_format.MessageToString(pipeline_config)
    with tf.io.gfile.GFile(ProjectDirectoryManager.files['PIPELINE_CONFIG'], "wb") as f:
        f.write(config_text)

    print("Pipeline configuration updated and saved successfully.")