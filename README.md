# Phone-Number-Validation-and-Processing-for-International-Contacts

### The purpose is to provide a reusable and customizable framework for validating and processing phone numbers in a dataset. It allows for handling different country formats, removing invalid characters, and converting phone numbers to a consistent format for further analysis or data manipulation.



### Summary:

The provided code performs several tasks related to processing and validating phone numbers in a given dataset. Here is a summary of each section and its purpose:

Importing Libraries:

The required libraries such as numpy, pandas, matplotlib.pyplot, plotly.express, seaborn, re, phonenumbers, and warnings are imported.
Setting Display Options:

The display option for pandas is set to show all columns.
Country Details:

A dictionary named country_details is created, which contains information about various countries and their phone number formats.
Phone Number Processing Functions:

Two functions are defined:
is_valid_phone_number(phone, country): Checks if a phone number is valid for a given country using the phonenumbers library.
add_valid_number(phone, country): Appends a valid phone number to the valid_numbers list.
Phone Number Processing:

The function process_phone_numbers(row) takes a row from a DataFrame and processes the phone numbers in columns 'Phone 1.1' and 'Phone 2.1'.
It checks the country code and length of each phone number and adds valid numbers to the valid_numbers list.
The function returns a list of valid phone numbers or None if no valid numbers are found.
Number Format Conversion:

The function convert_number_format(phone_number) removes non-digit characters and converts scientific notation to a normal number format.
It is applied to the 'Phone 1.1' and 'Phone 2.1' columns of the DataFrame using the apply() method.
Reading and Processing the Dataset:

The provided CSV file is read into a DataFrame named df1 using pd.read_csv().
The 'Phone 1.1' and 'Phone 2.1' columns of df1 are converted to the desired number format using convert_number_format().
The process_phone_numbers() function is applied to each row of df1 using apply() to obtain the valid phone numbers.
The valid phone numbers are stored in a new column called 'Valid Phone Numbers' in df1.
Cleaning 'Valid Phone Numbers' Column:

The 'Valid Phone Numbers' column is cleaned to remove 'None' values and convert the list of numbers to a string representation.
This is done using a lambda function and the apply() method.
Counting Valid Phone Numbers:

The count of valid phone numbers is calculated by filtering out the 'None' values in the 'Valid Phone Numbers' column.
Saving the Processed DataFrame:

The processed DataFrame is saved to a new CSV file specified by file_path using to_csv().
Note: The code assumes the existence of a CSV file named "Part 1.csv" in the specified file path and saves the processed DataFrame to a new CSV file named "phonenumber.csv".
