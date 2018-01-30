#!/usr/bin/env python3
# coding: utf-8

# In[19]:


import requests               #to request list of documents in htlm format
from bs4 import BeautifulSoup #to parse html
from datetime import datetime #to convert date to ISO8601
import pandas as pd           #to save it as csv. 
import urllib.request         #to download documents
import time                   #to give doc downloaded time to operate
import os                     #to create dirs and check existing ones
import shutil                 #to delete, move dirs
import csvdiff
import json                   #to open json files
import sys
# TODO:
# Change use of pandas to save to a csv file (use csv module instead)


# In[46]:


# CONSTANTS


SAVE_DOCS =int(sys.argv[1])
DEBUG_FLAG = int(sys.argv[2])
NEW_DIR = "./new-downloaded-docs/"
OLD_DIR = "./old-downloaded-docs/"

print(SAVE_DOCS)
# In[61]:


print("Loading website:")
if DEBUG_FLAG:
    r = open('./test-files/docs-day-2.html')
    soup = BeautifulSoup(r, 'html.parser')
else:
    tries_count = 0
    while True:
        try:
            r = requests.get('https://juntasupervision.pr.gov/index.php/en/documents/')
            break
        except:
            tries_count += 1
            if tries_count>10:
                print("Already tried 10 times...I'm giving up. Sorry.")
                break
            else:
                print("Could not access the website. Trying again...")
    soup = BeautifulSoup(r.content, 'html.parser')
print("Done.")


# In[62]:


# Documents are placed in each row, so go straight to it

doc_list_soup = soup.findAll("div",{"class": "doc-row"});


# In[63]:


# Store every document in a table row

table = []

for doc in doc_list_soup:
    title = doc.a.getText()
    
    category = doc.find("div",{"class": "span2 cat"}).getText()
    
    tmp_date = doc.find("div",{"class": "span2 date"}).getText()
    date = str(datetime.strptime(tmp_date, '%b.%d.%Y')) # convert to ISO-8601 date
    
    download_url = doc.a.get('href')
    
    download_title = doc.a.get('download')
    
    table.append( [title,category,date,download_url,download_title] )


# In[64]:


# Move the last downloaded data to the old directory so that the new
# data goes in the new directory. 

new_dir_exists = os.path.isdir(NEW_DIR)
old_dir_exists = os.path.isdir(OLD_DIR)

if new_dir_exists: #if new dir exists
    # move to the old dir, but delete current content of old dir first
    if old_dir_exists:
        for the_file in os.listdir(OLD_DIR):
            file_path = os.path.join(OLD_DIR, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
    for the_file in os.listdir(NEW_DIR):
        file_path = os.path.join(NEW_DIR, the_file)
        shutil.move(file_path, os.path.join(OLD_DIR,the_file))


# In[65]:


# Store data to a csv file

csv_filename = 'doc-table.csv'

df = pd.DataFrame(table)
df.columns = ['title','category','date','download_url','download_title']
df.to_csv(NEW_DIR+csv_filename,index=False)


# In[66]:


# Download documents

if SAVE_DOCS:
    num_files = len(df.download_url)

    for url,i in zip(df.download_url, range(num_files)):
        fn = url.split('/')[-1]    
        tries_count = 0

        while True:
            try:
                print("Downloading file #" + str(i+1) + "/" + str(num_files) + " - " + fn)
                urllib.request.urlretrieve(url, filename=NEW_DIR+fn)
                break
            except:
                tries_count += 1
                if tries_count>10:
                    print("Already tried 10 times...I'm giving up. Sorry")
                else:
                    print("Could not download file. Trying again.")

    print("Done.")


# In[67]:


# Check differences and store them in a json file format

json_filename = "differences.json"
try:
    os.remove(json_filename)
except:
    pass

os.system("csvdiff --style=pretty --output=" + json_filename + " title " +           OLD_DIR + "doc-table.csv " +           NEW_DIR + "doc-table.csv")

with open(json_filename) as json_data:
    d = json.load(json_data)
    print(json.dumps(d, indent=4))

