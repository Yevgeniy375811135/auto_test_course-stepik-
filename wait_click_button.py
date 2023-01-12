from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
drv = webdriver.Chrome()
#drv.implicitly_wait(5)
drv.get(link)



#price = WebDriverWait(drv, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100')) 
#time.sleep(5)
assert WebDriverWait(drv, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button = drv.find_element(By.ID, 'book') 
button.click()


x = drv.find_element(By.ID, 'input_value')
y = calc(x.text)
answer = drv.find_element(By.ID, 'answer')
answer.send_keys(y)
button = drv.find_element(By.ID, 'solve')
button.click()
time.sleep(30)
drv.quit()
