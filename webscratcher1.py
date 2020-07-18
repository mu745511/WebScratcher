import pandas as pd
import requests

from bs4 import BeautifulSoup
page=requests.get("https://forecast.weather.gov/MapClick.php?site=twc&textField1=32.19580&textField2=-110.89170#.XwCO_tyxWDI")
soup=BeautifulSoup(page.content,'html.parser')
week=soup.find(id="seven-day-forecast-body")
#print(week)
items=week.find_all(class_="tombstone-container")
#print(items[2])
print(items[2].find(class_="period-name").get_text())
print(items[2].find(class_="short-desc").get_text())
print(items[2].find(class_="temp").get_text())
period_names= [item.find(class_="period-name").get_text() for item in items ]
print(period_names)
short_descp=[item.find(class_="short-desc").get_text() for item in items ]
print(short_descp)
tempe=[item.find(class_="temp").get_text() for item in items ]
print(tempe)
weather_stuff=pd.DataFrame({"period":period_names,"descprition":short_descp,"temperature":tempe})
print(weather_stuff)
weather_stuff.to_csv("weather.csv")
