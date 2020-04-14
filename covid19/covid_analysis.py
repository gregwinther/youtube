import numpy as np
from matplotlib import pyplot as plt
import json
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


def logistic_function(x, a=1, b=0, c=1, d=0):
    return a / (1 + np.exp(-c * (x - d))) + b


def exponential_function(x, a=1, b=0, c=0, d=0):
    return a * np.exp(c * (x + d)) + b


def fit_data_to_function(
    x, y, function, plot=True, initial_guess=[1, 1, 1, 1]
):
    params, _ = curve_fit(function, x, y, p0=initial_guess)
    plt.plot(x, y, ".", label="Observations")
    y_fit = function(x, *params)
    print(r2_score(y, y_fit))
    if plot:
        plt.plot(x, y_fit, label="Fitted curve")
        plt.legend()
        plt.show()
    return params


def plateau(x, y, params, function, diff=10):
    confirmed_now = y[-1]
    confirmed_then = y[-2]
    days = 0
    now = x[-1]
    while confirmed_now - confirmed_then > diff:
        days += 1
        confirmed_then = confirmed_now
        confirmed_now = function(now + days, *params)

    return days, confirmed_now


if __name__ == "__main__":
    with open("./covid_data.json", "r") as file:
        data = json.load(file)

    y = np.asarray(data["new york"])
    x = np.arange(len(y))

    params = fit_data_to_function(
        x, y, logistic_function, initial_guess=[y[-1], 1, 1, 1]
    )
    print(params)
    diff = 500
    days, confirmed = plateau(
        x, y, params, logistic_function, diff=diff
    )
    print(f"{days} days until growth is less than {diff}")
    print(f"Number of cases will be {int(confirmed)}")
