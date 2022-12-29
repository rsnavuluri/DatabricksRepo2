from google.cloud import storage
from google.cloud import bigquery
import json
import pandas as pd
from io import BytesIO
from io import StringIO
# import lxml
pd.set_option('display.expand_frame_repr', False)

project = 'deleteprojrct-367413'
bucket_name = 'niaan-bucket-1'
blob_name = 'Employee.csv'

bq_client = bigquery.Client(project=project)
storagr_client = storage.Client(project=project)

bucket = storagr_client.bucket(bucket_name)
blob = bucket.blob(blob_name)

f1 = blob.download_as_string()
b1 = blob.download_as_bytes()

print(type(f1))
print(type(b1))

df = pd.read_csv(BytesIO(f1))
df2 = pd.read_csv(BytesIO(f1))

# print(len(df.columns))
# print(df.shape[1])

# print(df.count())

# print(df.describe())

# print(df.drop_duplicates(subset='DEPARTMENT_ID', keep='last', inplace=True))

# print(df.drop(['DEPARTMENT_ID','COMMISSION_PCT'], axis=1))
# print(df.drop(columns=['DEPARTMENT_ID', 'COMMISSION_PCT']))

# Drop the rows where at least one element is missing.
# print(df.dropna())
# Drop the columns where at least one element is missing.
# print(df.dropna(axis='columns'))
# Drop the rows where all elements are missing.
# print(df.dropna(how='all'))
# Keep only the rows with at least 2 non-NA values
# print(df.dropna(thresh=2))
# Define in which columns to look for missing values.
# print(df.dropna(subset=['COMMISSION_PCT']))

# print(df.empty) -- False

# print(df.equals(df2)) --True

# Replace all NaN elements with 0s.
# print(df.fillna(0))
# We can also propagate non-null values forward or backward.
# print(df.fillna(method="ffill"))
# Replace all NaN elements in column 'A', 'B', 'C', and 'D', with 0, 1, 2, and 3 respectively.
# values = {"A": 0, "B": 1, "C": 2, "D": 3}
# print(df.fillna(value=values))
# Only replace the first NaN element.
# print(df.fillna(value=values, limit=1))


# select columns by name
# print(df.filter(items=['EMPLOYEE_ID','DEPARTMENT_ID']))
# print(df.filter(['EMPLOYEE_ID','DEPARTMENT_ID']))

# select columns by regular expression
# print(df.filter(regex='E$', axis=1))

# select rows containing index '40'
# print(df.filter(like='40', axis=0))

# print(df[(df['DEPARTMENT_ID'] > 30) & (df['JOB_ID'] == 'FI_ACCOUNT')])

# Creates DataFrame object from dictionary by columns or by index allowing dtype specification.
# data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
# print(pd.DataFrame.from_dict(data))
# data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
# print(pd.DataFrame.from_dict(data, orient='index'))

# print(df[["DEPARTMENT_ID","SALARY"]].groupby(["DEPARTMENT_ID"]).sum(["SALARY"]))

#Insert column into DataFrame at specified location.
# df2.insert(1, 'new_colmn', None)
# print(df2)

# df2.loc[df2['DEPARTMENT_ID'] > 50]
# print(df.join(df2.set_index('DEPARTMENT_ID'), on='DEPARTMENT_ID', rsuffix='_df2'))

# df2.pop("COMMISSION_PCT")
# print(df2.head())

# print(df.query("DEPARTMENT_ID == 50 and  SALARY > 7000"))

# print(df.rename(columns={"COMMISSION_PCT": "COMMISSION"}).tail())
# print(df.rename(str.lower, axis='columns').head())

# df.replace({'COMMISSION_PCT':'- '},0.0, inplace=True)
# ## print(df['PHONE_NUMBER'].str.translate({ord('.'): None}))
# df['PHONE_NUMBER'] = df['PHONE_NUMBER'].str.replace('.','', regex=True)
# print(df.head())

# # Return an int representing the number of elements in this object.
# print(df.size)

# # Sort by the values along either axis.
# print(df.sort_values(by=["SALARY"], ascending=False))

# # Return the elements in the given *positional* indices along an axis.
# print(df.take([33]))

# print(df.to_csv(index=False))
# print(df.to_dict())
# print(df.to_json())
# print(df.to_html())
# print(df.to_latex())
# print(df.to_parquet())
# print(df.to_string())
# print(df.to_xml())

# # Truncate a Series or DataFrame before and after some index value.
# print(df.truncate(before=2, after=7))
# print(df.truncate(before="LAST_NAME", after="PHONE_NUMBER", axis='columns'))

print(df.where(df['DEPARTMENT_ID'] == 50))


