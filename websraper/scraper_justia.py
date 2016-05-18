##################################################################################
#import modules

# to retrieve webpage
import requests

# for retreiving information from websites 
from bs4 import BeautifulSoup

# to read arguments from command line
import os 

#To use numpy arrays which are more efficient than regular data structures
import numpy as np

#to add randomised waiting time
import time, random
#import xml.etree.ElementTree as ET
#import json

# for reading html
from lxml import html

##################################################################################



htmlpage = requests.get(
    'http://law.justia.com/cases/new-york/court-of-appeals/2016/').text
bs = BeautifulSoup(htmlpage)
possible_links = bs.find_all('a')
good_links = []

for link in possible_links:
    if (link.has_attr('class') and link['class']==['case-name']):
        good_links.append("http://law.justia.com" + link.attrs['href'])


all_texts = []

for idx, url in enumerate(good_links):
	#random delay between 1 and 2 secs
    delay = random.randint(1,2)
    #pause execution for delay seconds
    time.sleep(delay)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    txt = tree.xpath('//*[@id="opinion"]/text()')
    all_texts.append(txt)
    print idx


#Save remaining data to file    
file_name = "justia_2016" + '.txt'
np.savetxt(file_name, all_texts, delimiter=',', fmt='%s')

