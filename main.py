##-----------run in the Terminal-----------
##pip3 install selenium--- for download selenium
##pip3 install pytest--- for download pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.by import By


url = 'https://www.ness-tech.co.il/careers/'


def openWeb(driver):
    driver.get(url)
# --------------------------- Shortcut function for find element by Css  ---------------------------

def find_element(driver, Css):
    element = driver.find_element(By.CSS_SELECTOR, Css)
    return element


def professional_field(driver, Css_professional_field):
    find_element(driver, Css_professional_field).click()

def location_filed(driver, Css_location_filed):
    find_element(driver, Css_location_filed).click()


def choose_position(driver, Id_number):
    tabale = find_element(driver, '#positions')
    body = find_element(driver, '#positions > tbody')
    rows = driver.find_elements(By.TAG_NAME, "tr")
    number = Id_number + 1
    for row in rows:
        row_id = row.get_attribute("id")
        if row_id == str(number):
            return row.click()




def applying_user_for_job(driver, full_name, email_adress, file_adress):
    Full_Name = find_element(driver, '#mainFirstName').send_keys(full_name)
    Email_Adress = find_element(driver, '#mainFormEmail').send_keys(email_adress)
    Choose_File = driver.find_element(By.ID, 'mainFormFile')
    Choose_File.send_keys(file_adress)