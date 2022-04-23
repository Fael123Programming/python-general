# Data Extraction and Manipulation
import pandas as pd

data = pd.read_csv("datasets/kc_house_data.csv/kc_house_data.csv")

'''
    Questions/activities to respond/do:
    (1) -> What is the oldest house in dataset? 16768 with date 20140502T000000, id 5561000190 and price US$437500
    (2) -> How many houses have the maximum number of floors?
    -> Create a house classification, dividing them into low or high standard, according to their prices:
        -> Prices above US$ 540,000, then high standard;
        -> Obviously, prices below it, then low standard.
    -> Create a price-sorted report that contains, as information, the following:
        -> house id, date it became available to purchase, number of bedrooms, terrain size, prices and classification 
        of each house concerning to its price.
        Note: all this information has to be inserted into a .csv file.
    -> Create a map which localizes geographically where each house is located
        Note: this map will be an image made up in HTML
'''
# (1)
print(data[['date', 'id', 'price']].sort_values('date', ascending=True))

# (2)
print(data[['floors']].sort_values('floors', ascending=False))  # 3.5 floors are the biggest quantity
counter = 0
for floors in data[['floors']]: print(floors)
