#! usr/bin/env python3

"""
yt_search.py - Searches YouTube with the user's query, and opens up a web browser with the top
result.
"""

from bs4 import BeautifulSoup
import webbrowser
import requests


def get_top_yt_result(url):
    res = requests.get(url)
    # check to see if the request was successful
    try:
        res.raise_for_status()
    except Exception as e:
        print('There was an error: {}'.format(e))
        return None
    html_content = res.content
    soup = BeautifulSoup(html_content, 'lxml')
    search_results = soup.find_all('a', class_='yt-uix-sessionlink spf-link ')
    top_result_url = 'https://www.youtube.com/{}'.format(search_results[0]['href'])
    return top_result_url

if __name__ == '__main__':
    search_query = input('YT Search Query: ').lower().strip().replace(' ', '+')
    yt_url = 'https://www.youtube.com/results?search_query={}'.format(search_query)
    top_result = get_top_yt_result(yt_url)
    if top_result is not None:
        webbrowser.open(top_result)
