import numpy as np
import pandas as pd
import re
import phonenumbers
import warnings
warnings.simplefilter('ignore')
# set the max columns to none
pd.set_option('display.max_columns', None)

country_details = {
    'India': {'code': 'IN', 'code_number': 91, 'len_with_code': 12, 'len_without_code': 10},
    'South Africa': {'code': 'ZA', 'code_number': 27, 'len_with_code': 11, 'len_without_code': 9},
    'UAE': {'code': 'AE', 'code_number': 971, 'len_with_code': 12, 'len_without_code': 9},
    'Pakistan': {'code': 'PK', 'code_number': 92, 'len_with_code': 12, 'len_without_code': 10},
    'Singapore': {'code': 'SG', 'code_number': 65, 'len_with_code': 11, 'len_without_code': 8},
    'Egypt': {'code': 'EG', 'code_number': 20, 'len_with_code': 11, 'len_without_code': 10},
    'Nigeria': {'code': 'NG', 'code_number': 234, 'len_with_code': 13, 'len_without_code': 11},
    'Kuwait': {'code': 'KW', 'code_number': 965, 'len_with_code': 12, 'len_without_code': 8},
    'Kenya': {'code': 'KE', 'code_number': 254, 'len_with_code': 12, 'len_without_code': 9},
    'Australia': {'code': 'AU', 'code_number': 61, 'len_with_code': 11, 'len_without_code': 9},
    'Qatar': {'code': 'QA', 'code_number': 974, 'len_with_code': 12, 'len_without_code': 8},
    'United States': {'code': 'US', 'code_number': 1, 'len_with_code': 12, 'len_without_code': 10},
    'Canada': {'code': 'CA', 'code_number': 1, 'len_with_code': 12, 'len_without_code': 10},
    'United Kingdom': {'code': 'GB', 'code_number': 44, 'len_with_code': 12, 'len_without_code': 10},
    'Malaysia': {'code': 'MY', 'code_number': 60, 'len_with_code': 11, 'len_without_code': 9},
    'Philippines': {'code': 'PH', 'code_number': 63, 'len_with_code': 12, 'len_without_code': 10},
    'New Zealand': {'code': 'NZ', 'code_number': 64, 'len_with_code': 11, 'len_without_code': 9},
    'Sri Lanka': {'code': 'LK', 'code_number': 94, 'len_with_code': 12, 'len_without_code': 9},
    'Indonesia': {'code': 'ID', 'code_number': 62, 'len_with_code': 12, 'len_without_code': 10},
    'Germany': {'code': 'DE', 'code_number': 49, 'len_with_code': 12, 'len_without_code': 10},
    'France': {'code': 'FR', 'code_number': 33, 'len_with_code': 12, 'len_without_code': 9},
    'Brazil': {'code': 'BR', 'code_number': 55, 'len_with_code': 12, 'len_without_code': 10},
    'Bangladesh': {'code': 'BD', 'code_number': 880, 'len_with_code': 13, 'len_without_code': 11},
    'Hong Kong': {'code': 'HK', 'code_number': 852, 'len_with_code': 12, 'len_without_code': 8},
    'Thailand': {'code': 'TH', 'code_number': 66, 'len_with_code': 11, 'len_without_code': 9},
    'Netherlands': {'code': 'NL', 'code_number': 31, 'len_with_code': 11, 'len_without_code': 9},
    'Italy': {'code': 'IT', 'code_number': 39, 'len_with_code': 12, 'len_without_code': 10},
    'Spain': {'code': 'ES', 'code_number': 34, 'len_with_code': 12, 'len_without_code': 9},
    'Turkey': {'code': 'TR', 'code_number': 90, 'len_with_code': 12, 'len_without_code': 10},
    'Greece': {'code': 'GR', 'code_number': 30, 'len_with_code': 12, 'len_without_code': 10},
    'Sweden': {'code': 'SE', 'code_number': 46, 'len_with_code': 11, 'len_without_code': 9},
    'Norway': {'code': 'NO', 'code_number': 47, 'len_with_code': 11, 'len_without_code': 8},
    'Portugal': {'code': 'PT', 'code_number': 351, 'len_with_code': 12, 'len_without_code': 9},
    'Russia': {'code': 'RU', 'code_number': 7, 'len_with_code': 12, 'len_without_code': 10},
    'Switzerland': {'code': 'CH', 'code_number': 41, 'len_with_code': 12, 'len_without_code': 9},
    'Belgium': {'code': 'BE', 'code_number': 32, 'len_with_code': 11, 'len_without_code': 9},
    'Poland': {'code': 'PL', 'code_number': 48, 'len_with_code': 12, 'len_without_code': 9},
    'Ireland': {'code': 'IE', 'code_number': 353, 'len_with_code': 12, 'len_without_code': 9},
    'Ukraine': {'code': 'UA', 'code_number': 380, 'len_with_code': 12, 'len_without_code': 9},
    'Argentina': {'code': 'AR', 'code_number': 54, 'len_with_code': 12, 'len_without_code': 10},
    'Mexico': {'code': 'MX', 'code_number': 52, 'len_with_code': 12, 'len_without_code': 10},
    'Japan': {'code': 'JP', 'code_number': 81, 'len_with_code': 12, 'len_without_code': 10},
    'China': {'code': 'CN', 'code_number': 86, 'len_with_code': 13, 'len_without_code': 11},
    'South Korea': {'code': 'KR', 'code_number': 82, 'len_with_code': 12, 'len_without_code': 10},
    'Vietnam': {'code': 'VN', 'code_number': 84, 'len_with_code': 12, 'len_without_code': 10},
    'Israel': {'code': 'IL', 'code_number': 972, 'len_with_code': 12, 'len_without_code': 9}
}


