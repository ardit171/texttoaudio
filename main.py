import pickle

import requests
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.ibm.com/demos/live/tts-demo/self-service/home'
class Dialect:
    dialect = []
    voice = []

    def getVoice(self):
        pass

class AmericanDialect(Dialect):
    voice = [
        "Michael",
        "Allison",
        "Emily",
        "Henry",
        "Kevin",
        "Lisa",
        "Olivia",
    ]
    def getVoice(self):
        return self.voice

class BritishDialect(Dialect):
    voice = [
        "Kate",
        "Charlotte",
        "James",
    ]
    def getVoice(self):
        return self.voice

def addDialect(driver, type="American"):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "dialect"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title*='" + type + "']"))).click()


def addNeuralVoice(driver, neuralVoice):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "voice"))).click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[title*='" + neuralVoice + "']"))).click()


def addText(driver, text):
    text_input: WebElement = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.ID,
                'text-area',

            )
        )
    )
    text_input.clear()
    text_input.send_keys(text)


def getAudioUrl(driver):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "play-btn.bx--btn.bx--btn--field.bx--btn--primary"))).click()
    if WebDriverWait(driver, 20).until(EC.element_attribute_to_include(
            (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[3]/audio"), "src")):
        audioElement = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[3]/audio")
        audioUrl = audioElement.get_attribute("src")
        return audioUrl
    return None


def saveCookies(driver):
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

def download(text,dialect,voice,folder_path):
    try:
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4430/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX,
        )
        driver.set_window_size(1280, 720)
        driver.get(url)
        addDialect(driver, dialect)
        addNeuralVoice(driver, voice)
        addText(driver, text)
        sleep(3)
        audioUrl = getAudioUrl(driver)
        cookies = driver.get_cookies()
        print(audioUrl)
        session = requests.session()  # or an existing session
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        doc = session.get(audioUrl)
        with open(folder_path+'/audio.mp3', 'wb') as f:
            f.write(doc.content)
        driver.quit()
        return True
    except:
        driver.quit()
        return False

dialects = {
    "American":AmericanDialect(),
    "British": BritishDialect()
}
# make runable 
if __name__ == '__main__':
    # here we go
    download(url)
