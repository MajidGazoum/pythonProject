from models import (
    get_portfolio_indicators,
)
from repository import get_data, get_weights, get_config, Calcul_Rendement, Calcul_Valeur_PF, Extract_rf
from view import display_results


def main():
    config = get_config()
    weights = get_weights(config)
    print(type(weights))
    data = get_data(config)
    assets_returns = Calcul_Rendement(data)
    PF_prices = Calcul_Valeur_PF(data, weights)
    PF_returns = Calcul_Rendement(PF_prices)
    rfr = Extract_rf()

    # Calculation
    indicators = get_portfolio_indicators(PF_returns, PF_prices, assets_returns, weights, rfr, config)

    # Display results
    display_results(indicators, config)


if __name__ == "__main__":
    main()
