# Main program

import pandas as pd
import Data.Demand as D
import Data.Parameters as P

##################################################
# IMPORT DATA
excel_file = 'Data/DataEntry_v2.xlsx'

# DataFrame creation
df_1 = pd.read_excel(excel_file, sheet_name=1)
df_2 = pd.read_excel(excel_file, sheet_name=2)

# Data object creation
demand = D.Demand(df_1)
parameters = P.Parameters(df_2)

##################################################