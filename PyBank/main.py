#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv


# In[5]:


budget_csv = os.path.join('Resources', 'budget_data.csv') 


# In[6]:


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csvheader = next(csvfile)
    firstrow = next(csvreader)
    
    months = 1
    totalprofloss = int(firstrow[1])
    totalchange = 0
    prevprofloss = int(firstrow[1])

    maxchange = 0
    minchange = 0
    
    for column in csvreader:
        # total months
        months = months + 1 

        # net total of profits/losses
        totalprofloss += int(column[1])
        # changes in profits/losses
            # profloss is Profit/Losses
            # prevprofloss is Previous Profit/Losses
        profloss = int(column[1])
        proflosstime = column[0]
        change = profloss - prevprofloss

        prevprofloss = profloss
        totalchange += change
        
        if change > maxchange:
            maxchange = change
            maxmonth = column[0]
    
            
        if change < minchange:
            minchange = change
            minmonth = column[0]

            
avgchange = round((totalchange/(months - 1)),2)


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalprofloss}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {maxmonth} ${maxchange}")
print(f"Greatest Decrease in Profits: {minmonth} ${minchange}")

# Write the textfile
output_path = os.path.join("Analysis", "financial_analysis.txt")

output = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {months}\n"
f"Total: ${totalprofloss}\n"
f"Average Change: ${avgchange}\n"
f"Greatest Increase in Profits: {maxmonth} ${maxchange}\n"
f"Greatest Decrease in Profits: {minmonth} ${minchange}\n")

with open(output_path, 'w')as textfile:

    textfile.write(output)


# In[ ]:





# In[ ]:




