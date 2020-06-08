from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

DRIVER_PATH = "C:\\Yossi\\DevOps\\0520\\4\\chromedriver.exe"
FX_DRIVER_PATH = "C:\\Yossi\\DevOps\\Lesson_4\\geckodriver.exe"
IE_DRIVER_PATH = "C:\\Yossi\\DevOps\\0520\\4\\IEDriverServer.exe"

# 1
# -----------------------------------------------------------------------------------------
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.walla.co.il/")
driver.quit()

driver_firefox = webdriver.Firefox(executable_path=FX_DRIVER_PATH)
driver_firefox.get('https://www.ynet.co.il/')
driver_firefox.quit()

# 2
# -----------------------------------------------------------------------------------------
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.walla.co.il/")
sleep(1)
page_title = driver.title
driver.refresh()
sleep(1)
if page_title == driver.title:
    print("Titles are the same")


# 3
# ------------------------------------------------------------------------------------------
# yes. the elements are located at the same location in html code.


# 4
# -----------------------------------------------------------------------------------------
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://translate.google.co.il/?hl=iw")
driver.find_element_by_id("source").send_keys("תרגיל")
driver.find_element_by_id("source").send_keys(Keys.ENTER)


# 5
# -----------------------------------------------------------------------------------------"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
song_name = "Smells Like Teen Spirit"
driver.get("https://www.youtube.com/")
driver.find_element_by_name("search_query").send_keys(song_name)
driver.find_element_by_id("search-icon-legacy").click()


# 6
# -----------------------------------------------------------------------------------------
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://translate.google.com/")
a = driver.find_element_by_id("source")
b = driver.find_element_by_class_name("tlid-source-text-input")
c = driver.find_element_by_xpath("//textarea[@id='source']")


# 7
# -----------------------------------------------------------------------------------------
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
f_email = "yossib26@gmail.com"
f_pass = "123456"
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys(f_email)
driver.find_element_by_id("pass").send_keys(f_pass)
driver.find_element_by_xpath('//*[@id="u_0_b"]').submit()

# Challenges
# 8
# -----------------------------------------------------------------------------------------
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("http://www.sport5.co.il")
# before delete
cookie_list = driver.get_cookies()
for c in cookie_list:
    print(c['name'] + " " + c['value'])
driver.delete_all_cookies()
# after delete
print(" -------------- cookies list after delete ----------------------")
cookie_list = driver.get_cookies()
for c in cookie_list:
    print(c['name'] + " " + c['value'])

# 9
# -----------------------------------------------------------------------------------------
url = "https://github.com/"
driver.get(url)
if not driver.find_element_by_name("q").is_displayed():
    driver.maximize_window()
# change window width
driver.find_element_by_name("q").send_keys("Selenium")
driver.find_element_by_name("q").send_keys(Keys.ENTER)


# 10
# -----------------------------------------------------------------------------------------
# chrome
from selenium.webdriver.chrome.options import Options
# path_to_chrome = "C:\\Yossi\\DevOps\\0520\\4\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.get("http://one.co.il")


# firefox
SETTINGS = {'extensions.update.autoUpdateEnabled': False,
            'extensions.checkCompatibility': False}
firefox_profile = webdriver.FirefoxProfile()
for key, value in SETTINGS.items():
    firefox_profile.set_preference(key, value)
driver_firefox = webdriver.Firefox(executable_path=FX_DRIVER_PATH, firefox_profile=firefox_profile)
driver_firefox.get("http://www.google.co.il")



