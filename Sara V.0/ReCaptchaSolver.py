#TODO code ReCaptcha Solver
from distutils.log import error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import random
import pydub
import urllib
from speech_recognition import Recognizer, AudioFile
import os


#os path
path = os.path.abspath(os.getcwd())
options = Options()
ua = UserAgent()
userAgent = ua.random
print("userAgent: "+ userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome("chromedriver.exe")


#login to google
driver.get("https://accounts.google.com/signin")
login_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
sleep((randint(1,2) + random.random()))
login_field.send_keys("saraliminal@gmail.com")
sleep((randint(1,2) + random.random()))
next_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
next_button.click()
sleep((randint(1,2) + random.random()))
password_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
password_field.send_keys("Yutan#123")
sleep((randint(1,2) + random.random()))
second_next_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
second_next_button.click()
sleep(randint(3,6))

#get website
driver.get("https://www.youtube.com/c/RealLifeLore/about")

sleep((randint(2,4)+random.random()))
button = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[4]/table/tbody/tr[1]/td[3]/ytd-button-renderer/a/tp-yt-paper-button")
print(button)
button.click()
sleep((randint(2,4)+random.random()))
 
recaptcha_iframe = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[4]/table/tbody/tr[1]/td[4]/div/div/div/iframe")
driver.switch_to.frame(recaptcha_iframe)
#sleep(1000)
driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()
sleep((randint(2,4)+random.random()))
driver.switch_to.default_content()
sleep((randint(1,2) + random.random()))
second_iframe = driver.find_element_by_xpath("/html/body/div/div[4]/iframe")
sleep((randint(1,2) + random.random()))
driver.switch_to.frame(second_iframe)
sleep((randint(1,2) + random.random()))
driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button").click()
sleep((randint(1,2) + random.random()))
driver.switch_to.default_content()
sleep((randint(1,2) + random.random()))

driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div/div[4]/iframe"))
sleep((randint(1,2) + random.random()))
try:
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
    print("--SUBSTEP 1 SUCCESS--")
    print("CONTINUING...")
    sleep((randint(2,4)+random.random()))
except:
    print("FAILED - HUMAN INTERVENTION REQUIRED")
    print("1000 seconds until crash...")
    sleep(1000)


try:
    src=driver.find_element_by_id("audio-source").get_attribute("src")
    print(src)
    urllib.request.urlretrieve(src, path+"\\audio.mp3")

    sound = pydub.AudioSegment.from_mp3(path+"\\audio.mp3").export(path+"\\audio.wav",format="wav")
    recognizer = Recognizer()
    recaptcha_audio = AudioFile(path+"\\audio.wav")
    with recaptcha_audio as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)

    print("PREDICTED TEXT: ")
    print(text)
    print("---------------------------------")
    
    inputfield = driver.find_element_by_id("audio-response")
    #inputfield.send_keys(text.lower())
    text = text.lower()
    response_list = list(text)
    for i in list:
        inputfield.send_keys(i)
        print("sent: " + i)
        sleep(random.random())

    inputfield.send_keys(Keys.ENTER)

    sleep(10)
    print("Success")
    sleep(1000)
    driver.quit()

except:
    print("Failed")
    print(error)
    #print(NameError)
    sleep(1000)
    driver.quit()
