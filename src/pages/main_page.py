
from pages.contactus_page import ContactUsPage
from utils.locators import Locators


class MainPage:

    locators = {
        "link_contact_us": (Locators.LINK_TEXT, "Contact us")
    }

    def __init__(self, driver):
        self.driver = driver

    def go_to_contact_us_page(self):
        link_contact_us = self.driver.find_element_by_link_text("Contact us")
        link_contact_us.click()
        return ContactUsPage(self.driver)
