import argparse
import base64
import re

import requests
from bs4 import BeautifulSoup


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, help='a website containing vmess or vless links text.')
    parser.add_argument('-ar', '--additional-regex', required=False, help='add more regex to match links.')
    return parser.parse_args()


def get_links(args):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        response = requests.get(args.url, headers=headers)
        response.raise_for_status()
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')
        page_text = soup.get_text()

        vmess_links = re.findall(r'vmess://[^\s]+', page_text)
        vless_links = re.findall(r'vless://[^\s]+', page_text)
        additional_links = re.findall(f'{args.additional_regex}', page_text)

        all_links = []
        all_links.extend(vmess_links)
        all_links.extend(vless_links)
        all_links.extend(additional_links)
        return all_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []


def write_links_to_file(links, file_path):
    links_str = "\n".join(links)
    links_base64 = base64.b64encode(links_str.encode('utf-8'))

    with open(file_path, 'w') as file:
        file.write(links_base64.decode('utf-8'))


if __name__ == "__main__":
    args = parse_args()
    links = get_links(args)
    write_links_to_file(links, 'links.txt')
