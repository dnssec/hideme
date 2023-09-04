import requests

burp0_url = "https://www.whitepages.com:443/name/Shawn-Keszler?fs=1&searchedName=Shawn%20Keszler"
burp0_cookies = {"cf_clearance": "fJurfVKuwrTmK9BRY4OdB.0oE6ajxVLs3fXDfaGi3u4-1693837873-0-1-afe7a181.811e9b1c.a99fde3d-0.2.1693837873", "wp_pid": "12efae9183ae4611b18fc76778e095cc", "_ga": "GA1.2.1997982928.1693559380", "amp_4452f9": "SP7IZoW9Gcgfs7I4QM2Do3...1h9g9ljst.1h9g9md6e.i.i.14", "OptanonConsent": "groups=C0004%3A0%2CC0001%3A1%2CC0002%3A1%2CC0003%3A1&datestamp=Mon+Sep+04+2023+09%3A31%3A42+GMT-0500+(Central+Daylight+Time)&version=202306.2.0&isGpcEnabled=1&hosts=&consentId=7b14764f-b719-46de-ad76-e2d62b82d78b&landingPath=NotLandingPage", "initial_referrer": "", "initial_referring_domain": "", "semUtmParams": "%7B%7D", "_csrf": "5wEsY6H6kopYhlbShWUF0suX", "com_whitepages_wp_app_test": "0", "__cf_bm": "rcXyXSPQoVDI0hNjUzhAr7IbgZ10o97qJY1nNlXxrCY-1693837871-0-Ad16u+6l0Za11TBmv4PpGw24kJ5pYqq7B6Y01clPJnZqflHv/1vrQ6NnVYvB4ILExDjP92UgyV5aMSVt/p3+o2U=", "_gcl_au": "1.1.612922273.1693837875", "_gid": "GA1.2.201868166.1693837893", "OptanonAlertBoxClosed": "2023-09-04T14:31:42.758Z"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Referer": "https://www.whitepages.com/suppression-requests", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "same-origin", "Sec-Fetch-Site": "same-origin", "Cache-Control": "max-age=0", "Te": "trailers", "Connection": "close"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

import requests

session = requests.session()

burp0_url = "https://www.whitepages.com:443/name/Shawn-Keszler/SD?fs=1&searchedName=Shawn%20Keszler"
burp0_headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Connection": "close"}
session.get(burp0_url, headers=burp0_headers)
