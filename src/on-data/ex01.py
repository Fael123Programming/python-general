#Introductory functions
#Pandas Library: data handling
#Firstly, install it:
#On command prompt: pip install [library]
#Load a CSV file from mass memory to memory.
#This type of file contains various collected data organized in a table with rows and columns
#read_csv(list_of_parameters) -> see documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

# import pandas as pd #Importation with direct nickname
#
# data = pd.read_csv("datasets/kc_house_data.csv/kc_house_data.csv") #The basic and only-required parameter is the path which points toward your dataset
# #showing the first 5 columns with their respective information table
# print(data.head())
#
# #Showing the quantity of rows and columns of that very file we just opened
# print(data.shape) #(rowns,columns)
#
# #Showing the number of columns
# print(data.columns)
#
# #Showing ordained by column 'price'
# print(data.sort_values('price')) #price is the specific column
#
# #Do the same though it shows only the columns I want
# print(data[['price','bedrooms','id']].sort_values('price',ascending=True))
#
# #Now,descending
# print(data[['price','bathrooms','id']].sort_values('price',ascending=False))

#To grab columns: data[['name1','name2',...,'nameN']]
'''
    Report:
        -> How many houses are available to buy? 21613
        -> How many attributes do they have? 21
        -> What are the attributes? ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
        'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
        'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
        'lat', 'long', 'sqft_living15', 'sqft_lot15']
        -> Which is the most expensive house? 7252 with id 6762700020 (US$ 7700000)
        -> Which have more bedrooms? 15870 with id 2402100895 (33 bedrooms)
'''