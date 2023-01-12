from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'

drv = webdriver.Chrome()
drv.get(link)

try:
    x = drv.find_element(By.ID, 'input_value')
    f_x = str(math.log(abs(12*math.sin(int(x.text)))))

    button = drv.find_element(By.TAG_NAME, "button")
    drv.execute_script("return arguments[0].scrollIntoView(true);", button)

    answer = drv.find_element(By.ID, "answer")
    drv.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(f_x)

    checkbox = drv.find_element(By.ID, 'robotCheckbox')
    drv.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio_button = drv.find_element(By.ID, 'robotsRule')
    drv.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    drv.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(30)

finally:
    drv.quit()
