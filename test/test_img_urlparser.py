import unittest

from src import img_urlparser


class TestUrlParser(unittest.TestCase):

    def test_get_http_netloc(self):
        url = 'http://www.mywebserver.com/images/271947.jpg'
        netloc = img_urlparser.get_netloc(url)
        self.assertEqual(netloc, 'mywebserver.com')

    def test_get_path(self):
        url = 'http://mywebserver.com/images/271947.jpg'
        path = img_urlparser.get_path(url)
        self.assertEqual(path, '/images/271947.jpg')

    def test_get_path_directly(self):
        url = 'http://mywebserver.com/271947.jpg'
        path = img_urlparser.get_path(url)
        self.assertEqual(path, '/271947.jpg')

    def test_get_dirname(self):
        url = 'http://mywebserver.com/images/271947.jpg'
        dirname = img_urlparser.get_dirname(url)
        self.assertEqual(dirname, '/images')

    def test_get_no_dirname(self):
        url = 'http://mywebserver.com/271947.jpg'
        dirname = img_urlparser.get_dirname(url)
        self.assertEqual(dirname, '/')

    def test_get_basename(self):
        url = 'http://mywebserver.com/images/271947.jpg'
        netloc = img_urlparser.get_basename(url)
        self.assertEqual(netloc, '271947.jpg')

    def test_get_no_basename(self):
        url = 'http://mywebserver.com/images/'
        netloc = img_urlparser.get_basename(url)
        self.assertEqual(netloc, '')

    def test_remove_empty_lines(self):
        url_list = ['http://mywebserver.com/images/271947.jpg', ' ', 'http://mywebserver.com/images/271947.jpg', '']
        url_list = img_urlparser.remove_empty_lines(url_list)
        self.assertTrue('' not in url_list)
        self.assertTrue(len(url_list) == 2)

    def test_remove_eol_character(self):
        url_list = []
        url_list = img_urlparser.remove_eol_character(url_list)
        self.assertEqual(url_list, [])

        url_list = ['http://mywebserver.com/images/271947.jpg\n']
        url_list = img_urlparser.remove_eol_character(url_list)
        self.assertEqual(img_urlparser.remove_eol_character(url_list)[0], 'http://mywebserver.com/images/271947.jpg')

    def test_remove_duplicates(self):
        url_list = []
        url_list = img_urlparser.remove_duplicates(url_list)
        self.assertEqual(url_list, [])

        url_list = ['http://mywebserver.com/images/271947.jpg', 'http://mywebserver.com/images/271947.jpg']
        url_list = img_urlparser.remove_duplicates(url_list)
        self.assertEqual(url_list, ['http://mywebserver.com/images/271947.jpg'])
