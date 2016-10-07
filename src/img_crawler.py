import os
import datetime
import urllib.request
import urllib.error


from src import img_urlparser
from src import img_urlvalidotor


def retrieve(filename, save_all_in_one_folder=False):
    list_of_url = read_txt_file(filename)
    list_of_url = prepare_url_list(list_of_url)
    timestamp = datetime.datetime.now().strftime('/%Y-%m-%d-%H-%M-%S/')
    number_of_successes = 0
    number_of_fails = 0
    for url in list_of_url:
        img_name = img_urlparser.get_basename(url)
        directory = '../download' + timestamp

        if not save_all_in_one_folder:
            netloc = img_urlparser.get_netloc(url)
            directory += netloc

        make_sure_path_exists(directory)

        if img_urlvalidotor.url_is_img(url):
            try:
                path = os.path.join(directory, img_name)
                urllib.request.urlretrieve(url, path)
                print('SUCCESS: Retrieved: ' + url)
                number_of_successes += 1
            except urllib.error.URLError:
                print('FAIL: Not reachable URL: ' + url)
                number_of_fails += 1
        else:
            print('FAIL: Not valid image URL: ' + url)
            number_of_fails += 1

    remove_empty_files('../download' + timestamp)
    print_status(number_of_fails, number_of_successes)


def read_txt_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except IOError:
        print("FAIL Read File: No such file or directory to read: " + filename)


def prepare_url_list(list_of_url):
    list_of_url = img_urlparser.remove_empty_lines(list_of_url)
    print('Preparing to retrieve from ' + str(len(list_of_url)) + ' URLs')

    list_of_url = img_urlparser.remove_eol_character(list_of_url)
    raw_size = len(list_of_url)
    list_of_url = img_urlparser.remove_duplicates(list_of_url)

    difference = raw_size - len(list_of_url)
    if difference > 0:
        print('Removed ' + str(difference) + ' duplicate URLs')
        print('Preparing to retrieve from ' + str(len(list_of_url)) + ' URLs')

    return list_of_url


def make_sure_path_exists(path):
    if path.startswith('/'):
        path = path[1:]
    if not path.endswith('/'):
        path += '/'
    os.makedirs(path, exist_ok=True)


def remove_empty_files(path, remove_root=True):
    if not os.path.isdir(path):
        return

    files = os.listdir(path)
    if len(files):
        for file in files:
            full_path = os.path.join(path, file)
            if os.path.isdir(full_path):
                remove_empty_files(full_path)

    files = os.listdir(path)
    if len(files) == 0 and remove_root:
        os.rmdir(path)


def print_status(number_of_fails, number_of_successes):
    print("Download complete: " + str(number_of_successes) + " Successes and " + str(number_of_fails) + " Fails")
