#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print len(enron_data)

#print len(enron_data['METTS MARK'])


"""
count = 0
for user in enron_data:
    if enron_data[user]['poi'] == True:
        count+=1
print count


"""
"""
fo = open('../final_project/poi_names.txt','r')
fr = fo.readlines()
print len(fr[2:])
"""

#print enron_data["PRENTICE JAMES"]['total_stock_value']
#print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

"""
SKILLING JEFFREY
Kenneth Lay
Andrew Fastow
"""

"""
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
"""

"""
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
print count_salary
print count_email
"""

# didnt do feature formating

count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp+=1
print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())

# for poi
count_NaN_tp_poi = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        print 
        count_NaN_tp_poi+=1
print count_NaN_tp_poi
print float(count_NaN_tp_poi)/len(enron_data.keys())

count = 0
for user in enron_data:
    if enron_data[user]['poi'] == True and enron_data[user]['total_payments'] == 'NaN':
        count+=1
print count