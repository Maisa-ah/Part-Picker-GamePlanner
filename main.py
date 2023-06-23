from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import carObjectClass
import csv


class TestMethod:
    def test(self):
        driver = webdriver.Chrome("/Users/spencerbaldwin/Desktop/vscodeProjects/Part-Picker-GamePlanner/Drivers/chromedriver_mac_arm64/chromedriver")
        driver.get("https://www.lkqpickyourpart.com/")

        #trying to keep chrome open
        chrome_options = Options()
        #chrome_options.add_experimental_option("detach", True)

        coding = SeleniumScraper(driver)
        coding.click_inventory_button()
        coding.click_drop_down_menu()
        coding.select_option_values()
        listOfListCar = coding.getListOfCarObjects()
        seperatedlist = coding.seperateyearmakemodel(listOfListCar)
        coding.createcsv(seperatedlist)
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

    def getListOfCarObjects(self):
        cars_list = self.driver.find_element(By.XPATH, self.car_card_wrappers)
        car_name1 = cars_list.find_elements(By.XPATH, self.car_detail_wrapper)
        carString = []
        for element in car_name1:
            carString.append(element.text.split('\n'))
        return carString
       
    def seperateyearmakemodel(self, list):
        cardeets = list
        yearmakemodel = []
        #cardeets is the list contains the list of each cars details
        #element is the individual car details
        for i,element in enumerate(cardeets):
            yearmakemodel.append(element[0].split(' '))
            element.remove(element[0])
            for i,field in enumerate(yearmakemodel[i]):
                element.insert(i,field)
        for element in cardeets:
            print(element, "2")
        return cardeets
    
    def createcsv(self, list):
        with open('carlist.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["year", "make", "model", "color", "vin", "Location", "stock num", "avalability date"]
            for element in list:
                writer.writerow(element)
        
            
        
        
        

        

run = TestMethod()
run.test()
        
#click one the options using value
