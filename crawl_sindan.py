from BeautifulSoup import BeautifulSoup
import urllib2
import pymongo
import datetime

LIST_URL = "http://shindanmaker.com/c/list?mode=%s"

def crawl(mode="hot"):
    url = LIST_URL % mode;
    
    html = urllib2.urlopen(url).read();
    bs = BeautifulSoup(html);
    sindans = get_sindan(bs);

    return sindans;

def get_sindan(bs):
    result = [];
    tags = bs.findAll("a", attrs={"class": "list_title"})
    for tag in tags:
        print tag;
        id = int(tag["href"][1:]);
        title = tag.text;
        result.append({"_id": id, "title": title});
    return result


if __name__ == "__main__":
    sindans = crawl();
    conn = pymongo.Connection();
    db = conn["autosindan"];
    db.sindans.insert(sindans);

