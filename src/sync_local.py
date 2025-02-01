import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

def syncing():
    print("Syncing local data...")
    # Add your syncing logic here
    # Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Add credentials to the account
    creds = Credentials.from_service_account_file('utils/credentials-gsheet.json', scopes=scope)

    # Authorize the clientsheet 
    client = gspread.authorize(creds)

    # Get the instance of the Spreadsheet
    sheet = client.open('[Price List]KTC Item Database')

    # Get the first sheet of the Spreadsheet
    worksheet = sheet.get_worksheet(0)

    # Get all the records of the data
    records = worksheet.get_all_records()

    # Convert the json to dataframe
    try:
        df = pd.DataFrame.from_dict(records)
    except Exception as e:
        print(f"Sync unsuccessful: {e}")
        return

    # Save the dataframe to csv
    df.to_csv('utils/data.csv', index=False)
    
    print("Sync successful")