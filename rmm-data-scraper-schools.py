#Thanks to Christopher Reeves for his excellent introductory YouTube tutorials on how to build a web scraper.
#Christopher Reeves Web Scraping Tutorial
#getting page source with python
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

#Author (derived): Shirley Hicks
#http://www.velochicdesign.com
#http://twitter.com/velochicdunord

#This data scraper was written to automate gathering of information about what Birmingham regional schools are providing for tech education.

#Chris's existing imports - may not be useful for this application
import urllib #remove this at a later date. Used for samples, but wont use for my file.
import urllib2
import mechanize
from bs4 import BeautifulSoup
import MySQLdb
import datetime

#I added this based on Chris's earlier tutorial:
import re

#First, we need to retrieve and save to a .csv file the Alabama State Board of education dataset of regional schools, with contact info. Saved as a .csv file at http://web.alsde.edu/home/SchoolInfo/Default.aspx

alsdeURL = 'https://web.alsde.edu/EdDirToList/Default.aspx?listtype=principal&dataformat=csv' #this is the source file

openurl(alsdeURL)

#def searchAP(searchterm):
#    newlinks = []
#    browser = mechanize.Browser()
#    browser.addheaders = [('User-agent', 'Firefox')]
#    text = ""
#   start = 0
#    while "There were no matches for your search" not in text:
#        url = "http://hosted.ap.org/dynamic/external/search.hosted.ap.org/wireCoreTool/Search?SITE=AP&SECTION=HOME&TEMPLATE=DEFAULT&start_at="+str(start)+"&query="+searchterm
#       text = urllib.urlopen(url).read()
#       soup = BeautifulSoup(text)



#       results = soup.findAll('a')
#       for r in results:
#            if "TEMPLATE=DEFAULT" in r['href'] and "/dynamic" in r["href"]:
#               newlinks.append("http://hosted.ap.org"+ str(r["href"]))
#       start +=25

#   return newlinks

#print searchAP("cars")
#Status API Training Shop Blog About Pricing
#© 2015 GitHub, Inc. Terms Privacy Security Contact Help
