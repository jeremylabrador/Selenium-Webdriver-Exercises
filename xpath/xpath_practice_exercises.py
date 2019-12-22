from selenium import webdriver
import time


class ExerciseOne():

    def test_one(self):
        base_URL = (
            "http://automationpractice.com/"
            "index.php?id_product=7&controller=product")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_URL)
        driver.implicitly_wait(3)

        if driver.find_element_by_xpath(
                "//div[@class='primary_block row']"
                "//h1[text()='Printed Chiffon Dress']") is not None:
            print("EX 1 - Element found with XPATH using text()")
        else:
            print("EX 1 - Element not found")

        if driver.find_element_by_xpath(
                "//a[contains(text(), 'Sign in')]") is not None:
            print("EX 2 - Element found with XPATH using contains")
        else:
            print("EX 2 - Element not found")

        if driver.find_element_by_xpath(
                "//a[contains(@class, 'fancybox') "
                "and contains(@href, '20-thickbox_default.jpg')]") is not None:
            print("EX 3 - Element found with XPATH using a double contains")
        else:
            print("EX 3 - Element not found")

        if driver.find_element_by_xpath(
                "//a[@href='javascript:print();']") is not None:
            print("EX 4 - Element found with XPATH using the href attribute")
        else:
            print("EX 4 - Element not found")

        if driver.find_element_by_xpath(
                "//img[starts-with(@class, 'logo')]") is not None:
            print("EX 5 - Element found with XPATH using starts-with")
        else:
            print("EX 5 - Element not found")

        if driver.find_element_by_xpath(
                "//button[@class='btn btn-default btn-facebook']"
                "//parent::p") is not None:
            print("EX 6 - Element found with XPATH "
                  "using the parent of an element")
        else:
            print("EX 6 - Element not found")

        if driver.find_element_by_xpath(
                "//button[@class='btn btn-default btn-facebook']"
                "//preceding-sibling::button") is not None:
            print("EX 7 - Element found with XPATH "
                  "using the preceding-sibling of an element")
        else:
            print("EX 7 - Element not found")

        if driver.find_element_by_xpath(
                "//button[@class='btn btn-default btn-facebook']"
                "//following-sibling::button[1]") is not None:
            print("EX 8 - Element found with XPATH "
                  "using the following-sibling of an element")
        else:
            print("EX 8 - Element not found")

        time.sleep(3)
        driver.quit()


ex = ExerciseOne()
ex.test_one()
