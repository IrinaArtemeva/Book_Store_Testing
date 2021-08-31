from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def add_book():
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
    shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]')
    shop.click()
    driver.execute_script("window.scrollBy(0, 300);")
    book = driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]')
    book.click()
    title = WebDriverWait(driver, 3).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[itemprop="name"]'), "HTML5 Forms"))
    print(title)
    driver.quit()


def number_of_goods():
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
    shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]')
    shop.click()
    html = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]')
    html.click()
    n = len(driver.find_elements_by_css_selector("a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart"))
    assert n == 3
    driver.quit()


def sorting():
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
    shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]')
    shop.click()
    sorting_selector = driver.find_element_by_css_selector("[name='orderby']")
    default_sorting = driver.find_element_by_css_selector("[value='menu_order']")
    s_checked = default_sorting.get_attribute('selected')
    if s_checked is not None:
        print("Default sorting")
    else:
        print("Other sorting")
    select = Select(sorting_selector)
    select.select_by_value('price-desc')
    price_desc = driver.find_element_by_css_selector("[value='price-desc']")
    s_checked = price_desc.get_attribute('selected')
    if s_checked is not None:
        print("By price")
    else:
        print("Other sorting")
    driver.quit()


def discount_price():
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
    shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]')
    shop.click()
    book = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
    book.click()
    default_price = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/del/span')
    t = default_price.text
    assert t == "₹600.00"
    new_price = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/ins/span')
    t1 = new_price.text
    assert t1 == "₹450.00"
    cover = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
    cover.click()
    img = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.ID, "fullResImage")))
    pp_close = driver.find_element_by_class_name("pp_close")
    pp_close.click()
    print(img)
    img_close = WebDriverWait(driver, 4).until(
        EC.invisibility_of_element_located((By.ID, "fullResImage")))
    print(img_close)
    driver.quit()


def add_to_cart():
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
    shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]')
    shop.click()
    add = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
    add.click()
    item = driver.find_element_by_class_name("cartcontents")
    assert item.text == "1 Item"
    price = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[2]')
    assert price.text == "₹180.00"
    view_cart = driver.find_element_by_css_selector('[title="View your shopping cart"]')
    view_cart.click()
    subtotal = driver.find_element_by_css_selector('[data-title="Subtotal"]')
    assert subtotal.text is not None
    total = driver.find_element_by_css_selector('[data-title="Total"]')
    assert total.text is not None
    driver.quit()


def cart_functions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(5)
    shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]')
    shop.click()
    driver.execute_script("window.scrollBy(0, 300);")
    add = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
    add.click()
    add1 = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]')
    add1.click()
    view_cart = driver.find_element_by_css_selector('[title="View your shopping cart"]')
    view_cart.click()
    remove = driver.find_element_by_css_selector('[data-product_id="182"]')
    remove.click()
    undo = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[1]/a')
    undo.click()
    quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
    quantity.clear()
    quantity.send_keys("3")
    update = driver.find_element_by_css_selector('[value="Update Basket"]')
    update.click()
    quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
    qt = quantity.get_attribute("value")
    assert qt == "3"
    apply_coupon = driver.find_element_by_css_selector('[value="Apply Coupon"]')
    apply_coupon.click()
    coupon_code = driver.find_element_by_class_name("woocommerce-error")
    assert coupon_code.text == "Please enter a coupon code."
    driver.quit()


def checkout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(5)
    shop = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]')
    shop.click()
    driver.execute_script("window.scrollBy(0, 300);")
    add = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
    add.click()
    view_cart = driver.find_element_by_css_selector('[title="View your shopping cart"]')
    view_cart.click()
    checkout_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
    checkout_btn.click()
    first_name = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "billing_first_name")))
    first_name.send_keys("Irina")
    last_name = driver.find_element_by_id("billing_last_name")
    last_name.send_keys("Artemeva")
    email = driver.find_element_by_id("billing_email")
    email.send_keys("test124883@test.ru")
    phone = driver.find_element_by_id("billing_phone")
    phone.send_keys("1234567890")
    country = driver.find_element_by_id("select2-chosen-1")
    country.click()
    country_field = driver.find_element_by_id("s2id_autogen1_search")
    country_field.send_keys("Russia")
    result_country = driver.find_element_by_id("select2-result-label-393")
    result_country.click()
    address = driver.find_element_by_id("billing_address_1")
    address.send_keys("Avenue 1")
    city = driver.find_element_by_id("billing_city")
    city.send_keys("Moscow")
    state = driver.find_element_by_id("billing_state")
    state.send_keys("Moscow")
    postcode = driver.find_element_by_id("billing_postcode")
    postcode.send_keys("115597")
    check_payments = driver.find_element_by_id("payment_method_cheque")
    check_payments.click()
    driver.execute_script("window.scrollBy(0, 300);")
    place_order = driver.find_element_by_id("place_order")
    place_order.click()
    text = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
    print(text)
    payments = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shop_table"), "Check Payments"))
    print(payments)
    driver.quit()


add_book()
number_of_goods()
sorting()
discount_price()
add_to_cart()
cart_functions()
checkout()
