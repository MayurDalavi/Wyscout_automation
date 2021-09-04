from selenium import webdriver

# Entering username and password
#username = input("Enter in your username: ")
#password = getpass("Enter your password: ")
username = "dalavimayur17@gmail.com"
password = "pw_IndiaTest!"

# Setting chrome webdriver path
driver = webdriver.Chrome(executable_path="C:\\Drivers\\chrome\\chromedriver.exe")
# Maximize the Chrome Window
driver.maximize_window()
# Open Wyscot website
driver.get("https://platform.wyscout.com/app/?")
# Adding delay of 10 seconds( website taking some time for loading)
driver.implicitly_wait(10)

# Passing the username and password
username_textbox = driver.find_element_by_id("login_username")
username_textbox.send_keys(username)
password_textbox = driver.find_element_by_id("login_password")
password_textbox.send_keys(password)
driver.implicitly_wait(10)
# Click on Login button
login_button = driver.find_element_by_id("login_button")
login_button.click()