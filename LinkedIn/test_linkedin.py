import json
import random
import time
from threading import Thread, Lock
import requests
from requests.adapters import Retry, HTTPAdapter
import html
import os
from lxml import etree
#import http.client
#http.client.HTTPConnection._http_vsn = 10
#http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

mutex = Lock()


def get_cookies_list():
    try:
        with open("cookie.json", "r") as f:
            return json.loads(f.read())
    except:
        print("Failed to read the cookies.json.")


data = get_cookies_list()
index = list(data.keys())
cookies = list(data.values())

C_COUNT = len(cookies)
T_COUNT = 0

headers = [
    {
        "authority": "www.linkedin.cn",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en,zh;q=0.9,zh-CN;q=0.8",
        "cache-control": "max-age=0",
        # Requests sorts cookies= alphabetically
        # 'cookie': 'bcookie="v=2&d9e8a714-aead-44ad-8a45-d394f52d5826"; bscookie="v=1&20220310032939fa1db3b0-7101-4e2f-820f-0c576b16e379AQHOTLr9vW3J4lycgLe7iFjimeuFKpS7"; li_rm=AQENWetDAtlkjAAAAX9x4AJb7_BPIgOLtqVDwxAzXblYv1wmrlAKZBy19TnL8bQOF7Yngnvhvn76xW4JkjLHw8GmuhcSmZnFzgX3oiPdp6CgwVSdoMW9G4G6; _gcl_au=1.1.843858691.1646901344; lang=v=2&lang=en-us; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19084%7CMCMID%7C60113125625897201843784351111825410046%7CMCOPTOUT-1648810194s%7CNONE%7CvVersion%7C5.1.1%7CMCAAMLH-1649407794%7C11%7CMCAAMB-1649407794%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; aam_uuid=60267572841279768833768273143941542965; li_at=AQEDATrWSEsBK1qiAAABf-RTX9sAAAGACF_j21YAwvOKxb69sWR7RA_81yLXWZb9LUPV5ZpRqP392uRAWL3ebq2LN20hWwJrf4b-6Y41kDPggucYiOUPmtroKMF4Gzhn9EBOSyYVgRmlzwzoDjZ0MkUu; liap=true; wwepo=true; JSESSIONID=ajax:2190211972747737782; lidc="b=OGST03:s=O:r=O:a=O:p=O:g=2628:u=1:x=1:i=1648803143:t=1648889543:v=2:sig=AQGgkzg3XccpFnPzebMQAZv1FdosBuf3"; li_cc=AQFb6SS84qrY8QAAAX_kU2Cd3c4NDwD9ZTzQC0OtC6l5AbxzQz3rOZtqKGPZtIo0QNCC7EdBcyNk',
        "dnt": "1",
        "referer": "https://www.linkedin.cn/injobs/onboarding/discoverability?session_redirect=https%3A%2F%2Fwww.linkedin.cn%2Finjobs",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
#        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    }
]

proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}


def write_no_pic_list(url):
    mutex.acquire()
    with open("no_pic_list.txt", "a+") as f:
        f.write(os.path.basename(url) + "\n")
    mutex.release()

def write_error_list(url):
    mutex.acquire()
    with open("no_error.txt", "a+") as f:
        f.write(os.path.basename(url) + "\n")
    mutex.release()


def dlProfilePic(id, url_index, url, switch, header, cookie):
    session = requests.Session()
    response = ''
    c = 0
    # session.max_redirects = 3
    while response == '':
	    c += 1
	    if c == 10:
	        print('尝试次数过多')
	        break
	    try:
	        response = session.get(url, headers=header, cookies=cookie)
	    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError) as err:
	        print('url_index %d, %s'%(url_index,url), 'requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError')
	        time.sleep(100)
	        continue
	    except BaseException as e:
	        e = str(e)
	        if "Connection to www.linkedin.cn timed out" in e:
	            return -1
	
	        if "redirects" in e:
	            return 302
	
    if response != '':
        status_code = response.status_code
    else:
        write_error_list(url)
        return 789

    if status_code != 200:
        return status_code
    else:
        # print('thekips: got html code.')
        res = html.unescape(response.text)
        if res.find("profile-displayphoto-shrink") == -1:
            return -2

        if switch == 1:
            beg = res.find('"picture":')
            beg = res.find("800_800", beg)
            index1 = res.find('",', beg)
            index2 = res.find('"rootUrl"', beg)
            index3 = res.find('",', index2)

            img_url = res[index2 + 11 : index3] + res[beg:index1]
        else:
            # ProfilePhotoDecoSpecEditableBackgroundPicture
            beg = res.find("ProfilePhotoDecoSpecEditableBackgroundPicture")
            beg = res.find("https://media-exp1.licdn.com/dms/image", beg)
            end = res.find("}]", beg)
            res = res[beg:]
            index1 = res.find('"')
            index2 = res.rfind("fileIdentifyingUrlPathSegment") + 32
            index3 = res.find('"', index2)
            img_url = res[:index1] + res[index2:index3]

        dl_Pic(id, url_index, url, img_url)
        return 0


