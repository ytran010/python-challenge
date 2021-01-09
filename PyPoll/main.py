#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


election_csv = os.path.join('Resources', 'election_data.csv')


# In[5]:


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csvheader = next(csvfile)
    
    i =0
    khan = 0
    correy = 0
    li = 0
    tooley = 0
    for row in csvreader:
        #total votes cast
        i = i + 1
        totalvotes = i
       
        #candidates and votes received
    
        if row[2] == "Khan":
            khan = khan + 1
            khanvotes = khan
            perkhan = round((100 * khanvotes/totalvotes),2)
        elif row[2] == "Correy":
            correy = correy + 1
            correyvotes = correy
            percor = round((100 * correyvotes/totalvotes),2)
        elif row[2] == "Li":
            li = li + 1
            livotes = li
            perli = round((100 * livotes/totalvotes),2)
        elif row[2] == "O'Tooley":
            tooley = tooley + 1
            toolvotes = tooley
            pertool = round((100 * toolvotes/totalvotes),2)

# winner

print("Election Results")
print("----------------------------")
print(f"Total Votes: {totalvotes}")
print("----------------------------")
print(f"Khan:     {perkhan}%   ({khanvotes})")
print(f"Correy:   {percor}%   ({correyvotes})")
print(f"Li:       {perli}%   ({livotes})")
print(f"O'Tooley: {pertool}%    ({toolvotes})")
print("----------------------------")
if khanvotes > correyvotes and livotes and toolvotes:
    print("Winner: Khan")
elif correyvotes > khanvotes and livotes and toolvotes:
    print("Winner: Correy")
elif livotes > correyvotes and khanvotes and toolvotes:
     print("Winner: Li")
elif toolvotes > correyvotes and livotes and khanvotes:
     print("Winner: O'Tooley")


# In[6]:


output_path = os.path.join("Analysis", "election_results.txt")

output = (
f"Election Results\n"
f"----------------------------\n"
f"Total Votes: {totalvotes}\n"
f"Khan:     {perkhan}%   ({khanvotes})\n"
f"Correy:   {percor}%   ({correyvotes})\n"
f"Li:       {perli}%   ({livotes})\n"
f"O'Tooley: {pertool}%    ({toolvotes})\n"
f"----------------------------\n"
f"Winner: Khan")

with open(output_path, 'w')as textfile:

    # Initialize csv.writer
   
    #file1 = open(election_results.txt, "w")

    textfile.write(output)


# In[ ]:




