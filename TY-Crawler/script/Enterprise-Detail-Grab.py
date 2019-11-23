from selenium import webdriver
import time as t

e_ids = []
with open('./TY-Crawler/storage/target_enterprise_id_list.txt', 'r') as f:
    e_ids = [line.strip('\n') for line in f.readlines()]

url_template = 'https://www.tianyancha.com/company/{}'
block_data_template = ".block-data[tyc-event-ch='CompangyDetail.{}']"

driver = webdriver.Chrome()
driver.implicitly_wait(1)

main_handle = driver.current_window_handle


def jingyingyichang():
    key = 'jingyingyichang'
    data = []
    try:
        block_data = driver.find_element_by_css_selector(
            block_data_template.format(key))
    except Exception:
        print(key, 'none')
        return 0
    # trs = block_data.find_elements_by_css_selector('div>table>tbody>tr')
    num = block_data.find_element_by_css_selector(
        'div>span.data-count').text
    print(key, num)
    """ for tr in trs:
        print('in tr')
        start = tr.find_element_by_xpath('//td[2]').text()
        end = tr.find_element_by_xpath('//td[5]').text()
        data.append({
            'start': start,
            'end': end
        })
    print(key, data) """
    # return key,data
    return num


def biangengjilu():
    key = 'biangengjilu'
    data = []
    try:
        block_data = driver.find_element_by_css_selector(
            block_data_template.format(key))
        num = block_data.find_element_by_css_selector(
            'div>span.data-count').text
        print(num)
        while True:
            try:
                t.sleep(1)
                block_data = driver.find_element_by_css_selector(
                    block_data_template.format(key))
                tds = block_data.find_elements_by_css_selector(
                    'div>table>tbody>tr>td:nth-child(2)')
                for i, td in enumerate(tds):
                    time = td.text
                    data.append(time)
                    print(time)
                next_bn = block_data.find_element_by_css_selector('a.-next')
                driver.execute_script('arguments[0].click();', next_bn)
                print('next')
            except Exception as e:
                print(e)
                print(key, data)
                return data
    except Exception as e:
        print(e)
        print(key, 'none')
        return 0


def guquanchuzhi():
    key = 'guquanchuzhi'
    data = []
    try:
        block_data = driver.find_element_by_css_selector(
            block_data_template.format(key))
        num = block_data.find_element_by_css_selector(
            'div>span.data-count').text
        print(num)
        while True:
            try:
                t.sleep(1)
                block_data = driver.find_element_by_css_selector(
                    block_data_template.format(key))
                tds1 = block_data.find_elements_by_css_selector(
                    'div>table>tbody>tr>td:nth-child(2)')
                tds2 = block_data.find_elements_by_css_selector(
                    'div>table>tbody>tr>td:nth-child(6)')
                tds3 = block_data.find_elements_by_css_selector(
                    'div>table>tbody>tr>td:nth-child(7)')
                for i, td in enumerate(tds1):
                    date = td.text
                    state = tds2[i].text
                    money = tds3[i].text
                    data.append({
                        'date':date,
                        'state':state,
                        'money':money
                    })
                    print(date,state,money)
                next_bn = block_data.find_element_by_css_selector('a.-next')
                driver.execute_script('arguments[0].click();', next_bn)
                print('next')
            except Exception as e:
                print(e)
                print(key, data)
                return data
    except Exception as e:
        print(e)
        print(key, 'none')
        return 0


def zhuyaorenyuan():
    key = 'zhuyaorenyuan'
    data = []
    try:
        block_data = driver.find_element_by_css_selector(
            block_data_template.format(key))
        num = block_data.find_element_by_css_selector(
            'div>span.data-count').text
        print(num)
        while True:
            try:
                t.sleep(1)
                block_data = driver.find_element_by_css_selector(
                    block_data_template.format(key))
                tds = block_data.find_elements_by_css_selector(
                    'div>table>tbody>tr>td:nth-child(2)')
                for i, td in enumerate(tds):
                    link = td.find_element_by_css_selector('a.link-click')
                    driver.execute_script('arguments[0].click();', link)
                    peo = link.text
                    driver.switch_to.window(driver.window_handles[1])
                    t.sleep(0.5)
                    risk = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/span').text
                    print(peo,risk)
                    data.append({
                        'name':peo,
                        'risk':risk
                    })
                    driver.close()
                    driver.switch_to.window(main_handle)
                next_bn = block_data.find_element_by_css_selector('a.-next')
                driver.execute_script('arguments[0].click();', next_bn)
                print('next')
            except Exception as e:
                print(e)
                print(key, data)
                return data
    except Exception as e:
        print(e)
        print(key, 'none')
        return 0


def gudongxinxi():
    key = 'gudongxinxi'
    data = []
    try:
        block_data = driver.find_element_by_css_selector(
            block_data_template.format(key))
        num = block_data.find_element_by_css_selector(
            'div>span.data-count').text
        print(num)
        while True:
            try:
                t.sleep(1)
                block_data = driver.find_element_by_css_selector(
                    block_data_template.format(key))
                tds = block_data.find_elements_by_css_selector(
                    'div>table>tbody>tr>td:nth-child(2)')
                for i, td in enumerate(tds):
                    vip_link = td.find_element_by_css_selector('.link-vip')
                    if '股权结构' not in vip_link.text:
                        continue
                    link = td.find_element_by_css_selector('a.link-click')
                    company = link.text
                    driver.switch_to.window(driver.window_handles[1])
                    t.sleep(0.5)
                    risk1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/span').text
                    risk2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/span').text
                    print(peo,risk1,risk2)
                    data.append({
                        'name':company,
                        'risk':risk1+risk2
                    })
                    driver.close()
                    driver.switch_to.window(main_handle)
                next_bn = block_data.find_element_by_css_selector('a.-next')
                driver.execute_script('arguments[0].click();', next_bn)
                print('next')
            except Exception as e:
                print(e)
                print(key, data)
                return data
    except Exception as e:
        print(e)
        print(key, 'none')
        return 0


driver.get('https://www.tianyancha.com/login')
t.sleep(2)
driver.find_element_by_xpath(
    '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]').click()
driver.find_element_by_xpath(
    '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/input').send_keys('15882418677')
driver.find_element_by_xpath(
    '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[3]/input').send_keys('zaq1234567890')
driver.find_element_by_xpath(
    '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[5]').click()

input('wait for labor to login,hit any key to continue')

all_data = {}

for e_id in e_ids:
    driver.get(url_template.format(e_id))
    print('id', e_id)
    """ all_data['e_id'] = {
        'jingyingyichang': jingyingyichang(),
        'biangengjilu': biangengjilu(),
        'guquanchuzhi':guquanchuzhi(),
        'zhuyaorenyuan':zhuyaorenyuan(),
        'gudongxinxi':gudongxinxi()
    } """
    all_data['e_id'] = {
        'gudongxinxi':gudongxinxi()
    } 

print(all_data)
