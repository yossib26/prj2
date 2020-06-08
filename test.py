from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

DRIVER_PATH = "C:\\Yossi\\DevOps\\0520\\4\\chromedriver.exe"
FX_DRIVER_PATH = "C:\\Yossi\\DevOps\\Lesson_4\\geckodriver.exe"
IE_DRIVER_PATH = "C:\\Yossi\\DevOps\\0520\\4\\IEDriverServer.exe"

# firefox
SETTINGS = {'extensions.update.autoUpdateEnabled': False,
            'extensions.checkCompatibility': False}
firefox_profile = webdriver.FirefoxProfile()

print(firefox_profile.default_preferences)

for key, value in SETTINGS.items():
    firefox_profile.set_preference(key, value)

driver_firefox = webdriver.Firefox(executable_path=FX_DRIVER_PATH, firefox_profile=firefox_profile)
driver_firefox.get("http://www.google.co.il")

exit()


# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome(executable_path=r"C:\\Yossi\\DevOps\\0520\\4\\chromedriver.exe")
# driver.get("https://www.google.com")
# for i in range(3):
#    driver.refresh()
#    sleep(2)
# driver.close()

# explorer
from selenium.webdriver.ie.options import Options
ie_options = Options()
ie_options.add_argument("--disable-extensions")
driver_ie = webdriver.Ie(executable_path=IE_DRIVER_PATH, options=ie_options)
driver_ie.get("http://www.google.co.il")
sleep(1)
driver_ie.quit()

name = "yossi"


def func_name(age, n="default"):
    print("hey {name}, welcome".format(name=n))

func_name(22, "aaaa")

with open("read_con.txt", "a+") as f:
    f.write("fdsfdsfsdf\n")g
    print(f.readline())
    f.close()



