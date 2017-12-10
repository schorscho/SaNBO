import os
from datetime import datetime


class SaNBOConfig:
    ROOT_DIR = "/home/ubuntu"
    PROJECT_ROOT_DIR = os.path.join(ROOT_DIR, "SaNBO")
    DATASETS_DIR = os.path.join(ROOT_DIR, "data")
    TF_LOG_DIR = os.path.join(PROJECT_ROOT_DIR, "tf_logs")
    TRAINING_SET_DATA_FILE = "sanbo_train_data.csv"
    TEST_SET_DATA_FILE = "sanbo_test_data.csv"

    @staticmethod
    def get_new_tf_log_dir():
        now = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        log_dir = "{}/run-{}/".format(Config.TF_LOG_DIR, now)

        return log_dir