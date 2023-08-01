#library
import pandas as pd
from scipy.stats import t

#pathway
arq_path = input (r"path:")
col_name = "QRN" #add the colunm name

#reading
df = pd.read_excel(arq_path)
colunm = df[col_name]

#main
def grubbs_test_outliers(data, alpha=0.05):
    n = len(data)
    critical_value = t.ppf(1 - alpha / (2 * n), n - 2)
    mean_val = data.mean()
    std_val = data.std()
    max_outlier = (data.max() - mean_val) / std_val
    min_outlier = (mean_val - data.min()) / std_val
    max_idx = data.idxmax()
    min_idx = data.idxmin()

    if max_outlier > critical_value or min_outlier > critical_value:
        if max_outlier > min_outlier:
            return max_idx
        else:
            return min_idx

    return None

# run
outliers = []
while True:
    outlier_idx = grubbs_test_outliers(colunm)
    if outlier_idx is not None:
        outliers.append(outlier_idx)
        colunm = colunm.drop(outlier_idx)
    else:
        break

print("outliers:", outliers)