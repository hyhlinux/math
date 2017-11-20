# coding:utf-8

import matplotlib.pyplot as plt


def main():
    # figure 网格图 3x2=6 总共可以放6个
    plt.subplot(3, 2, 1)
    plt.subplot(3, 2, 2)
    plt.subplot(3, 2, 3)
    plt.subplot(3, 2, 4)
    plt.subplot(3, 2, 5)
    plt.subplot(3, 2, 6)
    # plt.subplot(2, 2, 1)
    plt.show()
    pass

if __name__ == '__main__':
    main()