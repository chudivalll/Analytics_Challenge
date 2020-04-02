#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:27:31 2020

@author: mac




                    '''Importation of Data'''
import numpy
import pandas
import pandasql

df = pandas.read_csv("C:\Scholastic_Challenge_Dataset.csv")

df.rename(columns = {'title':'TITLE'}, inplace = True)
#%%
                        '''Modification Data'''

#Elimates duplicate records, but keeps the last instance of that record
df = df.drop_duplicates(keep='last')

#Updating Null Rows
df.loc[df['ZIP_CODE'] == '.','ZIP_CODE'] = numpy.nan

df.loc[df['EDU_NO_HS'] == '.','EDU_NO_HS'] = numpy.nan

df.loc[df['EDU_HS_SOME_COLLEGE'] == '.','EDU_HS_SOME_COLLEGE'] = numpy.nan

df.loc[df['EDU_BACHELOR_DEG'] == '.','EDU_BACHELOR_DEG'] = numpy.nan

df.loc[df['EDU_GRADUATE_DEG'] == '.','EDU_GRADUATE_DEG'] = numpy.nan

#Updating Region

df.loc[df['ZIP_CODE'] == '14881','REGION'] = 'NORTHEAST'

df.loc[df['ZIP_CODE'] == '30035','REGION'] = 'SOUTH'

df.loc[df['ZIP_CODE'] == '43725','REGION'] = 'MIDWEST'

df.loc[df['ZIP_CODE'] == '45843', 'REGION'] = 'MIDWEST'

df.loc[df['ZIP_CODE'] == '22134', 'REGION'] = 'SOUTH'

df.loc[df['COUNTY'] == 'NEW YORK', 'REGION'] = 'NORTHEAST'

df.loc[df['COUNTY'] == 'WELLS', 'REGION'] = 'MIDWEST'

#Cloning Column for manipulation on ID
df['TITLE_ID'] = df['TITLE_CODE']

#Altering ID for those books that are potentially varying
df.loc[(df['TITLE'] == 'Chomp')&(df['CH1_GENRE'] == "['School Stories']"), 'TITLE_ID'] = '71191A'

df.loc[(df['TITLE'] == 'Official Guide')&(df['CH1_GENRE'] == "['Action & Adventure', 'Media']"), 'TITLE_ID'] = '74949A'

df.loc[(df['TITLE'] == 'Official Handbook')&(df['CH1_GENRE'] == "['Humor & Funny Stories']"), 'TITLE_ID'] = '74951A'

df.loc[(df['TITLE'] == 'Hidden')&(df['CH1_GENRE'] == "['Realistic Fiction']"), 'TITLE_ID'] = '72993A'

df.loc[(df['TITLE'] == 'Life on Mars')&(df['CH1_GENRE'] == "['Informative Nonfiction']"), 'TITLE_ID'] = '73910A'

df.loc[(df['TITLE'] == 'Life on Mars')&(df['CH1_GENRE'] == "['Realistic Fiction']"), 'TITLE_ID'] = '73910B'

df.loc[(df['TITLE'] == 'Courageous')&(df['CH1_GENRE'] == "['Realistic Fiction']"), 'TITLE_ID'] = '71389A'

df.loc[(df['TITLE'] == 'Gingerbread Man, The')&(df['CH1_GENRE'] == "['Fairy Tales, Folk Tales & Fables']"), 'TITLE_ID'] = '72565A'

df.loc[(df['TITLE'] == 'Sink or Swim')&(df['CH1_GENRE'] == "['Historical Fiction', 'Action & Adventure']"), 'TITLE_ID'] = '76237A'

df.loc[(df['TITLE'] == 'Hideout')&(df['CH1_GENRE'] == "['Realistic Fiction']"), 'TITLE_ID'] = '73002A'

df.loc[(df['TITLE'] == 'Troublemaker')&(df['CH1_GENRE'] == "['Humor & Funny Stories', 'School Stories']"), 'TITLE_ID'] = '77125A'

df.loc[(df['TITLE'] == 'Troublemaker')&(df['CH2_CATEGORY'] == 'FAMILY & FRIENDSHIP'), 'TITLE_ID'] = '77125A'

#Different Code but referring to same books
df.loc[df['TITLE_ID'] == 70480, 'TITLE_ID'] = 70481

