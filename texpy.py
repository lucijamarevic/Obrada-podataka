import numpy as np
import pandas as pd

# kao parametar prima pandas dataframe, a vraca tablicu
def make_table(data):
    tbl = str(data.columns[0]) + " & " + str(data.columns[1]) + " \\\\ \n"
    arr = np.array(data)
    a,b  = arr.shape[0], arr.shape[1]
    for i in range(a):
        for j in range(b-1):
            tbl += str(arr[i][j]) + " & "
        tbl += str(arr[i][b-1]) + " \\\\ \n"
    return tbl

# primjer
"""dat = pd.read_csv("h1.csv")
print(make_table(dat))"""