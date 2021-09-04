# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:21:19 2020

@author: raang


pip install names
pip install selenium
pip install requests
pip install xlsxwriter
Results to be found at

>>> import datetime
>>> datetime.datetime.strptime('24052010', "%d%m%Y").date()
datetime.date(2010, 5, 24)
"""

#                              1. Packages and Libraries
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import datetime, timedelta
from lxml import html
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib import request
import itertools
import lxml.html as lh
import names
import os
import pandas as pd
import operator
import random, string
import re
import requests
import ssl
import time
import numpy as np
from dateutil.relativedelta import relativedelta

os.getcwd()
path = os.getcwd()
print(path)


"""
del tag['another-attribute']
del tag['id']
from bs4 import BeautifulSoup
os.getcwd()
print(soup)
print(soup.b)
print(soup.b.name)
print(soup.find('b'))
print(soup.find_all('b'))
print(soup.p)
print(soup.prettify())
print(soup.prettyfy)
print(soup_level1)
print(tag)
print(tag.attrs) #dictionary key and Value
print(tag['another-attribute'])
print(tag['id'])## array index notation tag has an attribute called id
soup = BeautifulSoup(html_doc, "lxml")
soup_level1=BeautifulSoup(driver.page_source, 'lxml')
tag = soup.b
tag = soup.find_all('b')[1]
tag.name = "blockquote" #name is a property instead of b set name equal to bolckquote
tag['another-attribute'] = 1
type(surveys_df)
pandas.core.frame.DataFrame
Next, let’s look at the structure of our surveys data. In pandas, we can check the type of one column in a DataFrame using the syntax dataFrameName[column_name].dtype:
#datatypes
surveys_df['sex'].dtype
dtype('O')
A type ‘O’ just stands for “object” which in Pandas’ world is a string (text).

surveys_df['record_id'].dtype
dtype('int64')
The type int64 tells us that Python is storing each value within this column as a 64 bit integer. 
We can use the dat.dtypes command to view the data type for each column in a DataFrame (all at once).
surveys_df.dtypes

df = pd.DataFrame(columns=['QuoteNumber', 'SubProduct', 'Destination', 'NumNights', 'GroupType', 'DOB', 'rank', 'insurer', 'price', 'product', 'medical', 'med_xs', 'baggage', 'baggage_xs', 'canx', 'canx_xs', 'single_limit'])


Scenarios at least
age 26
•	with up to 3 passengers
•	ST and AMT
•	Duration ST 8 , 11, 15 and AMT 365
•	Destination Spain Vs USA  

