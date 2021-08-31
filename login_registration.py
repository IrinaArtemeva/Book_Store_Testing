from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def register_new_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(3)
    a_menu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
    a_menu.click()
    email = driver.find_element_by_id("reg_email")
    email.send_keys("test124883@test.ru")
    password = driver.find_element_by_id("reg_password")
    password.send_keys("7CCPh1QvBg")
    register_btn = driver.find_element_by_css_selector('[value="Register"]')
    register_btn.click()
    driver.quit()


def user_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(5)
    a_menu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
    a_menu.click()
    email = driver.find_element_by_id("username")
    email.send_keys("test124883@test.ru")
    password = driver.find_element_by_id("password")
    password.send_keys("7CCPh1QvBg")
    login_btn = driver.find_element_by_name("login")
    login_btn.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a'))
    )
    driver.quit()


register_new_user()
user_login()
