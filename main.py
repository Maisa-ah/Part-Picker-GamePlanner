from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

#trying to keep chrome open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()



#open window to LKQ
driver.get("https://www.lkqpickyourpart.com/")

#click inventory button
inventoryoption = driver.find_element(By.LINK_TEXT,"VIEW OUR INVENTORY")
inventoryoption.click()

#click the dropdown menu
dropdown = driver.find_element(By.ID,"locationBox")
dropdown.click()


#click one the options using value
oppgroup = driver.find_element(By.XPATH, "//optgroup[@label='Alabama']")
opp = oppgroup.find_element(By.XPATH, "//option[@value='1223']")
opp.click()
time.sleep(2)

cars_list = driver.find_element(By.ID, "pypvi_results")
if cars_list != None:
    print("nothing")
individual_cars = cars_list.find_elements(By.CLASS_NAME, "pypvi_resultRow")




for elements in individual_cars:
    print(elements)



#cars_image = individual_cars.find_element(By.CSS_SELECTOR, "a.pypvi_image")

#print(cars_image)
# car_name = cars.text
# for cars in range(1, 5):
#     print(car_name)





time.sleep(2)
driver.quit()


