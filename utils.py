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

def vote_imodna(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i60 > .uHMk6b").click()  # imodna
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_bees(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i27 > .uHMk6b").click()  # bees
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_kanthony(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i21 > .uHMk6b").click()  # kanthony
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_hizzie(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i36 > .uHMk6b").click()  # hizzie
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_palmsprings(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i72 > .uHMk6b").click()  # palm springs
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_allb4b(driver):
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, "#i6 > .uHMk6b").click()  # simmosa
    driver.find_element(By.CSS_SELECTOR, "#i9 > .uHMk6b").click()  # ava/deborah
    driver.find_element(By.CSS_SELECTOR, "#i12 > .uHMk6b").click()  # bellamy/raven
    driver.find_element(By.CSS_SELECTOR, "#i18 > .uHMk6b").click()  # big red/ashlyn
    driver.find_element(By.CSS_SELECTOR, "#i24 > .uHMk6b").click()  # brooklyn/malibu
    driver.find_element(By.CSS_SELECTOR, "#i45 > .uHMk6b").click()  # will/elizabeth
    driver.find_element(By.CSS_SELECTOR, "#i54 > .uHMk6b").click()  # glimbow
    #driver.find_element(By.CSS_SELECTOR, "#i60 > .uHMk6b").click()  # handon (this one is for nia)
    driver.find_element(By.CSS_SELECTOR, "#i90 > .uHMk6b").click()  # korrasami
    driver.find_element(By.CSS_SELECTOR, "#i111 > .uHMk6b").click()  # marhsall/lily
    driver.find_element(By.CSS_SELECTOR, "#i114 > .uHMk6b").click()  # megamind
    driver.find_element(By.CSS_SELECTOR, "#i120 > .uHMk6b").click()  # moonshine/hardwon
    driver.find_element(By.CSS_SELECTOR, "#i171 > .uHMk6b").click()  # sukka
    driver.find_element(By.CSS_SELECTOR, "#i180 > .uHMk6b").click()  # jjk
    driver.find_element(By.CSS_SELECTOR, "#i183 > .uHMk6b").click()  # zagreus/meg
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.5)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_jules(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i75 > .uHMk6b").click()  # glimbow
    driver.find_element(By.CSS_SELECTOR, "#i87 > .uHMk6b").click()  # howl sophie
    driver.find_element(By.CSS_SELECTOR, "#i126 > .uHMk6b").click()  # korrasami
    driver.find_element(By.CSS_SELECTOR, "#i153 > .uHMk6b").click()  # seahawk/mermista
    driver.find_element(By.CSS_SELECTOR, "#i222 > .uHMk6b").click()  # sukka
    driver.find_element(By.CSS_SELECTOR, "#i240 > .uHMk6b").click()  # jjk
    time.sleep(30)
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_multi(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i12 > .uHMk6b").click()  # bellamy/raven
    driver.find_element(By.CSS_SELECTOR, "#i42 > .uHMk6b").click()  # eleanor/chidi
    driver.find_element(By.CSS_SELECTOR, "#i66 > .uHMk6b").click()  # janine/gregory
    driver.find_element(By.CSS_SELECTOR, "#i108 > .uHMk6b").click()  # maddie/chimney
    driver.find_element(By.CSS_SELECTOR, "#i141 > .uHMk6b").click()  # percabeth
    driver.find_element(By.CSS_SELECTOR, "#i210 > .uHMk6b").click()  # fig/gorgug
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_jules2(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i75 > .uHMk6b").click()  # glimbow
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i87 > .uHMk6b").click()  # korrasami
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i126 > .uHMk6b").click()  # seahawk/mermista
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i153 > .uHMk6b").click()  # sukka
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i222 > .uHMk6b").click()  # jjk
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i240 > .uHMk6b").click()  # jjk
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_nia(driver):
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, "#i18 > .uHMk6b").click()  # big red/ashlyn
    #driver.find_element(By.CSS_SELECTOR, "#i60 > .uHMk6b").click()  # handon (this one is for nia)
    driver.find_element(By.CSS_SELECTOR, "#i171 > .uHMk6b").click()  # sukka
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_extra(driver):
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, "#i9 > .uHMk6b").click()  # ava/deborah
    driver.find_element(By.CSS_SELECTOR, "#i111 > .uHMk6b").click()  # marhsall/lily
    driver.find_element(By.CSS_SELECTOR, "#i114 > .uHMk6b").click()  # megamind
    driver.find_element(By.CSS_SELECTOR, "#i120 > .uHMk6b").click()  # moonshine/hardwon
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.6)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_tier1(driver):
    driver.find_element(By.CSS_SELECTOR, "#i54 > .uHMk6b").click()  # glimbow
    driver.find_element(By.CSS_SELECTOR, "#i180 > .uHMk6b").click()  # jjk
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_tier2(driver):
    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, "#i54 > .uHMk6b").click()  # glimbow
    driver.find_element(By.CSS_SELECTOR, "#i90 > .uHMk6b").click()  # korrasami
    driver.find_element(By.CSS_SELECTOR, "#i180 > .uHMk6b").click()  # jjk
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_tier3(driver):
    driver.find_element(By.CSS_SELECTOR, "#i54 > .uHMk6b").click()  # glimbow
    driver.find_element(By.CSS_SELECTOR, "#i90 > .uHMk6b").click()  # korrasami
    driver.find_element(By.CSS_SELECTOR, "#i171 > .uHMk6b").click()  # sukka
    driver.find_element(By.CSS_SELECTOR, "#i180 > .uHMk6b").click()  # jjk
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_glimbbow(driver):
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, "#i54 > .uHMk6b").click()  # glimbow
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_korrasami(driver):
    driver.find_element(By.CSS_SELECTOR, "#i87 > .uHMk6b").click()  # korrasami
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_sukka(driver):
    driver.find_element(By.CSS_SELECTOR, "#i171 > .uHMk6b").click()  # sukka
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_jjk(driver):
    driver.find_element(By.CSS_SELECTOR, "#i180 > .uHMk6b").click()  # jjk
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_simmosa(driver):
    driver.find_element(By.CSS_SELECTOR, "#i6 > .uHMk6b").click()  # simmosa
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_avadeb(driver):
    driver.find_element(By.CSS_SELECTOR, "#i9 > .uHMk6b").click()  # ava/deborah
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_bellraven(driver):
    driver.find_element(By.CSS_SELECTOR, "#i12 > .uHMk6b").click()  # bellamy/raven
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_redlyn(driver):
    time.sleep(0.05)
    driver.find_element(By.CSS_SELECTOR, "#i21> .uHMk6b").click()  # big red/ashlyn
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    time.sleep(0.3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_barbie(driver):
    driver.find_element(By.CSS_SELECTOR, "#i24 > .uHMk6b").click()  # brooklyn/malibu
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_willizabeth(driver):
    driver.find_element(By.CSS_SELECTOR, "#i45 > .uHMk6b").click()  # will/elizabeth
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_handon(driver):
    driver.find_element(By.CSS_SELECTOR, "#i60 > .uHMk6b").click()  # handon (this one is for nia)
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_janinegregory(driver):
    driver.find_element(By.CSS_SELECTOR, "#i66 > .uHMk6b").click()  # janine/gregory
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_marshalllily(driver):
    driver.find_element(By.CSS_SELECTOR, "#i111 > .uHMk6b").click()  # marhsall/lily
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_megamind(driver):
    driver.find_element(By.CSS_SELECTOR, "#i114 > .uHMk6b").click()  # megamind
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_moonshine(driver):
    driver.find_element(By.CSS_SELECTOR, "#i120 > .uHMk6b").click()  # moonshine/hardwon
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

def vote_zagmeg(driver):
    driver.find_element(By.CSS_SELECTOR, "#i183 > .uHMk6b").click()  # zagreus/meg
    driver.find_element(By.CSS_SELECTOR, ".Y5sE8d .NPEfkd").click()  # submit
    driver.find_element(By.LINK_TEXT, "Submit another response").click()