"""
#***********************************************************************************************

#                                2. Generating Input Fields

#***********************************************************************************************
#2.Generating input fields

#2.1. TrypType_input 

tryptype_input = [
        'ST'
        ,
        'AMT' 
                  ]

#2.2 Destination Input
dest_st_input = ['Spain'
                    ,'USA'
                     ,'Australia'
                    ,'United Kingdom'
                     
                     ]
dest_amt_input = [
        #'United Kingdom'
         #            ,
                     'Europe'
                ,'Worldwide'
                   #,'Worldwide (excluding USA, Canada, Mexico and Caribbean)'
                     ]



#2.3 Origin_Dae and Return Date

#For st orgina date and return date
delta_origin=61 ##one plus to allow for the difference
delta_return=9 #duration1
delta_return2=12#duration2
delta_return3=16#duration3
delta_return4=366#amt duration
delta_age_1=9490
delta_age_2=14400

origin_date=datetime.today() + timedelta(delta_origin)# has time also 
origin_date_input=origin_date
origin_date_cleaned=origin_date.strftime("%d-%m-%Y")
print(origin_date_cleaned)

#############################################RETURN DATE NEEDS TO INCREASE SCENARIOS
return_date = origin_date + timedelta(delta_return)#has time also
return_date2 = origin_date + timedelta(delta_return2)#has time also
return_date3 = origin_date + timedelta(delta_return3)
return_date4 = origin_date + timedelta(delta_return4)
return_date_input=return_date
return_date_list=[return_date, return_date2, return_date3, return_date4]
print(return_date_list)
return_date_list_cleaned= [return_date_list[0].strftime("%d-%m-%Y")
,return_date_list[1].strftime("%d-%m-%Y")
,return_date_list[2].strftime("%d-%m-%Y")
,return_date_list[3].strftime("%d-%m-%Y")]
print(return_date_list_cleaned)

#Format with no "time"
return_date_cleanedx=return_date.strftime("%d-%m-%Y")
print(return_date_cleanedx)

#2.5 Optional Cover
#optional_cover=['Gadget Cover','Cruise Cover','Winter Sports']
optional_cover=[''
                #,'Winter Sports'
                ]

#2.6 Who is travelling

who_input =[
        #'Individual'
           # ,'Couple'
           # ,
            'Family'
           # ,'Group'
            ]
#when couple the preex is affected
#2.7  Main Traveller Name
#title_input=['Mrs','Ms','Miss','Mr','Sir']#only one option for now
title_input=['Mr']#only one option for now

#2.8 Traveller's Date of Birth (DOB) 
#2.8.1 Main Traveller
#Three Scenarios for Main Traveller
#Main Traveller scenario 1
delta_age_m_sc1=26*366#Number of days for a person aged 26 years old as of today()
main_t_dob1=datetime.today()-timedelta(delta_age_m_sc1)#main traveller date
print(main_t_dob1)
main_t_dob1_cleaned=main_t_dob1.strftime("%d-%m-%Y")
print(main_t_dob1_cleaned)
main_t_dob1.day
main_t_dob1.month
main_t_dob1.year
#print(df_tree6)
#Main Traveller scenario 2
delta_age_m_sc2=36*366#Number of days for a person aged 40 years old as of today()
main_t_dob2=datetime.today()-timedelta(delta_age_m_sc2)#main traveller date
print(main_t_dob2)
main_t_dob2_cleaned=main_t_dob2.strftime("%d-%m-%Y")
print(main_t_dob2_cleaned)

#Main Traveller scenario 3
delta_age_m_sc3=46*366#Number of days for a person aged 50 years old as of today()
main_t_dob3=datetime.today()-timedelta(delta_age_m_sc3)#main traveller date
print(main_t_dob3)
main_t_dob3_cleaned=main_t_dob3.strftime("%d-%m-%Y")
print(main_t_dob3_cleaned)

#Main Traveller scenario 4
delta_age_m_sc4=56*366#Number of days for a person aged 61 years old as of today()
main_t_dob4=datetime.today()-timedelta(delta_age_m_sc4)#main traveller date
print(main_t_dob4)
main_t_dob4_cleaned=main_t_dob4.strftime("%d-%m-%Y")
print(main_t_dob4_cleaned)

#Main Traveller scenario 5
delta_age_m_sc5=61*366#Number of days for a person aged 61 years old as of today()
main_t_dob5=datetime.today()-timedelta(delta_age_m_sc5)#main traveller date
print(main_t_dob5)
main_t_dob5_cleaned=main_t_dob5.strftime("%d-%m-%Y")
print(main_t_dob5_cleaned)


## scenarios in a list
main_t_dob_input =[main_t_dob1
                   , main_t_dob2
                   , main_t_dob3
                   , main_t_dob4
                   #, main_t_dob5
                   ]
main_t_dob_cleaned=[main_t_dob1_cleaned, main_t_dob2_cleaned, main_t_dob3_cleaned, main_t_dob4_cleaned, main_t_dob5_cleaned]
print(main_t_dob_input)
main_t_dob_cleaned =[main_t_dob1_cleaned, main_t_dob2_cleaned, main_t_dob3_cleaned, main_t_dob4_cleaned, main_t_dob_cleaned]
print(main_t_dob_cleaned)

#2.8.2 Second Traveller if Who is Couple 
delta_age_sec_sc1=8760#

sec_t_dob1=datetime.today()-timedelta(delta_age_sec_sc1)#second traveller date
print(sec_t_dob1)
sec_t_dob1_cleaned=sec_t_dob1.strftime("%d-%m-%Y")
print(sec_t_dob1_cleaned)
sec_t_dob_input =[sec_t_dob1]
print(sec_t_dob_input)

#2.8.3 if family a third traveler and so on.
delta_age_third_sc1=1825# Child 

third_t_dob1=datetime.today()-timedelta(delta_age_third_sc1)#second traveller date
print(third_t_dob1)
third_t_dob1_cleaned=third_t_dob1.strftime("%d-%m-%Y")
print(third_t_dob1_cleaned)
third_t_dob1_input =[third_t_dob1]
print(third_t_dob1_input)

#... add more depending on number of children

#2.8.4 if Group a third traveler and so on.In this scenario all travellers are younger than main traveller
delta_age_thirdb_sc1=8360#

thirdb_t_dob1=datetime.today()-timedelta(delta_age_thirdb_sc1)#third traveller date in group
print(thirdb_t_dob1)
thirdb_t_dob1_cleaned=thirdb_t_dob1.strftime("%d-%m-%Y")
print(thirdb_t_dob1_cleaned)
thirdb_t_dob1_input =[thirdb_t_dob1]
print(thirdb_t_dob1_input)


delta_age_fourth_sc1=8260#

fourth_t_dob1=datetime.today()-timedelta(delta_age_fourth_sc1)#second traveller date
print(fourth_t_dob1)
fourth_t_dob1_cleaned=fourth_t_dob1.strftime("%d-%m-%Y")
print(fourth_t_dob1_cleaned)
fourth_t_dob_input =[fourth_t_dob1]
print(fourth_t_dob_input)

#2.9 Preexisting Medical Conditions

preex_input=['NO'
             #,'YES'
             ]#only one option for now?

#2.10 email generator
#email = (firstname_input)+(lastname_input)+''.join(random.choices(string.ascii_letters + string.digits, k=3))+'@yahoo.com'#.join'@yahoo.com'
#print(email)
#***********************************************************************************************
#                                          4. Combinations
#***********************************************************************************************
# result contains all possible combinations.
#ST with three alternatives for duration
combinationsST0 = list(itertools.product(
        tryptype_input[0:1] 
        ,dest_st_input,optional_cover,who_input
                                         ,main_t_dob_input
                                         ,preex_input,return_date_list_cleaned[0:1]))
print(combinationsST0)

combinationsST1 = list(itertools.product(tryptype_input[0:1] 
                                        ,dest_st_input
                                      ,optional_cover
                                      ,who_input
                                      ,main_t_dob_input
                                      ,preex_input
                                      ,return_date_list_cleaned[1:2]
                                       ))
print(combinationsST1)
combinationsST2 = list(itertools.product(tryptype_input[0:1]
                                      ,dest_st_input
                                      ,optional_cover
                                      ,who_input
                                      ,main_t_dob_input
                                      ,preex_input
                                      ,return_date_list_cleaned[2:3]
                                       ))
print(combinationsST2)


#print( tryptype_input[1:2]) for AMT
combinations2 = list(itertools.product(
                                        tryptype_input[1:2]
                                      ,dest_amt_input
                                      ,optional_cover
                                      ,who_input
                                        ,main_t_dob_input
                                        ,preex_input
                                      ,return_date_list_cleaned[3:4]
                                                          ))
print(combinations2)
combinations_raw=combinationsST0+combinationsST1+combinationsST2+combinations2



print(combinations_raw)
len(combinations_raw)
## To get the list of all possible scenarios 
l=0
combinations=[]
for l in range(0,len(combinations_raw)):
    print(combinations_raw[l][0]+'_'+combinations_raw[l][1])
    if combinations_raw[l][0]+'_'+combinations_raw[l][1] in (
        #'ST_Spain'
       # ,
        'ST_USA'
           #,'ST_Australia','ST_United Kingdom'
            #           ,
         ,
        #            ##
                  'AMT_Worldwide'
                    ,
                     'AMT_Europe'
                       #,'AMT_United Kingdom','AMT_Worldwide (excluding USA, Canada, Mexico and Caribbean)'
                       ):
        #print(combinations_raw[l][0]+'_'+combinations_raw[l][1])
        combinations.append(combinations_raw[l])
    else:
        continue
    
print(combinations)
len(combinations)
#***********************************************************************************************
#                                               5. Scenarios View
#***********************************************************************************************

print("The Combinations of iterating fields is:" + str(combinations))

print("List index-value for scenarios are:")
for x in range(len(combinations)):
    #print(x)
    print(x, end =" ")
    print(combinations[x])

#*********************************************************************************************

                               # 6. Launching Selenium and Beautiful soup

#***********************************************************************************************
#launch url
url = "https://www.kayak.co.uk/quote/" 
print(url)
# create a new Firefox session
driver = webdriver.Firefox()
time.sleep(5)
#driver.implicitly_wait(5)
#driver.get(url)
#driver.implicitly_wait(5)
#print(df_tree6)
#***********************************************************************************************

#***********************************************************************************************
#                                           6. Populate Input Fields 
#***********************************************************************************************
#for i in range(0,len(combinations)):

#new WebDriverWait(driver, 20).until(ExpectedConditions.elementToBeClickable(By.cssSelector("input[value='a_working_locator']"))).click();

df_tree16=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree15=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree14=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree13=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree12=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree11=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree10=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree9=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree8=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree7=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree6=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree5=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree4=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree3=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree2=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])
df_tree1=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT'])                                                                                                                                                                                                                                                                                                                                                                                        
                        
j=0
#i=13
i=13
scenario=combinations[i]
for j in range(0,len(scenario)):
    while i < 14:
    #while i < len(combinations):
        j=0
        print(i,j)
        print('LIGAS MENORES')
        time.sleep(2)
        #url = "https://www.kayak.co.uk/quote/" 
        print(url)
        driver.get(url)
        time.sleep(7)
        #5. Location of Fields 
        #ST
        radio_TripType_ST = driver.find_element_by_xpath('//*[@id="qs_policyType"]/div/div[2]/div/div/div[1]/label/span')
        #radio_TripType_ST.click()
        #AMT
        radio_TripType_AMT = driver.find_element_by_xpath('//*[@id="qs_policyType"]/div/div[2]/div/div/div[2]/label')
        #radio_TripType_AMT.click()
        #Where are you travelling to?
        #For ST
        Field_Destination= driver.find_element_by_id("countriesAutocomplete")
        #Field_Dest_AutoC_Agree=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/form/div/fieldset[2]/div[3]/div/div[1]/div[1]/ul/li/a/mark')
        #Field_Destination.clear()
        #Field_Destination.send_keys("")
        #driver.find_element_by_xpath('//*[@id="Quote_Country_Wrap"]/div[1]/ul/li/a').click()
        #alternative Field_Destination.send_keys("Spain"+Keys.RETURN)
        #Field_Dest_AutoC_Agree=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/form/div/fieldset[2]/div[3]/div/div[1]/div[1]/ul/li/a/mark').click()
        #For AMT
        DDown_Select_AMTDEST= Select(driver.find_element_by_xpath('//*[@id="Quote_Destination"]'))
        #4 choices 
        #DDown_Select_AMTDEST.select_by_value("100")#Europe
        #DDown_Select_AMTDEST.select_by_value("101")#Worldwide (exclusing USA, Canada, Mexico and Caribbean)
        #DDown_Select_AMTDEST.select_by_value("102")#Worldwide
        #DDown_Select_AMTDEST.select_by_value("104")#United Kingdom
        #When are you going away?
        Field_TripStartDate= driver.find_element_by_id("dp_startdate")
        #Field_TripStartDate.clear()
        #Field_TripStartDate.send_keys(origin_data_input)
        #When are you coming back?
        Field_TripEndDate= driver.find_element_by_id("dp_enddate")
        #Field_TripEndDate.clear()
        #Field_TripEndDate.send_keys("return_date_input")
        #Selected optional cover
        radio_OptionalCover_GadgetCover = driver.find_element_by_xpath('//*[@id="qs_extras"]/div[3]/div/div/div[1]/label/span')
        #radio_OptionalCover_GadgetCover.click()
        radio_OptionalCover_CruiseCover = driver.find_element_by_xpath('//*[@id="qs_extras"]/div[3]/div/div/div[2]/label/span')
        #radio_OptionalCover_CruiseCover.click()
        radio_OptionalCover_WSCover = driver.find_element_by_xpath('//*[@id="qs_extras"]/div[3]/div/div/div[3]/label/span')
        #radio_OptionalCover_WSCover.click()
        #Who would you like the insurance to cover? 
        #Individual
        radio_Who_Individual = driver.find_element_by_xpath('//*[@id="who_opt100"]/span')
        #radio_Who_Individual.click()
        #Couple
        radio_Who_Couple = driver.find_element_by_xpath('//*[@id="who_opt101"]/span')
        #radio_Who_Couple.click()
        #if family extra questions
        radio_Who_Family = driver.find_element_by_xpath('//*[@id="who_opt102"]/span')
        #radio_Who_Family.click()
        #number of Adults
        DDown_Select_Adult= Select(driver.find_element_by_id("NumberOfParents"))
        #DDown_Select_Adult.select_by_value("1")
        #DDown_Select_Adult.select_by_value("2")
        #Number of Children
        DDown_Select_Children= Select(driver.find_element_by_id("NumberOfChildren"))
        #DDown_Select_Children.select_by_value("1")
        #DDown_Select_Children.select_by_value("2")
        #DDown_Select_Children.select_by_value("3")
        #DDown_Select_Children.select_by_value("4")
        #DDown_Select_Children.select_by_value("5")
        #DDown_Select_Children.select_by_value("6")
        #DDown_Select_Children.select_by_value("7")
        #DDown_Select_Children.select_by_value("8")
        #DDown_Select_Children.select_by_value("9")
        #DDown_Select_Children.select_by_value("10")
        
        #If A group extra questions
        radio_Who_Group= driver.find_element_by_id("who_opt103")
        #radio_Who_Group.click()
        #Number of People in the Group
        DDown_Select_People= Select(driver.find_element_by_id("NumberOfPeople"))
        #DDown_Select_People.select_by_value("1")
        #DDown_Select_People.select_by_value("2")
        #DDown_Select_People.select_by_value("3")
        #DDown_Select_People.select_by_value("4")
        #DDown_Select_People.select_by_value("5")
        #DDown_Select_People.select_by_value("6")
        #DDown_Select_People.select_by_value("7")
        #DDown_Select_People.select_by_value("8")
        #DDown_Select_People.select_by_value("9")
        #DDown_Select_People.select_by_value("10")
        #DDown_Select_People.select_by_value("11")
        #DDown_Select_People.select_by_value("12")
        
        ##Main Travelller's Name
        #input title
        field_title=driver.find_element_by_id("qs_title_t1")
        #field_title.send_keys("Mr")
        #field_title.send_keys("Mrs")
        #field_title.send_keys("Ms")
        #field_title.send_keys("Miss")
        #field_title.send_keys("Sir")
        #field_title.send_keys("Dr")
        #field_title.select_by_visible_text("Sir")
        
        ##Input field Forename
        field_forename=driver.find_element_by_id("qs_firstname_t1")
        #field = driver.findElement(locator);
        #field_forename.clear()
        #field_forename.send_keys("Andres")
        #field_forename.send_keys("Mario")
        
        #Input Surname
        field_surname=driver.find_element_by_id("qs_surname_t1")
        #surname_field.send_keys("Ramirez")
        
        #Main traveller's date of birth
        #1 passenger#
        field_Day_DOB_p1 = driver.find_element_by_id("qs_dob_t1_Day")
        #field_Day_DOB_p1.send_keys(11)
        field_Month_DOB_p1 = driver.find_element_by_id("qs_dob_t1_Month")
        #field_Month_DOB_p1.send_keys(5)
        ##18-30
        field_Year_DOB_p1 = driver.find_element_by_id("qs_dob_t1_Year")
        #field_Year_DOB_p1.send_keys(1994)
        ##31-45
        #field_Year_DOB_p1 = driver.find_element_by_id("qs_dob_t1_Year")
        #field_Year_DOB_p1.send_keys(1984)
        #45-65
        #field_Year_DOB_p1 = driver.find_element_by_id("qs_dob_t1_Year")
        #field_Year_DOB_p1.send_keys(1974)
        ##65-85
        #field_Year_DOB_p1 = driver.find_element_by_id("qs_dob_t1_Year")
        #field_Year_DOB_p1.send_keys(1954)
        #2nd passenger#
        field_Day_DOB_p2 = driver.find_element_by_id("qs_dob_t2_Day")
        #field_Day_DOB_p2.send_keys(11)
        field_Month_DOB_p2 = driver.find_element_by_id("qs_dob_t2_Month")
        #field_Month_DOB_p2.send_keys(5)
        field_Year_DOB_p2 = driver.find_element_by_id("qs_dob_t2_Year")
        #field_Year_DOB_p2.send_keys(1994)
        #3rd passenger being it a child (1st child)
        field_Day_DOB_p3 = driver.find_element_by_id("qs_dob_t3_Day")
        #field_Day_DOB_p3.send_keys(11)
        field_Month_DOB_p3 = driver.find_element_by_id("qs_dob_t3_Month")
        #field_Month_DOB_p3.send_keys(5)
        field_Year_DOB_p3= driver.find_element_by_id("qs_dob_t3_Year")
       
        #3rd passenger in a Group not a child 
        field_Day_DOB_p3b = driver.find_element_by_id("qs_dob_t3_Day")
        #field_Day_DOB_p3.send_keys(11)
        field_Month_DOB_p3b = driver.find_element_by_id("qs_dob_t3_Month")
        #field_Month_DOB_p3.send_keys(5)
        field_Year_DOB_p3b= driver.find_element_by_id("qs_dob_t3_Year")
        
        #4th passenger in a Group
        field_Day_DOB_p4 = driver.find_element_by_id("qs_dob_t4_Day")
        #field_Day_DOB_p4.send_keys(11)
        field_Month_DOB_p4 = driver.find_element_by_id("qs_dob_t4_Month")
        #field_Month_DOB_p4.send_keys(5)
        field_Year_DOB_p4= driver.find_element_by_id("qs_dob_t4_Year")
        #field_Year_DOB_p4.send_keys(5)
        #//*[@id="qs_dob_t4_Day"]
        #field_Year_DOB_p3.send_keys(1994)
        #if amt max number of days
        #no preproduced fields 
        #31days and under 
        # The selection comes by default when AMT is chosen. so it is not needed to do anything else. Only if max days need to change. 
        #field_MaxNDays_31under= driver.find_element_by_xpath('//*[@id="qs_maxdays"]/div[3]/div/div/div[1]/label/span/i')
        field_MaxNDays_32to60= driver.find_element_by_xpath('//*[@id="qs_maxdays"]/div[3]/div/div/div[2]/label/span')
        #field_MaxNDays_32to60.click()
        field_MaxNDays_61to90= driver.find_element_by_xpath('//*[@id="qs_maxdays"]/div[3]/div/div/div[3]/label/span')
        #field_MaxNDays_61to90.click()
        field_MaxNDays_ALLD= driver.find_element_by_xpath('//*[@id="qs_maxdays"]/div[3]/div/div/div[4]/label/span')
        #field_MaxNDays_ALLD.click()
        # OPTIONAL Does any person to be insured have a pre-existing medical condition? 
        field_preex_no = driver.find_element_by_id("preex_no_label")
        #field_preex_no.click()
        field_preex_yes = driver.find_element_by_id("preex_yes_label")
        #field_preex_yes.click()
        #Your email address
        field_email = driver.find_element_by_id("EmailAddress")
        #field_email.send_keys("fdl503@yahoo.com")
        ##Information Consent
        radio_infoconsent = driver.find_element_by_xpath('//*[@id="qs_sensitivedata"]/div/label/span/span[2]')
        #radio_infoconsent.click()
        ##Getquotes
        radio_getquotes = driver.find_element_by_id('getQuotes')
        #radio_getquotes.click()
        #Edit Details
        #radio_EditDetails=driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]')
        ##########Scenarios################
        #First and Last Names Random     
        firstname_input=names.get_first_name(gender='male')
        print(firstname_input)
        lastname_input=names.get_last_name()
        print(lastname_input)
        #2.10 email generator
        email = (firstname_input)+(lastname_input)+''.join(random.choices(string.ascii_letters + string.digits, k=3))+'@yahoo.com'#.join'@yahoo.com'
        time.sleep(2)
        #driver.implicitly_wait(5)
        ###input of names and email per scenario#
        field_title.send_keys(title_input)
        field_forename.clear()
        field_surname.clear()
        field_forename.send_keys(firstname_input)
        field_surname.send_keys(lastname_input)
        email = (firstname_input)+(lastname_input)+''.join(random.choices(string.ascii_letters + string.digits, k=3))+'@yahoo.com'#.join'@yahoo.com'
        field_email.clear()
        time.sleep(5)
        field_email.send_keys(email)
        print("j=",j)
        print(scenario)
        print(i,j)
        time.sleep(5)
        #TREES 1 TO 2
        #,'Destination','CoverType','Duration','Age','PartyType'
        if combinations[i][j] == 'ST':
            covertype=combinations[i][j]
            print("step0_st")
            print(combinations[i][j])
            print(scenario[j])
            radio_TripType_ST.click()
            #Field_TripStartDate.clear()
            Field_TripStartDate.send_keys(origin_date_cleaned+Keys.RETURN)
            #Field_TripEndDate.clear()
            print(origin_date_cleaned)
            time.sleep(2)
            return_date_cleaned=combinations[i][6]
            returndatex = datetime.strptime(return_date_cleaned, "%d-%m-%Y")
            print(returndatex)
            duration= relativedelta(returndatex,origin_date).days
            print(duration)
            print(return_date_cleaned)
            Field_TripEndDate.send_keys(return_date_cleaned+Keys.RETURN)
            time.sleep(3)
            j+=1
            print("step1_st")
            print(combinations[i][j])
            destination=combinations[i][j]
            print(i,j)
            Field_Destination.clear()
            
            Field_Destination.send_keys(combinations[i][j]+Keys.RETURN)
            time.sleep(3)
            #class="countryhighlightedtext"
            driver.find_elements_by_xpath('//*[@id="Quote_Country_Wrap"]/div[1]/ul')[0].click()
            #driver.find_elements_by_class_name("countryhighlightedtex").click()
            #driver.find_element_by_xpath('//*[@id="Quote_Country_Wrap"]/div[1]/ul').click()
            #driver.find_element_by_xpath('//*[@id="Quote_Country_Wrap"]/div[1]/ul/li/a').click()
            #driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/form/div/fieldset[2]/div[3]/div/div[1]/div[1]/ul/li/a/mark').click()
            
            j+=1
            print(i,j)
            print("step2_st")
            if combinations[i][j] == 'Winter Sports':
                print(combinations[i][j])
                radio_OptionalCover_WSCover.click()
                j+=1
                print(i,j)
                print("step3")
                if combinations[i][j] == 'Family':
                    partytype=combinations[i][j]
                    print(combinations[i][j])
                    radio_Who_Family.click()
                    #DDown_Select_Adult.select_by_value("1")
                    DDown_Select_Adult.select_by_value("2")
                    #Number of Children
                    DDown_Select_Children.select_by_value("1")
                    #DDown_Select_Children.select_by_value("2")
                    #family will bring partner and then children p2 and p3
                    time.sleep(3)
                    field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                    field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                    field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                    #child
                    field_Day_DOB_p3.send_keys(third_t_dob1.day)
                    field_Month_DOB_p3.send_keys(third_t_dob1.month)
                    field_Year_DOB_p3.send_keys(third_t_dob1.year)
                    j+=1
                    print("step4")
                    print(i,j)
                    age = relativedelta(datetime.today(),combinations[i][j]).years
                    main_t_dob_day=combinations[i][j].day
                    main_t_dob_month=combinations[i][j].month
                    main_t_dob_yr=combinations[i][j].year
                    time.sleep(3)
                    field_Day_DOB_p1.send_keys(main_t_dob_day)
                    field_Month_DOB_p1.send_keys(main_t_dob_month)
                    field_Year_DOB_p1.send_keys(main_t_dob_yr)
                    j+=1
                    print(i,j)
                    print("step5")
                    if combinations[i][j]=='Yes':
                        tree='1'
                        time.sleep(3)
                        print('tree1_decoy')
                        print('tree1')
                        print(combinations[i][j])
                        field_preex_yes.click()
                        print(i,j)
                        time.sleep(5)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print("step5")
                        print(scenario)
                        #soup+str(i) = BeautifulSoup(requests.get(driver.page_source).content, 'lxml')
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1p
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days='na'
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree1 = df_tree1.append(data)
                            print(i,j,k)
                            k+=1
                            print(i,j,k)
                        i+=1
                        print(df_tree1)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
    

                    
                    else:
                        time.sleep(3)
                        #driver.implicitly_wait(5)
                        tree='2'
                        print('tree2')
                        print(combinations[i][j])
                        field_preex_no.click()
                        field_preex_no.click()
                        print(i,j)
                        print("step5")
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(10)
                        print(i,j)
                        print(i, end =" ")
                        print(scenario)
                        #continue
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree2=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree2 = df_tree2.append(data)
                            k+=1
                            print(i,j,k)
                        i+=1
                        print(df_tree2)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
                    
               #TREES 3 TO 4  
                else:
                    print(combinations[i][j])
                    partytype=combinations[i][j]
                    radio_Who_Group.click()
                    time.sleep(2)
                    #DDown_Select_People.select_by_value("1")
                    #DDown_Select_People.select_by_value("2")
                    #DDown_Select_People.select_by_value("3")
                    DDown_Select_People.select_by_value("4")
                    time.sleep(4)
                    #third passenger dob not a child
                    field_Day_DOB_p3b.send_keys(thirdb_t_dob1.day)
                    field_Month_DOB_p3b.send_keys(thirdb_t_dob1.month)
                    field_Year_DOB_p3b.send_keys(thirdb_t_dob1.year)
                    #fourth passenger dob
                    field_Day_DOB_p4.send_keys(fourth_t_dob1.day)
                    field_Month_DOB_p4.send_keys(fourth_t_dob1.month)
                    field_Year_DOB_p4.send_keys(fourth_t_dob1.year)
                    j+=1
                    age=relativedelta(datetime.today(),combinations[i][j])
                    main_t_dob_day=combinations[i][j].day
                    main_t_dob_month=combinations[i][j].month
                    main_t_dob_yr=combinations[i][j].year
                    time.sleep(3)
                    field_Day_DOB_p1.send_keys(main_t_dob_day)
                    field_Month_DOB_p1.send_keys(main_t_dob_month)
                    field_Year_DOB_p1.send_keys(main_t_dob_yr)
                    # DOB does not change so fine to leave
                    field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                    field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                    field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                    time.sleep(3)
                    j+=1
                    print(i,j)
                    print("step5")
                    if combinations[i][j]=='Yes':
                        tree='3'
                        print('tree3_decoy')
                        print('tree3')
                        print(combinations[i][j])
                        field_preex_yes.click()
                        print(i,j)
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print("step5")
                        print(i, end =" ")
                        print(scenario)
                        #continue
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree3=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days='na'
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree3 = df_tree3.append(data)
                            k+=1
                            print(i,j,k)
                            
                        i+=1
                        print(df_tree3)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
                            
                          
                    else:
                        time.sleep(5)
                        tree='4'
                        print('tree4')
                        print('tree4_decoy')
                        print(combinations[i][j])
                        time.sleep(10)
                        field_preex_no.click()
                        field_preex_no.click()
                        time.sleep(10)
                        print(i,j)
                        print("step5")
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print(i, end =" ")
                        print(scenario)
                        #continue
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree4=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days='na'
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree4 = df_tree4.append(data)
                            k+=1
                            print(i,j,k)
                            
                        i+=1
                        print(df_tree4)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
                #TREES 5 TO 6  
            #### NO WINTER SPORTS#########
            else:
                time.sleep(5)
                print(scenario)
                print(combinations[i][j])
                #print(combinations[0][2])
                radio_OptionalCover_WSCover.click()
                radio_OptionalCover_WSCover.click()
                j+=1
                print(i,j)
                print("step3")
                if combinations[i][j] == 'Family':
                    #print(combinations[1][3])
                    partytype=combinations[i][j]
                    print(combinations[i][j])
                    radio_Who_Family.click()
                    #DDown_Select_Adult.select_by_value("1")
                    DDown_Select_Adult.select_by_value("2")
                    #Number of Children
                    DDown_Select_Children.select_by_value("1")
                    #DDown_Select_Children.select_by_value("2")
                    #family will bring partner and then children p2 and p3
                    time.sleep(3)
                    field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                    field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                    field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                    #child
                    field_Day_DOB_p3.send_keys(third_t_dob1.day)
                    field_Month_DOB_p3.send_keys(third_t_dob1.month)
                    field_Year_DOB_p3.send_keys(third_t_dob1.year)
                    j+=1
                    print("step4")
                    print(i,j)
                    age = relativedelta(datetime.today(),combinations[i][j]).years
                    main_t_dob_day=combinations[i][j].day
                    main_t_dob_month=combinations[i][j].month
                    main_t_dob_yr=combinations[i][j].year
                    time.sleep(5)
                    field_Day_DOB_p1.send_keys(main_t_dob_day)
                    field_Month_DOB_p1.send_keys(main_t_dob_month)
                    field_Year_DOB_p1.send_keys(main_t_dob_yr)
                    j+=1
                    print(i,j)
                    print("step5")
                    time.sleep(5)
                    #driver.implicitly_wait(5)
                    if combinations[i][j]=='Yes':
                        tree='5'
                        print('tree5')
                        print('tree5decoy')
                        print(combinations[i][j])
                        time.sleep(5)
                        field_preex_yes.click()
                        print(i,j)
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print("step5")
                        print(i, end =" ")
                        print(scenario)
                        #continue
                        time.sleep(5)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree5=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days='na'
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree5 = df_tree5.append(data)
                            k+=1
                            print(i,j,k)
                            
                        i+=1
                        print(df_tree5)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
                        
                    
                    else:
                        time.sleep(3)
                        tree='6'
                        print('tree6')
                        print('tree6decoy')
                        print(combinations[i][j])
                        field_preex_no.click()
                        field_preex_no.click()
                        print(i,j)
                        print("step5")
                        time.sleep(2)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(8)
                        print(i, end =" ")
                        print(scenario)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree6=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days='na'
                            
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            print(Max_Excess)
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            #k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            time.sleep(1)
                            #driver.implicitly_wait(2)
                            #Price2='£45.00'
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree6 = df_tree6.append(data)
                            k+=1
                            print(i,j,k)
                            time.sleep(1)
                            #driver.implicitly_wait(2)
                            
                        i+=1
                        print(df_tree6)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(2)
                        continue
                            
                                          
                   
                    #TREES 7 TO 8 
                else:
                    print(i,j)
                    print(combinations[i][j])
                    partytype=combinations[i][j]
                    radio_Who_Group.click()
                    time.sleep(1)
                    #driver.implicitly_wait(2)
                    #DDown_Select_People.select_by_value("1")
                    #DDown_Select_People.select_by_value("2")
                    #DDown_Select_People.select_by_value("3")
                    DDown_Select_People.select_by_value("4")
                    time.sleep(1)
                    #driver.implicitly_wait(5)
                    #third passenger dob not a child
                    field_Day_DOB_p3b.send_keys(thirdb_t_dob1.day)
                    field_Month_DOB_p3b.send_keys(thirdb_t_dob1.month)
                    field_Year_DOB_p3b.send_keys(thirdb_t_dob1.year)
                    field_Day_DOB_p4.send_keys(fourth_t_dob1.day)
                    field_Month_DOB_p4.send_keys(fourth_t_dob1.month)
                    field_Year_DOB_p4.send_keys(fourth_t_dob1.year)
                    j+=1
                    age=relativedelta(datetime.today(),combinations[i][j])
                    main_t_dob_day=combinations[i][j].day
                    main_t_dob_month=combinations[i][j].month
                    main_t_dob_yr=combinations[i][j].year
                    time.sleep(2)
                    field_Day_DOB_p1.send_keys(main_t_dob_day)
                    field_Month_DOB_p1.send_keys(main_t_dob_month)
                    field_Year_DOB_p1.send_keys(main_t_dob_yr)
                    #couple DOB does not change so fine to leave
                    #couple DOB does not change so fine to leave
                    field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                    field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                    field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                    j+=1
                    print(i,j)
                    print("step5")
                    if combinations[i][j]=='Yes':
                        tree='7'
                        print('tree7')
                        print(combinations[i][j])
                        field_preex_yes.click()
                        print(i,j)
                        time.sleep(1)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print("step5")
                        print(i, end =" ")
                        print(scenario)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree7=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            print('ligas menores')
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days='na'
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree7 = df_tree7.append(data)
                            k+=1
                            print(i,j,k)                            
                        i+=1
                        print(df_tree7)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
    
                    else:
                        print('tree8')
                        tree='8'
                        print(combinations[i][j])
                        field_preex_no.click()
                        field_preex_no.click()
                        print(i,j)
                        print("step5")
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print("step5")
                        print(i, end =" ")
                        print(scenario)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree8=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days='na'
                            Max_Excess=quotes[k].find_all('strong')[0].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[1].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[2].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            Cancellation=quotes[k].find_all('strong')[3].get_text()
                            print(Cancellation)#
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree8=df_tree8.append(data)
                            k+=1
                            print(i,j,k)
                        i+=1
                        print(df_tree8)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(3)
                        continue
                        
      ###################################################################################################################################################AMT TREES                                                                                        
          
        else:
            time.sleep(3)
            print(combinations[i][j])
            covertype=combinations[i][j]
            radio_TripType_AMT.click()
            print("step0_amt")
            #Field_TripStartDate.clear()
            print(origin_date_cleaned)
            Field_TripStartDate.send_keys(origin_date_cleaned)
            time.sleep(3)
            return_date_cleaned='na'
            duration=365
            #amt does not require a return date but a max number of staying days
            j+=1
            print(i,j)
            print("step1_amt")
            dest_amt_dict = {"Europe" : '100',
                         "Worldwide" : '102',
                         "United Kingdom" : '104',
                         "Worldwide (exclusing USA, Canada, Mexico and Caribbean)": '101'}
            print(dest_amt_dict)
            destination=combinations[i][j]
            key=combinations[i][j]
            value=dest_amt_dict[key]
            print(value)
            DDown_Select_AMTDEST.select_by_value(value)
            j+=1
            print(i,j)
            if combinations[i][j] == 'Winter Sports':
                    radio_OptionalCover_WSCover.click()
                    j+=1
                    print(i,j)
                    print("step3")
                    if combinations[i][j] == 'Family':
                        print(combinations[i][j])
                        partytype=combinations[i][j]
                        radio_Who_Family.click()
                        #Family w partner and one child
                        #DDown_Select_Adult.select_by_value("1")
                        DDown_Select_Adult.select_by_value("2")
                        #Number of Children
                        DDown_Select_Children.select_by_value("1")
                        #DDown_Select_Children.select_by_value("2")
                        #family will bring partner and then children p2 and p3
                        time.sleep(3)
                        field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                        field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                        field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                        #child
                        field_Day_DOB_p3.send_keys(third_t_dob1.day)
                        field_Month_DOB_p3.send_keys(third_t_dob1.month)
                        field_Year_DOB_p3.send_keys(third_t_dob1.yr)
                        j+=1
                        print(i,j)
                        age = relativedelta(datetime.today(),combinations[i][j]).years
                        main_t_dob_day=combinations[i][j].day
                        main_t_dob_month=combinations[i][j].month
                        main_t_dob_yr=combinations[i][j].year
                        time.sleep(5)
                        field_Day_DOB_p1.send_keys(main_t_dob_day)
                        field_Month_DOB_p1.send_keys(main_t_dob_month)
                        field_Year_DOB_p1.send_keys(main_t_dob_yr)
                        j+=1
                        print(i,j)
                        print("step5")
                        if combinations[i][j]=='Yes':
                            tree='9'
                            print('tree9')
                            print(combinations[i][j])
                            field_preex_yes.click()
                            print(i,j)
                            time.sleep(3)
                            radio_infoconsent.click()
                            radio_getquotes.click()
                            time.sleep(5)
                            print("step5")
                            soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                            print(soup_level)  
                            quote = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                            df_tree9=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                            k=1
                            soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                            print(soup_level)  
                            quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                            #df_tree9=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                            acc_p = 0
                            acc_nq = 0
                            k=1
                            for k in range(1,len(quote)):
                                i
                                DateofRun=datetime.today()
                                main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                                Insurer = quotes[k].find("img", alt=True)['alt']
                                Insurer=Insurer[0:32]
                                print(Insurer)#k+=1
                                Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                                Defaqtostr=str(Defaqto_long)
                                Defaqto=Defaqtostr[-21:-13]
                                print(Defaqto_long)
                                # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                                print(Defaqto)#k+=1
                                #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                                #k+=1
                                Max_Days=quotes[k].find_all('strong')[0].get_text()
                                #print(quotes[0].find_all('strong')[3].get_text())
                                Max_Excess=quotes[k].find_all('strong')[1].get_text()
                                #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                                print(Max_Excess)#k+=1
                                Medical=quotes[k].find_all('strong')[2].get_text()
                                print(Medical)#
                                #print(Medical)
                                Baggage =quotes[k].find_all('strong')[3].get_text()
                                print(Baggage)#
                                #print(Baggage)
                                #Cancellation=quotes[k].find_all('strong')[4].get_text()
                                #print(Cancellation)#
                                Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                                print(Cancellation)
                                #print(Cancellation)
                                Price=quotes[k].find_all('strong')[5].get_text()
                                print(Price)#
                                #print(Price)
                                Price2=quotes[k].find_all('strong')[6].get_text()
                                print(Price2)#
                                v=int(float(Price2[1:]))
                                #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                                acc_p=+v
                                acc_nq =+k
                                mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                                data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                                df_tree9 = df_tree9.append(data)
                                k+=1
                                print(i,j,k)
                            i+=1
                            print(df_tree9)
                            driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                            time.sleep(3)
                            continue
                            
                                
                        else:
                            print('tree10')
                            tree='10'
                            print(combinations[i][j])
                            field_preex_no.click()
                            field_preex_no.click()
                            print(i,j)
                            print("step5")
                            time.sleep(3)
                            radio_infoconsent.click()
                            radio_getquotes.click()
                            time.sleep(5)
                            print(i, end =" ")
                            print(scenario)
                            soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                            print(soup_level)  
                            quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                            #df_tree10=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                            acc_p = 0
                            acc_nq = 0
                            k=1
                            for k in range(1,len(quotes)):
                                i
                                DateofRun=datetime.today()
                                main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                                Insurer = quotes[k].find("img", alt=True)['alt']
                                Insurer=Insurer[0:32]
                                print(Insurer)#k+=1
                                Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                                Defaqtostr=str(Defaqto_long)
                                Defaqto=Defaqtostr[-21:-13]
                                print(Defaqto_long)
                                # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                                print(Defaqto)#k+=1
                                #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                                #k+=1
                                Max_Days=quotes[k].find_all('strong')[0].get_text()
                                #print(quotes[0].find_all('strong')[3].get_text())
                                Max_Excess=quotes[k].find_all('strong')[1].get_text()
                                #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                                print(Max_Excess)#k+=1
                                Medical=quotes[k].find_all('strong')[2].get_text()
                                print(Medical)#
                                #print(Medical)
                                Baggage =quotes[k].find_all('strong')[3].get_text()
                                print(Baggage)#
                                #print(Baggage)
                                #Cancellation=quotes[k].find_all('strong')[4].get_text()
                                #print(Cancellation)#
                                Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                                print(Cancellation)
                                #print(Cancellation)
                                Price=quotes[k].find_all('strong')[5].get_text()
                                print(Price)#
                                #print(Price)
                                Price2=quotes[k].find_all('strong')[6].get_text()
                                print(Price2)#
                                v=int(float(Price2[1:]))
                                #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                                acc_p=+v
                                acc_nq =+k
                                mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                                data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                                df_tree10 = df_tree10.append(data)
                                k+=1
                                print(i,j,k)
                            i+=1
                            print(df_tree10)
                            driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                            time.sleep(3)
                            continue
                            
                            
                    else:
                        print(combinations[i][j])
                        partytype=combinations[i][j]
                        radio_Who_Group.click()
                        time.sleep(2)
                        #DDown_Select_People.select_by_value("1")
                        #DDown_Select_People.select_by_value("2")
                        #DDown_Select_People.select_by_value("3")
                        DDown_Select_People.select_by_value("4")
                        time.sleep(7)
                        #third passenger dob not a child
                        field_Day_DOB_p3b.send_keys(thirdb_t_dob1.day)
                        field_Month_DOB_p3b.send_keys(thirdb_t_dob1.month)
                        field_Year_DOB_p3b.send_keys(thirdb_t_dob1.year)
                        #fourth passenger dob
                        field_Day_DOB_p4.send_keys(fourth_t_dob1.day)
                        field_Month_DOB_p4.send_keys(fourth_t_dob1.month)
                        field_Year_DOB_p4.send_keys(fourth_t_dob1.year)
                        j+=1
                        age=relativedelta(datetime.today(),combinations[i][j])
                        main_t_dob_day=combinations[i][j].day
                        main_t_dob_month=combinations[i][j].month
                        main_t_dob_yr=combinations[i][j].year
                        time.sleep(3)
                        field_Day_DOB_p1.send_keys(main_t_dob_day)
                        field_Month_DOB_p1.send_keys(main_t_dob_month)
                        field_Year_DOB_p1.send_keys(main_t_dob_yr)
                        #couple DOB does not change so fine to leave
                        #couple DOB does not change so fine to leave
                        field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                        field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                        field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                        j+=1
                        print(i,j)
                        print("step5")
                        if combinations[i][j]=='Yes':
                            tree='11'
                            print('tree11')
                            print(combinations[i][j])
                            field_preex_yes.click()
                            print(i,j)
                            time.sleep(3)
                            radio_infoconsent.click()
                            radio_getquotes.click()
                            time.sleep(5)
                            print("step5")
                            print(i, end =" ")
                            print(scenario)
                            soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                            print(soup_level)  
                            quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                            #df_tree11=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                            acc_p = 0
                            acc_nq = 0
                            k=1
                            for k in range(1,len(quotes)):
                                i
                                DateofRun=datetime.today()
                                main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                                Insurer = quotes[k].find("img", alt=True)['alt']
                                Insurer=Insurer[0:32]
                                print(Insurer)#k+=1
                                Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                                Defaqtostr=str(Defaqto_long)
                                Defaqto=Defaqtostr[-21:-13]
                                print(Defaqto_long)
                                # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                                print(Defaqto)#k+=1
                                #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                                #k+=1
                                Max_Days=quotes[k].find_all('strong')[0].get_text()
                                #print(quotes[0].find_all('strong')[3].get_text())
                                Max_Excess=quotes[k].find_all('strong')[1].get_text()
                                #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                                print(Max_Excess)#k+=1
                                Medical=quotes[k].find_all('strong')[2].get_text()
                                print(Medical)#
                                #print(Medical)
                                Baggage =quotes[k].find_all('strong')[3].get_text()
                                print(Baggage)#
                                #print(Baggage)
                                #Cancellation=quotes[k].find_all('strong')[4].get_text()
                                #print(Cancellation)#
                                Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                                print(Cancellation)
                                #print(Cancellation)
                                Price=quotes[k].find_all('strong')[5].get_text()
                                print(Price)#
                                #print(Price)
                                Price2=quotes[k].find_all('strong')[6].get_text()
                                print(Price2)#
                                v=int(float(Price2[1:]))
                                #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                                acc_p=+v
                                acc_nq =+k
                                mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                                data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                                df_tree11 = df_tree11.append(data)
                                k+=1
                                print(i,j,k)
                                
                            i+=1
                            print(df_tree11)
                            driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                            time.sleep(5)
                            continue
                            
                               
                        else:
                            tree='12'
                            print('tree12')
                            print(combinations[i][j])
                            field_preex_no.click()
                            print(i,j)
                            print("step5")
                            time.sleep(5)
                            radio_infoconsent.click()
                            radio_getquotes.click()
                            time.sleep(5)
                            print(i, end =" ")
                            print(scenario)
                            soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                            print(soup_level)  
                            quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                            #df_tree12=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                            acc_p = 0
                            acc_nq = 0
                            k=1
                            for k in range(1,len(quotes)):
                                i
                                DateofRun=datetime.today()
                                main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                                Insurer = quotes[k].find("img", alt=True)['alt']
                                Insurer=Insurer[0:32]
                                print(Insurer)#k+=1
                                Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                                Defaqtostr=str(Defaqto_long)
                                Defaqto=Defaqtostr[-21:-13]
                                print(Defaqto_long)
                                # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                                print(Defaqto)#k+=1
                                #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                                #k+=1
                                Max_Days=quotes[k].find_all('strong')[0].get_text()
                                #print(quotes[0].find_all('strong')[3].get_text())
                                Max_Excess=quotes[k].find_all('strong')[1].get_text()
                                #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                                print(Max_Excess)#k+=1
                                Medical=quotes[k].find_all('strong')[2].get_text()
                                print(Medical)#
                                #print(Medical)
                                Baggage =quotes[k].find_all('strong')[3].get_text()
                                print(Baggage)#
                                #print(Baggage)
                                #Cancellation=quotes[k].find_all('strong')[4].get_text()
                                #print(Cancellation)#
                                Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                                print(Cancellation)
                                #print(Cancellation)
                                Price=quotes[k].find_all('strong')[5].get_text()
                                print(Price)#
                                #print(Price)
                                Price2=quotes[k].find_all('strong')[6].get_text()
                                print(Price2)#
                                v=int(float(Price2[1:]))
                                #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                                acc_p=+v
                                acc_nq =+k
                                mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                                data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                                df_tree12 = df_tree12.append(data)
                                k+=1
                                print(i,j,k)
                                #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                                #radio_EditDetails=driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]')
                                #radio_EditDetails.click() 
                            i+=1
                            print(df_tree12)
                            driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                            time.sleep(5)
                            continue
                                         
            else:
                print(combinations[i][j])
                radio_OptionalCover_WSCover.click()
                radio_OptionalCover_WSCover.click()
                j+=1
                print(i,j)
                print("step3")
                if combinations[i][j] == 'Family':
                    print(combinations[i][j])
                    partytype=combinations[i][j]
                    radio_Who_Family.click()
                    #Family w partner and one child
                    #DDown_Select_Adult.select_by_value("1")
                    DDown_Select_Adult.select_by_value("2")
                    #Number of Children
                    DDown_Select_Children.select_by_value("1")
                    #DDown_Select_Children.select_by_value("2")
                    #family will bring partner and then children p2 and p3
                    time.sleep(3)
                    #partner
                    field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                    field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                    field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                    #child
                    field_Day_DOB_p3.send_keys(third_t_dob1.day)
                    field_Month_DOB_p3.send_keys(third_t_dob1.month)
                    field_Year_DOB_p3.send_keys(third_t_dob1.year)
                    j+=1
                    print("step4")
                    print(i,j)
                    age = relativedelta(datetime.today(),combinations[i][j]).years
                    main_t_dob_day=combinations[i][j].day
                    main_t_dob_month=combinations[i][j].month
                    main_t_dob_yr=combinations[i][j].year
                    time.sleep(5)
                    field_Day_DOB_p1.send_keys(main_t_dob_day)
                    field_Month_DOB_p1.send_keys(main_t_dob_month)
                    field_Year_DOB_p1.send_keys(main_t_dob_yr)
                    j+=1
                    print(i,j)
                    print("step5")
                    if combinations[i][j]=='Yes':
                        tree='13'
                        print('tree13')
                        print(combinations[i][j])
                        field_preex_yes.click()
                        print(i,j)
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print("step5")
                        print(i, end =" ")
                        print(scenario)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree13=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days=quotes[k].find_all('strong')[0].get_text()
                            #print(quotes[0].find_all('strong')[3].get_text())
                            Max_Excess=quotes[k].find_all('strong')[1].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[2].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[3].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            #Cancellation=quotes[k].find_all('strong')[4].get_text()
                            #print(Cancellation)#
                            Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                            print(Cancellation)
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree13 = df_tree13.append(data)
                            k+=1
                            print(i,j,k)
                        i+=1
                        print(df_tree13)
                        driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
                               
                    else:
                        print('tree14')
                        tree='14'
                        print(combinations[i][j])
                        field_preex_no.click()
                        field_preex_no.click()
                        print(i,j)
                        print("step5")
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(8)
                        print(i, end =" ")
                        print(scenario)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree14=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days=quotes[k].find_all('strong')[0].get_text()
                            #print(quotes[0].find_all('strong')[3].get_text())
                            Max_Excess=quotes[k].find_all('strong')[1].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[2].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[3].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            #Cancellation=quotes[k].find_all('strong')[4].get_text()
                            #print(Cancellation)#
                            Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                            print(Cancellation)
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree14 = df_tree14.append(data)
                            k+=1
                            print(i,j,k)
                        i+=1
                        print(df_tree14)
                        #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
                               
                else:
                    print(combinations[i][j])
                    partytype=combinations[i][j]
                    radio_Who_Group.click()
                    time.sleep(2)
                    #DDown_Select_People.select_by_value("1")
                    #DDown_Select_People.select_by_value("2")
                    #DDown_Select_People.select_by_value("3")
                    DDown_Select_People.select_by_value("4")
                    time.sleep(7)
                    #third passenger dob not a child
                    field_Day_DOB_p3b.send_keys(thirdb_t_dob1.day)
                    field_Month_DOB_p3b.send_keys(thirdb_t_dob1.month)
                    field_Year_DOB_p3b.send_keys(thirdb_t_dob1.year)
                    #fourth passenger dob
                    field_Day_DOB_p4.send_keys(fourth_t_dob1.day)
                    field_Month_DOB_p4.send_keys(fourth_t_dob1.month)
                    field_Year_DOB_p4.send_keys(fourth_t_dob1.year)
                    j+=1
                    age = relativedelta(datetime.today(),combinations[i][j]).years
                    main_t_dob_day=combinations[i][j].day
                    main_t_dob_month=combinations[i][j].month
                    main_t_dob_yr=combinations[i][j].year
                    time.sleep(3)
                    field_Day_DOB_p1.send_keys(main_t_dob_day)
                    field_Month_DOB_p1.send_keys(main_t_dob_month)
                    field_Year_DOB_p1.send_keys(main_t_dob_yr)
                    #couple DOB does not change so fine to leave
                    time.sleep(3)
                    field_Day_DOB_p2.send_keys(sec_t_dob1.day)
                    field_Month_DOB_p2.send_keys(sec_t_dob1.month)
                    field_Year_DOB_p2.send_keys(sec_t_dob1.year)
                    j+=1
                    print(i,j)
                    print("step5")
                    if combinations[i][j]=='Yes':
                        tree='15'
                        print(combinations[i][j])
                        field_preex_yes.click()
                        print(i,j)
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print("step5")
                        print(i, end =" ")
                        print(scenario)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree15=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days=quotes[k].find_all('strong')[0].get_text()
                            #print(quotes[0].find_all('strong')[3].get_text())
                            Max_Excess=quotes[k].find_all('strong')[1].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[2].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[3].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            #Cancellation=quotes[k].find_all('strong')[4].get_text()
                            #print(Cancellation)#
                            Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                            print(Cancellation)
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree15 = df_tree15.append(data)
                            k+=1
                            print(i,j,k)
                            print('tree15decoy')
                            #driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                            #radio_EditDetails=driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]')
                            #radio_EditDetails.click() 
                        i+=1
                        print('tree15decoy')
                        print(df_tree15)
                        driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
                        
                    else:
                        print('tree16')
                        tree='16'
                        print(combinations[i][j])
                        field_preex_no.click()
                        field_preex_no.click()
                        print(i,j)
                        print("step5")
                        time.sleep(3)
                        radio_infoconsent.click()
                        radio_getquotes.click()
                        time.sleep(5)
                        print(i, end =" ")
                        print(scenario)
                        soup_level=BeautifulSoup(driver.page_source, 'lxml') 
                        print(soup_level)  
                        quotes = soup_level.findAll(attrs={'class' : "quote-heading result-row"})
                        #df_tree16=pd.DataFrame(columns=['DateofRun','i','k','Insurer', 'Defaqto','Max_Excess','Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario'])
                        acc_p = 0
                        acc_nq = 0
                        k=1
                        for k in range(1,len(quotes)):
                            i
                            DateofRun=datetime.today()
                            main_t_dob_fv=str(main_t_dob_day) + '/'+str(main_t_dob_month) +'/'+ str(main_t_dob_yr)
                            Insurer = quotes[k].find("img", alt=True)['alt']
                            Insurer=Insurer[0:32]
                            print(Insurer)#k+=1
                            Defaqto_long = quotes[k].find('span', class_='defaqto-img') 
                            Defaqtostr=str(Defaqto_long)
                            Defaqto=Defaqtostr[-21:-13]
                            print(Defaqto_long)
                            # Defaqto = quotes[k].find("div", alt="defaqto img")['alt']
                            print(Defaqto)#k+=1
                            #Defaqto2int(filter(str.isdigit,'<span class="defaqto-img"><img alt="This policy by Southdowns has a defaqto rating of 5 stars" src="/quote/Content/img-defaqto/defaqto-stars-5.png"/></span>)')
                            #k+=1
                            Max_Days=quotes[k].find_all('strong')[0].get_text()
                            #print(quotes[0].find_all('strong')[3].get_text())
                            Max_Excess=quotes[k].find_all('strong')[1].get_text()
                            #Max_Excess = quotes[0].find("strong", class_="sr-only-md mtc-grey")
                            print(Max_Excess)#k+=1
                            Medical=quotes[k].find_all('strong')[2].get_text()
                            print(Medical)#
                            #print(Medical)
                            Baggage =quotes[k].find_all('strong')[3].get_text()
                            print(Baggage)#
                            #print(Baggage)
                            #Cancellation=quotes[k].find_all('strong')[4].get_text()
                            #print(Cancellation)#
                            Cancellation=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/section/div'+str([k+2])+'/div/div[1]/div[8]/strong').text
                            print(Cancellation)
                            #print(Cancellation)
                            Price=quotes[k].find_all('strong')[5].get_text()
                            print(Price)#
                            #print(Price)
                            Price2=quotes[k].find_all('strong')[6].get_text()
                            print(Price2)#
                            v=int(float(Price2[1:]))
                            #v=pd.Series(Price2[1:]).str.replace('.00', '').astype(int)
                            acc_p=+v
                            acc_nq =+k
                            mydata= [tree,DateofRun,i,k,Insurer, Defaqto, Max_Excess, Medical, Baggage,Cancellation,Price,Price2,origin_date_cleaned,return_date_cleaned,main_t_dob_fv,email,Defaqto_long,combinations[i],destination,covertype,duration,age,partytype,Max_Days,acc_p,acc_nq]
                            data = pd.DataFrame(data=[mydata],columns=['Tree','DateofRun','i','k','Insurer', 'Defaqto', 'Max_Excess', 'Medical', 'Baggage','Cancellation','Price','Price2','OriginDate','ReturnDate','MainTraveller_DOB','email','Defaqto_long','Scenario','Destination','CoverType','Duration','Age','PartyType','Max_Days_AMT','Cumulative_Prem','Cumulative_Quotes'])
                            df_tree16 = df_tree16.append(data)
                            k+=1
                            print(i,j,k)
                            
                        i+=1
                        print(df_tree16)
                        driver.find_element_by_xpath('//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]').click()
                        time.sleep(5)
                        continue
 #//*[@id="results-summary-article"]/div[3]/div[2]/div/a[1]

    
 

    results_FAM_GP=pd.concat([df_tree16,
                           df_tree15,
                           df_tree14,
                           df_tree13,
                           df_tree12,
                           df_tree11,
                           df_tree10,
                           df_tree9,
                           df_tree8,
                           df_tree7,
                           df_tree6,
                           df_tree5,
                           df_tree4,
                           df_tree3,
                           df_tree2,
                           df_tree1])    




results_FAM_GP["Insurer"] = results_FAM_GP["Insurer"].str.replace("Logo Image", " ") 
results_FAM_GP["Insurer"] = results_FAM_GP["Insurer"].str.replace("Logo Imag", " ")  
results_FAM_GP['Channel']='Aggregator'
results_FAM_GP['Aggregator']='CYTI'
results_FAM_GP['Couple_Partner_DOB'] = np.where(results_FAM_GP['PartyType'] == 'Couple', sec_t_dob1_cleaned, 'na')
results_FAM_GP['Fam_Child_DOB'] = np.where(results_FAM_GP['PartyType'] == 'Family', third_t_dob1_cleaned, 'na')
results_FAM_GP['Fam_Partner_DOB'] = np.where(results_FAM_GP['PartyType'] == 'Family', sec_t_dob1_cleaned, 'na')
results_FAM_GP['AgeCode'] = np.where(results_FAM_GP['Age'] ==26, '1',np.where(results_FAM_GP['Age'] == 36,'2',np.where(results_FAM_GP['Age'] == 46,'3','4')))
results_FAM_GP['CoverTypeCode'] = np.where(results_FAM_GP['CoverType'] == 'ST', '1', '2')
results_FAM_GP['DestinationCode']= np.where(results_FAM_GP['Destination'] == 'Spain', '1',np.where(results_FAM_GP['Destination'] == 'Europe', '1','2'))
results_FAM_GP['DurationCode']= np.where(results_FAM_GP['Duration'] == 8, '1',np.where(results_FAM_GP['Duration'] == 11, '2',np.where(results_FAM_GP['Duration'] == 15,'3','4')))
results_FAM_GP['PartyTypeCode'] = np.where(results_FAM_GP['PartyType'] == 'Individual', '1',np.where(results_FAM_GP['PartyType'] == 'Couple','2','3'))

#print(results_FAM_GP)
print(results_FAM_GP)

results_FAM_GP.to_csv("DWSResultsFAMGP_csv.csv", index=False,encoding='utf-8-sig')
results_FAM_GP.to_excel("DWSResultsFAMGP_xl.xlsx",sheet_name='Results'+str(datetime.today())[0:10])         

results_FAM_GP.to_csv('DWSResultsFAMGP_'+str(datetime.today())[0:10]+'.csv', index=False,encoding='utf-8-sig')
results_FAM_GP.to_excel('DWSResultsFAMGP_xl_'+str(datetime.today())[0:10]+'.xlsx',sheet_name='Results'+str(datetime.today())[0:10]) 


                
   


