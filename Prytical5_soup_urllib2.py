"""
Created on Wed Apr  4 16:00:48 2018
images crawler tested on Python2.7 on Ubuntu 16.04.
Usage: python Prytical5_soup_urllib2.py --key "cat" --num 10 --dir "./data"
most part modified from Ref. https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57#file-scrapeimages-py-L35
@author: yongweiw
"""

from bs4 import BeautifulSoup
import urllib2
import os
import argparse
import sys
import json

def get_soup(url, header):
    req = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(req)
    return BeautifulSoup(response,'html.parser')

def main(args):
    parser = argparse.ArgumentParser(description='Scrap Google images')
    parser.add_argument('-k', '--key', default='cat', type=str, help='search key')
    parser.add_argument('-n', '--num', default=20, type=int, help='num images to save')
    parser.add_argument('-d', '--dir', default='./data', type=str, help='save directory')
    
    args = parser.parse_args()
    query = args.key
    max_images = args.num
    save_dir = args.dir
    
    query = query.split()
    query = '+'.join(query)
    
    url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    soup = get_soup(url, header)
    
    Images = []
    
    for tmp in soup.find_all("div", {"class": "rg_meta"}):
        link, Type = json.loads(tmp.text)["ou"], json.loads(tmp.text)["ity"]
        Images.append((link, Type))
        
    print("Find " + query + "'s images, starting downloading now!")
    for i , (img , Type) in enumerate( Images[0:max_images]):
        try:
            req = urllib2.Request(img, headers={"User-Agent": header})
            raw_img = urllib2.urlopen(req).read()
            
            if len(Type) == 0:
                f= open(os.path.join(save_dir, "img" + "_" + str(i+1) + ".jpg"),'wb')  
            else:
                f= open(os.path.join(save_dir, "img" + "_" + str(i+1) + "."+Type),'wb')
                print("Downloading " + query + " image {}..".format(i+1))
#                print("Downloading the" + i +"-th image..")  # error since i is number, thus cannot be concatenated      
            f.write(raw_img)
            f.close()
            
        except Exception as err:
            print("could not load:" + img)
            print(err)
            
    print("Downloading done!")
            
if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
            
