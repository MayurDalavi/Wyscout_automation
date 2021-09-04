from behave import *
from selenium import webdriver

@given("Launch Chrome Browser")
def openChrome(context):
    context.driver=webdriver.Chrome(executable_path="C:\\Drivers\\chrome\\chromedriver.exe")
    context.driver.maximize_window()

@when("open wyscout login page")
def openHomepage(context):
    context.driver.get("https://platform.wyscout.com/app/?")
    context.driver.implicitly_wait(10)

@then("Enter User name and Password")
def enterUnameandPass(context):
    username = "dalavimayur17@gmail.com"
    password = "pw_IndiaTest!"
    username_textbox = context.driver.find_element_by_id("login_username")
    username_textbox.send_keys(username)
    password_textbox = context.driver.find_element_by_id("login_password")
    password_textbox.send_keys(password)
    context.driver.implicitly_wait(10)

@then("click on login button")
def clickOnLogin(context):
    login_button = context.driver.find_element_by_id("login_button")
    login_button.click()
    while True:
        pass


