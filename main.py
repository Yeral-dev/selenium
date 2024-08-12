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
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)


   
    def tearDown(self):
        self.driver.quit()


    def login(self, email, username, password):
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
            email_input.send_keys(email)
            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']")))
            next_button.click()
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
            username_input.send_keys(username)
            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']")))
            next_button.click()
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
            tweet = self.wait.until(EC.presence_of_element_located((By.XPATH, "//article[@data-testid='tweet']")))
            tweet.find_element(By.XPATH, ".//button[@data-testid='retweet']").click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()
        except Exception as e:
            self.fail(f"El test de retweet falló: {str(e)}")


    def test_search(self):
        self.login("yeraldsony5@gmail.com", "yerald_dev", "YeraldklkGG120")
        
        try:
            search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search query']")))
            search_input.send_keys("Python Software Foundation")
            search_input.send_keys(Keys.RETURN)
            search_results = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='primaryColumn']")))
            self.assertTrue(search_results.is_displayed(), "No se encontraron resultados de búsqueda.")
        
        except Exception as e:
            self.fail(f"El test de búsqueda falló: {str(e)}")


    def test_like_tweet(self):
        self.login("yeraldsony5@gmail.com", "yerald_dev", "YeraldklkGG120")

        try:
            self.driver.get("https://x.com/home")
            tweet = self.wait.until(EC.presence_of_element_located((By.XPATH, "//article[@data-testid='tweet']")))
            like_button = tweet.find_element(By.XPATH, ".//button[@data-testid='like']")
            like_button.click()
     
            

        
        except Exception as e:
            self.fail(f"El test de dar like falló: {str(e)}")
        

    def test_delete_tweet(self):
        self.login("yeraldsony5@gmail.com", "yerald_dev", "YeraldklkGG120")

        try:
            self.driver.get("https://x.com/home")
            tweet = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='tweet de test automizado.']/ancestor::article")))
            tweet_menu_button = tweet.find_element(By.XPATH, ".//div[@data-testid='caret']")
            tweet_menu_button.click()
            
            delete_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Delete']")))
            delete_button.click()

            confirm_delete_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Delete']")))
            confirm_delete_button.click()

            self.wait.until(EC.invisibility_of_element(tweet))
        
        except Exception as e:
            self.fail(f"El test de eliminar tweet falló: {str(e)}")


    def test_follow_user(self):
        self.login("yeraldsony5@gmail.com", "yerald_dev", "YeraldklkGG120")

        try:
            self.driver.get("https://x.com/home")
            search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search query']")))
            search_input.send_keys("Selenium")
            search_input.send_keys(Keys.RETURN)
            
            profile_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/Selenium')]")))
            profile_link.click()
            
            follow_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='placementTracking']//span[text()='Follow']")))
            follow_button.click()
           
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='placementTracking']//span[text()='Following']")))
        
        except Exception as e:
            self.fail(f"El test de seguir usuario falló: {str(e)}")

    

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reportes'))
