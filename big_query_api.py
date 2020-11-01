from google.icloud import bigquery

# create a 'client' object

client = bigquery.Client()

# determine dataset, project, table

desired_dataset = 'crypto_bitcoin'          # input your desired dataset
desired_project = 'bigquery-public.data'    # input your desired dataset
desired_table   = 'transactions'            # input your desired table

# construct dataset reference

dataset_ref = client.dataset(desired_dataset, project = desired_project)

# API request the dataset

dataset = client = client.get_dataset(dataset_ref)

# construct table reference

table_ref = dataset_ref.table(desired_table)

# API request the table

table = client.get_table(table_ref)

# preview first five rows in a dataframe for initial inspection

client.list_rows(table, max_results = 5).to_dataframe()