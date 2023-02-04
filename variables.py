from dotenv import load_dotenv
import os

load_dotenv()

my_username = os.environ['LINKEDIN_USERNAME']
my_password = os.environ['LINKEDIN_PASSWORD']

file_name = 'results.csv' # file where the results will be saved

query = 'site:linkedin.com/in/ AND "Umair Chowdhry" AND "United States"'

contactList = [
    'https://www.linkedin.com/in/malikalihamza/',
    'https://www.linkedin.com/in/atifchwdhry/'
]

    # 'https://www.linkedin.com/in/chwdhry/',
    # 'https://www.linkedin.com/in/rubiachowdhry/',