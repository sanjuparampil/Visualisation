import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Reading data to dataframe

df_stolen18 = pd.read_csv("2018.csv")
df_stolen18 = df_stolen18[0:10]
df_stolen19 = pd.read_csv("2019.csv")
df_stolen19 = df_stolen19[0:10]
df_stolen18_full = pd.read_csv("2018 full table.csv")
df_stolen19_full = pd.read_csv("2019 full table.csv")
df_bank_nifty = pd.read_csv("Nifty_bank.csv")

def theft_bargraphs():
    """ This function reads data from 2018.csv and
    2019.csv and plots number of stolen items(y-axis)
    vs type of property(x-axis).Visualization method used is BAR GRAPH"""
    
    plt.figure()
    plt.bar(df_stolen18['Type of property'], df_stolen18['Stolen'], alpha = 1.0 , label = 'Stolen')
    plt.bar(df_stolen18['Type of property'], df_stolen18['Recovered'], alpha = 0.9 , label = 'Recovered')
    plt.xlabel("Type of Property")
    plt.ylabel("Number of items (in lakhs)")
    plt.legend()
    plt.title('Cargo theft in US (2018)')
    plt.xticks(rotation=90)
    plt.savefig('bar1.png', bbox_inches="tight", dpi = 300)
    plt.show()


    plt.figure()
    plt.bar(df_stolen19['Type of property'], df_stolen19['Stolen'], alpha = 1.0 , label = 'Stolen')
    plt.bar(df_stolen19['Type of property'], df_stolen19['Recovered'], alpha = 0.9 , label = 'Recovered')
    plt.xlabel("Type of Property")
    plt.ylabel("Number of items (in lakhs)")
    plt.legend()
    plt.title('Cargo theft in US (2019)')
    plt.savefig('bar2.png') #bbox_inches="tight")
    plt.xticks(rotation = 90)
    plt.savefig('bar2.png', bbox_inches="tight", dpi = 300)
    plt.show()
    
def theft_subplots():
    """ This function reads data from 2018.csv and
    2019.csv and sub-plots number of stolen items in lakhs (y-axis)
    vs type of property(x-axis).Visualization method used is SUB-PLOTS"""
    plt.figure()
    plt.subplot(2,2,1)
    plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=1.0,wspace=0.4,hspace=0.4)
    plt.bar(df_stolen19['Type of property'], df_stolen19['Stolen'], alpha = 1.0 , label = 'Stolen')
    plt.legend()
    plt.xticks(rotation = 90)

    plt.subplot(2,2,2)
    plt.bar(df_stolen19['Type of property'], df_stolen19['Recovered'], alpha = 1.0 , label = 'Recovered')
    plt.xticks(rotation = 90)
    plt.title('Cargo theft in US (2019)')
    plt.savefig('sub_plot1.png', bbox_inches="tight", dpi = 300)
    plt.legend()
    plt.show()

    #plt.figure()
    plt.subplot(2,2,1)
    plt.bar(df_stolen18['Type of property'], df_stolen18['Stolen'], alpha = 1.0 , label = 'Stolen')
    plt.legend()
    plt.xticks(rotation = 90)

    plt.subplot(2,2,2)
    plt.bar(df_stolen18['Type of property'], df_stolen18['Recovered'], alpha = 1.0 , label = 'Recovered')
    plt.xticks(rotation = 90)
    plt.legend()
    plt.savefig('sub_plot.png', bbox_inches="tight", dpi = 300)
    plt.title('Cargo theft in US (2018)')
    plt.show()
    
def nifty_pie():
    """ This function reads data from NIFTY_BANK.csv 
    and plots weightage of banks.Visualization method used is PIE GRAPH"""
    plt.figure(figsize=(10,10))
    plt.pie(df_bank_nifty['WEIGHT'],labels = df_bank_nifty['COMPANY NAME'], pctdistance= 1,textprops={'fontsize': 18}) 
    plt.title('NIFTY BANK WEIGHTAGE', fontsize = 40)
    plt.savefig('pie.png', bbox_inches="tight", dpi = 300)
    plt.show()
    
def USincidents_line():
    """ This function reads data from 2018 full table.csv
    and plots number of incidents(y-axis) vs 
    states in US(x-axis).Visualization method used is LINE GRAPH"""
    plt.figure()
    plt.plot(df_stolen18_full['State'], df_stolen18_full['Number of agencies reporting an incident'], label = 'Incidents reported by agencies')
    plt.plot(df_stolen18_full['State'], df_stolen18_full['Number of incidents reported'],label = 'Incidents reported')
    plt.xticks(rotation = 90)
    plt.title('Incidents regarding cargo theft in the US (2018)')
    plt.legend()
    plt.savefig('line_graph.png', bbox_inches="tight", dpi = 300)
    plt.show()
  
    
#Calling theft_bargraphs() function
theft_bargraphs()

#Calling theft_subplots() function
theft_subplots()

#Calling nifty_pie() function
nifty_pie()

#Calling USincidents_line() function
USincidents_line()

