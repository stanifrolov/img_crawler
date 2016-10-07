import unittest

from src import img_crawler


class TestUrlCrawler(unittest.TestCase):

    def test_file_not_exist(self):
        print("Test reading not existing file")
        filename = '../not_exist.txt'
        img_crawler.read_txt_file(filename)
