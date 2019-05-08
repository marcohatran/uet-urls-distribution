from config.config_project import folder_output_path
from helper.reader_helper import store_json
from helper.sitemap_helper import get_url_from_sitemap


def crawl_vnexpress():
    urls = get_url_from_sitemap('https://vnexpress.net/articles-2019-sitemap.xml?m=4&d=24')
    file_output_urls_path = folder_output_path + '/vnexpress/urls.json'
    store_json(urls, file_output_urls_path)


def crawl_baomoi():
    urls = get_url_from_sitemap('https://baomoi.com/sitemaps/article-20190424.xml')
    file_output_urls_path = folder_output_path + '/baomoi/urls.json'
    store_json(urls, file_output_urls_path)


def crawl_baophapluat():
    urls = get_url_from_sitemap('http://baophapluat.vn/sitemaps/news-2019-4.xml')
    file_output_urls_path = folder_output_path + '/baophapluat/urls.json'
    store_json(urls, file_output_urls_path)


crawl_vnexpress()
crawl_baomoi()
crawl_baomoi()
crawl_baophapluat()