df.loc[df['TITLE_ID'] == 71766, 'TITLE_ID'] = 71494

df.loc[df['TITLE_ID'] == 72096, 'TITLE_ID'] = 72094

df.loc[df['TITLE_ID'] == 74017, 'TITLE_ID'] = 74018

df.loc[df['TITLE_ID'] == 74380, 'TITLE_ID'] = 74381

df.loc[df['TITLE_ID'] == 74602, 'TITLE_ID'] = 74601

df.loc[df['TITLE_ID'] == 74960, 'TITLE_ID'] = 74958

df.loc[df['TITLE_ID'] == 74934, 'TITLE_ID'] = 74996

df.loc[df['TITLE_ID'] == 75076, 'TITLE_ID'] = 75077

df.loc[df['TITLE_ID'] == 75628, 'TITLE_ID'] = 75597

df.loc[df['TITLE_ID'] == 76340, 'TITLE_ID'] = 76343

df.loc[df['TITLE_ID'] == 75830, 'TITLE_ID'] = 76635

df.loc[df['TITLE_ID'] == 76755, 'TITLE_ID'] = 76756

df.loc[df['TITLE_ID'] == 77121, 'TITLE_ID'] = 77122

df.loc[df['TITLE_ID'] == 77533, 'TITLE_ID'] = 77535

df.loc[df['TITLE_ID'] == 77613, 'TITLE_ID'] = 77660

#Filtered by different lexiles, would could represent different books
df.loc[(df['LEXILE_11_DESC'] == '630L')&(df['TITLE_ID'] == 71545), 'TITLE_ID'] = '71545A'

df.loc[(df['LEXILE_11_DESC'] == '400L')&(df['TITLE_ID'] == 72349), 'TITLE_ID'] = '72349A'

df.loc[(df['LEXILE_11_DESC'] == 'NC870L')&(df['TITLE_ID'] == 74505), 'TITLE_ID'] = '74505A'

df.loc[(df['LEXILE_11_DESC'] == 'AD480L')&(df['TITLE_ID'] == 75263), 'TITLE_ID'] = '75263A'

df.loc[(df['LEXILE_11_DESC'] == 'NC730L')&(df['TITLE_ID'] == 75759), 'TITLE_ID'] = '75759A'

df.loc[(df['LEXILE_11_DESC'] == 'HL510L')&(df['TITLE_ID'] == 76121), 'TITLE_ID'] = '76121A'

df.loc[(df['LEXILE_11_DESC'] == 'AD810L')&(df['TITLE_ID'] == 76365), 'TITLE_ID'] = '76365A'

df.loc[(df['LEXILE_11_DESC'] == 'AD830L')&(df['TITLE_ID'] == 76630), 'TITLE_ID'] = '76630A'
#%%
                    '''Creating Unique Key for Analysis'''

uniqueID = pandas.DataFrame(pandasql.sqldf("SELECT DISTINCT TITLE_ID FROM df", locals()))

uniqueID = uniqueID.reset_index()

uniqueID.rename(columns = {'index':'ID'}, inplace = True)

uniqueID.ID = uniqueID['ID'] + 1
#%%
                        ''' Isolation of Tables '''
                       
ch1_genre = pandas.DataFrame(pandasql.sqldf("SELECT DISTINCT TITLE_ID, CH1_GENRE FROM df WHERE CH1_GENRE IS NOT NULL", locals()))

ch1_theme = pandas.DataFrame(pandasql.sqldf("SELECT DISTINCT TITLE_ID, CH1_THEME FROM df WHERE CH1_THEME IS NOT NULL", locals()))

ch2_category = pandas.DataFrame(pandasql.sqldf("SELECT DISTINCT TITLE_ID, CH2_CATEGORY FROM df WHERE CH2_CATEGORY IS NOT NULL", locals()))

ch2_subcategory = pandas.DataFrame(pandasql.sqldf("SELECT DISTINCT TITLE_ID, CH2_SUBCATEGORY FROM df WHERE CH2_SUBCATEGORY IS NOT NULL", locals()))
#%%
                        ''' Linking Modified Key '''
                       
