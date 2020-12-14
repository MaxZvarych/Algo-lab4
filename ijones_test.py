import unittest

from ijones import ijones


class IjonesTest(unittest.TestCase):
    def test1(self):
        corridor = [['a', 'a', 'a'], ['c', 'a', 'b'], ['d', 'e', 'f']]
        self.assertEqual(ijones(corridor,3,3), 5)

    def test2(self):
        corridor = [['a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a', 'a']]
        self.assertEqual(ijones(corridor,6,7), 201684)

    def test3(self):
        corridor = [['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']]
        self.assertEqual(ijones(corridor,1,10), 2)

    def test_one_column(self):
        corridor = [['a'], ['b'], ['c'], ['a']]
        self.assertEqual(ijones(corridor,4,1), 2)

    def test_one_tile(self):
        corridor = [['a']]
        self.assertEqual(ijones(corridor,1,1), 1)

    def test_one_row_with_unique_tiles(self):
        corridor = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
        self.assertEqual(ijones(corridor,1,8), 1)

    def test4(self):
        corridor = [['s', 'a', 'r', 'c', 's', 'a'], ['m', 'a', 'r', 's', 'o', 'l'], ['b', 'a', 'l', 'k', 'a', 's']]
        self.assertEqual(ijones(corridor,3,6), 22)

if __name__ == '__main__':
    unittest.main()