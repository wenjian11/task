import requests

cookies = {
    'bcookie': '"v=2&d9e8a714-aead-44ad-8a45-d394f52d5826"',
    'bscookie': '"v=1&20220310032939fa1db3b0-7101-4e2f-820f-0c576b16e379AQHOTLr9vW3J4lycgLe7iFjimeuFKpS7"',
    'li_rm': 'AQENWetDAtlkjAAAAX9x4AJb7_BPIgOLtqVDwxAzXblYv1wmrlAKZBy19TnL8bQOF7Yngnvhvn76xW4JkjLHw8GmuhcSmZnFzgX3oiPdp6CgwVSdoMW9G4G6',
    '_gcl_au': '1.1.843858691.1646901344',
    'lang': 'v=2&lang=en-us',
    'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
    'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19084%7CMCMID%7C60113125625897201843784351111825410046%7CMCOPTOUT-1648810194s%7CNONE%7CvVersion%7C5.1.1%7CMCAAMLH-1649407794%7C11%7CMCAAMB-1649407794%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
    'aam_uuid': '60267572841279768833768273143941542965',
    'li_at': 'AQEDATrWSEsBK1qiAAABf-RTX9sAAAGACF_j21YAwvOKxb69sWR7RA_81yLXWZb9LUPV5ZpRqP392uRAWL3ebq2LN20hWwJrf4b-6Y41kDPggucYiOUPmtroKMF4Gzhn9EBOSyYVgRmlzwzoDjZ0MkUu',
    'liap': 'true',
    'wwepo': 'true',
    'JSESSIONID': 'ajax:2190211972747737782',
    'lidc': '"b=OGST03:s=O:r=O:a=O:p=O:g=2628:u=1:x=1:i=1648803143:t=1648889543:v=2:sig=AQGgkzg3XccpFnPzebMQAZv1FdosBuf3"',
    'li_cc': 'AQFb6SS84qrY8QAAAX_kU2Cd3c4NDwD9ZTzQC0OtC6l5AbxzQz3rOZtqKGPZtIo0QNCC7EdBcyNk',
}

headers = {
    'authority': 'www.linkedin.cn',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en,zh;q=0.9,zh-CN;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'bcookie="v=2&d9e8a714-aead-44ad-8a45-d394f52d5826"; bscookie="v=1&20220310032939fa1db3b0-7101-4e2f-820f-0c576b16e379AQHOTLr9vW3J4lycgLe7iFjimeuFKpS7"; li_rm=AQENWetDAtlkjAAAAX9x4AJb7_BPIgOLtqVDwxAzXblYv1wmrlAKZBy19TnL8bQOF7Yngnvhvn76xW4JkjLHw8GmuhcSmZnFzgX3oiPdp6CgwVSdoMW9G4G6; _gcl_au=1.1.843858691.1646901344; lang=v=2&lang=en-us; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19084%7CMCMID%7C60113125625897201843784351111825410046%7CMCOPTOUT-1648810194s%7CNONE%7CvVersion%7C5.1.1%7CMCAAMLH-1649407794%7C11%7CMCAAMB-1649407794%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; aam_uuid=60267572841279768833768273143941542965; li_at=AQEDATrWSEsBK1qiAAABf-RTX9sAAAGACF_j21YAwvOKxb69sWR7RA_81yLXWZb9LUPV5ZpRqP392uRAWL3ebq2LN20hWwJrf4b-6Y41kDPggucYiOUPmtroKMF4Gzhn9EBOSyYVgRmlzwzoDjZ0MkUu; liap=true; wwepo=true; JSESSIONID=ajax:2190211972747737782; lidc="b=OGST03:s=O:r=O:a=O:p=O:g=2628:u=1:x=1:i=1648803143:t=1648889543:v=2:sig=AQGgkzg3XccpFnPzebMQAZv1FdosBuf3"; li_cc=AQFb6SS84qrY8QAAAX_kU2Cd3c4NDwD9ZTzQC0OtC6l5AbxzQz3rOZtqKGPZtIo0QNCC7EdBcyNk',
    'dnt': '1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
}

response = requests.get('https://www.linkedin.cn/injobs/in/conner-danskin', headers=headers, cookies=cookies)
print(response.status_code)