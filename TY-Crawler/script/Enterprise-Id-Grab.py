from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(1)

driver.get('https://www.tianyancha.com')

input('tap any key to continue')

target_url_template = 'https://www.tianyancha.com/search/or1000-ot2/p{}?key=酒店管理'
lines = []
for p in range(5):
    url = target_url_template.format(p+1)
    driver.get(url)
    print('url', url)
    for el in driver.find_elements_by_css_selector('.search-result-single'):
        data_id = el.get_attribute('data-id')
        money = el.find_element_by_css_selector("span[title*='万人民币']").get_attribute('title')
        print(data_id)
        lines.append('{},{}\n'.format(data_id,money))

with open('./TY-Crawler/storage/target_enterprise_id&money_list.txt', 'w') as f:
    f.writelines(lines)

driver.quit()
