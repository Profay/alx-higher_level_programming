#!/usr/bin/python3
""" This module fetch response from github url and
print the last 10 commit
"""

from sys import argv
from requests import get


def get_commits():
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

    try:
        r = get(url)
        j = r.json()
        for commit in j[:10]:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit')
                                  .get('author')
                                  .get('name')))
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    get_commits()
