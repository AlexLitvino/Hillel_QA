from random import *
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'
names_list = ['olena', 'val', 'katie', 'daisy', 'sasha', 'alex', 'randy', 'arnold', 'steve', 'maryjane', 'lesly',
              'michael', 'frazer',
              'william', 'sam']
surnames_list = ['doe', 'babyers', 'sriggs', 'johnsons', 'creeks', 'williamson', 'sanders', 'keene', 'queen', 'baggins',
                 'smith',
                 'hilland']


def email_generator():
    domains_list = ['@yahoo.com', '@com.ua', '@com.de', '@gmail.com']
    seq = choice(names_list) + choice(surnames_list)
    for _ in range(5):
        seq += chr(randint(48,57))
    current_email = seq + choice(domains_list)
    return current_email

def login_generator():
    seq = choice(names_list).capitalize() + choice(surnames_list).capitalize()
    for _ in range(2):
        seq += chr(randint(48,57)) + chr(randint(48,57))
    return seq

def password_generator():
    seq = ''
    for _ in range(5):
        seq += chr(randint(48,57)) + chr(randint(65,90))+chr(randint(97,122))
    return seq


def test_register_data_writer(*args):
    test_data =''
    for i in args:
        test_data += i +','
    test_data = test_data[:-1]
    with open('helpers/register_page_data.py', 'a') as f:
        f.writelines(test_data + '\n')
    f.close()


def create_registered_user(driver):
    driver.get ('https://hdrezka.ag/')

    register_button = driver.find_element (By.CSS_SELECTOR, 'a.b-tophead__register')
    register_button.click ()
    wait = WebDriverWait (driver, 5)

    register_popup = wait.until (EC.visibility_of_element_located ((By.ID, 'register-popup')))

    valid_register_email = email_generator()
    input_register_email = driver.find_element(By.ID, 'email')
    input_register_email.send_keys(valid_register_email)
    valid_register_login = login_generator()
    input_register_login = driver.find_element (By.ID, 'name')
    input_register_login.send_keys(valid_register_login)

    valid_register_password = password_generator()
    input_register_password = driver.find_element (By.ID, 'password1')
    input_register_password.send_keys(valid_register_password)

    register_submit_button = driver.find_element(By.XPATH, "//button[@name='submit']")
    register_submit_button.click()

    driver.delete_all_cookies()

    driver.refresh ()


    return [valid_register_login, valid_register_password]
