import base64
import datetime
import re

import requests
from bs4 import BeautifulSoup


def get_links(url):
    try:
        # 请求网页内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        page_text = soup.get_text()

        # 使用正则表达式提取vmess和vless链接
        vmess_links = re.findall(r'vmess://[^\s]+', page_text)
        vless_links = re.findall(r'vless://[^\s]+', page_text)

        # 输出结果
        all_links = []
        all_links.extend(vmess_links)
        all_links.extend(vless_links)
        return all_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []


def write_links_to_file(links, file_path):
    links_str = "\n".join(links)
    links_base64 = base64.b64encode(links_str.encode('utf-8'))

    with open(file_path, 'w') as file:
        file.write(links_base64.decode('utf-8'))


# 使用示例
if __name__ == "__main__":
    url = "https://github.com/Alvin9999/new-pac/wiki/v2ray%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"
    links = get_links(url)
    write_links_to_file(links, "links.txt")
