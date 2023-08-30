# youTube_Subscription_bot
This is a simple python project that can notify a telegram bot every time your Youtube subscribed channels upload new video.\n
The project runs in the sequence below:\n
a- The code goes to the youtube accounts page using the ChromeDriver.\n
b- Using selenium library, the webdriver enters the username and password from the credintials file to log in.\n
c- Now we have been logged in into the subscriptions page and waiting the Telegram user to send {/start} command to the telegram bot.\n
d- When {/start} is sent, webdriver using Selenium will scrape the videos names,channel name and link and saving them in three lists.\n
e- The code then comparing the name lists with the names in the data.csv file.
f- If the name isn't exist the python-telegram-bot send the video's information to the telegram bot the adding them to the data.csv file
g- Else nothing will happend.
h- The webdriver will refreash the page every minute and do the cycle again.

Requirments:
1- python-telegram-bot version 20.3 to install it:
pip install python-telegram-bot==20.3
2- selenium library : 
pip install selenium
3- Google Chrome browser version 114.0.5735.134 (stop the auto updating so that the Chrome version keep up with the Chromdriver version)
4- ChromeDriver 114.0.5735.90 you can download it from:
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
5- Pandas and CSV libraries:
pip install pandas
6- Telegram account and platform(App/Desktop/Web)
7- Creating Telegram bot using botFather and save the bot token.
8- A good network speed

Note:
The credintials.py file have 3 values to be enterd:
username: your email name the assosiated with Youtube.
password: your email password.
botToken: the token of your Telegram bot.

