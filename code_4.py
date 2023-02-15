import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query_string = f"(iso_a3 == '{country_code.upper()}' and (date > '{year}-01-01' and date <'{year}-12-31'))"
    price_year_df = df.query(query_string)
    mean_price_country = round(price_year_df['dollar_price'].mean(),2)
    return mean_price_country

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    input_year = input("ENTER YEAR: ")
    input_country_code = input("ENTER COUNTRY CODE: ")

    answer = get_big_mac_price_by_year(input_year,input_country_code)
    print(answer)