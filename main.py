import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LOGIN = ''
PASS = ''


class YandexPassportTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://passport.yandex.ru/auth')

    def test_search_in_python_org(self):
        time.sleep(random.randint(3, 6))

        elem = self.driver.find_element_by_name('login')
        elem.send_keys(LOGIN)

        time.sleep(random.randint(1, 3))
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()

        time.sleep(random.randint(1, 3))
        elem = self.driver.find_element_by_name('passwd')
        elem.send_keys(PASS)

        time.sleep(random.randint(1, 3))
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()
        time.sleep(2)
        self.assertIn("Яндекс.Паспорт", self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
