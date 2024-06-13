import requests
import datetime
from bs4 import BeautifulSoup
current_date = datetime.datetime.now().strftime("%Y%m%d")
url = "https://clashgithub.com/clashnode-{}.html".format(current_date)
req = requests.get(url)
req.encoding = 'utf-8'
if req.status_code == 200:
    soup = BeautifulSoup(req.text, 'html.parser')
    pre_tags = soup.find_all('pre')
    pre_tags = [tag.text.strip() for tag in pre_tags]
    pre_tags = [tag.split('\r\n') for tag in pre_tags]
    with open('upload/clashgithub.txt', 'w', encoding='utf-8') as f:
        for tag in pre_tags[0]:
            f.write(tag)
            f.write('\n')
else:
    print("request failed, code {}".format(req.status_code))
