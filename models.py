from typing import Dict

import numpy as np
import pandas as pd


def Calcul_Mean(df: pd.DataFrame) -> np.float64:
    return df.mean()


def Calcul_Variance_PF(assets_returns: pd.DataFrame, weights: np.array) -> np.float64:
    covariance = assets_returns.cov()*252
    return np.dot(weights.T, np.dot(covariance, weights))


def Calcul_Std(assets_returns: pd.DataFrame, weights: np.array) -> np.float64:
    covariance = assets_returns.cov()*252
    variance = np.dot(weights.T, np.dot(covariance, weights))
    return np.sqrt(variance)


def Calcul_Sharpe_Ratio (PF_Returns_Mean, rfr, PF_Std) -> np.float64:
    return ((PF_Returns_Mean - rfr) / PF_Std)


def Calcul_Sortino_Ratio (df_Return: pd.DataFrame, rfr) -> np.float64:
    # Create a downside return series with the negative returns only
    downside_returns = df_Return.iloc[:, 0].loc[df_Return.iloc[: 0] < 0]

    # Calculate expected return and std dev of downside
    expected_return = df_Return.iloc[:, 0].mean()
    down_stdev = downside_returns.std()

    # Calculate the sortino ratio
    return (expected_return - rfr)/down_stdev


def Calcul_DrawDown(df_Prices) -> np.float64:
    # Calculate the max value
    roll_max = df_Prices.rolling(center=False, min_periods=1, window=252).max()

    # Calculate the daily draw-down relative to the max
    daily_drawdown = df_Prices/roll_max - 1.0

    # Calculate the minimum (negative) daily draw-down
    max_daily_draw_down = daily_drawdown.rolling(center=False, min_periods=1, window=252).min()

    # Valeur minimum daily draw-down
    return max_daily_draw_down.iloc[-1, 0]


def Calcul_VaR_95 (df_returns) -> np.float64:
    return df_returns.quantile(0.05)


def Calcul_CVaR_95 (df_returns, VaR95) -> np.float64:
    return df_returns[df_returns <= VaR95].mean()


def get_portfolio_indicators(PF_returns, PF_prices, assets_returns, weights, rfr, config: Dict) -> Dict:
    results = {}
    port_return = Calcul_Mean(PF_returns)
    port_variance = Calcul_Variance_PF(assets_returns, weights)
    port_standard_dev = Calcul_Std(assets_returns, weights)
    port_sharpe = Calcul_Sharpe_Ratio(port_return, rfr, port_standard_dev)
    port_sortino = Calcul_Sortino_Ratio(PF_returns, rfr)
    port_drawdown = Calcul_DrawDown(PF_prices)
    port_Var_95 = Calcul_VaR_95(PF_returns)
    port_CVar_95 = Calcul_CVaR_95(PF_returns, port_Var_95)

    results[config['view']['return']] = port_return
    results[config['view']['variance']] = port_variance
    results[config['view']['std']] = port_standard_dev
    results[config['view']['sharpe']] = port_sharpe
    results[config['view']['sortino']] = port_sortino
    results[config['view']['drawdown']] = port_drawdown
    results[config['view']['sortino']] = port_Var_95
    results[config['view']['drawdown']] = port_CVar_95

    return results










