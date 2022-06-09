from this import d
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import urllib.request


PATH="C:/Users/Gustavo/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/Scripts/chromedriver.exe"
options=webdriver.chrome.options.Options()
options.add_argument("--headless")
driver = webdriver.Chrome(PATH,options=options)

driver.get("https://www.fourmilab.ch/cgi-bin/Yoursky") #site


#fixed parameters

driver.find_element(By.NAME, value="consto").click() #Const outlines

driver.find_element(By.NAME, value="limag").clear() #brightness mag
driver.find_element(By.NAME, value="limag").send_keys(6)  #brightness mag

driver.find_element(By.NAME, value="imgsize").clear()  #image size
driver.find_element(By.NAME, value="imgsize").send_keys(2048) #image size

select = Select(driver.find_element(By.XPATH, value="/html/body/form/center/table/tbody/tr[3]/td/select")) #Back colour dropdown
select.select_by_value('2')

driver.find_element(by=By.XPATH, value="/html/body/form/center/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input").click() #botao date


from datetime import datetime, timedelta

lista =[]
d=1000
for x in range (0,d):
    lista.append((datetime(2022, 2, 13) - timedelta(days=x)).strftime("%Y-%m-%d"))     #create array of dates / establish first date


cidades=["New York", "Boston", "Madrid", "Washington DC", "San Francisco", "London", "Toronto", "Dublin", "Mexico City", "Chicago", "Los Angeles", "Paris", "Vienna", "Stockholm", "Zurich", "Helsinki", "Kyiv", "Cairo", "Tel Aviv", "Beijing", "Shanghai", "Seoul", "Singapore", "Tokyo", "Hong Kong", "Moscow", "Sydney", "Cape Town", "Rio de Janeiro"] #cities
clat=["40.7128", "42.3601", "40.4168","38.9072", "37.7749", "51.5072","43.6532","53.3498","19.4326", "41.8781", "34.0522", "48.8566", "48.2082","59.3293","47.3769","60.1699","50.4501","30.0444", "32.0853","39.9042","31.2304","37.5665","1.3521","35.6762","22.3193","55.7558","-33.8688","-33.9249","-22.9068"] #lat coordinates
clon= ["-74.0060", "-71.0589","-3.7038","-77.0369","-122.4194","-0.1276", "-79.3832", "-6.2603","-99.1332", "-87.6298", "-118.2437", "2.3522", "16.3738","18.0686","8.5417", "24.9384","30.5234","31.2357", "34.7818","116.4074","121.4737","126.9780","103.8198","139.6503","114.1694","37.6173","151.2093","18.4241","-43.1729"] #lon coordinates


d = 50
for i in range (0,d):

    driver.find_element(By.XPATH, value="/html/body/form/center/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input").clear() #date
    driver.find_element(By.XPATH, value="/html/body/form/center/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input").send_keys(lista[i]+" 23:59:00") #date

    for j in range (0,len(cidades)):

        driver.find_element(By.NAME, value="lat").clear() #input de lat
        driver.find_element(By.NAME, value="lat").send_keys(abs(float(clat[j]))) #input de lat
        driver.find_element(By.NAME, value="lon").clear() #input de lon
        driver.find_element(By.NAME, value="lon").send_keys(abs(float(clon[j]))) #input de lon


        driver.find_element(By.XPATH, value="//*[contains(text(), 'North')]").click() #norte
        driver.find_element(By.XPATH, value="//*[contains(text(), 'West')]").click() #west        
        #if j==27:
        #    driver.find_element(By.XPATH, value="//*[contains(text(), 'South')]").click() #south
            
        #if j==11 or j==32:
        #    driver.find_element(By.XPATH, value="//*[contains(text(), 'East')]").click() #east
        #if j==0 or j==18:



        driver.find_element(By.XPATH, value="/html/body/form/center/input").click() #update

        img = driver.find_element(By.XPATH, value='/html/body/center[2]/img')
        src = img.get_attribute('src')

        urllib.request.urlretrieve(src,lista[i]+" "+cidades[j]+".png") # download the image


#driver. close()

