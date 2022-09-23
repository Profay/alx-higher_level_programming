#!/usr/bin/python3
""" This module fetch response from github url and
print the last 10 commit
"""

import sys
import requests


def get_commits():
        """ This function print the last 10 commits
        """
        url = "https://api.github.com/repos/sys.argv[2]/sys.argv[1]/commits"
        response = requests.get(url)
        my_dict = response.json()
        for commit in my_dict[:10]:
                print("{}: {}".format(commit.get(sha),/
                                      commit.get(commit)/
                                      get(author).get(name)


if __name__ == "__main__":
        get_commits()


