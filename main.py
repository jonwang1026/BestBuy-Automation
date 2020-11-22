from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import Personal_Info
import time


def order(web, info):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(web['url'])
    #refresh until add to cart shows up
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'add-to-cart-button')))
        except NoSuchElementException:
            driver.refresh()
        else:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                            'add-to-cart-button'))).click()
            break
    #go to cart webÍ
    driver.get(web['cart'])
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.NAME, 'availability-selection')))[
            1].click()
    except:
        driver.refresh()
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.NAME, 'availability-selection')))[
            1].click()
    #free ship options
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.NAME, 'availability-selection')))[1].click()
    time.sleep(1)
    #checkout button
    driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]'
                                 '/div/div/div[3]/div/div[1]/button').click() #checkout button


    #continue as guest
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/'
                                                                                  'section/main/div[4]/'
                                                                              'div/div[2]/button'))).click()
    except:
        driver.refresh()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[4]/'
                                                      'div/div[2]/button'))).click()
    time.sleep(2)

    #fill out form
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="consolidatedAddresses.ui_address_2.firstName"]'))) \
            .send_keys(info["firstname"])
    except:
        driver.refresh()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="consolidatedAddresses.ui_address_2.firstName"]'))) \
            .send_keys(info["firstname"])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.lastName"]').send_keys(info["lastName"])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.street"]').send_keys(info["street"])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.city"]').send_keys(info["city"])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.state"]/option[9]').click()  # state
    driver.find_element_by_xpath('//*[@id="user.emailAddress"]').send_keys(info["email"])
    driver.find_element_by_xpath('//*[@id="user.phone"]').send_keys(info["phone"])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.zipcode"]').send_keys(info["zip"])
    driver.find_element_by_xpath(
        '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button').click()
    time.sleep(0.5)
    #payment info
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="optimized-cc-card-number"]'))) \
            .send_keys(info["creditCard"])
    except:
        driver.refresh()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="optimized-cc-card-number"]'))) \
            .send_keys(info["creditCard"])
    driver.find_element_by_xpath('//*[@id="credit-card-expiration-month"]/div/div/select/option[5]').click()
    driver.find_element_by_xpath('//*[@id="credit-card-expiration-year"]/div/div/select/option[5]').click()
    driver.find_element_by_xpath('//*[@id="credit-card-cvv"]').send_keys(info["cvv"])
    time.sleep(1000)



order(Personal_Info.web, Personal_Info.info)