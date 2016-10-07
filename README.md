# img_crawler
Python program to download all images from URLs given in a plain textfile

### Built with

Python 3.5

### How to use

 - Download repository

 - Edit main.py and provide path to textfile containing URLs
 
 - run script

```
# main.py

from src import img_crawler

filename = '../url.txt'

# set save_all_in_one_folder to True to save all images in one folder.
img_crawler.retrieve(filename, save_all_in_one_folder=False)
```

### Example console output

```
Preparing to retrieve from 13 URLs
Removed 2 duplicate URLs
Preparing to retrieve from 11 URLs
FAIL: Not reachable URL: http://mywebserver.com/images/271947.jpg
FAIL: Not reachable URL: http://mywebserver.com/images/24174.jpg
FAIL: Not reachable URL: http://somewebsrv.com/img/992147.jpg
FAIL: Not reachable URL: http://somewebsrv.com/992147.jpg
SUCCESS: Retrieved: https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Clematis_macro_1.JPG/120px-Clematis_macro_1.JPG
SUCCESS: Retrieved: https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Coffea_canephora_berries.JPG/120px-Coffea_canephora_berries.JPG
SUCCESS: Retrieved: https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Elaeagnus_umbellata_berries.JPG/120px-Elaeagnus_umbellata_berries.JPG
SUCCESS: Retrieved: http://www.adpic.de/data/picture/detail/Pflanze_in_der_Erde_159054.jpg
FAIL: Not valid image URL: fake
FAIL: Not valid image URL: google.com/123.jpeg
FAIL: Not reachable URL: http://www.google.com/123.jpeg
Download complete: 4 Successes and 7 Fails
```

### Task
Given a plaintext file containing URLs, one per line, e.g.:

http://mywebserver.com/images/271947.jpg

http://mywebserver.com/images/24174.jpg

http://somewebsrv.com/img/992147.jpg

Write a script that takes this plaintext file as an argument and downloads all images, storing them on the local hard disk.
