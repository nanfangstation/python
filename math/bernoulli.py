from scipy.stats import binom  # 导入伯努利分布
import matplotlib.pyplot as plt
import numpy as np


def bernoulli():
    # 次数
    n = 10
    # 概率
    p = 0.3
    # 导入特征系数
    k = np.arange(0, 21)
    # 伯努利分布的特征值导入
    binomial = binom.pmf(k, n, p)
    plt.plot(k, binomial, 'o-')
    plt.title('Binomial: n = %i, p=%0.2f' % (n, p), fontsize=15)
    plt.xlabel('Number of successes')
    plt.ylabel('Probability of sucesses', fontsize=15)
    plt.show()


if __name__ == '__main__':
    bernoulli()
