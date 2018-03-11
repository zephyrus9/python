# -*-coding: utf-8 -*-
# Author: 
class Solution:
    def maxProfit(self, prices):
        """
        :param prices:
        :return:
        """
        return sum(max(0, n-m) for m, n in zip(prices[1:], prices[:-1]))


if __name__ == '__main__':
    s = [1,3,5,2,7,3,2,5,3,4,5,6,33,12,32,43]
    print(Solution().maxProfit(s))

    # plot s
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.plot(s)
    plt.show()