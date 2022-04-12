import requests

cookies = {
    'bcookie': '"v=2&dafb93fb-7e04-41f9-83c3-2c1ecd04965b"',
    'bscookie': '"v=1&20220310023604ed4547a1-dc79-4694-8e70-55e9b3b43742AQEVmjqaUQQJvLeAkO7SpPpdHo3FDgJQ"',
    '_gcl_au': '1.1.947310258.1646879768',
    'aam_uuid': '55328011215210602892095764879695649408',
    'li_rm': 'AQF0xo3FJ_i4UgAAAX9xr2LiS9uZL1QLhGzBd4rI_d5_9gsyUtZthqipovvGQ8fIKFytMd_x4D6vbxbSxy8dbzlc5LgNEc4oAv-C9XYeN0ilgxOtIBCU6N5e',
    'JSESSIONID': '"ajax:7293579205689671566"',
    'li_theme': 'light',
    'li_theme_set': 'app',
    '_guid': '86f179ba-4563-408f-8bff-77323f523caf',
    'li_sugr': '01f2d46a-b956-4499-b822-786bbc3314f9',
    'lang': 'v=2&lang=zh-cn',
    'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
    'g_state': '{"i_p":1648636050040,"i_l":1}',
    'liap': 'true',
    'li_at': 'AQEDARWjsUYCNJFQAAABf9n5WWEAAAF__gXdYU4ARKydFyxYM6d-LmrMKKuov-ZkTO1MJuUiV2D8ULv6SxTh04rHYiXf0x34RsGsSMpvFUaUkDNVrnD_D7eKJ5hQyB_7XRb4WLzEunnL1Py7VGKkvfr1',
    'timezone': 'Asia/Shanghai',
    'AnalyticsSyncHistory': 'AQK_7r0I-ZwpnwAAAX_Z-arnIboOOPyyJ79DYHPRG3w_nsaJWX0jf5ah1S0YbUDKpdMahd9a5l-6Zt7k0x-HvA',
    'lms_ads': 'AQFKlQwerP9zIQAAAX_Z-ay5_yQpkGYGpZCffeS6lgNBIl0DUgR7Jy9bvBfzuKwSY9x_KqhcKYcejOX2yBSFGGhBvxnDweM8',
    'lms_analytics': 'AQFKlQwerP9zIQAAAX_Z-ay5_yQpkGYGpZCffeS6lgNBIl0DUgR7Jy9bvBfzuKwSY9x_KqhcKYcejOX2yBSFGGhBvxnDweM8',
    'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19082%7CMCMID%7C54784469213154985062151181517635545419%7CMCAAMLH-1649234297%7C11%7CMCAAMB-1649234297%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1648636697s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1423170193',
    'UserMatchHistory': 'AQLWzJrngEwARgAAAX_aGp_qycAqn-WkE7UQWTc511LCIvp_HnfgmVwi03a2RVNcuM58nrZ1y0NURQCcBUGHHe1TGDCkAQzYa_AWFkjFZsYGkOJOhfQIpKrRFZNF_fPbT_GYlSKkyRS7i-yimRE7BhMEJu7QODvd6TRHM1svB1VO-qbbr_64uEvm7ueCaiMVbiv_PlcLE2M4eEzff-1IvNwJ0n-5Oyd5nWHUPw-toWccNYEZXnDfeHKB26bLDaR2GmyZBvrFABgtREVns0CIIMHVbHo5Z2vRMdFkvIs',
    'lidc': '"b=OB86:s=O:r=O:a=O:p=O:g=2243:u=19:x=1:i=1648631655:t=1648715525:v=2:sig=AQEWlHBr0ezSXpoPeeIyGDA6qItclBXY"',
}

headers = {
    'authority': 'www.linkedin.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'bcookie="v=2&dafb93fb-7e04-41f9-83c3-2c1ecd04965b"; bscookie="v=1&20220310023604ed4547a1-dc79-4694-8e70-55e9b3b43742AQEVmjqaUQQJvLeAkO7SpPpdHo3FDgJQ"; _gcl_au=1.1.947310258.1646879768; aam_uuid=55328011215210602892095764879695649408; li_rm=AQF0xo3FJ_i4UgAAAX9xr2LiS9uZL1QLhGzBd4rI_d5_9gsyUtZthqipovvGQ8fIKFytMd_x4D6vbxbSxy8dbzlc5LgNEc4oAv-C9XYeN0ilgxOtIBCU6N5e; JSESSIONID="ajax:7293579205689671566"; li_theme=light; li_theme_set=app; _guid=86f179ba-4563-408f-8bff-77323f523caf; li_sugr=01f2d46a-b956-4499-b822-786bbc3314f9; lang=v=2&lang=zh-cn; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; g_state={"i_p":1648636050040,"i_l":1}; liap=true; li_at=AQEDARWjsUYCNJFQAAABf9n5WWEAAAF__gXdYU4ARKydFyxYM6d-LmrMKKuov-ZkTO1MJuUiV2D8ULv6SxTh04rHYiXf0x34RsGsSMpvFUaUkDNVrnD_D7eKJ5hQyB_7XRb4WLzEunnL1Py7VGKkvfr1; timezone=Asia/Shanghai; AnalyticsSyncHistory=AQK_7r0I-ZwpnwAAAX_Z-arnIboOOPyyJ79DYHPRG3w_nsaJWX0jf5ah1S0YbUDKpdMahd9a5l-6Zt7k0x-HvA; lms_ads=AQFKlQwerP9zIQAAAX_Z-ay5_yQpkGYGpZCffeS6lgNBIl0DUgR7Jy9bvBfzuKwSY9x_KqhcKYcejOX2yBSFGGhBvxnDweM8; lms_analytics=AQFKlQwerP9zIQAAAX_Z-ay5_yQpkGYGpZCffeS6lgNBIl0DUgR7Jy9bvBfzuKwSY9x_KqhcKYcejOX2yBSFGGhBvxnDweM8; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19082%7CMCMID%7C54784469213154985062151181517635545419%7CMCAAMLH-1649234297%7C11%7CMCAAMB-1649234297%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1648636697s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1423170193; UserMatchHistory=AQLWzJrngEwARgAAAX_aGp_qycAqn-WkE7UQWTc511LCIvp_HnfgmVwi03a2RVNcuM58nrZ1y0NURQCcBUGHHe1TGDCkAQzYa_AWFkjFZsYGkOJOhfQIpKrRFZNF_fPbT_GYlSKkyRS7i-yimRE7BhMEJu7QODvd6TRHM1svB1VO-qbbr_64uEvm7ueCaiMVbiv_PlcLE2M4eEzff-1IvNwJ0n-5Oyd5nWHUPw-toWccNYEZXnDfeHKB26bLDaR2GmyZBvrFABgtREVns0CIIMHVbHo5Z2vRMdFkvIs; lidc="b=OB86:s=O:r=O:a=O:p=O:g=2243:u=19:x=1:i=1648631655:t=1648715525:v=2:sig=AQEWlHBr0ezSXpoPeeIyGDA6qItclBXY"',
}
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

response = requests.get('https://www.linkedin.com/in/sabinaschaefer/', headers=headers,proxies=proxies, cookies=cookies)
print(response.status_code)