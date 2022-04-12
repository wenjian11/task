#%%
import os
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
from mongo import LinkDB
from utils import dlProfilePic

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def wait_element(element):
    while True:
        try:
            return driver.find_element(By.CSS_SELECTOR, element)
        except:
            pass

def css_select(driver, element, all=False):
    try:
        if all:
            return driver.find_elements(By.CSS_SELECTOR, element)
        else:
            return driver.find_element(By.CSS_SELECTOR, element)
    except:
        return False

def get_profile():
    profile = css_select(driver, '.artdeco-card.ember-view.pv-top-card')
    if profile:
        name = css_select(profile, 'h1[class="text-heading-xlarge inline t-24 v-align-middle break-words"]')
        headline = css_select(profile, 'div[class="text-body-medium break-words"]')
        company = css_select(profile, 'div[aria-label="目前就职"]')
        education = css_select(profile, 'div[aria-label="教育经历"]')
        address = css_select(profile, 'span[class="text-body-small inline t-black--light break-words"]')

        name = name.text if name else ''
        headline = headline.text if headline else ''
        company = company.text if company else ''
        education = education.text if education else ''
        address = address.text if address else ''
        
        return {'name': name, 'headline': headline, 'company': company, 'edu': education, 'address': address}
    else:
        return {'name':'', 'headline':'', 'company':company, 'edu':'', 'address':''}

def crawl_about(element):
    if element:
        expand_button = css_select(element, '.inline-show-more-text__link-container-collapsed')
        if expand_button:
            expand_button.click()

        about = css_select(element, 'span[aria-hidden="true"]')
    if about:
        return about.text
    else:
        return ''

def crawl_usual(element):
    experiences = []
    if element:
        exp_button = css_select(element, 'div[class="pvs-list__footer-wrapper"]')
        if exp_button:
            exp_button.click()
            time.sleep(1)
            lis = css_select(driver, '.pvs-entity.pvs-entity--padded.pvs-list__item--no-padding-when-nested', True)
        else:
            lis = css_select(element, 'li', True)
            inl_buttons = css_select(element, '.inline-show-more-text__button.inline-show-more-text__button--light.link', True)
            for button in inl_buttons:
                button.click()

        for li in lis:
            if li.text != '':
                experiences.append(li.text)
        
        if exp_button: driver.back()

    return experiences

def crawl_skill(element):
    skills = []

    if element:
        exp_button = css_select(element, 'div[class="pvs-list__footer-wrapper"]')
        if exp_button:
            exp_button.click()
            time.sleep(0.2)
            print('thekips:1')
            see_all = css_select(driver, 'button[class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button"]')
            if see_all:
                see_all.click()
            print('thekips:2')

            lis = css_select(driver, '.pvs-entity.pvs-entity--padded.pvs-list__item--no-padding-when-nested', True) 
            print(len(lis))
        else:
            lis = css_select(element, 'li', True)

        print('thekips: get skills')
        for li in lis:
            if li.text != '':
                skill = li.text
                skills.append(skill[:skill.find('\n')])

        print('thekips: back')
        if exp_button: driver.back()

    return skills

def crawl(link, force=False):
    driver.get(link)
    print('thekips: get link')
    id = os.path.basename(link)
    if not force:
        if linkdb.exist(id):
            print('thekips: \'%s\' exists' % id)
            return

    print('thekips: not force')
    collection = get_profile()
    collection['_id'] = id
    print('thekips: get id')

    table = []  # Use table to recorde fields that have been crawled.
    flag = True # Use flag to recognize whether it doesn't chooses continue.
    while flag:
        flag = False
        # sections elements will change after click,
        # so we should end when a iterate process only chooses continue.
        sections = css_select(driver, 'section', True)
        for section in sections:
            div = css_select(section, 'div')
            if div:
                identifier = div.get_attribute('id')
                if identifier in table:
                    continue
                table.append(identifier)
            else:
                continue

            match identifier:
                case 'about': 
                    collection[identifier] = crawl_about(section)
                case 'experience': 
                    collection[identifier] = crawl_usual(section)
                case 'education': 
                    collection[identifier] = crawl_usual(section)
                case 'volunteering_experience':
                     collection[identifier] = crawl_usual(section)
                case 'licenses_and_certifications': 
                    collection[identifier] = crawl_usual(section)
                case 'skills': 
                    collection[identifier] = crawl_skill(section)
                case 'interests': 
                    collection[identifier] = crawl_usual(section)

            flag = True

    # print(collection)
    linkdb.insert_one(collection)

# # Link to MongoDB.
# linkdb = LinkDB() 
# # Start Google Chrome.
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=127.0.0.1:7890')
# # options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)

# # Query the keyword.
# query = 'site:linkedin.com University of California'
# driver.get("https://www.bing.com")
# q = driver.find_element(By.NAME, 'q')
# q.send_keys(query)
# q.send_keys(Keys.ENTER)
# # Get all links.
# num_pages = int(input('Please input pages: '))
# links = []
# for i in range(num_pages):
#     title = driver.find_elements(By.TAG_NAME, 'cite')
#     for x in title:
#         if 'www.linkedin.com/in/' in x.text:    # Sift personal profile.
#             if x.text not in links:
#                 links.append(x.text)
#     if num_pages - 1 == i: break

#     next_page = driver.find_element(By.CSS_SELECTOR, 'a[title="下一页"]')
#     next_page.send_keys(Keys.ENTER)

# print(len(links))
# data = {'index': 1, 'urls': links}
# with open('config.json', 'w') as f:
#     json.dump(data, f)


# download all.
# # Add cookies.
# driver.get("https://www.linkedin.com")
# with open('cookie.json', 'r') as f:
#     cookies = json.load(f)
# for key in cookies:
#     cookie = {'name': key, 'value': cookies[key]}
#     driver.add_cookie(cookie)

# time.sleep(2)
# # Begin crawling.
# for link in links:
#     crawl(link, True)


SWITCH = 1  # 0 means com, 1 means cn.

# Only download pictures.
with open('config.json', 'r') as f:
    data = json.load(f)

cnt = 0
count = 0
for url in data['urls']:
    if cnt != data['index']:
        cnt += 1
        continue

    if SWITCH == 1:
        url = url.replace('https://www.linkedin.com', 'https://www.linkedin.cn')
    print(url, 'HANDING')
    dlProfilePic(url, SWITCH)

    cnt += 1
    data['index'] += 1
    with open('config.json', 'w') as f:
        json.dump(data, f)

    time.sleep(random.randint(40, 80))
    count += 1
    if count % 15 == 0:
        time.sleep(random.randint(2500, 2900))
