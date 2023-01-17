#!/usr/bin/python3
"""
A Python script that takes GitHub credentials(username & password)
and uses the GitHub API to display the user `id`
It must use Basic Authentication with a personal access token as password
to access to your information (only `read:user` permission is needed)
The first argument will be`username`& second argument will be password or PAT
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(r.json().get('id'))
