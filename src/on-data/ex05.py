def remove_inconsistencies(data_frame, cols, to_remove):
    for col in cols:
        data_frame[col] = data_frame[col].str.strip(to_remove)


if __name__ == "__main__":
    import pandas as p
    data = p.read_csv("/home/leafar/documents/prg/code/py/python-general/src/on-data/datasets/sales/sales_3.csv")
    # data.drop_duplicates(keep='first', inplace=True)
    # data.to_csv("datasets/sales/sales_3.csv")
    print(data[['nome_produto', 'quantidade']].groupby('nome_produto').sum()[0].sort_values('quantidade', ascending=False))
    total_sales = 0
    for price, qtt in zip(data['preco'], data['quantidade']):
        total_sales += price * qtt
    print("-"*150)
    print(f'Total of sales: ${total_sales}')
    print("-"*150)
