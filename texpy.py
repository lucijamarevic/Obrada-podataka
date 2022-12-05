import numpy as np
import pandas as pd

# kao parametar prima pandas dataframe, a vraca tablicu
def make_table(data):
    tbl = ""
    arr = np.array(data)
    a,b  = arr.shape[0], arr.shape[1]
    for i in range(b-1):
        tbl += f"{data.columns[i]:.5f}" + " & " 
    tbl += f"{data.columns[b-1]:.5f}" + " \\\\ \n"
    for i in range(a):
        for j in range(b-1):
            tbl += f"{arr[i][j]:.5f}" + " & "
        tbl += f"{arr[i][b-1]:.5f}" + " \\\\ \n"
    return tbl

# primjer
"""dat = pd.read_csv("h1.csv")
print(make_table(dat))"""