import unittest

from exercice1 import compute_period, compute_auto_correlation


class MyTestCase(unittest.TestCase):
#     def test_exercice1(self):
#         k = 899  # faire varier k
#         l = 0  # faire varier l
#         m = 32768
#         x_0 = 12  # faire varier x_0
#
# #        k_values = [600, 899, ]
#
#         for x_0 in range(1, 20, 1):
#             compute_period(k, l, m, x_0)

    def test_exercice1(self):
        # k = pow(7, 5)  # faire varier k
        #
        # l = 0  # faire varier l
        # m = 6075 #pow(2, 31) - 1
        # x_0 = 12  # faire varier x_0

        # k = pow(7, 5) # faire varier k
        #
        # l = 0  # faire varier l
        # m = pow(2, 31) - 1
        # x_0 = 12  # faire varier x_0

        k = 899  # faire varier k

        l = 0  # faire varier l
        m = 32768
        x_0 = 12  # faire varier x_0

        compute_period(k, l, m, x_0)
    #    tau = 10
     #   correlation = compute_auto_correlation(k, l, m, x_0, tau)
        #print(correlation)