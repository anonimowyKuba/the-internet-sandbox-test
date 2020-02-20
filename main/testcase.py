import unittest

import selene
from selenium import webdriver
from selene import api
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains

from selene.support.shared.jquery_style import ss, s

from pages.addRemoveElement import add_remove_element
from pages.checkboxes import checkboxesClass

from main import data


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.FirefoxOptions()
        #options.add_argument("--fullscreen")
        selene.api.browser.set_driver(webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                                        options=options))  # sprawdza webdriver i instaluje jesli nie ma
        selene.api.browser.open_url('https://the-internet.herokuapp.com/')


    @classmethod
    def tearDownClass(cls):
        print("Stop")
        #browser.close()

    #def setUp(self):
    #    print("przed testem")

    def tearDown(self):
        print("++++++++++++")

    def test_01correctPageName(self):
        print("correct page name")
        selene.api.browser.open_url('https://the-internet.herokuapp.com/')
        assert "The Internet" == selene.api.browser.title()

    # TODO add A/B Testing

    def test_02coscos(self):
        assert 2 == 2

    def test_03addRemmoveElement(self):
        print("Add/remove element")
        browser.open_url('https://the-internet.herokuapp.com/add_remove_elements/')

        #add elements
        howmanyadd = date.howmanyadd
        add_remove_element().add_elemnts(howmanyadd)
        howmanydeletesexist = ss("button[onclick='deleteElement()']")
        assert len(howmanydeletesexist) == howmanyadd

        # remove elements
        howmanydelete = date.howmanydlelete
        add_remove_element().delete_element(howmanydelete)
        if howmanyadd > howmanydelete:
            assert len(howmanydeletesexist) == howmanyadd - howmanydelete
        else:
            assert howmanydeletesexist.size() == 0

    #TODO this test
    #def test_04basicauth(self):
    #    browser.open_url('https://the-internet.herokuapp.com/basic_auth/')

    def test_05brokenimage(self):
        print("broken image")
        browser.open_url('https://the-internet.herokuapp.com/broken_images')
        images = ss(by.css("img"))
        for image in images:
            if image.get_attribute("naturalWidth") == "0":
                print("Image", image.get_attribute("outerHTML"), "is broken")


    def test_06checkbox(self):
        print("chceckboxes test")
        browser.open_url('https://the-internet.herokuapp.com/checkboxes')

        checkboxesClass().checkboxOn(0)
        assert checkboxesClass().checkboxStatus(0) == True

        checkboxesClass().checkboxOff(1)
        assert checkboxesClass().checkboxStatus(1) == False

        checkboxesClass().checkboxOff(1)
        assert checkboxesClass().checkboxStatus(1) == False


    def test_07contexmenu(self):
        print("context_menu test")
        selene.api.browser.open_url('https://the-internet.herokuapp.com/context_menu')
        #s(by.id("hot-spot")).click()
        ActionChains(selene.api.browser).context_click(selene.api.browser.element(selene.api.by.id("hot-spot"))).perform()


if __name__ == '__main__':
    unittest.main(warnings='ignore')