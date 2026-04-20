import pandas as pd
import sys

def load_file(path):
    try:
        if path.endswith('.csv'):
            df = pd.read_csv(path)
        elif path.endswith('.json'):
            df = pd.read_json(path)
        elif path.endswith('.xlsx'):
            df = pd.read_excel(path)
        else:
            print('Unsuported file format')
            sys.exit()
            
    except Exception as e:
        print(f'Error: {e}')
        sys.exit()
        
    if df.empty:
        print('File is empty')
        sys.exit()
        
    return df

def analyze_dataframe(df):
    rows = df.shape[0]
    columns_quantity = df.shape[1]
    columns_names = list(df.columns)
    missing_values = df.isnull().sum().to_dict()
    duplicates = df.duplicated().sum()

    return {
        'rows': rows,
        'columns_quantity': columns_quantity,
        'columns_names': columns_names,

        'missing_values': missing_values,
        'duplicates': duplicates,
    }

def format_report(data):
    return f'''rows: {data['rows']}
columns_quantity: {data['columns_quantity']}
columns_names: {data['columns_names']}

missing_values: {data['missing_values']}
duplicates: {data['duplicates']}'''

df = load_file('data.csv')
data = analyze_dataframe(df)
report_data = format_report(data)

with open('report.txt','w') as report:
    report.write(report_data)