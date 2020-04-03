#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 8:30:16 2020

@author: mac
"""

import pyodbc
import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import pandasql
import matplotlib.pyplot as plt
import numpy

server = 'localhost'
database = 'ScholasticDB'
username = 'AIS'
password = 'ScholasticChallenge'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

#%%
demo = "Humor & Funny Stories"

df = pandas.read_sql_query(
'''
SELECT S.CHANNEL, S.PROD_TYP, S.SERIES, L.NumberRange, S.UNIT_PRICE, S.SCHOOL_TYPE, Z.STATE
FROM Scholastic S, LexileStuff L, ZipcodeDB Z
where S.LEXILE_11_DESC=L.LEXILE_11_DESC
AND Z.zip=S.ZIP_CODE
AND S.CH1_GENRE LIKE '%'''+demo+'''%'
AND S.LEXILE_11_DESC IS NOT NULL
''', cnxn)
#%%

BinaryChannel = {'CHANNEL 1': 0, 'CHANNEL 2': 1}

df.CHANNEL = [BinaryChannel[item] for item in df.CHANNEL]

BinaryProd_typ = {'PAPERBACK': 0, 'HARDBACK': 1}
iodf.PROD_TYP = [BinaryProd_typ[item] for item in df.PROD_TYP]

BinarySeries = {'Y': 0, 'N': 1}

df.SERIES = [BinarySeries[item] for item in df.SERIES]

BinarySchool_type = {'PUBLIC': 0, 'OTHER': 1}

df.SCHOOL_TYPE = [BinarySchool_type[item] for item in df.SCHOOL_TYPE]
#%%
States = pandas.DataFrame(pandasql.sqldf("SELECT DISTINCT STATE FROM df", locals()))

States = States.reset_index()

States.rename(columns = {'index':'StateID'}, inplace = True)

States.StateID = States['StateID'] + 1

df = pandas.DataFrame(pandasql.sqldf('''SELECT CHANNEL, PROD_TYP, SERIES, NumberRange,
                                        UNIT_PRICE, SCHOOL_TYPE, StateID
                                        FROM df
                                        JOIN States
                                        ON States.STATE = df.STATE''', locals()))
#%%
print(df.dtypes)
print(df.count())
#%%
df['UNIT_PRICE'] = df['UNIT_PRICE'].fillna((df['UNIT_PRICE'].mean()))
df['NumberRange'] = df['NumberRange'].fillna((df['NumberRange'].mean()))

Y = df[['CHANNEL']]
X = df[['PROD_TYP']+['SERIES']+['NumberRange']+['UNIT_PRICE']+['SCHOOL_TYPE']+['StateID']]

#%%
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)

log = LogisticRegression()
log.fit(x_train,y_train)
log.score(x_test,y_test)
#%%
logit = sm.Logit(Y, sm.add_constant(X)).fit()

logit.summary()
#%%
log = LogisticRegression()
log.fit(X,Y)
#%%
X.to_numpy()

p_pred = log.predict_proba(X)
predict1 = log.predict(X)
#%%

vPROD_TYP = input("Is the book Paperback or Hardback: ")

if vPROD_TYP.lower() == "paperback":
    vPROD_TYP = 0
else:
    vPROD_TYP = 1

vSERIES = input("Is the book a series? (Y/N): ")

if vSERIES.lower() == "Y":
    vSERIES = 0
else:
    vSERIES = 1

vNumberRange = input("What is the lexile code of the book?: ")

vPrice = input("How much does the book cost in USD?: ")

vschooltype = input("Distributing to Public school or other?: ")

if vschooltype.lower() == "public" :
    vschooltype = 0
else:
    vschooltype = 1
   
vSTATE = input("What state would you like to send the book out (2 initials): ")

vSTATE = vSTATE.upper()  

actualstate = pandas.DataFrame(pandasql.sqldf("SELECT StateID FROM States WHERE STATE = "+'\''+str(vSTATE)+'\'', locals()))

vSTATE = actualstate.iloc[0,0]

Z = pandas.DataFrame(numpy.array([[vPROD_TYP, vSERIES, vNumberRange, vPrice, vschooltype, vSTATE],]),
                   columns=['PROD_TYP', 'SERIES', 'NumberRange','UNIT_PRICE','SCHOOL_TYPE', 'StateID'])
Z.to_numpy()

p_pred1 = log.predict_proba(Z)  

p_prediction = pandas.DataFrame(p_pred1)

print("")
print("There is a "+ str(p_prediction.iloc[0,0]*100)+"% chance this resembles a book that would be sold in Channel 1")
print("")
if p_prediction.iloc[0,1] > p_prediction.iloc[0,0]:
    print("Therefore the Scholastic algorithm suggests that you use Channel 2 as your means of distribution")
else: 
    print("Therefore the Scholastic algorithm suggests that you use Channel 1 as your means of distribution")
#%%
cm = confusion_matrix(Y, predict1)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()

