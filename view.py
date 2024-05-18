from typing import Dict

import pandas as pd
from pandasgui import show
import streamlit as st
import numpy as np

def display_results(
    results: Dict, config: Dict
) -> None:
    indicators = pd.DataFrame.from_dict(
        {key: [value] for key, value in results.items()},
        orient="index",
        columns=[config["view"]["column_values"]]
    )

    if config["view_mode"]["print"]:
        _results_to_console(indicators)

    if config["view_mode"]["pandasgui"]:
        _results_to_pandasgui(indicators)

    if config["view_mode"]["streamlit"]:
        _results_to_streamlit(indicators)


def _results_to_console(indicators: pd.DataFrame):
    print(indicators)


def _results_to_pandasgui(indicators: pd.DataFrame):
    show(indicators)

def _results_to_streamlit(indicators: pd.DataFrame):
    # Titre de l'application
    st.title("Résultats")

    # Ajouter un texte
    st.write("Résultat d'un PF composé des valeurs équipondérées des composants du S&P 500 à plus de 1 Milliards de cap"
             "italisation boursière.")

    # Créer un dataframe et l'afficher
    data = indicators
    st.write(data)