def dl_Pic(id, url_index, url, img_url):
#    response = requests.get(img_url)
#    response = ''
   
    try:
        response = requests.get(img_url)
        if response.status_code != 200:
            print(
                "[%d] %d/%d %s IMAGE ERROR %d"
                % (id, url_index, dispatcher.return_len(), url, response.status_code)
            )
        else:
            with open("pictures/" + os.path.basename(url) + ".jpg", "wb") as f:
                f.write(response.content)
    except:
        print(
            "[%d] %d/%d %s TRY AGAIN" % (id, url_index, dispatcher.return_len(), url)
        )
        dl_Pic(id, url_index, url, img_url)


def update_data(thread_index):
    data.pop(thread_index)
    with open("cookie.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)
    print("==============================================")
    print("WARNING, A COOKIE HAS BEEN BANED!!!")
    print("==============================================")


class Dispatcher:
    def __init__(self):
        self.index = self.get_index()
        self.id_list = eval(self.get_id_list())
        self.id_len = len(self.id_list)

    def get_index(self):
        with open("index.txt", "r") as f:
            idx = f.readline()
            if idx == "":
                return 0
            return int(idx)

    def get_id_list(self):
        with open("id.txt", "r") as f:
            return f.read()

    def return_len(self):
        return self.id_len

    def return_id(self):
        with open("index.txt", "w") as f:
            f.write(str(self.index))
        self.index += 1

        if self.index < self.id_len + 1:
            return self.id_list[self.index - 1], self.index
        else:
            return -1, self.index

    def return_fin(self):
        return True if self.index >= self.id_len else False


dispatcher = Dispatcher()


class MyThread(Thread):
    def __init__(self, thread_index, header, thread_cookie):  # 可以通过初始化来传递参数
        super(MyThread, self).__init__()
        self.index = thread_index
        self.cookie = thread_cookie
        self.header = header
        self.total = dispatcher.return_len()

    def run(self):  # 必须有的函数
        cnt = 0
        flag = False
        while True:
            if flag:
                print("{} restart".format(self.index))
                flag = False
            cnt += 1

            mutex.acquire()
            url, url_index = dispatcher.return_id()
            mutex.release()

            if url == -1:
                print("FINISHED TASK")
                return

            url = url.replace(
                "https://www.linkedin.com", "https://www.linkedin.cn/injobs"
            )

            while True:
                print("[%d] %d/%d %s" % (self.index, url_index, self.total, url))
                ret_code = dlProfilePic(
                    self.index, url_index, url, 1, self.header, self.cookie
                )

                if ret_code == 999:
                    print(
                        "[%d] %d/%d %s BAN!!!"
                        % (self.index, url_index, self.total, url)
                    )
                    global C_COUNT
                    C_COUNT -= 1
                    update_data(self.index)
                    return
                elif ret_code == -2:
                    print(
                        "[%d] %d/%d %s NO PICTURE"
                        % (self.index, url_index, self.total, url)
                    )
                    write_no_pic_list(url)
                    break
                elif ret_code == 0:
                    print(
                        "[%d] %d/%d %s SUCCESS"
                        % (self.index, url_index, self.total, url)
                    )
                    break
                elif ret_code == 302:
                    print(
                        "[%d] %d/%d %s TOO MANY REDIRECTS"
                        % (self.index, url_index, self.total, url)
                    )
                    break
                elif ret_code != -1:
                    print(
                        "[%d] %d/%d %s ERR CODE %d"
                        % (self.index, url_index, self.total, url, ret_code)
                    )
                    break

            time.sleep(random.randint(40, 80))
            if cnt == 15:
                print("[%d] SLEEP" % self.index)
                time.sleep(random.randint(2500, 2900))
                cookies.append(self.cookie)
                index.append(self.index)
                return


if __name__ == "__main__":
    if not os.path.exists("pictures"):
        os.mkdir("pictures")

    while True:
        if dispatcher.return_fin():
            break

#        if len(index) >= int(1 / 3.0 * C_COUNT):
        if len(index) > 0:
            c_index = random.randint(0, len(index) - 1)
            h_index = random.randint(0, len(headers) - 1)

            MyThread(int(index[c_index]), headers[h_index], cookies[c_index]).start()

            index.pop(c_index)
            cookies.pop(c_index)

        time.sleep(random.randint(14, 18))

    print("TASK SUCCESS")
