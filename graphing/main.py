import pandas as pd

import matplotlib.pyplot as plt



#read in both csv files
temp_df = pd.read_csv("data/china_temps.csv")
use_df = pd.read_csv("data/china_usage.csv")

#drop all missing data rows
use_df.dropna(axis=0, inplace=True);

#select all columns for 1990 to 2018
use_df = use_df.loc[:, ["Country", "1990","1991","1992","1993","1994",
"1995","1996","1997","1998","1999","2000","2001","2002","2003","2004",
"2005","2006","2007","2008","2009","2010","2011","2012","2013","2014",
"2015","2016","2017","2018"]]


#limit rows to just china and all of asia
use_df = use_df.iloc[[1, 17, 18], :]

#change country to year for graph later
use_df.columns.values[0] = "Year"

#turn columns into rows and rows into columns
use_df = use_df.transpose(copy=True)

#only select dates from 1990 to 2013(where dataset ends)
temp_df = temp_df.iloc[2040:2317, :]
#then specifically for the date and avg temp columns
temp_df = temp_df.iloc[:, 0:2]

#select only August for each year
temp_df = temp_df[temp_df.date.str.startswith("01/08")]

#add to array
temp_list = temp_df.values.tolist()

#setup figure and subplot
figure1 = plt.figure(figsize=(20,10))
ax1 = figure1.add_subplot(211)

#loop through first list
for i in range(0, 24):
  #convert date from DD/MM/YYYY to just YYYY
  curr_date = temp_list[i][0]
  curr_year = curr_date[-4:]
  y=temp_list[i][1]
  
  ax1.scatter(curr_year, y, c="Red")
 

#finish setup of first graph
ax1.set_title("Average Temperature in China in August 1990-2013")
ax1.set_ylabel("Avg Temp (°C)")
ax1.set_xlabel("Year")
ax1.grid(True)


#plot 2nd graph
ax2 = figure1.add_axes([0.15,0.05,0.75,0.4])

#loop through each result
for f in range(1,30):
  usage = use_df.iloc[f, :]
  x2=usage.name
  #plot 3 graphs for each country
  c_y2=usage[2]
  china = ax2.scatter(x2, c_y2, c="Red")

  a_y2=usage[18]
  asia = ax2.scatter(x2, a_y2, c="Green")

  w_y2=usage[19]
  world = ax2.scatter(x2, w_y2, c="Purple")
  
#setup legend labels
china.set_label("China")
asia.set_label("Asia")
world.set_label("World")
ax2.legend()

#finish graph 2 headings
ax2.set_title("Energy Consumption in China and Asia 1990-2018")
ax2.set_ylabel("Energy Consumption (Mtoe)")
ax2.set_xlabel("Year")
ax2.grid(True)

#display graphs
plt.show()
plt.savefig("graph.png")
