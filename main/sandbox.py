import unittest
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains

import time
from selenium.webdriver.common.keys import Keys

from pages.addRemoveElement import add_remove_element
from pages.checkboxes import checkboxes_Class
from main import data


class TheIntrnerTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox(executable_path='C:/Users/Kuba/PycharmProjects/testexample/drivers/geckodriver.exe')
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("Stop")
        self.driver.close()

    def setUp(self):
        print("++++++++test+++++++++")

    def tearDown(self):
        print("+++++++")
        if sys.exc_info()[0]:
            print("blad+++++++")
            self.driver.save_screenshot("screenshots/failshot_%s.png" % self._testMethodName)

        '''
        try:
        # do some webdriver stuff here
        except Exception as e:
        print e
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        browser.get_screenshot_as_file('screenshot-%s.png' % now)
        '''

    def test_01correctPageName(self):
        print(self._testMethodName)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.assertIn('The Internet0', self.driver.title)


        # TODO add A/B Testing test_02


    def test_03addRemmoveElement(self):
        print(self._testMethodName)
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

        # add elements
        add_remove_element(driver).add_elemnts(data.howmanyadd)
        howManyElementsExist = driver.find_elements_by_css_selector("button[onclick='deleteElement()']")
        assert len(howManyElementsExist) == data.howmanyadd

        # remove elements

        add_remove_element(driver).delete_element(data.howmanydlelete)
        if data.howmanyadd > data.howmanydlelete:
            howManyElementsExist = driver.find_elements_by_css_selector("button[onclick='deleteElement()']")
            assert len(howManyElementsExist) == data.howmanyadd - data.howmanydlelete
        else:
            assert howManyElementsExist.size() == 0

        # TODO this test
        # def test_04basicauth(self):
        #    browser.open_url('https://the-internet.herokuapp.com/basic_auth/')

    '''
    def test_05brokenimage(self):
        print("broken image")
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/broken_images')
        images = driver.find_elements_by_css_selector("img")
        for image in images:
            if image.get_attribute("naturalWidth") == "0":
                print("Image", image.get_attribute("outerHTML"), "is broken")
    

    def test_06checkbox(self):
        print("chceckboxes test")
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/checkboxes')

        checkboxes_Class(driver).checkboxOn(0)
        assert checkboxes_Class(driver).checkboxStatus(0) == True

        checkboxes_Class(driver).checkboxOff(1)
        assert checkboxes_Class(driver).checkboxStatus(1) == False

        checkboxes_Class(driver).checkboxOff(1)
        assert checkboxes_Class(driver).checkboxStatus(1) == False
    
   
    def test_07contexmenu(self):
        print("context_menu test")
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/context_menu')
        ActionChains(driver).context_click(
            driver.find_element_by_id("hot-spot")).perform()

        time.sleep(1)

        driver.switch_to.alert.accept()
   

    def test_08DigestAuthent(self):
        print("Digest Authentication")
        driver = self.driver
        driver.get('https://admin:admin@the-internet.herokuapp.com/digest_auth')

        try:
            ele = driver.find_element_by_xpath("//*[contains(text(), 'Congratulations! You must have the proper credentials.')]")
            ele.is_displayed()
        except (NoSuchElementException, TimeoutException):
            print("nia zalogowany")
    '''

if __name__ == "__main__":
    unittest.main()