import urllib.request
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin #this module converts relative links to absolute links

#Open link using urllib urlopen method
base_url = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(base_url).read()

#Use beautiful soup to parse out the html
for link in BeautifulSoup(content,"html.parser").findAll("a"):
    print("following link: ", link)
    href = urljoin(base_url, link["href"])

    #follow the link and download the image on that linked page
    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, "html.parser").findAll("img"):
        img_href = urljoin(href, img["src"])
        print("Downloading image: ", img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join("Image_Downloads", img_name))
