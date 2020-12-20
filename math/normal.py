import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def demo1():
    mu, sigma = 0, 1
    sampleNo = 1000
    np.random.seed(0)
    s = np.random.normal(mu, sigma, sampleNo)

    plt.hist(s, bins=100, density=True)
    plt.show()


def demo2():
    mu, sigma, num_bins = 0, 1, 50
    x = mu + sigma * np.random.randn(1000000)
    # 正态分布的数据
    n, bins, patches = plt.hist(x, num_bins, density=True, facecolor='blue', alpha=0.5)
    # 拟合曲线
    y = norm.pdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('histogram of normal distribution: $\mu = 0$, $\sigma=1$')

    plt.subplots_adjust(left=0.15)
    plt.show()


if __name__ == '__main__':
    demo2()
