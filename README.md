# youTube_Subscription_bot
This is a simple python project that can notify a telegram bot every time your Youtube subscribed channels upload new video.<br>
The project runs in the sequence below:<br>
a- The code goes to the youtube accounts page using the ChromeDriver.<br>
b- Using selenium library, the webdriver enters the username and password from the credintials file to log in.<br>
c- Now we have been logged in into the subscriptions page and waiting the Telegram user to send {/start} command to the telegram bot.<br>
d- When {/start} is sent, webdriver using Selenium will scrape the videos names,channel name and link and saving them in three lists.<br>
e- The code then comparing the name lists with the names in the data.csv file.<br>
f- If the name isn't exist the python-telegram-bot send the video's information to the telegram bot the adding them to the data.csv file<br>
g- Else nothing will happend.<br>
h- The webdriver will refreash the page every minute and do the cycle again.<br>
<br>
<b>Requirments:<br>
1- python-telegram-bot version 20.3 to install it:<br>
pip install python-telegram-bot==20.3<br>
2- selenium library : <br>
pip install selenium<br>
3- Google Chrome browser version 114.0.5735.134 (stop the auto updating so that the Chrome version keep up with the Chromdriver version)<br>
4- ChromeDriver 114.0.5735.90 you can download it from:<br>
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/<br>
5- Pandas and CSV libraries:<br>
pip install pandas<br>
6- Telegram account and platform(App/Desktop/Web)<br>
7- Creating Telegram bot using botFather and save the bot token.<br>
8- A good network speed<br>
<br>
<b>Note:<br>
The credintials.py file have 3 values to be enterd:<br>
username: your email name the assosiated with Youtube.<br>
password: your email password.<br>
botToken: the token of your Telegram bot.<br>

