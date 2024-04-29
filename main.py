#importer les librairies necessaires
from pandas_datareader import data as web
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
import seaborn as sns
import yfinance as yf
import yahoo_fin.stock_info as yfn
import scipy.stats as SS
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib
import financedatabase as fd
from pypfopt.efficient_frontier import EfficientCVaR
from pypfopt.expected_returns import mean_historical_return
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.cla import CLA
import fredapi
import pyfolio as pf
from scipy.stats import norm, anderson
from scipy.stats import skewnorm, skewtest
from pypfopt import risk_models
from pypfopt import expected_returns
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import math
from pandas.plotting import table
