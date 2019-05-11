from lxml import etree
import requests


def get_url_from_sitemap(url_sub_sitemap):
    r = requests.get(url_sub_sitemap)
    root = etree.fromstring(r.content)
    print("The number of sitemap tags are {0}".format(len(root)))
    xmlDict = {}
    urls_tvpl = []
    for sitemap in root:
        children = sitemap.getchildren()
        xmlDict[children[0].text] = children[1].text
        link = children[0].text
        # print(link)
        urls_tvpl.append(link)
    return urls_tvpl
