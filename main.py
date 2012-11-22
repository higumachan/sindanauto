import pymongo
import urllib
import urllib2
import datetime
from BeautifulSoup import BeautifulSoup

SINDAN_URL = "http://shindanmaker.com/";

DEFAULT_NAME = "higumachan725"

def try_sindan(id, name):
    post_data = urllib.urlencode({"u": name});
    url = SINDAN_URL + str(id);
    html = urllib2.urlopen(url, post_data).read();
    bs = BeautifulSoup(html);
    result = {"result": bs.find(attrs={"class": "result"}).text, "title": bs.find("title").text, "url": SINDAN_URL + str(id)};

    return result


if __name__ == "__main__":
    conn = pymongo.Connection();
    db = conn.autosindan;

    now = datetime.datetime.now();
    
    sindans = db.sindans.find();
    for sindan in sindans:
        result = try_sindan(sindan, DEFAULT_NAME);
        print result

