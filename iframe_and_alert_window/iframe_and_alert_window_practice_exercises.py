from selenium import webdriver
import time


class ExerciseTwo():

    def test_two(self):
        base_URL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_URL)
        driver.implicitly_wait(3)

        driver.switch_to.frame("courses-iframe")
        driver.find_element_by_id("search-courses").send_keys("JavaScript")
        time.sleep(3)

        driver.switch_to.default_content()
        driver.find_element_by_id("name").send_keys("Tester 1")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(3)
        alert = driver.switch_to.alert
        if ("Hello Tester 1, share this practice page "
                "and share your knowledge" in alert.text):
            print("Text found in alert window one")
        else:
            print("Text not found in alert window one")
        alert.accept()
        time.sleep(3)

        driver.find_element_by_id("name").send_keys("Tester 2")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(3)
        alert = driver.switch_to.alert
        if ("Hello Tester 2, Are you sure you want to confirm?" in alert.text):
            print("Text found in alert window two")
        else:
            print("Text not found in alert window two")
        alert.dismiss()
        time.sleep(3)
        driver.quit()


ex = ExerciseTwo()
ex.test_two()
