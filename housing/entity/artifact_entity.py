from collections import namedtuple

DataIngestionArtifact=namedtuple('DataIngestionArtifact',['train_file_path','test_file_path','actual_message','is_ingested'])