def read_csv_through_unicodecsv(file_path):
    import unicodecsv
    with open(file_path, "rb") as file:
        return list(unicodecsv.DictReader(file))


if __name__ == "__main__":
    import pandas as p
    print("Testing csv files in Python")
    # path = "/home/leafar/documents/testwget/municipio/exportacao/EXP_2022_MUN.csv"
    path = "/home/leafar/documents/prg/code/py/python-general/src/on-data/datasets/kc_house_data.csv/kc_house_data.csv"
    # data = read_csv_through_unicodecsv(path)
    # print(len(data))
    print("-"*100)
    data_frame = p.read_csv(path)
    # print(data_frame.count())
    # print("-"*100)
    # print(data_frame.head(5))
    # print("-"*100)
    # print(data_frame.info())
    # print("-" * 100)
    # print(data_frame.describe())
    # print("-" * 100)
    # total_price = data_frame['price'].sum()
    # print(f"Total price: ${total_price}")
    # print(data_frame[['id', 'price']].sort_values('price'))
    # print("-"*100)
    # print(data_frame[['id', 'price']].groupby('id').sum())
    # print(data_frame["price"].min())
    # print(data_frame["price"].max())
    # print(data_frame['price'].idxmin())  # In which line the min price is.
    # print(data_frame['price'].idxmax())  # In which line the max price is.
    # print(data_frame['id'].unique())
    # print(data_frame[data_frame.duplicated(keep='first')])
    # print(data_frame.drop_duplicates(keep='first', inplace=True))
