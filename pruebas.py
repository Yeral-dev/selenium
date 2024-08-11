from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import unittest
import HtmlTestRunner

class LoginTests(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://twitter.com/login")
        self.wait = WebDriverWait(self.driver, 12)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def login(self, email, username, password):
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
            email_input.send_keys(email)

            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']")))
            next_button.click()

            user_input = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
            user_input.send_keys(username)

            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']")))
            next_button.click()

            password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password_input.send_keys(password)

            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Iniciar sesión']")))
            next_button.click()

            self.wait.until(EC.url_contains("https://x.com/home"))
        
        except Exception as e:
            self.fail(f"El test de login falló: {str(e)}")



    def test_user_search_in_explore(self):
        self.login("Yeraldsony5@gmail.com", "yerald_dev", "YeraldklkGG120")
        
        self.wait.until(EC.url_contains("home"))

        explore_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/explore']")))
        explore_tab.click()
        self.wait.until(EC.url_contains("/explore"))
        search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Buscar en Twitter']")))
        search_input.send_keys("Yerald_dev")  
        search_input.send_keys(u'\ue007')  
        user_profile = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='usuario_a_buscar']")))
        self.assertTrue(user_profile.is_displayed(), "El perfil del usuario no se muestra en los resultados de búsqueda.")
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reporte'))
