# Distributed Url Crawler

> Distributed Url Crawler

## Version
Status: Development

Start date: 03/2019


## Structure

Full Document: [Wiki](#)



### Installation

```bash
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt


# Change project folder path
# Change folder output path

source venv/bin/activate
python init.py

# Run crawl url news
python collection_url/collect_news.py

python worker/update_urls_service.py 
python worker/select_urls.py
python worker/crawler.py



```

#### Development

```bash
git config credential.helper store
pip freeze > requirements.txt

```

### Deploy
```bash

sudo -s
apt-get update
apt-get install -y git zip unzip htop screen
apt-get install -y software-properties-common python-software-properties
add-apt-repository ppa:jonathonf/python-3.6
apt-get update
apt-get install python3.6


export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
sudo apt-get -y upgrade
python3 -V
apt-get install -y python3-pip
apt-get install -y build-essential libssl-dev libffi-dev python-dev
apt-get install -y python3-venv
pip3 install virtualenv 
apt install -y python-pip
pip install --upgrade pip
pip install --upgrade pip3

pip3 install --user --upgrade pip




mkdir git
cd git
git clone 
cd DistributedUrlCrawler

virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt

git config credential.helper store

git pull

# TODO update init_deploy
python init_server.py


```

## Team

Tran Minh Tuan - tuantmtb@gmail.com - [facebook](https://www.facebook.com/tuantmtb)
