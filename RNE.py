import pandas as pd
url= 'https://www.registre-entreprises.tn/search/RCCSearch.do?action=getPage&rg_type=PM&search_mode=NORMAL'
ident=input('Donner votre identifiant unique: ') # you can try ident='0031458D'
webdriver_path= 'C:\\Webdriver\\chromedriver.exe' # the path to the folder containing the web driver + the name of the webdriver

from selenium import webdriver
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get(url) # accessing the website
search_by_id= driver.find_element_by_name('searchRegistrePmRcc.registrePm.numPatente') 
# Getting the text field by using its name (you can also use the xpath like i ve used below)
search_by_id.send_keys(ident)
# Inserting the id into the text field
send= driver.find_element_by_xpath('//*[@id="page"]/form[1]/div/div[7]/div[2]/div/div/div')
# Since the search button doesn't have a suitable attribute we can use, we have to use the xpath
send.click() # Clicking on the search button

try:
    # If the id is valide the following instructions we be executed
    search= driver.find_element_by_xpath('//*[@id="page"]/form[1]/div/div/div/div/table/tbody/tr[8]/td[2]/table/tbody/tr/td[4]')
    search.click()
    table_data=[] # We will store the data of the table into a list
    for row in range (2,8):
        l=[]
        for column in range (1,5):
            xpath=f'//*[@id="page"]/form[1]/div/div/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table[3]/tbody/tr[{row}]/td[{column}]'
            l.append(driver.find_element_by_xpath(xpath).text) 
            # Transforming the selenium object into text and adding it to the list
        table_data.append(l)
    driver.close() # Closing the webdriver
    df= pd.DataFrame(data=table_data) # Transforming the data in the list into a dataframe
    print(df)
    df.to_excel(fr'C:\Users\ilyes\Desktop\IdUnique_{ident}.xlsx') 
    # Saving our dataframe as an excel file (you can also use other formats such as csv)
except:
    # If the ID is invalide then we print a messge and we close the webdriver
    print('votre identifiant est invalide')
    driver.close()