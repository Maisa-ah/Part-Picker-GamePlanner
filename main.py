from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import carObjectClass


class TestMethod:
    def test(self):
        driver = webdriver.Chrome("/Users/spencerbaldwin/Desktop/vscodeProjects/Part-Picker-GamePlanner/Drivers/chromedriver_mac_arm64/chromedriver")
        driver.get("https://www.lkqpickyourpart.com/")

        #trying to keep chrome open
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        coding = SeleniumScraper(driver)
        coding.click_inventory_button()
        coding.click_drop_down_menu()
        coding.select_option_values()
        coding.populate_car_objects()
        time.sleep(2)
        driver.quit()


class SeleniumScraper:
    #xpath for each element
    driver = ""
    listofcars = "//*[@id='pypvi_results']"
    car_card_wrappers = "//*[@class='pypvi_resultRow']"
    car_detail_wrapper = "//*[@class='pypvi_details text--small']"
    car_name = "//*[@class='pypvi_ymm']"
    car_color = ""
    car_vin = ""
    car_section = ""
    car_row = ""
    car_space = ""
    car_stocknum = ""
    car_avalibilitydate = ""
    def __init__(self, driver):
        self.driver = driver

    # Selenium script to access webpage
    def click_inventory_button(self):
        inventoryoption = self.driver.find_element(By.LINK_TEXT,"VIEW OUR INVENTORY")
        inventoryoption.click()

    def click_drop_down_menu(self):
        dropdown = self.driver.find_element(By.ID,"locationBox")
        dropdown.click()
    
    def select_option_values(self):
        oppgroup = self.driver.find_element(By.XPATH, "//optgroup[@label='Alabama']")
        opp = oppgroup.find_element(By.XPATH, "//option[@value='1223']")
        opp.click()
        time.sleep(2)

    def populate_car_objects(self):
        cars_list = self.driver.find_element(By.XPATH, self.listofcars)
        # individual_car_list = cars_list.find_elements(By.XPATH, self.car_card_wrappers)
        # count = 0
        # print(individual_car_list)
        # carobjectclasslist = []
        #car_details = cars_list.find_elements(By.XPATH, self.car_detail_wrapper)
        car_names = self.driver.find_elements(By.XPATH, self.car_name)
        for element in car_names:
            print("check ", element.text)
        # for elements in individual_car_list:
        # for i, element in enumerate(car_details):
            # print(i, ": ", element)
            # print(elements.find_element(By.XPATH, self.car_detail_wrapper))
            # carobjectclasslist.append(carObjectClass.carobject())
            # print(carobjectclasslist[count])
            # carobjectclasslist[i].InfoWrapper = elements.find_element(By.XPATH, self.car_detail_wrapper)
            # if count == 9:
            #     break
            # count +=1

        # for element in carobjectclasslist:
        #     print(element.InfoWrapper)


run = TestMethod()
run.test()
        
#click one the options using value
