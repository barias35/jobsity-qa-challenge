from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.path_helper import get_project_root


class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver

    def fulfill_form(self, subject_index: int = 1, email: str = "", id_order: str = "123", message: str = ""):
        self.__select_subject(subject_index)
        self.__set_email(email)
        self.__set_order_reference(id_order)
        self.__set_message(message)
        self.__set_attachment_file()

    def click_send(self):
        send_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "submitMessage"))
        )
        send_button.click()

    def is_submitted_form(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='alert alert-success']"))
        ).is_displayed()

    def is_displayed_alert_validation(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
        ).is_displayed()

    #
    def __select_subject(self, index_option: int):
        dropdown_subject = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@class='form-control']"))
        )
        dropdown_subject = Select(dropdown_subject)
        dropdown_subject.options[index_option].click()

    def __set_email(self, email: str):
        email_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_textbox.send_keys(email)

    def __set_order_reference(self, id_order: str):
        order_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_order"))
        )
        order_textbox.send_keys(id_order)

    def __set_message(self, message: str):
        message_textarea = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        message_textarea.send_keys(message)

    def __set_attachment_file(self):
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "fileUpload"))
        )
        file_path = str(get_project_root()) + "\\resources\\test.txt"
        file_input.send_keys(file_path)
