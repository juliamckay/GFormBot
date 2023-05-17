import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_method():
    driver = webdriver.Chrome()
    return driver

def teardown_method(driver):
    driver.quit()

def vote_all(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i9 > .uHMk6b").click()  # taylor X diana
    driver.find_element(By.CSS_SELECTOR, "#i12 > .uHMk6b").click()  # zoe X sam
    driver.find_element(By.CSS_SELECTOR, "#i15 > .uHMk6b").click()  # jasmin x liv
    driver.find_element(By.CSS_SELECTOR, "#i18 > .uHMk6b").click()  # oatisa
    driver.find_element(By.CSS_SELECTOR, "#i36 > .uHMk6b").click()  # anna x brit
    driver.execute_script("window.scrollTo(0,500)")
    driver.find_element(By.CSS_SELECTOR, "#i48 > .uHMk6b").click()  # jenna x dakota
    driver.find_element(By.CSS_SELECTOR, "#i51 > .uHMk6b").click()  # jasmin x devyn
    driver.find_element(By.CSS_SELECTOR, "#i54 > .uHMk6b").click()  # rachel x a24
    driver.find_element(By.CSS_SELECTOR, "#i57 > .uHMk6b").click()  # ben x a job
    driver.find_element(By.CSS_SELECTOR, "#i71 > .uHMk6b").click()  # pacino x inceldmen
    driver.find_element(By.CSS_SELECTOR, "#i77 > .uHMk6b").click()  # bastille x imagine dragons
    driver.find_element(By.CSS_SELECTOR, "#i88 > .uHMk6b").click()  # emily x aabria
    driver.find_element(By.CSS_SELECTOR, "#i97 > .uHMk6b").click()  # wb x the dome
    driver.find_element(By.CSS_SELECTOR, "#i131 > .uHMk6b").click()  # wga x winning
    driver.find_element(By.CSS_SELECTOR, "#i146 > .uHMk6b").click()  # angels manager x death
    driver.find_element(By.CSS_SELECTOR, "#i183 > .uHMk6b").click()  # mojos no good day
    driver.find_element(By.CSS_SELECTOR, "#i203 > .uHMk6b").click()  # lauras mom x ron swanson
    driver.find_element(By.CSS_SELECTOR, "#i228 > .uHMk6b").click()  # ayo x women
    driver.find_element(By.CSS_SELECTOR, "#i231 > .uHMk6b").click()  # natasha x women
    driver.find_element(By.CSS_SELECTOR, "#i240 > .uHMk6b").click()  # ashley x women
    driver.find_element(By.CSS_SELECTOR, "#i248 > .uHMk6b").click()  # rapture x botw
    driver.find_element(By.CSS_SELECTOR, "#i254 > .uHMk6b").click()  # rapture x movies
    driver.find_element(By.CSS_SELECTOR, "#i274 > .uHMk6b").click()  # keegan x patrick
    driver.find_element(By.CSS_SELECTOR, "#i277 > .uHMk6b").click()  # keegan x lindt
    driver.find_element(By.CSS_SELECTOR, "#i286 > .uHMk6b").click()  # nia x courtney
    driver.find_element(By.CSS_SELECTOR, "#i298 > .uHMk6b").click()  # jules x renee rapp
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_jules_favs(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i9 > .uHMk6b").click()  # taylor X diana
    driver.find_element(By.CSS_SELECTOR, "#i15 > .uHMk6b").click()  # jasmin x liv
    driver.find_element(By.CSS_SELECTOR, "#i18 > .uHMk6b").click()  # oatisa
    driver.find_element(By.CSS_SELECTOR, "#i36 > .uHMk6b").click()  # anna x brit
    driver.execute_script("window.scrollTo(0,500)")
    driver.find_element(By.CSS_SELECTOR, "#i48 > .uHMk6b").click()  # jenna x dakota
    driver.find_element(By.CSS_SELECTOR, "#i51 > .uHMk6b").click()  # jasmin x devyn
    driver.find_element(By.CSS_SELECTOR, "#i54 > .uHMk6b").click()  # rachel x a24
    driver.find_element(By.CSS_SELECTOR, "#i57 > .uHMk6b").click()  # ben x a job
    driver.find_element(By.CSS_SELECTOR, "#i71 > .uHMk6b").click()  # pacino x inceldmen
    driver.find_element(By.CSS_SELECTOR, "#i77 > .uHMk6b").click()  # bastille x imagine dragons
    driver.find_element(By.CSS_SELECTOR, "#i97 > .uHMk6b").click()  # wb x the dome
    driver.find_element(By.CSS_SELECTOR, "#i228 > .uHMk6b").click()  # ayo x women
    driver.find_element(By.CSS_SELECTOR, "#i231 > .uHMk6b").click()  # natasha x women
    driver.find_element(By.CSS_SELECTOR, "#i240 > .uHMk6b").click()  # ashley x women
    driver.find_element(By.CSS_SELECTOR, "#i298 > .uHMk6b").click()  # jules x renee rapp
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_top_two(driver):
    time.sleep(0.05)
    #celebrities
    driver.find_element(By.CSS_SELECTOR, "#i9 > .uHMk6b").click()  # taylor X diana
    driver.execute_script("window.scrollTo(0,500)")
    driver.find_element(By.CSS_SELECTOR, "#i57 > .uHMk6b").click()  # ben x a job
    #celebrities 2
    driver.find_element(By.CSS_SELECTOR, "#i71 > .uHMk6b").click()  # pacino x inceldmen
    driver.find_element(By.CSS_SELECTOR, "#i77 > .uHMk6b").click()  # bastille x imagine dragons
    #d20
    driver.find_element(By.CSS_SELECTOR, "#i88 > .uHMk6b").click()  # emily x aabria
    driver.find_element(By.CSS_SELECTOR, "#i97 > .uHMk6b").click()  # wb x the dome
    #not rpf
    driver.find_element(By.CSS_SELECTOR, "#i131 > .uHMk6b").click()  # wga x winning
    driver.find_element(By.CSS_SELECTOR, "#i146 > .uHMk6b").click()  # angels manager x death
    #polycule
    driver.find_element(By.CSS_SELECTOR, "#i183 > .uHMk6b").click()  # mojos no good day
    #parents
    driver.find_element(By.CSS_SELECTOR, "#i203 > .uHMk6b").click()  # lauras mom x ron swanson
    #sexuality theory
    driver.find_element(By.CSS_SELECTOR, "#i228 > .uHMk6b").click()  # ayo x women
    driver.find_element(By.CSS_SELECTOR, "#i231 > .uHMk6b").click()  # natasha x women
    #rapture friendship
    driver.find_element(By.CSS_SELECTOR, "#i248 > .uHMk6b").click()  # rapture x botw
    driver.find_element(By.CSS_SELECTOR, "#i254 > .uHMk6b").click()  # rapture x movies
    #y/n
    driver.find_element(By.CSS_SELECTOR, "#i274 > .uHMk6b").click()  # keegan x patrick
    driver.find_element(By.CSS_SELECTOR, "#i277 > .uHMk6b").click()  # keegan x lindt
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_top_1(driver):
    time.sleep(0.05)
    # celebrities
    driver.execute_script("window.scrollTo(0,500)")
    driver.find_element(By.CSS_SELECTOR, "#i57 > .uHMk6b").click()  # ben x a job
    # celebrities 2
    driver.find_element(By.CSS_SELECTOR, "#i77 > .uHMk6b").click()  # bastille x imagine dragons
    # d20
    driver.find_element(By.CSS_SELECTOR, "#i97 > .uHMk6b").click()  # wb x the dome
    # not rpf
    driver.find_element(By.CSS_SELECTOR, "#i131 > .uHMk6b").click()  # wga x winning
    # polycule
    driver.find_element(By.CSS_SELECTOR, "#i183 > .uHMk6b").click()  # mojos no good day
    # parents
    driver.find_element(By.CSS_SELECTOR, "#i203 > .uHMk6b").click()  # lauras mom x ron swanson
    # sexuality theory
    driver.find_element(By.CSS_SELECTOR, "#i231 > .uHMk6b").click()  # natasha x women
    # rapture friendship
    driver.find_element(By.CSS_SELECTOR, "#i248 > .uHMk6b").click()  # rapture x botw
    # y/n
    driver.find_element(By.CSS_SELECTOR, "#i274 > .uHMk6b").click()  # keegan x patrick
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()