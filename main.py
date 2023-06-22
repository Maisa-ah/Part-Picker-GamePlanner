from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import carObjectClass



class TestMethod:
    def test(self):
        driver = webdriver.Chrome("/Users/spencerbaldwin/Desktop/vscodeProjects/Part-Picker-GamePlanner/chromedriver_mac_arm64/chromedriver")
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
    car_name = ""
    car_color = ""
    car_vin = ""
    car_section = ""
    car_row = ""
    car_space = ""
    car_stocknum = ""
    car_avalibilitydate = ""
    def __init__(self, driver):
        self.driver = driver

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
        individual_car_list = cars_list.find_elements(By.XPATH, self.car_card_wrappers)
        count = 0
        carobjectclasslist = []
        for i,elements in enumerate(individual_car_list):
            print(elements)
            carobjectclasslist.append(carObjectClass.carobject())
            carobjectclasslist[i].InfoWrapper = elements.find_element(By.XPATH, self.car_detail_wrapper)
            if count == 9:
                break
            count +=1

        for element in carobjectclasslist:
            print(element.InfoWrapper)


run = TestMethod()
run.test()
        
#click one the options using value
