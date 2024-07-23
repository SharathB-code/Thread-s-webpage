import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Set up the Edge WebDriver
        edge_options = Options()
        edge_options.add_argument("--start-maximized")  # Example option to maximize the window
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
        self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_invalid_login(self):
        driver = self.driver
        driver.get("https://www.threads.net/login")

        username_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]/form/div/div[1]/input') 
        username_field.send_keys('chandu') 

        password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]/form/div/div[2]/input')
        password_field.send_keys('deekshi1')

        button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]/form/div/div[3]/div[2]")
        button.click()
        time.sleep(3)
        print("\nInvalid input")
        print("1st test successfull\n")

        time.sleep(2)
        username_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]/form/div/div[1]/input')
        username_field.send_keys(Keys.CONTROL + "a")
        username_field.send_keys(Keys.DELETE)
        username_field.send_keys('chandu000082') 

        password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]/form/div/div[2]/input')
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
        password_field.send_keys('deekshi1')

        button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]/form/div/div[3]/div[2]")
        button.click()
        
        print("\nValid input")
        print("2nd test successful\n")

        time.sleep(5)
        try:
            post = driver.find_element(By.XPATH, '//*[@id="barcelona-page-layout"]/div/div/div[2]/div[1]/div[2]/div/div[1]')
            post.click()
            time.sleep(3)
            post_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/div[1]/div[1]/p')
            
            post_button.send_keys('new to threads')
            time.sleep(3)
            add_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div')
            add_button.click()

            time.sleep(4)
            print("\nnew thread added")
            print("3rd test sucessfully\n")

            
            select =driver.find_element(By.XPATH , '//*[@id="barcelona-page-layout"]/div/div/div[1]/div[4]/div[2]/div/div')
            select.click()
            time.sleep(2)

            like = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/a[3]')
            like.click()
            time.sleep(3)

            unlike = driver.find_element(By.XPATH,'//*[@id="barcelona-page-layout"]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/div[3]/div/div[3]/div/div[1]/div/div')
            unlike.click()
            

            print("\nunlike succesfull\n")
            print("4th test successfull\n")
            
        finally:
            time.sleep(5)
       
        try:
            account =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/a')
            account.click()
            time.sleep(5)

            print("\nAccount selected")
            print("5th test successfull\n")

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            print("\nPage scroll down")
            print("6th test successfull\n")

            s_set = driver.find_element(By.XPATH,'//*[@id="barcelona-page-layout"]/div/div/div[2]/div[1]/div[5]/div/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div')
            s_set.click()
            time.sleep(3)

            save = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]')
            save.click()
            time.sleep(3)

            print("\npost saved")
            print("7th test successfull\n")

            
            p_set =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/div/div[1]/div[5]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div')
            p_set.click()
            time.sleep(3)

            delete =driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div')
            delete.click()
            time.sleep(3)

            d_sel =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[1]')
            d_sel.click()
            time.sleep(4)

            print("\ndeleted")
            print("8th test successfull\n")

            driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

            home= driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/a/div[2]')
            home.click()
            time.sleep(3)

            select =driver.find_element(By.XPATH , '//*[@id="barcelona-page-layout"]/div/div/div[1]/div[4]/div[2]/div/div')
            select.click()
            time.sleep(3)

            save_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/a[4]')
            save_btn.click()

            print("\nsaved view")
            print("9th test successfull\n")
        finally:
            time.sleep(5)
      

        search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/a')
        search.click()
        
        
        print("\nSearch button working")
        print("10th test successfull\n")
        time.sleep(3)

        search_field = driver.find_element(By.XPATH, '//*[@id="barcelona-page-layout"]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/label')
        search_field.send_keys('indiancricketteam')

        print("\n search completed")
        print("11th test successfull\n")

        find_elem1=driver.find_element(By.XPATH,'//*[@id="2091666763"]/div/a/div/div/div/div/div[2]')
        elem_text1=find_elem1.text
        print(f"Reselt :'{elem_text1}'\n")
        time.sleep(3)

        follow_field = driver.find_element(By.XPATH,'//*[@id="2091666763"]/div/a/div/div/div/div/div[2]/div[1]/div[2]')
        follow_field.click()

        elem_text2=follow_field.text
        print(f"Reselt :'{elem_text2}'\n")
        time.sleep(4)

       

        find_elem1=driver.find_element(By.XPATH,'//*[@id="2091666763"]/div/a/div/div/div/div/div[2]')
        elem_text1=find_elem1.text
        print(f"Reselt :'{elem_text1}'\n")

        print("\nFollow done")
        print("12th test successfull\n")
        time.sleep(3)

        search_id = driver.find_element(By.XPATH,'//*[@id="2091666763"]/div/a/div/div/div/div/div[2]/div[1]')
        search_id.click()

        print("\nSearch id Accessable")
        print("13th teat successfull\n ")

        time.sleep(4)

        unfollow_id =driver.find_element(By.XPATH, '//*[@id="barcelona-page-layout"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div')
        unfollow_id.click()
        time.sleep(4)

        print("\nUnfollow done")
        print("14th teat successfull\n ")
        time.sleep(1)

        try:
            t_set = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div[4]/div[3]/div/div/div')))
            t_set.click()
            time.sleep(2)

            pin_home = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div')))
            pin_home.click()

            print("\npin home")
            print("15 th test successfull\n")
            time.sleep(5)


            t_set1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="barcelona-header"]/div/div/div')))
            t_set1.click()
            time.sleep(4)

            un_pin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[2]')))
            un_pin.click()

            print("\nunpin succesfull")
            print("16th test successfull\n")
           
        finally:
            time.sleep(5)

        s_button =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[3]/div[2]')))
        s_button.click()

        time.sleep(2)

        appearance = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div')
        appearance.click()
        time.sleep(3)

        print("\nAppearence button worked")
        print("17th test successfull\n")
        
        bright = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]')
        bright.click()
        time.sleep(4)

        print("\nNight mode off")
        print("18th test succesfull\n")

        night = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]')
        night.click()
        time.sleep(4)

        print("\nNight mode on")
        print("19th test succesfull\n")

        areturn =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]')
        areturn.click()
        time.sleep(2)

        print("\nreturn ")
        print("20th test successfull\n")

        try:
            setting = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/a')
            setting.click()
            time.sleep(5)

            print("\nsetting accesable")
            print("21th test successfull\n ")

            
            pri_box =driver.find_element(By.XPATH,'//*[@id="barcelona-page-layout"]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/div/input')
            pri_box.click()
            time.sleep(5)

            pri_switch =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[1]')
            pri_switch.click()
            time.sleep(3)

            print("\nSwitch private")
            print("22th test Successfull\n")

            back = driver.find_element(By.XPATH, '//*[@id="barcelona-page-layout"]/div/div/div[1]/div[4]/div[1]/div/div')
            back.click()
            time.sleep(3)

            print("\nreturn successfull")

            s_button =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[3]/div[2]')))
            s_button.click()
            time.sleep(3)

            setting = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/a')
            setting.click()
            time.sleep(5)

            pri_box =driver.find_element(By.XPATH,'//*[@id="barcelona-page-layout"]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/div/input')
            pri_box.click()
            time.sleep(5)

            pri_switch =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[1]')
            pri_switch.click()
            time.sleep(3)

            print("\nSwitch public")
            print("23th test Successfull\n")

            back = driver.find_element(By.XPATH, '//*[@id="barcelona-page-layout"]/div/div/div[1]/div[4]/div[1]/div/div')
            back.click()
            time.sleep(3)

            print("\nreturn successfully")
            print("24th test successfull\n")

            s_button =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div[3]/div[2]')))
            s_button.click()
            time.sleep(3)


            log_out =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]')
            log_out.click()
            time.sleep(5)

            print("\nLog out successfull")
            print("25th test succesfull\n")

        finally:
            time.sleep(5)        


       
       
        

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
