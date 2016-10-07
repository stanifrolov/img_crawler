from urllib.parse import urlparse

import re


def url_is_img(url):
        if not scheme_is_empty(url) and not netloc_is_empty(url) and ending_is_img_file(url):
            return True
        else:
            return False


def scheme_is_empty(url):
    parse_result = urlparse(url)
    return parse_result.scheme == ''


def netloc_is_empty(url):
    parse_result = urlparse(url)
    return parse_result.netloc == ''


def ending_is_img_file(url):
    parse_result = urlparse(url)
    str(parse_result.path).lower()
    r_image = re.compile(r".*\.(jpg|png|gif|bmp|jpeg)$")
    return r_image.match(str(parse_result.path).lower())
