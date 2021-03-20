import unittest

from countMoves import countMoves


class TestArrayGame(unittest.TestCase):

    def test_just_one_movement(self):
        self.assertEqual(countMoves([3, 2, 2, 2]), 1)

    def test_base_movement(self):
        self.assertEqual(countMoves([3, 4, 6, 6, 3]), 7)

    def test_with_equals_but_not_all(self):
        self.assertEqual(countMoves([5, 5, 6, 8, 8, 5]), 7)

    def test_with_a_big_list(self):
        self.assertEqual(countMoves(
            [40, 32, 14, 27, 17, 50, 94, 96, 71, 60, 79, 68, 64, 25, 14, 76, 28, 97, 12, 34, 15, 98, 26, 36, 43, 19, 85,
             19, 99, 37, 68, 45, 53, 26, 16, 59, 49, 11, 69, 20, 61]), 1501)

    def test_with_huge_list(self):
        self.assertEqual(countMoves(
            [844, 750, 222, 807, 599, 466, 723, 144, 127, 559, 966, 527, 896, 276, 171, 948, 749, 763, 482, 577, 841,
             813, 85, 992, 714, 954, 462, 723, 733, 736, 98, 713, 953, 493, 99, 167, 328, 258, 782, 330, 152, 87, 222,
             946, 843, 912, 583, 83, 904, 964, 354, 532, 187, 802, 642, 946, 123, 324, 439, 669, 281, 563, 590, 464,
             808, 415, 772, 802, 163, 177, 711, 777, 316, 599]), 34880)
