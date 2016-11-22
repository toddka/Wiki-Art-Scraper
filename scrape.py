import urllib
import requests
import json
import sys
import time
from bs4 import BeautifulSoup
from xml.etree import ElementTree


reload(sys)  # Reload system to fix some encoding issues
sys.setdefaultencoding('UTF8')

def getImgUrls():
    imgURLs=[]
    i=1
    download = 0
    while True:
        try:
            string = "https://www.wikiart.org/en/paintings-by-style/impressionism?json=2&page=" + str(i)
            r = requests.post(string)
            data = json.loads(r.text)
        #KeyError occurs if the website boots us out temporarily
        except ValueError:
            print 'Reached the end of list - JSON object not detected... saving URLs'
            break
        #Parsing json for 'image' keys
        j=0
        for img in data['Paintings']:
            try:
                imgURLs.append(img['image'])
            except:
                print "Error adding JSON urls"
        i+=1
        break
        print "Saving the " + str(i*60) + "th image url"
    return imgURLs

def saveImg(downloadURLs, saveLocation):
    i = 1
    download = 0
    try:
        for url in downloadURLs:
            try:
                urllib.urlretrieve(url, (saveLocation) + '/img' + str(i) +url[-4:])
            except:
                print "Save Failed"
            download+=1
            i+=1
            time.sleep(.5) #Give servers a break
            print 'Downloaded ' + str(download) +' images...'
    except:
        print 'Invalid Save Location'

def execute(saveLocation):
    print "Getting list of img URLs..."
    imgURLs = getImgUrls()
    print "Saving urls..."
    saveImg(imgURLs, saveLocation)
    print 'Save complete!'

#Example: execute('toddashley13','Desktop')
execute('imgs')
