# -*- coding: utf-8 -*-
import unittest
import wubi


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_chinese_with_english1(self):
        self.assertEqual(wubi.to_wubi('Wen Chao Wang 爱自由'),
                         'WenChaoWang ep thd mh')

    def test_chinese_with_english2(self):
        self.assertEqual(wubi.to_wubi('WenChao Wang 爱自由'),
                         'WenChaoWang ep thd mh')

    def test_chinese_with_english3(self):
        self.assertEqual(wubi.to_wubi('WenChaoWang 爱自由'),
                         'WenChaoWang ep thd mh')

    def test_chinese_with_english4(self):
        self.assertEqual(wubi.to_wubi('爱wang'), 'ep wang')

    def test_wibi_with_english1(self):
        self.assertEqual(wubi.from_wubi('WenChaoWang ep thd mh'),
                         'WenChaoWang爱自由')

    def test_wubi_with_english2(self):
        self.assertEqual(wubi.from_wubi('WenChaoWang ep thd mh'),
                         'WenChaoWang爱自由')

    def test_wubi_with_english3(self):
        self.assertEqual(wubi.from_wubi('WenChaoWang ep thd mh'),
                         'WenChaoWang爱自由')


if __name__ == '__main__':
    unittest.main()
