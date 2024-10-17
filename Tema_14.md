# Тема 14. Работа с Matplotlib и Seaborn.
Отчет по Теме #14 выполнил(а):
- Куликов Максим Александрович
- ИВТ-22-1

| Задание    | Лабораторная работа | 
|------------|---------| 
| Задание 1  | +       | 
| Задание 2  | +       |  
| Задание 3  | +       |  
| Задание 4  | +       |  
| Задание 5  | +       |  
| Задание 6  | +       | 
| Задание 7  | +       | 
| Задание 8  | +       | 


знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа 14
## Задание №1
### Загрузка и предобработка данных
##### Библиотеки:
```python
import pandas as pd
import numpy as np
```
---
```python
df = pd.read_csv('diabetes_prediction_dataset-1.csv')

print(df.head())
print(df.isnull().sum())
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_1.png)

## Задание №2
### Описательный анализ данных
Рассмотрите данные —  изучите медианы, средние, дисперсии и т.д. 
Что можете сказать о данных? Сделайте вывод.
```python
desc_stats = df.describe()
print(desc_stats)

medians = df.select_dtypes(include=['float64', 'int64']).median()
print("Медианы:\n", medians)

variances = df.select_dtypes(include=['float64', 'int64']).var()
print("Дисперсии:\n", variances)

mins = df.select_dtypes(include=['float64', 'int64']).min()
maxs = df.max()

std_devs = df.select_dtypes(include=['float64', 'int64']).std()

print("Минимумы:\n", mins)
print("Максимумы:\n", maxs)
print("Стандартные отклонения:\n", std_devs)
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_2_1.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_2_2.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_2_3.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_2_4.png)
## Вывод
Средний возраст пациентов составляет около 41.9 года, с небольшой долей имеющих гипертонию (7.5%) и сердечно-сосудистые заболевания (3.9%). Средний индекс массы тела (ИМТ) находится на уровне 27.3, что указывает на избыточный вес, в то время как уровень HbA1c и уровень глюкозы в крови средние значения составляют 5.53% и 138.1 соответственно, что может указывать на предрасположенность к диабету. Около 8.5% пациентов имеют диагноз диабет.

## Задание №3
### Предобработка данных
Предобработайте датасет —  проверьте на наличие дубликатов и удалите, если они есть.
```python
duplicates = df.duplicated()
print("Количество дубликатов:", duplicates.sum())

df_cleaned = df.drop_duplicates()
print("Количество дубликатов после удаления:", df_cleaned.duplicated().sum())
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_3.png)

## Задание №4
### Отсутствующие значения
Предобработайте датасет — проверьте на наличие NaN и удалите или заполните значения.
```python
missing_values = df.isnull().sum()
print("Количество отсутствующих значений в каждом столбце:\n", missing_values)
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_4.png)

## Задание №5
### Изменение типа данных
Рассмотрев все данные, замените типы на нужные (при необходимости):
- Если есть числа — на `int` или `float`
- Если категории — можно оставить `object`

```python
print("Типы данных в датасете:\n", df.dtypes)
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_5.png)

## Задание №6
### Визуализация
Построим графики:
1. Построение гистограмм числовых переменных
2. Построение диаграмм размаха для определения наличия выбросов (ящики с усами) числовых переменных
3. Построение столбчатых диаграмм для категориальных переменных
4. Построение матрицы корреляции признаков (Phik или Пирсона)

После построения опишите выборку. Что она из себя представляет? Есть ли зависимости?

```python
import matplotlib.pyplot as plt
import seaborn as sns 

df.hist(bins=30, figsize=(15, 10))
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 10))
sns.boxplot(data=df[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']])
plt.title('Диаграммы размаха для числовых переменных')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='gender')
plt.title('Столбчатая диаграмма по полу')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='smoking_history')
plt.title('Столбчатая диаграмма по истории курения')
plt.xticks(rotation=45)
plt.show()

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation_matrix = numeric_df.corr(method='pearson')

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Матрица корреляции для числовых переменных')
plt.show()
plt.show()
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_6_1.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_6_2.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_6_3.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_6_4.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_6_5.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_6_6.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_6_7.png)

## Вывод
В выборке представлены медицинские и демографические данные пациентов, включая возраст, индекс массы тела (BMI), уровень HbA1c и уровень глюкозы в крови. Средний возраст составляет 42 года, а средний BMI — 27.32, что указывает на тенденцию к избыточному весу среди участников. Также наблюдаются случаи гипертонии и сердечных заболеваний, что характерно для старших возрастных групп.

Корреляционный анализ выявил несколько значимых зависимостей. Например, возраст связан с повышенным риском гипертонии и сердечных заболеваний, а высокий BMI коррелирует с повышенной вероятностью диабета. Сильная связь между уровнями HbA1c и глюкозы подтверждает их влияние на риск развития диабета.


## Задание №7
### Сравнение выборок
После построения всех типов графиков, необходимо провести анализ:

Отобразите на одном графике две выборки — люди с диабетом и без и сравните их.

1. Для числовых признаков — гистограммы и ящики с усами.
2. Для категориальных — столбчатые диаграммы.

После напишите вывод, есть ли какая-то зависимость?

```python
diabetes_positive = df[df['diabetes'] == 1]
diabetes_negative = df[df['diabetes'] == 0]
import matplotlib.pyplot as plt
import seaborn as sns

numerical_columns = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']

for column in numerical_columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(diabetes_positive[column], color='red', label='С диабетом', kde=True)
    sns.histplot(diabetes_negative[column], color='blue', label='Без диабета', kde=True)
    plt.title(f'Гистограмма для {column}')
    plt.legend()
    plt.show()

for column in numerical_columns:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='diabetes', y=column, data=df, palette=['blue', 'red'])
    plt.title(f'Ящики с усами для {column}')
    plt.show()
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_1.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_2.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_3.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_4.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_5.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_6.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_7.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_8.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_9.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_10.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_11.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_12.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_13.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_14/screen/lab14_7_14.png)

## Вывод
Люди с диабетом имеют в среднем более высокий возраст, индекс массы тела (BMI), уровень HbA1c и уровень глюкозы по сравнению с людьми без диабета. Это подтверждается как на гистограммах, так и на ящиках с усами, где значения у людей с диабетом смещены в сторону более высоких уровней.
У людей с диабетом чаще наблюдаются гипертония и сердечные заболевания, что видно на столбчатых диаграммах. Эти состояния также являются ключевыми факторами риска для диабета.

## Задание №8
### Общий вывод
Основные выводы:

Числовые признаки: Люди с диабетом, как правило, старше, имеют более высокий индекс массы тела, повышенные уровни HbA1c и глюкозы по сравнению с людьми без диабета. Это подтверждается на гистограммах и диаграммах размаха, где значения у диабетиков более смещены в сторону высоких уровней.

Категориальные признаки: Гипертония и сердечные заболевания чаще встречаются у людей с диабетом. Однако по таким признакам, как пол и история курения, значительных различий не выявлено.

Данные подтверждают наличие четких зависимостей между риском развития диабета и такими факторами, как возраст, BMI, уровень HbA1c и глюкозы. Также важную роль играют сопутствующие заболевания, такие как гипертония и сердечные заболевания. 
