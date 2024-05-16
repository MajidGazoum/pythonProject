from typing import Dict

import pandas as pd
from pandasgui import show


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


def _results_to_console(indicators: pd.DataFrame):
    print(indicators)


def _results_to_pandasgui(indicators: pd.DataFrame):
    show(indicators)


