#from selene.support.jquery_style_selectors import s
#from selene.support.shared.jquery_style import s

class add_remove_element():
    def __init__(self, driver):
       self.driver = driver

    def add_elemnts(self, howmanyadd):
        self.addelementbutton = self.driver.find_element_by_css_selector("button[onclick='addElement()']")
        for i in range(howmanyadd):
            self.addelementbutton.click()

    def delete_element(self, howmanydelelte):
        self.removeelementbutton = self.driver.find_elements_by_css_selector("button[onclick='deleteElement()']")
        for i in range(howmanydelelte):
            self.removeelementbutton[i].click()