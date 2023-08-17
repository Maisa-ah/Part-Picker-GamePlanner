import os
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as Finding
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

pd.set_option('max_colwidth', 1000)
pd.set_option('max_rows', 1000)

APPLICATION_ID = os.getenv('APPLICATION_ID')
