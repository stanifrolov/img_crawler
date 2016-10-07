from src import img_crawler

filename = '../url.txt'

# set save_all_in_one_folder to True to save all images in one folders.
img_crawler.retrieve(filename, save_all_in_one_folder=False)
