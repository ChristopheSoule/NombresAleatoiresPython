import matplotlib.pyplot as plt
import numpy as np


def compute_period(k, l, m, x_0):

    x_plot = []
    y_plot = []

    x = [x_0]  # création tableau x initialisé à x0


    period_result = 1  # initialisation période = 0

    x_n = x_0  # initialisation x_n
    x_n_plus_1 = (k * x_n + l) % m

    x_plot.append(x_n)
    y_plot.append(x_n_plus_1)
    while not (x_n_plus_1 in x):  # tant que xn+1 différent des xn du tableau, continuer

        x.append(x_n_plus_1)
        x_n = x_n_plus_1
        x_n_plus_1 = (k * x_n + l) % m
        x_plot.append(x_n)
        y_plot.append(x_n_plus_1)
        period_result += 1
        if (period_result == 2048) :
            break

    print(len(x_plot))
    plt.scatter(x_plot, y_plot, label='energy')
    plt.xlabel('xn')
    plt.ylabel('xn+1')
    plt.legend()
    plt.grid(True)
    plt.show()


    print('period : ' + str(period_result))


def compute_auto_correlation(k, l, m, x_0, tau):

    x = [x_0]  # création tableau x initialisé à x0
    N = 10000
    N_moyenne = N - tau


    x_n = x_0  # initialisation x_n
    x_n_plus_1 = (k * x_n + l) % m

    for i in range(1 ,N,1) :
        x.append(x_n_plus_1)
        x_n = x_n_plus_1
        x_n_plus_1 = (k * x_n + l) % m

    correlation_numerator = 0
    correlation_denominator = 0
    x_mean = np.mean(x)


    for i in range(1 ,N_moyenne,1):
        correlation_numerator += (x[i] - x_mean) * (x[i + tau] - x_mean)
        correlation_denominator += pow((x[i] - x_mean), 2)

    correlation = correlation_numerator / correlation_denominator
    return correlation
    #print(correlation)


