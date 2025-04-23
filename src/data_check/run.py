import pandas as pd
import os
import hydra
from omegaconf import DictConfig

from .test_data import test_row_count, test_price_range

@hydra.main(config_name="config", config_path="../../conf", version_base="1.1")
def go(cfg: DictConfig):
    data = pd.read_csv(cfg.data_check.csv)

    test_row_count(data)
    test_price_range(data, cfg.data_check.min_price, cfg.data_check.max_price)