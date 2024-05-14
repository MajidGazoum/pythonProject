import os
from typing import Dict

import numpy as np
import yfinance as yf

from constants import CONFIG_FILE
from helpers import get_toml_data


def get_config() -> Dict:
    path = os.path.join(os.getcwd(), CONFIG_FILE)
    return get_toml_data(path)




def get_weights(config: Dict) -> np.array:
    return np.array(list(config["portfolio"].values()))


def get_data(config: Dict):
    tickers = list(config["portfolio"].keys())
    data = yf.download(
        tickers,
        start=config["initialisation"]["begin_date"],
        end=config["initialisation"]["end_date"],
    )
    return data[config["initialisation"]["field_to_keep"]]


if __name__ == "__main__":
    conf = get_config()
    print(get_weights(conf))
    results = get_data(conf)
    print(results)
    print(conf)