df = pandas.DataFrame(pandasql.sqldf('''SELECT ID, TITLE, TITLE_CODE, CHANNEL, PROD_TYP, SERIES, CH1_GENRE,
                                        CH1_THEME, CH2_CATEGORY, CH2_SUBCATEGORY, LEXILE_11_DESC, total_units,
                                        UNIT_PRICE, SCHOOL_TYPE, REGION, STATE, COUNTY, EDU_NO_HS,
                                        EDU_HS_SOME_COLLEGE, EDU_BACHELOR_DEG, EDU_GRADUATE_DEG, HHI_BAND, ZIP_CODE
                                        FROM uniqueID, df
                                        WHERE uniqueID.TITLE_ID=df.TITLE_ID''', locals()))

ch1_genre = pandas.DataFrame(pandasql.sqldf('''SELECT ID, CH1_GENRE
                                               FROM ch1_genre, uniqueID
                                               WHERE ch1_genre.TITLE_ID = uniqueID.TITLE_ID
                                            ''', locals()))

ch1_theme = pandas.DataFrame(pandasql.sqldf('''SELECT ID, CH1_THEME
                                               FROM ch1_theme, uniqueID
                                               WHERE ch1_theme.TITLE_ID = uniqueID.TITLE_ID
                                            ''', locals()))

ch2_category = pandas.DataFrame(pandasql.sqldf('''SELECT ID, CH2_CATEGORY
                                                  FROM ch2_category, uniqueID
                                                  WHERE ch2_category.TITLE_ID = uniqueID.TITLE_ID
                                               ''', locals()))

ch2_subcategory = pandas.DataFrame(pandasql.sqldf('''SELECT ID, CH2_SUBCATEGORY
                                                     FROM ch2_subcategory, uniqueID
                                                     WHERE ch2_subcategory.TITLE_ID = uniqueID.TITLE_ID
                                                  ''', locals()))
#%%
                            '''Cleaning Algorithm'''
class clean:
    def __init__(self, dataframe, SheetName):
        self.dataframe = dataframe
        self.SheetName = SheetName      
   
    def normalize(self):
       
        df = (self.dataframe)
       
        df[(self.SheetName)] = [x.strip().replace('[', '') for x in df[(self.SheetName)]]
        df[(self.SheetName)] = [x.strip().replace(']', '') for x in df[(self.SheetName)]]
        new_df = pandas.DataFrame(df[(self.SheetName)].str.split(',').tolist(), index=df.ID).stack()
        new_df = new_df.reset_index([0, 'ID'])
        new_df.columns = ['ID', (self.SheetName)]
        new_df[(self.SheetName)] = [x.strip().replace('\'', '') for x in new_df[(self.SheetName)]]
        new_df= new_df.drop_duplicates(keep='last')
       
        return(new_df)
       
ch1_genre = clean(ch1_genre, 'CH1_GENRE').normalize()
ch1_theme = clean(ch1_theme, 'CH1_THEME').normalize()
ch2_category = clean(ch2_category, 'CH2_CATEGORY').normalize()
ch2_subcategory = clean(ch2_subcategory, 'CH2_SUBCATEGORY').normalize()

#%%
                                        '''Zipcode Table'''
                                       
Zipcode_Stat = pandas.DataFrame(pandasql.sqldf('''
                                               SELECT DISTINCT ZIP_CODE, EDU_NO_HS, EDU_HS_SOME_COLLEGE,
                                               EDU_BACHELOR_DEG, EDU_GRADUATE_DEG, HHI_BAND
                                               FROM df
                                               WHERE ZIP_CODE IS NOT NULL
                                               ''', locals()))
#%%
                                    '''Don't need these columns'''
                                   
df = df.drop(columns=['EDU_NO_HS', 'EDU_HS_SOME_COLLEGE','EDU_BACHELOR_DEG','EDU_GRADUATE_DEG','HHI_BAND'])

#Fixing these particular values
df['UNIT_PRICE']= df['UNIT_PRICE'].mask(df['UNIT_PRICE'].ge(150),df['UNIT_PRICE'].div(100))
#df.where(df['UNIT_PRICE']== 650, inplace = True) 
#%%

df.to_csv('Scholastic.csv',index=False)
ch1_genre.to_csv('Genres.csv',index=False)
ch1_theme.to_csv('Theme.csv',index=False)
ch2_category.to_csv('Category.csv',index=False)
ch2_subcategory.to_csv('Subcategory.csv',index=False)
Zipcode_Stat.to_csv('ZipcodeStats.csv',index=False)
uniqueID.to_csv('TitleCode.csv',index=False)

