import requests
from bs4 import BeautifulSoup

url = 'http://ticket.interpark.com/TPGoodsList.asp?Ca=Mus&Sort=1'
source_code = requests.get(url)
plain_text = source_code.text

soup = BeautifulSoup(plain_text, 'lxml')
interpark_address = 'http://ticket.interpark.com/'

# print(soup)
# for num, a in enumerate(soup.select('td.RKtxt > span.fw_bold > a')):
#     print(num+1, a.text)

for detail_address in soup.select('span.fw_bold > a'):
    detail_url = interpark_address + detail_address.get('href')

    detail_source_code = requests.get(detail_url)
    detail_plain_text = detail_source_code.text

    detail_soup = BeautifulSoup(detail_plain_text, 'lxml')

    # print(detail_soup)

    # for detail_info in detail_soup.select('div.TabA_Info > ul.info_Li > li'):
    #     print(detail_info)

    # 뮤지컬 이름
    raw_script = detail_soup.find_all('script')
    var_collection = str(raw_script[56])
    split_name_var = var_collection.split('var vGN =')
    musical_name = split_name_var[1].split(';')[0]
    print(musical_name)

    # 배우 리스트
    print('배우 리스트')
    for member in detail_soup.select('li.members > div > a'):
        name = member.text

        if name != '더보기 ':
            print(name)

    if True:
        break

