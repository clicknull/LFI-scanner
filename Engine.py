import requests
from http.cookies import SimpleCookie


class Engine:
    def __init__(self, urls, payloads, matches, cookie, verbose):
        self.urls = urls
        self.verbose = verbose
        self.payloads = payloads
        self.matches = matches
        self.cookies = cookie

    def start(self):
        cookie = SimpleCookie()
        request_cookies = {}

        if self.cookies is not None:
            cookie.load(self.cookies)

            for key, morsel in cookie.items():
                request_cookies[key] = morsel.value

        else:
            print("[*] No cookie set, continuing...")

        count_matched = 0
        for payload in self.payloads:
            for url in self.urls:
                urlTarget = url + payload
                r = requests.get(urlTarget, cookies=request_cookies)
                if self.verbose:
                    print('GET [{0}] {1}'.format(r.status_code, urlTarget))

                for match in self.matches[payload]:
                    if match in r.text:
                        print("Interesting: " + url + payload)
                        count_matched = count_matched + 1
                    if "syntax error" in r.text:
                        print("PHP error: " + url + payload)
        if count_matched == 0:
            print("[-] Nothing found")

        print("[*] Scan completed")
