#!/usr/bin/python3
"""
A Python script that shows the last 10 commits of a repository in GitHub
The first argument will be the `repository name`
The second argument will be the `owner name`
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        r = get(url)
        json_o = r.json()
        for i in range(0, 10):
            print("{}: {}".format(json_o[i].get('sha'), json_o[i].get('commit')
                                  .get('author').get('name')))
    except Exception as ex:
        pass
