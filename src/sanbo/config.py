import os
from datetime import datetime


class Config:
    PROJECT_ROOT_DIR = "/Users/gopora/MyStuff/Dev/Workspaces/Sandbox/SantanderNBO"

    DATASETS_DIR = os.path.join(PROJECT_ROOT_DIR, "data")
    TF_LOG_DIR = os.path.join(PROJECT_ROOT_DIR, "tf_logs")
    TRAINING_SET_DATA_FILE = "train_ver2.csv"
    TEST_SET_DATA_FILE = "test_ver2.csv"

    @staticmethod
    def get_new_tf_log_dir():
        now = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        log_dir = "{}/run-{}/".format(Config.TF_LOG_DIR, now)

        return log_dir