def process_phone_numbers(row):
    phone1 = row['Phone 1.1']
    phone2 = row['Phone 2.1']
    valid_numbers = []

    def is_valid_phone_number(phone, country):
        parsed_number = phonenumbers.parse(phone, country)
        return phonenumbers.is_valid_number(parsed_number)

    def add_valid_number(phone, country):
        valid_numbers.append(phone if is_valid_phone_number(phone, country) else None)

    if phone1 is not None:
        for country, details in country_details.items():
            code = '+' + str(details['code_number'])
            if phone1.startswith(code):
                if len(phone1) == details['len_with_code']:
                    add_valid_number(phone1, details['code'])
            elif len(phone1) == details['len_without_code']:
                add_valid_number(code + phone1, details['code'])

    if phone2 is not None:
        for country, details in country_details.items():
            code = '+' + str(details['code_number'])
            if phone2.startswith(code):
                if len(phone2) == details['len_with_code']:
                    add_valid_number(phone2, details['code'])
            elif len(phone2) == details['len_without_code']:
                add_valid_number(code + phone2, details['code'])

    return valid_numbers if len(valid_numbers) > 0 else None


def convert_number_format(phone_number):
    if pd.isna(phone_number):
        return None

    # Remove non-digit characters
    digits_only = re.sub(r'\D', '', str(phone_number))

    # Convert scientific notation to normal number format
    if 'E' in digits_only:
        digits_only = str(float(digits_only))

    return digits_only

df =pd.read_csv(r"C:\Users\ADITYA PC\Downloads\Part 1.csv",encoding='latin-1')

# Assuming the phone numbers are in a pandas DataFrame column called 'Phone Numbers'
df['Phone 1.1'] = df['Phone 1.1'].apply(convert_number_format)
df['Phone 2.1'] = df['Phone 2.1'].apply(convert_number_format)

df['Valid Phone Numbers'] = df.apply(process_phone_numbers, axis=1)

df['Valid Phone Numbers'] = df['Valid Phone Numbers'].apply(lambda x: [number for number in x if number is not None] if x is not None else 'None')

df['Valid Phone Numbers'][df['Valid Phone Numbers'] != "None"].count()

file_path = r"C:\Users\ADITYA PC\Downloads\CSV_1.csv"
# Save the concatenated data frame to the specified path
df.to_csv(file_path, index=False)