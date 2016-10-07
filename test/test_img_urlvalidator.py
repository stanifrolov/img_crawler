import unittest

from src import img_urlvalidotor


class TestUrlValidator(unittest.TestCase):

    def test_url_is_img(self):
        self.assertTrue(img_urlvalidotor.url_is_img('http://mywebserver.com/images/271947.jpg'))
        self.assertTrue(img_urlvalidotor.url_is_img('http://mywebserver.com/images/24174.jpg'))
        self.assertTrue(img_urlvalidotor.url_is_img('http://somewebsrv.com/img/992147.jpg'))

        self.assertTrue(img_urlvalidotor.url_is_img('https://somewebsrv.com/img/992147.jpg'))
        self.assertTrue(img_urlvalidotor.url_is_img('https://www.mywebserver.com/271947.jpeg'))
        self.assertTrue(img_urlvalidotor.url_is_img('https://www.mywebserver.com/images/271947.png'))

        self.assertFalse(img_urlvalidotor.url_is_img('mywebserver.com/images/271947.jpg'))
        self.assertFalse(img_urlvalidotor.url_is_img('mywebserver.com/images/271947.html'))
        self.assertFalse(img_urlvalidotor.url_is_img('www.mywebserver.com/images/271947.jpg'))

        self.assertFalse(img_urlvalidotor.url_is_img('http://somewebsrv.com/img/992147.jpg.exe'))

    def test_netloc_is_empty(self):
        self.assertTrue(img_urlvalidotor.netloc_is_empty('mywebserver.com/images/271947.jpg'))
        self.assertTrue(img_urlvalidotor.netloc_is_empty('www.mywebserver.com/images/271947.jpg'))

    def test_scheme_is_empty(self):
        self.assertFalse(img_urlvalidotor.scheme_is_empty('http://mywebserver.com/images/271947.jpg'))

        self.assertTrue(img_urlvalidotor.scheme_is_empty('mywebserver.com/images/271947.jpg'))
        self.assertTrue(img_urlvalidotor.scheme_is_empty('www.mywebserver.com/images/271947.jpg'))

    def test_ending_is_img_file(self):
        self.assertTrue(img_urlvalidotor.ending_is_img_file('http://mywebserver.com/images/271947.jpg'))
        self.assertTrue(img_urlvalidotor.ending_is_img_file('http://mywebserver.com/271947.bmp'))
        self.assertTrue(img_urlvalidotor.ending_is_img_file('http://www.mywebserver.com/271947.png'))
        self.assertTrue(img_urlvalidotor.ending_is_img_file('mywebserver.com/271947.gif'))
