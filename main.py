from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import unittest

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service = Service(executable_path='chromedriver.exe')
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://twitter.com/login")
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.implicitly_wait(10)

    def login(self, email, username, password):
        try:
            # Espera a que el campo de correo electrónico esté presente y lo encuentra
            email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
            email_input.send_keys(email)

            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']")))
            next_button.click()

            # Espera a que el campo de nombre de usuario esté presente y lo encuentra
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
            username_input.send_keys(username)

            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']")))
            next_button.click()

            # Espera a que el campo de contraseña esté presente y lo encuentra
            password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password_input.send_keys(password)

            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Iniciar sesión']")))
            next_button.click()

            self.wait.until(EC.url_contains("https://x.com/home"))
            
        except Exception as e:
            self.fail(f"El test de login falló: {str(e)}")

    
    def test_post_tweet(self):
        self.login("yeraldsony5@gmail.com", "yerald_dev", "YeraldklkGG120")

        try:
            self.driver.get("https://x.com/home")
            tweet_textbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))
            tweet_textbox.click()
            tweet_textbox.send_keys("tweet de test automizado.")
            post_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButtonInline']")))
            post_button.click()
            confirmation = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='tweet de test automizado.']")))
            self.assertTrue(confirmation.is_displayed(), "Tweet no fue enviado correctamente")
        except Exception as e:
            self.fail(f"El test de posteo de tweet falló: {str(e)}") 

    def test_retweet(self):
        self.login("yeraldsony5@gmail.com", "yerald_dev", "YeraldklkGG120")

        try:
       
         self.driver.get("https://x.com/home")
         tweet = self.wait.until(EC.presence_of_element_located((By.XPATH, "//article[@data-testid='tweet']")))
         tweet.find_element(By.XPATH, ".//button[@data-testid='retweet']").click()
         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()
         self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Repost']")))
        except Exception as e:
         self.fail(f"El test de retweet falló: {str(e)}")



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


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


