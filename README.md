# img_crawler
Python program to download all images from URLs given in a plain textfile

# How to Use

```
from src import img_crawler

filename = '../url.txt'

# set save_all_in_one_folder to True to save all images in one folder.
img_crawler.retrieve(filename, save_all_in_one_folder=False)
```

#Task:
Given a plaintext file containing URLs, one per line, e.g.:

http://mywebserver.com/images/271947.jpg

http://mywebserver.com/images/24174.jpg

http://somewebsrv.com/img/992147.jpg

Write a script that takes this plaintext file as an argument and downloads all images, storing them on the local hard disk.
