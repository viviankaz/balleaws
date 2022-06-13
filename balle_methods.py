import datetime
from time import sleep
from selenium import webdriver # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import balle_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select # ----------add this import for drop down lists
# from selenium.webdriver import Keys# import selenium to the file
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

def setUp():
    print(f'Launch {locators.adv} Funnel')
    print(f'___________________________________________')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(50)
    # navigate to Balle Media Funnel
    driver.get(locators.bmfunnel_url)

    # check that Balle Media URL and the home page title are as expected
    if driver.current_url == locators.bmfunnel_url:
        print(f'Yey! {locators.adv} Funnel launched successfully!')
        print(f'{locators.adv} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.adv} Funnel did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'______________________________________________')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def grow_your_clinic():
    print(f'****************************************************')
    if driver.current_url == locators.bmfunnel_url and driver.title == locators.bm_home_page_title:
        driver.find_element(By.ID, 'modal_btn').click()
        print(f'Hello, You are on survey page1')
        sleep(0.25)
    else:
        driver.find_element(By.ID, 'modal_btn').click()
        sleep(0.25)


def page_one():
    print(f'*************Survey Page1********************************************')
    driver.find_element(By.ID, 'first_name').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'last_name').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'phone').send_keys(locators.phone_number)
    sleep(0.25)
    driver.find_element(By.ID, 'email').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)
    print(f'Congrats! You are moving one step ahead, Continue to Page 2')

def page_two():
    print(f'*************Survey Page2********************************************')
    assert driver.find_element(By.XPATH, '//h1[contains(., " Step 2 of 5")]').is_displayed()
    sleep(0.25)
    print(f'This is Page 2 , fill in the details')
    driver.find_element(By.ID, 'website').send_keys(locators.website)
    sleep(0.25)
    Select(driver.find_element(By.ID,'how_long_in_business')).select_by_value('2 - 5 Years')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'paying_patients')).select_by_value('51-100')
    sleep(0.25)
    driver.find_element(By.ID, 'area_you_serve').send_keys(locators.area)
    sleep(0.25)
    driver.find_element(By.ID, 'how_are_you_getting_clients').send_keys(locators.subject)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'current_advertising')).select_by_value('$1,001 - $5,000')
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)
    print(f'Congrats! You are moving one step ahead, Continue to Page 3')


def page_three():
    print(f'************* Survey Page3 ********************')
    assert driver.find_element(By.XPATH, '//h1[contains(., " Step 3 of 5")]').is_displayed()
    sleep(0.25)
    print(f'This is Page 3 , fill in the details')
    sleep(0.25)
    driver.find_element(By.NAME, 'current_monthly_revenue').click()
    sleep(0.25)
    random_revenue = random.choice(locators.monthly_revenue)
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'current_monthly_revenue')).select_by_visible_text(random_revenue)
    sleep(0.25)
    print(random_revenue)
    sleep(0.25)
    driver.find_element(By.ID, 'target_monthly_revenue').click()
    if random_revenue == locators.monthly_revenue[0]:
        driver.find_element(By.ID, 'target_monthly_revenue').send_keys('5000')
    elif random_revenue == locators.monthly_revenue[1]:
        driver.find_element(By.ID, 'target_monthly_revenue').send_keys('10000')
    elif random_revenue == locators.monthly_revenue[2]:
        driver.find_element(By.ID, 'target_monthly_revenue').send_keys('20000')
    elif random_revenue == locators.monthly_revenue[3]:
        driver.find_element(By.ID, 'target_monthly_revenue').send_keys('30000')
    elif random_revenue == locators.monthly_revenue[4]:
        driver.find_element(By.ID, 'target_monthly_revenue').send_keys('100000')
    elif random_revenue == locators.monthly_revenue[5]:
        driver.find_element(By.ID, 'target_monthly_revenue').send_keys('150000')
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)




def page_four():
    print(f'************* Survey Page 4 ********************')
    assert driver.find_element(By.XPATH, '//h1[contains(., " Step 4 of 5")]').is_displayed()
    sleep(0.25)
    print(f'This is Page 4 , fill in the details')
    sleep(0.25)
    driver.find_element(By.ID, 'daily_painful_problems').send_keys(locators.subject)
    sleep(0.25)
    driver.find_element(By.ID, 'biggest_obstacle').send_keys(locators.subject)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'how_willing')).select_by_index("2")
    sleep(0.25)
    driver.find_element(By.ID, 'how_soon_get_started').send_keys('2022-06-15')
    sleep(0.25)
    driver.find_element(By.ID, 'why_choose_you').send_keys(locators.why)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()
    sleep(0.25)


def page_five():
    print(f'************* Survey Page 5 ********************')
    assert driver.find_element(By.XPATH, f'//h1[contains(., " Thank you {locators.first_name}. Your Session is now booked")]').is_displayed()
    sleep(0.25)
    print(f'This is Page 5 , Thank you {locators.first_name}. Your Session is now booked')
    sleep(0.25)
    print('Check your inbox for your appointment')
    sleep(0.25)


# setUp()
# grow_your_clinic()
# page_one()
# page_two()
# page_three()
# page_four()
# page_five()
# tearDown()