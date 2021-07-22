import sys
import pytest
from selenium import webdriver
sys.path.append("../../")

from utils.path_helper import get_project_root


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    exe_path = str(get_project_root()) + "\\resources\\chromedriver.exe"
    chrome_driver = webdriver.Chrome(executable_path=exe_path)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
