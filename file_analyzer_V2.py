import pandas as pd
import sys

def load_file(path):
    try:
        if path.endswith('.csv'):
            df = pd.read_csv(path)
        elif path.endswith('.json'):
            df = pd.read_json(path)
        elif path.endswith(('.xlsx','.xls')):
            df = pd.read_excel(path)
        else:
            print('Unsupported file format')
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

    mean_age = df['age'].mean()
    mean_salary = df['salary'].mean()
    mean_experience = df['experience'].mean()

    max_age = df['age'].max()
    max_salary = df['salary'].max()
    max_experience = df['experience'].max()

    min_age = df['age'].min()
    min_salary = df['salary'].min()
    min_experience = df['experience'].min()

    return{
        'rows': rows,
        'columns_quantity': columns_quantity,
        'columns_names': columns_names,

        'missing_values': missing_values,
        'duplicates': duplicates,
        'mean_age': mean_age,
        'mean_salary': mean_salary,
        'mean_experience': mean_experience,

        'min_age': min_age,
        'min_salary': min_salary,
        'min_experience': min_experience,

        'max_age': max_age,
        'max_salary': max_salary,
        'max_experience': max_experience
    }

def format_report(data):
    return f'''rows: {data['rows']}
columns quantity: {data['columns_quantity']}
columns names: {data['columns_names']}

missing values: {data['missing_values']}
duplicate: {data['duplicates']}

mean age: {data['mean_age']}
mean salary: {data['mean_salary']}
mean experince: {data['mean_experience']}

min/max age: {data['min_age']} / {data['max_age']}
min/max salary: {int(data['min_salary'])}USD / {int(data['max_salary'])}USD
min/max experience: {data['min_experience']} / {data['max_experience']}'''


df = load_file('data.csv')
data = analyze_dataframe(df)
report_data = format_report(data)

with open('report.txt','w') as report:
    report.write(report_data)