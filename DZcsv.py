import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
df = pd.read_csv('dz.csv')

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Информация о данных
print("\nИнформация о данных:")
print(df.info())

# Статистическое описание данных
print("\nСтатистическое описание данных:")
print(df.describe())

# Преобразование Salary в числовое значение
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Удаление строк с пустыми значениями в Salary
df.dropna(subset=['Salary'], inplace=True)

# Группировка данных по городу и вычисление средней зарплаты
city_salary_mean = df.groupby('City')['Salary'].mean()

# Вывод результата
print("\nСредняя зарплата по городам:")
print(city_salary_mean)

# Сохранение результатов в новый CSV-файл
city_salary_mean.to_csv('output.csv', index=True)
