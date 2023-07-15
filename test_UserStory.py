
from main import*


#-------------------------Job search in use with 'filtering by: Professional & location'-------------------------#

class TestSerchCareers:

    # ------------------use in 'filtering by: Professional & location' and click back to all jobs ------------------#

    def test_back_to_careers_list_1(self):
        driver = webdriver.Chrome()
        openWeb(driver)
        driver.maximize_window()
        time.sleep(2)
        Selected_Professional = professional_field(driver, '#domain > option:nth-child(4)')
        time.sleep(2)
        Selected_location = location_filed(driver, '#Location > option:nth-child(2)')
        time.sleep(2)
        Search_Button = find_element(driver, '#search > main > section > div > form > fieldset > div > div.input-unit.Search-btnWrap > button').click()
        time.sleep(2)
        choose_position(driver, 4)
        time.sleep(3)
        Back_To_List = find_element(driver, 'body > app-root > job-description > section > div > div.job_descriptionHeader > div.btnWrap').click()
        time.sleep(2)
        select_element_Professional = driver.find_element(By.ID, "domain")
        select_element_location = driver.find_element(By.ID, 'Location')
        Expected = f'{"2"} + {"40"}'
        Actual = f'{select_element_Professional.get_attribute("value")} + {select_element_location.get_attribute("value")}'
        assert Expected == Actual



    # ------------------Use in 'filtering by: Professional & location' and applying and returning to jobs ------------------#


    def test_back_to_careers_list_2(self):
        driver = webdriver.Chrome()
        openWeb(driver)
        driver.maximize_window()
        time.sleep(2)
        Selected_Professional = professional_field(driver, '#domain > option:nth-child(4)')
        time.sleep(2)
        Selected_location = location_filed(driver, '#Location > option:nth-child(2)')
        time.sleep(2)
        Search_Button = find_element(driver, '#search > main > section > div > form > fieldset > div > div.input-unit.Search-btnWrap > button').click()
        time.sleep(2)
        choose_position(driver, 4)
        time.sleep(2)
        Applying_Job = find_element(driver, 'body > app-root > job-description > section > div > div.job_descriptionRow > div > div.job_descriptionFooter > div.NominationBTNWrap > button').click()
        applying_user_for_job(driver, 'Yarin Shmaryahu', 'shm.yarin@gmail.com', '/Users/yarin/Desktop/Yarin Shmaryahu CV copy.pdf')
        Applying_Button = find_element(driver, '#contactFrom > fieldset > div.popUpColumn > div > div.input-unit.AccMainForm-Item.popUpbtnWrap > button').click()
        time.sleep(2)
        Back_to_List2 = find_element(driver, 'body > app-root > app-thank-you > main > section > div.thankYouMassage > div > a').click()
        select_element_Professional = driver.find_element(By.ID, "domain")
        select_element_location = driver.find_element(By.ID, 'Location')
        Expected = f'{"2"} + {"40"}'
        Actual = f'{select_element_Professional.get_attribute("value")} + {select_element_location.get_attribute("value")}'
        assert Expected == Actual