from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
import time
dict1={}
list1=[]

a=webdriver.Chrome()
a.maximize_window()

a.get("https://www.zomato.com/chennai")
time.sleep(4)

b=a.find_element_by_xpath("//a[@class='col-l-1by3 col-s-8 pbot0']").click()

d=a.find_elements_by_xpath("//div[@class='col-l-4 mtop pagination-number']")
for j in d:
	page=j.text[10:]
	pprint(page)
for k in range(1,int(page)):
	print(k)
	a.get("https://www.zomato.com/chennai/t-nagar-restaurants?page="+str(1))
	c=a.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")
	add=a.find_elements_by_xpath("//div[@class='col-m-16 search-result-address grey-text nowrap ln22']")
	cuisines=a.find_elements_by_xpath("//span[@class='col-s-11 col-m-12 nowrap  pl0']")
	cost=a.find_elements_by_xpath("//span[@class='col-s-11 col-m-12 pl0']")
	hours=a.find_elements_by_xpath("//div[@class='col-s-11 col-m-12 pl0 search-grid-right-text ']")

	name={}
	for g in range(len(c)):
		name["name"]=c[g].text
		name["address"]=add[g].text
		name["cuisines"]=cuisines[g].text
		name["cost"]=cost[g].text
		name["hours"]=hours[g].text
	list1.append(name)
dict1["t_nagar"]=list1
pprint(dict1)
a.close()