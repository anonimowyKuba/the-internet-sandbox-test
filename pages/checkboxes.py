

class checkboxes_Class:
    def __init__(self, driver):
        self.driver = driver
        global checkboxes
        checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")

    def checkboxOn(self, checkboxnumber):
        global chceckboxes
        if checkboxes[checkboxnumber].is_selected():
            pass
        else:
            checkboxes[checkboxnumber].click()

    def checkboxOff(self, checkboxnumber):
        if checkboxes[checkboxnumber].is_selected():
            checkboxes[checkboxnumber].click()

    def checkboxStatus(self, checkboxnumber):
        return checkboxes[checkboxnumber].is_selected()