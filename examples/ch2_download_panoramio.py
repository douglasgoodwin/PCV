import os
import urllib.request, urllib.parse, urllib.error, urllib.parse 
import json

"""
This is the Panoramio image download example from section 2.3.
"""

# query for images
url = 'http://www.panoramio.com/map/get_panoramas.php?order=popularity&set=public&from=0&to=20&minx=-77.037564&miny=38.896662&maxx=-77.035564&maxy=38.898662&size=medium'
c = urllib.request.urlopen(url)

# get the urls of individual images from JSON
j = json.loads(c.read()) 
imurls = []
for im in j['photos']:
    imurls.append(im['photo_file_url'])

# download images
for url in imurls:
    image = urllib.request.URLopener()
    image.retrieve(url, os.path.basename(urllib.parse.urlparse(url).path)) 
    print('downloading:', url)