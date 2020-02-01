from selenium import webdriver
from pprint import pprint
import time
a=webdriver.Chrome()
a.get("https://www.zomato.com/chennai")
a.maximize_window()

a.find_element_by_xpath("//input[@id='keywords_input']").send_keys("Cake Square")
list1=a.find_element_by_xpath("//div[@id='search_button']")
time.sleep(3)
list1.click()
cost=a.find_elements_by_xpath("//span[@class='col-s-11 col-m-12 pl0']")
costs=[i.text for i in cost]
# pprint(costs)
name=a.find_elements_by_xpath("//a[@class='ln24 search-page-text mr10 zblack search_result_subzone left']/b")
name=[i.text for i in name]
# pprint(name)
adress=a.find_elements_by_xpath("//div[@class='col-m-16 search-result-address grey-text nowrap ln22']")
adress=[i.text for i in adress]
# pprint(adress)
CUISINES=a.find_elements_by_xpath("//span[@class='col-s-11 col-m-12 nowrap  pl0']")
cuisines=[i.text for i in CUISINES]
# pprint(cuisines)
time=a.find_elements_by_xpath("//div[@class='col-s-11 col-m-12 pl0 search-grid-right-text ']")
duratiion=[]
days_available=[]
for i in time:
	o=i.text.split("(")
	if len(o)==2:
		duratiion.append(o[0])
		days_available.append(o[1].strip(")"))
# pprint(duratiion)
# pprint(days_available)
Total={}
for i in range((len(adress))):	
	Total["name"]=name[i]
	Total["adress"]=adress[i]
	Total["cuisines"]=cuisines[i]
	Total["duratiion"]=duratiion[i]
	Total["costs"]=costs[i]
	Total["days_available"]=days_available[i]
	pprint(Total)
a.quit()