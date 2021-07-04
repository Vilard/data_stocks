import tinvest as ti


with open('token.txt', encoding="utf-8") as f:
    token = f.read()

''' Получитть список акций с данными'''
client = ti.SyncClient(token)
c = client.get_market_search_by_figi('BBG004S68758')

# Акции
market_stoks = client.get_market_stocks().payload.instruments

# Облигации
bonds = client.get_market_bonds().payload.instruments

# Ввалюта
# currencies = client.get_market_currencies()

# Портфель
# portfolio = client.get_portfolio()

if __name__ == '__main__':

    
    def get_all_stoks(bool=True):
        if bool:
            csv_row = f'название, обьем, min_price_increment, тип, min_quantity, i.ticker, i.currency, i.figi\n'
            for i in market_stoks:
                # if i.currency[:3] != 'USD' and i.currency[:3] != 'EUR':
                if i.currency == "RUB":
                        csv_row += f'"{i.name}", {i.lot}, {i.min_price_increment}, {i.type}, {i.min_quantity}, {i.ticker}, {i.currency}, {i.figi} \n'
            return csv_row
        else: 
            return False
        

    def save_csv(bool=True):
        if bool:     
            with open("market.csv", "w", encoding='utf-8') as f:
                f.write(get_all_stoks())
        else:
            print('save_csv off')
    
    '''для сохранения в файл передать save_csv атрибут "save_csv(True)" или удалить False "save_csv()"'''
    save_csv(False)