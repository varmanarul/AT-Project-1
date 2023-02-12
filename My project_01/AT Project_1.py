from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time 

class Project_of_Orange_HRM():
    def TC_Login_01(self):
        # open the browser on firefox or chrome
        driver = webdriver.Chrome()

        driver.maximize_window()

        # browser will be maximize 
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        #open the webpage
        driver.get(url)
        time.sleep(3)
    
        # find the xpath to login the page 
        
        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.XPATH,xpath_username)
        username.send_keys("Admin")
        # Wait for loaded the page to the path 
        driver.implicitly_wait(2)

        #Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH,xpath_password)
        password.send_keys("admin123")
        driver.implicitly_wait(3)

        #xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH,xpath_login_button).click()
        time.sleep(10)
        driver.implicitly_wait(10)
        # get the output in terminal
        print("User Logged in successfully")

        driver.quit()

    def TC_Login_02(self):
        # open the browser on firefox or chrome
        driver = webdriver.Chrome()

        # browser will be maximize
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        #open the webpage
        driver.get(url)
        time.sleep(3)
    
        # find the xpath to login the page 
        
        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME,"username").send_keys("Admin")
        # Wait for loaded the page to the path 
        driver.implicitly_wait(2)

        #Xpath for password
        #xpath_password = "//input[@name='password']"
        password = driver.find_element(By.NAME,"password").send_keys("amin123")
        driver.implicitly_wait(3)

        #xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH,xpath_login_button).click()
        driver.implicitly_wait(2)

        Xpath_for_getting_error = "//div[@class='oxd-alert oxd-alert--error']"
        Error_message = driver.find_element(By.XPATH,Xpath_for_getting_error)
        print(Error_message.text)
        driver.quit()

    def TC_PIM_01(self):
        # open the browser on firefox or chrome
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.implicitly_wait(3)
        # find the xpath to login the page 
        
        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME,"username").send_keys("Admin") 
        driver.implicitly_wait(2)

        #Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH,xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        #xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH,xpath_login_button).click()
        driver.implicitly_wait(2)
        
        # open the HRM Page
        #click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH,xpath_pim).click()
        driver.implicitly_wait(2)

        # click on add button by xpath
        driver.implicitly_wait(2)
        xpath_add_person = "//button[@type='button'][@class='oxd-button oxd-button--medium oxd-button--secondary']"
        driver.find_element(By.XPATH,xpath_add_person).click()
        driver.implicitly_wait(3)

        #add a image 
        xpath_image = "//i[@class='oxd-icon bi-plus']"
        image = driver.find_element(By.XPATH,xpath_image)

        # add a person detail in employee path
        xpath_of_first_name = "//input[@name='firstName']"
        driver.find_element(By.XPATH,xpath_of_first_name).send_keys("Arul")
        driver.implicitly_wait(3)

        xpath_of_middle_name = "//input[@name='middleName']"
        driver.find_element(By.XPATH,xpath_of_middle_name).send_keys("mozhi")
        driver.implicitly_wait(3)

        xpath_of_last_name = "//input[@name='lastName']"
        driver.find_element(By.XPATH,xpath_of_last_name).send_keys("Varman")
        driver.implicitly_wait(3)
        time.sleep(4)

        #add a employee id xpath 
        xpath_of_id = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
        driver.find_element(By.XPATH,xpath_of_id).send_keys("2653")

        # Xpath for submit button 
        xpath_of_submit = '//button[@type="submit"]'
        time.sleep(3)
        driver.find_element(By.XPATH,xpath_of_submit).click()
        time.sleep(4)
        # entering the nick name
        edit_nick_name = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input"
        driver.find_element(By.XPATH,edit_nick_name).send_keys("Nani")
        time.sleep(3)

        # enetring the Employee Id
        edir_employe_employee_id_name = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"
        driver.find_element(By.XPATH,edir_employe_employee_id_name).send_keys('2653')

        # entering Other Id
        driver.implicitly_wait(3)
        edir_employe_other_name = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"
        driver.find_element(By.XPATH,edir_employe_other_name).send_keys("nanivarman")
        driver.implicitly_wait(3)

        # entering Other Driver's License Number
        edir_employe_driver_name = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
        driver.find_element(By.XPATH,edir_employe_driver_name).send_keys("TN 202300000769")
        driver.implicitly_wait(3)
        
        # select the License Expiry Date
        cal_for_select = '//label[text()="License Expiry Date"]/following::div[3]/input'
        driver.find_element(By.XPATH,cal_for_select).send_keys("2036-02-06")
        time.sleep(4)

        #entering the SSN Number
        SSN_number = '//label[text()="SSN Number"]/following::div[1]/input'
        driver.find_element(By.XPATH,SSN_number).send_keys("677485432")
        time.sleep(3)

        SSN_number1 = '//label[text()="SSN Number"]/following::div[5]/input'
        driver.find_element(By.XPATH,SSN_number1).send_keys("677485432")
        time.sleep(3)

        # selecting the Nationality
        select_the_nationality = '//label[text()="Nationality"]/following::div[4]'
        driver.find_element(By.XPATH,select_the_nationality).send_keys("Indian")
        time.sleep(3)

        select_the_DOB = '//label[text()="Date of Birth"]/following::div[3]/input'
        driver.find_element(By.XPATH, select_the_DOB).send_keys("1994-08-06")
        time.sleep(4)

        # click on male option
        select_the_male = '//label[text()="Gender"]/following::div[2]/div[2]'
        driver.find_element(By.XPATH,select_the_male).click()

        # enetring the Military option as No
        Military = '//label[text()="Military Service"]/following::input[1]'
        driver.find_element(By.XPATH,Military).send_keys("NO")
        time.sleep(3)

        #click on save button
        enter_the_save = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"
        driver.find_element(By.XPATH,enter_the_save).send_keys(Keys.ENTER)
        time.sleep(6)

        # select the blood group
        time.sleep(4)
        select_the_blood = '//label[text()="Blood Type"]/following::div[4]'
        select_the_xpath = driver.find_element(By.XPATH,select_the_blood).send_keys(Keys.ARROW_DOWN)

        # clcik on save button option 2
        time.sleep(3)
        click_on_sec_option_save_button ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button"
        driver.find_element(By.XPATH,click_on_sec_option_save_button).send_keys(Keys.ENTER)
        time.sleep(7)

        print("Successfully added  Employee detail")

        driver.quit()

    def TC_PIM_02(self):    # If This Testcase get error mean please re-run it again this testcase only
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.implicitly_wait(3)
        driver.maximize_window()
        # find the xpath to login the page

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)


        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the name
        employe_select = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
        clcik_on = driver.find_element(By.XPATH,employe_select).send_keys("Arul mozhi Varman")
        driver.implicitly_wait(2)
        xpath_for_lisa = "//button[@type='submit']"
        driver.find_element(By.XPATH,xpath_for_lisa).click()
        time.sleep(10)
        #action = ActionChains(driver)
        #action.move_to_element(xpath_for_lisa).click().perform()
        #clcik_on.send_keys(Keys.ARROW_DOWN).click()
        driver.implicitly_wait(2)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)

        # add edit information in edit option
        driver.implicitly_wait(3)
        add_on_edit_option = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i"
        driver.find_element(By.XPATH,add_on_edit_option).click()
        driver.implicitly_wait(3)
        time.sleep(7)

        # entering the nick name
        edit_nick_name = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input"
        driver.find_element(By.XPATH, edit_nick_name).send_keys("nani")
        time.sleep(3)


        #click On contact detail
        click_on_contact_detail = '//a[text()="Contact Details"]'
        time.sleep(7)
        driver.find_element(By.XPATH,click_on_contact_detail).click()
        driver.implicitly_wait(2)

        #add_on_addres
        add_on_addres = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_addres).send_keys("No.40 south street ")

        add_on_address2 = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_address2).send_keys("1st cross Street ")

        add_on_city = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_city).send_keys("Virudhachalam")

        add_on_state = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_state).send_keys("Tamil Nadu")

        add_on_pincode = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_pincode).send_keys("31")

        add_on_country = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]"
        driver.find_element(By.XPATH,add_on_country).send_keys("India")

        add_on_home = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_home).send_keys("No.2")

        add_on_moblie_number = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_moblie_number).send_keys("9087550076")

        add_on_work = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_work).send_keys("kk Donnelley")

        click_on_save_button = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button"
        driver.find_element(By.XPATH,click_on_save_button).click()

        print("Successfully edited Employee detail")

        driver.quit()

    def TC_PIM_03(self):
        
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(3)
        # find the xpath to login the page


        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)


        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)
        
        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # seaching for name
        emlpoee = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
        clcik_on = driver.find_element(By.XPATH,emlpoee).send_keys("Arul mozhi Varman")
        driver.implicitly_wait(2)
        xpath_for_name = "//button[@type='submit']"
        driver.find_element(By.XPATH,xpath_for_name).click()
        time.sleep(4)

        # find the link
        click_on_the_selecting = "//i[@class ='oxd-icon bi-trash']"
        driver.find_element(By.XPATH,click_on_the_selecting).click()

        #deleted the add elements
        xpath_for_deleted = '//button[@type="button"][@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'
        driver.find_element(By.XPATH,xpath_for_deleted).click()
        time.sleep(10)
        print("Sucessfully Deleted the Employee information")
        driver.quit()

Arul = Project_of_Orange_HRM()
Arul.TC_Login_01()
Arul.TC_Login_02()
Arul.TC_PIM_01()
Arul.TC_PIM_02()
Arul.TC_PIM_03()