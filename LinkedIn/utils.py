#%%
import requests
import html
import os
from lxml import etree


cookies = {
    # 'bcookie': '"v=2&dafb93fb-7e04-41f9-83c3-2c1ecd04965b"',
    # 'bscookie': '"v=1&20220310023604ed4547a1-dc79-4694-8e70-55e9b3b43742AQEVmjqaUQQJvLeAkO7SpPpdHo3FDgJQ"',
    # '_gcl_au': '1.1.947310258.1646879768',
    # 'aam_uuid': '55328011215210602892095764879695649408',
    # 'li_rm': 'AQF0xo3FJ_i4UgAAAX9xr2LiS9uZL1QLhGzBd4rI_d5_9gsyUtZthqipovvGQ8fIKFytMd_x4D6vbxbSxy8dbzlc5LgNEc4oAv-C9XYeN0ilgxOtIBCU6N5e',
    # 'JSESSIONID': '"ajax:7293579205689671566"',
    # 'li_theme': 'light',
    # 'li_theme_set': 'app',
    # '_guid': '86f179ba-4563-408f-8bff-77323f523caf',
    # 'li_sugr': '01f2d46a-b956-4499-b822-786bbc3314f9',
    # 'lang': 'v=2&lang=zh-cn',
    # 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
    # 'g_state': '{"i_p":1648636050040,"i_l":1}',
    # 'liap': 'true',
    # 'li_at': 'AQEDARWjsUYCNJFQAAABf9n5WWEAAAF__gXdYU4ARKydFyxYM6d-LmrMKKuov-ZkTO1MJuUiV2D8ULv6SxTh04rHYiXf0x34RsGsSMpvFUaUkDNVrnD_D7eKJ5hQyB_7XRb4WLzEunnL1Py7VGKkvfr1',
    # 'timezone': 'Asia/Shanghai',
    # 'AnalyticsSyncHistory': 'AQK_7r0I-ZwpnwAAAX_Z-arnIboOOPyyJ79DYHPRG3w_nsaJWX0jf5ah1S0YbUDKpdMahd9a5l-6Zt7k0x-HvA',
    # 'lms_ads': 'AQFKlQwerP9zIQAAAX_Z-ay5_yQpkGYGpZCffeS6lgNBIl0DUgR7Jy9bvBfzuKwSY9x_KqhcKYcejOX2yBSFGGhBvxnDweM8',
    # 'lms_analytics': 'AQFKlQwerP9zIQAAAX_Z-ay5_yQpkGYGpZCffeS6lgNBIl0DUgR7Jy9bvBfzuKwSY9x_KqhcKYcejOX2yBSFGGhBvxnDweM8',
    # 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19082%7CMCMID%7C54784469213154985062151181517635545419%7CMCAAMLH-1649234297%7C11%7CMCAAMB-1649234297%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1648636697s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1423170193',
    # 'UserMatchHistory': 'AQLWzJrngEwARgAAAX_aGp_qycAqn-WkE7UQWTc511LCIvp_HnfgmVwi03a2RVNcuM58nrZ1y0NURQCcBUGHHe1TGDCkAQzYa_AWFkjFZsYGkOJOhfQIpKrRFZNF_fPbT_GYlSKkyRS7i-yimRE7BhMEJu7QODvd6TRHM1svB1VO-qbbr_64uEvm7ueCaiMVbiv_PlcLE2M4eEzff-1IvNwJ0n-5Oyd5nWHUPw-toWccNYEZXnDfeHKB26bLDaR2GmyZBvrFABgtREVns0CIIMHVbHo5Z2vRMdFkvIs',
    # 'lidc': '"b=OB86:s=O:r=O:a=O:p=O:g=2243:u=19:x=1:i=1648631655:t=1648715525:v=2:sig=AQEWlHBr0ezSXpoPeeIyGDA6qItclBXY"',



    # HaiTao
    "AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg": "1",
    "AMCV_14215E3D5995C57C0A495C55%40AdobeOrg": "-637568504%7CMCIDTS%7C19082%7CMCMID%7C90253975030174670091689183801432751504%7CMCAAMLH-1649233588%7C11%7CMCAAMB-1649233588%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1648635988s%7CNONE%7CvVersion%7C5.1.1",
    "JSESSIONID": "ajax:8498462594851442263",
    "_gcl_au": "1.1.425907791.1648628814",
    "aam_uuid": "90475997502740437221710805505452854875",
    "bcookie": "v=2&2a7060e7-a113-4d6c-8212-4588afd3500b",
    "bscookie": "v=1&202203300826243fb2d6e1-a8b7-4c69-8803-21f4ff7c0d45AQGHx_nlLMtDSnTR-ugeWSh1ZyeexI_x",
    "lang": "v=2&lang=zh-cn",
    "li_at": "AQEDATrK40UDiBZaAAABf9nvTPoAAAF__fvQ-lYAw3nE4rjqn1EBQs11cGCc2971feOBR8gJLJVBUdTqxHZoeXdrVjbxZmWl8HpVn5XxxCIoRe60dgM45ecamlhpWyRzpzxlm-xvFXjor9sv9kYYA053",
    "li_cc": "AQGmmmay9yX0CgAAAX_Z704CReYPMzjkPSpc0OE9Xng5uXnDICc1n7P75vmmGI6nCf9RVIsxk2cx",
    "li_rm": "AQEIt5pskSUJMgAAAX_Z7uHDolNTehISt1BF47tYPykcppKhATsbfW_aAZodI44sZ3E7a5s2f8UuPGaGb3-UzYycatdif-opAZ6DRYGlIRivrV_BvDNC0gzQ",
    "liap": "true",
    "lidc": "b=OGST04:s=O:r=O:a=O:p=O:g=2591:u=1:x=1:i=1648628813:t=1648715184:v=2:sig=AQHJDm-5RpUt3u64dV7qLFW6moeu72Xn",
    "wwepo": "true"

    #ou
    # "AnalyticsSyncHistory": "AQKryEGBZO6zawAAAX-vcwmz2P6KP4Af-QKUcH2CajTL-cX7YnKzZ5cZ2RL12mi452E1Y5jgbvS_J7xs9pWWBQ",
    # "JSESSIONID": "ajax:0445394188085472606",
    # "UserMatchHistory": "AQJa_1TOm5p8kAAAAX-vcwmzbUr5hQrHiaZrBCLbnRFEn2c9UvGLjQ_CtlBGx6kwbtwzB5wkieQBNA",
    # "bcookie": "v=2&2fc3114d-6716-4894-8163-f4dee27859cb",
    # "bscookie": "v=1&202109221240481cc06061-79f4-4451-8da4-a843bac06fcdAQGeQxc0siyFFIcsZNqHsNz7b1GVrFZJ",
    # "lang": "v=2&lang=zh-cn",
    # "li_at": "AQEDATrK_MQAM88SAAABf9nv76cAAAF__fxzp1YAoqOuJ4r9TVJvK_OI_vroe5QHohIWNwGjTksyZboX60kghBnz8EZfinTFvKVQ1FOwAot-u_XICeaXzpbksmCIPIk3C8Mhcah_PdRYHTcnWW8wFfe4",
    # "li_cc": "AQE8M082mf-4LwAAAX_Z7_BzWJ49svM3qop2cO_ru97Es8upqA5fHd8OSe2Br-NTF8FIEvj447Pc",
    # "li_rm": "AQH49oOkJjy9RwAAAX_GU9QTkmHJdLL-IuE6zk-m3rxnIppNgU8GXlYjsiQYM_y87dKZI_WJkijl2_PUhynlj5tSqRVkGebMxfVUUq3VTGpDGzV0JCwQ54CQ",
    # "li_sugr": "b85a77ad-b712-4f07-acab-2c967aa7f822",
    # "liap": "true",
    # "lidc": "b=OGST09:s=O:r=O:a=O:p=O:g=2225:u=1:x=1:i=1648628854:t=1648715254:v=2:sig=AQHcLWctD4DnCyockFOcy4TwnqPWZQt1",
    # "wwepo": "true"

    #huangbeing
    # "AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg": "1",
    # "AMCV_14215E3D5995C57C0A495C55%40AdobeOrg": "-637568504%7CMCIDTS%7C19082%7CMCMID%7C80673983653266533133621310667846638213%7CMCAAMLH-1649233416%7C11%7CMCAAMB-1649233416%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1648635816s%7CNONE%7CvVersion%7C5.1.1",
    # "JSESSIONID": "ajax:1590208914177592838",
    # "_gcl_au": "1.1.1842261345.1648628623",
    # "aam_uuid": "80147263841998121703642943573825300814",
    # "bcookie": "v=2&b691eb9e-7f37-4274-8cc8-06098e339cc8",
    # "bscookie": "v=1&20220330082333291a0001-e582-40e3-8b9a-90265a863181AQGbcblh2u3ivOrqAKXf6Nsh51XEtaZ4",
    # "lang": "v=2&lang=zh-cn",
    # "li_at": "AQEDATrK_JMCkBI-AAABf9nsaksAAAF__fjuS1YAfaSKCimmgSSfp2uMk12VS0v5J6lMTNp5jzEnHEaiUgLaxJq26oLqMZVyIf4uINLbP0vv7R_JGG53mwhZoNqnC60eB67tawPelmPBoAiX4GK9b-fl",
    # "li_cc": "AQFYldMNmz54IgAAAX_Z7GuB9KA3_dkiNmouXPhUy9XLSF17fQ0ISnvya1V030GDUEfUB9lzESvg",
    # "li_rm": "AQFOGFWNZ_enDgAAAX_Z7EPamNBiqkqO9W-YYiogt6q8ahMnLZvjavZxRUjcBX7OpfD9g4oCQHx7jRYYZYJfKiMdoXhr4bbckaSf7oo754MJMpnPrsB2ZQ89",
    # "liap": "true",
    # "lidc": "b=OGST03:s=O:r=O:a=O:p=O:g=2626:u=1:x=1:i=1648628624:t=1648714977:v=2:sig=AQEq0FqHYBXGjtE9SOfIfekT-wouMegU",
    # "wwepo": "true"

    #sufang
    # "AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg": "1",
    # "AMCV_14215E3D5995C57C0A495C55%40AdobeOrg": "-637568504%7CMCIDTS%7C19082%7CMCMID%7C88535047883677196920172957467285357116%7CMCAAMLH-1649248786%7C11%7CMCAAMB-1649248786%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1648651186s%7CNONE%7CvVersion%7C5.1.1",
    # "JSESSIONID": "ajax:0495610726586368720",
    # "bcookie": "v=2&ea1c8af7-b422-4486-8b10-be55aeee2a8e",
    # "lang": "v=2&lang=zh-cn",
    # "li_cc": "AQGwSfnzQ73uUQAAAX_a1vHBXhh6WyTtglEKHN0hXdNJBNnuJNXGfCPNQIq8LFCY6TV7PuWg9h0q",
    # "liap": "true",
    # "lidc": "b=OGST06:s=O:r=O:a=O:p=O:g=2366:u=1:x=1:i=1648643994:t=1648716839:v=2:sig=AQE0IQBbJDCxZFedUaLnjl-tZs6fBkpD",
    # "wwepo": "true"
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


def dlProfilePic(url, switch):
    print('url', url)
    response = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
    print(response.status_code)
    if response.status_code != 200:
        print('profile Error Code %d' % response.status_code)
    else:
        res = html.unescape(response.text)
        if res.find('profile-displayphoto-shrink') == -1:
            print('thekips:can\'t get the img url...')
            print('pass')
            return

        if switch == 1:
            beg = res.find('"picture":')
            beg = res.find('800_800', beg)
            index1 = res.find('",', beg)
            index2 = res.find('"rootUrl"', beg)
            index3 = res.find('",', index2)

            img_url = res[index2+11:index3] + res[beg:index1]
        else:
            # ProfilePhotoDecoSpecEditableBackgroundPicture
            beg = res.find('ProfilePhotoDecoSpecEditableBackgroundPicture')
            beg = res.find('https://media-exp1.licdn.com/dms/image', beg)

            end = res.find('}]', beg)
            res = res[beg:]


            index1 = res.find('"')
            index2 = res.rfind('fileIdentifyingUrlPathSegment') + 32
            index3 = res.find('"', index2)
            img_url = res[:index1] + res[index2:index3]

        print('thekips:img url is:', img_url)

        try:
            response = requests.get(img_url, proxies=proxies)
            print(img_url)
            if response.status_code != 200:
                print('image Error Code %d' % response.status_code)
            else:
                with open('pictures/' + os.path.basename(url) + '.jpg', 'wb') as f:
                    f.write(response.content)
                print(url, 'SUCCEES')
        except:
            print(img_url, 'FAILED')



def getURL(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        print('Network Error, Retrying')
        getURL(url)

def twitter2college(twt_ID):

    # Use Google search the twitter ID.
    # twt_ID = 'RepDerekKilmer'
    search_res = getURL('https://www.google.com/search?q=%s+education' % twt_ID)

    # Get url of wikipedia.
    begin_pos = search_res.find('https://en.wikipedia.org')
    end_pos = search_res.find('&', begin_pos)
    wiki_url = search_res[begin_pos:end_pos]

    # Get html from wiki_url and then resolve it.
    wiki_res = getURL(wiki_url)
    element = etree.HTML(wiki_res)
    education = element.xpath('//tr//th[contains(text(), "Education")]/..//a[@title]')

    # Resolve the college and specialty.
    dicts = ['College', 'Institude', 'University']
    college = []
    for i in range(len(education)):
        title = education[i].xpath('@title')[0]
        for dic in dicts:
            if dic in title:
                college.append(title)

    return college


if __name__ == '__main__':
    dlProfilePic('https://www.linkedin.cn/in/kathleen-keyser-58303b223', 1)
    # dlProfilePic('https://www.linkedin.cn/in/rachel-rothschild', 1)