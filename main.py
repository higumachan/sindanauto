import pymongo
import urllib2
import datetime
import BeautifulSoup

SINDAN_URL = "http://shindanmaker.com/";

def try_sindan(sindan):
    url = SINDAN_URL + str(sindan["_id"]);
    html = urllib2.urlopen(url).read();
    bs = BeautifulSoup(html);
    result = bs.find(attrs={"class": "result"}).text;
    print sindan["_id"], sindan["title"]

    return result


if __name__ == "__main__":
    conn = pymongo.connection();
    db = conn.autosindan;

    now = datetime.datetime.now();
    now.replace(houre=0, minuetus=0);
    sindans = db.sindans.find({"datetime": {"$gt": now, "$lt": now + datetime.timedelta(days=1));

    for sindan in sindans:
        result = try_sindan(sindan);
        print result

