import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query_string = f"(iso_a3 == '{country_code.upper()}' and (date >= '{year}-01-01') and (date <= '{year}-12-31'))"
    price_year_countrycode_df = df.query(query_string)
    mean_price_country = round(price_year_countrycode_df['dollar_price'].mean(),2)
    return mean_price_country

def get_big_mac_price_by_country(country_code):
    query_string = f"(iso_a3 == '{country_code.upper()}')"
    price_country_df = df.query(query_string)
    mean_price_country = round(price_country_df['dollar_price'].mean(),2)
    return mean_price_country

def get_the_cheapest_big_mac_price_by_year(year):
    query_string = (f"date >= '{year}-01-01' and date <= '{year}-12-31'")
    min_df = df.query(query_string)
    min_df_idx = min_df['dollar_price'].idxmin()
    min_item = min_df.loc[min_df_idx]
    min_answer = f"{min_item['name']}({min_item['iso_a3']}): ${round(min_item['dollar_price'],2)}"
    return min_answer

def get_the_most_expensive_big_mac_price_by_year(year):
    query_string = (f"date >= '{year}-01-01' and date <= '{year}-12-31'")
    max_df = df.query(query_string)
    max_df_idx = max_df['dollar_price'].idxmax()
    max_item = max_df.loc[max_df_idx]
    max_answer = f"{max_item['name']}({max_item['iso_a3']}): ${round(max_item['dollar_price'],2)}"
    return max_answer

if __name__ == "__main__":
    input_year = input("ENTER YEAR: ")
    input_country_code = input("ENTER COUNTRY CODE: ")

    year_countrycode_answer = get_big_mac_price_by_year(input_year,input_country_code)
    print(f"\nMean price based on year: {year_countrycode_answer}")

    year_answer = get_big_mac_price_by_country(input_country_code)
    print(f"Mean price based on country: {year_answer}")

    min_answer = (get_the_cheapest_big_mac_price_by_year(input_year))
    print(min_answer)
    max_answer = (get_the_most_expensive_big_mac_price_by_year(input_year))
    print(max_answer) 
    