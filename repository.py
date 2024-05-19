import os
from typing import Dict

import numpy as np
import yfinance as yf
import pandas as pd
import fredapi
from datetime import datetime, timedelta

from constants import CONFIG_FILE
from helpers import get_toml_data


def get_config() -> Dict:
    path = os.path.join(os.getcwd(), CONFIG_FILE)
    return get_toml_data(path)


def get_weights(config: Dict) -> np.array:
    return np.array(list(config["portfolio"].values()))


def get_data(config: Dict):
    tickers = list(config["portfolio"].keys())
    end_date = datetime.today()
    start_date = end_date - timedelta(days=10*365)  # 10 years back from today
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
    )
    return data[config["initialisation"]["field_to_keep"]]


def Calcul_Rendement(dataframe: pd.DataFrame):
    rendement = dataframe.pct_change()
    rendement = rendement.dropna()
    return rendement

def Calcul_Valeur_PF(prix_actifs: pd.DataFrame, weights: np.array):
    valeur = np.dot(prix_actifs.values, weights)
    valeur = pd.DataFrame(valeur, columns=['Portefeuille'], index=prix_actifs.index)
    return valeur

def Extract_rf() -> np.float64:
    fred = fredapi.Fred(api_key='55cc7affbaba092c1f14f4fd882eaaf5')
    us_treasury_10y = fred.get_series_latest_release('GS10') / 100
    rfr = us_treasury_10y.iloc[-1]
    return rfr


if __name__ == "__main__":
    conf = get_config()
    print(get_weights(conf))
    results = get_data(conf)
    print(results)
    assets_returns = Calcul_Rendement(results)
    PF_returns = Calcul_Valeur_PF(assets_returns, get_weights(conf))
    print(assets_returns, PF_returns)
    print(Extract_rf() * 100, '%')
    print(conf)

