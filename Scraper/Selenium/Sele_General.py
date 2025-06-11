from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random 


class selenium:
    def __init__(self,settings):
        self.browser = settings[0]
        self.defSite= settings[1]
        self.low    = settings[2][0]
        self.high   = settings[2][1]

        
    #random timer; small way to try and fool security systems with random fluxuations in typing speeds    
    def type_speed(self):
        return random.randint(self.low,self.high)

    def typing(self,sentence):
        typer=self.driver.switch_to.active_element
        for letter in range(len(sentence)):
            typer.send_keys(sentence[letter])
            time.sleep(self.type_speed())
        typer.send_keys(Keys.ENTER)

    def open_edge(self):
        self.driver = webdriver.Edge()
        try:
            self.driver.get("https://www."+self.defSite+".com")
            time.sleep(self.type_speed)
        except Exception as e:
            print(e)

    def navigate_address_bar(self,destination,delay=5):
        self.driver.get(destination)
        time.sleep(delay)
    

    def find_elements(self,func,search_term,get_att=None,get_text=False,collection_amount=None):
        selection = []
        items = self.driver.find_elements(func,search_term)
        if collection_amount is None:
            collection_amount = len(items)
        for i in range(collection_amount):
            item = items[i]
            if get_att is not None:
                selection.append([item.get_attribute(get_att)])
            elif get_text:
                selection.append([item.text])
            else:
                selection.append([item])
        return selection
        

    def close_page(self):
        self.driver.quit()

