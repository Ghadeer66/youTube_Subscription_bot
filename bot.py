###################--- importing libraries ---######################
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from csv import writer
import pandas as pd
from time import sleep
from credintials import username,password,botToken

#######################################################################################
notefied = []

###################--- establishing the webDriver and make it undetected ---######################
driver = uc.Chrome()

###################--- connecting webDriver youtube Sign In page then signing in using selenium---######################
driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Ffeed%252Fsubscriptions%253FthemeRefresh%253D1&ec=65620&hl=en&ifkv=AXo7B7VTFaHsLJgT-tq7m4B6RrdlNC5ltjgRKQWFj7EAZ27E7b-IuUFTEQnQ7RWOwhjrKoackdCH9w&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-16493631%3A1693300940426380')
usr = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'identifierId')))
usr.send_keys(username)
sleep(1)
driver.find_element(By.ID,'identifierNext').click() 
sleep(2)
pwd = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")))
pwd.send_keys(password)
driver.find_element(By.ID,'passwordNext').click() 
sleep(15)

###################--- defining the function that will send the data to the bot ---######################
###################--- also connecting with database {csv file} to get and store data from it ---######################
async def st(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   
    while(1):
        csv_vids= pd.read_csv("data.csv",on_bad_lines='skip')
        saved_vids = csv_vids['vid'].tolist()
        driver.refresh()

###################--- getting data from web page and store them into three lists ---######################
        my_ch = list(driver.find_elements(By.ID, 'text'))
        my_vid = list(driver.find_elements(By.ID, 'video-title-link'))
        videos = [vid.text for vid in my_vid]
        vid = videos[:8]
        channels = [ch1.text for ch1 in my_ch]
        links = [elem.get_attribute('href') for elem in my_vid]

###################--- Reading and Storing data from and to the database ---######################
        with open('data.csv', 'a',encoding="utf-8-sig") as f_object:

###################--- Comparing between web page content and saved videos name in database ---######################
                for i in vid:
                        if i in saved_vids:
                            pass
                        else:
                                print(i)
                                notefied.append(i)
                                notefied.append(channels[videos.index(i)])
                                notefied.append(links[videos.index(i)])
                                writer_object = writer(f_object,lineterminator = '\n')
                                writer_object.writerow(notefied)
                                await update.message.reply_text(f'Video Name: {i} \n Channel: {channels[videos.index(i)]}  \n Link: {links[videos.index(i)]}')
                                notefied.clear()
                f_object.close() 

###################--- Redoing the operation after one minute ---######################
        sleep(60)   

###################--- Linking with the Telegram bot ---######################
app = ApplicationBuilder().token(botToken).read_timeout(20).write_timeout(20).build()

###################--- Waiting user to send /start order to the Telegram bot ---######################
app.add_handler(CommandHandler("start", st))
app.run_polling()