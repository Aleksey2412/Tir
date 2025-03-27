import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
df = pd.read_csv('dz.csv')

# Группировка данных по городу и вычисление средней зарплаты
city_salary_mean = df.groupby('City')['Salary'].mean()

# Вывод результата
print(city_salary_mean)
