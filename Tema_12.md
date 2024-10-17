# Тема 12. Введение в библиотку Pandas.
Отчет по Теме #12 выполнил(а):
- Куликов Максим Александрович
- ИВТ-22-1

| Задание    | Exercise_1.ipynb | 
|------------|---------| 
| Задание 1  | +       | 
| Задание 2  | +       |  
| Задание 3  | +       |  
| Задание 4  | +       |  
| Задание 5  | +       |  
| Задание 6  | +       |  
| Задание 7  | +       |  
| Задание 8  | +       |  
| Задание 9  | +       |  
| Задание 10  | +       |  
| Задание 11  | +       |  
| Задание 12  | +       |  

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа 12
## Задание №1
### Загрузите ваш DataFrame в переменную df и выведете на экран первые пять строк
```python
df = pd.read_csv('googleplaystore.csv')

print(df.head())
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_1.png)
## Вывод
Загрузил датафрейм в переменную df и отобразил первые 5 строк.

## Задание №2
### Отобразите количество строк и столбцов в DataFrame
```python
num_rows, num_columns = df.shape
print(f'Количество строк: {num_rows}, Количество столбцов: {num_columns}')
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_2.png)
## Вывод
Отобразил количесто строк и стобцов с помощью df.shape

## Задание №3
### Выведете основную информацию о DataFrame методом info(). Проанализируйте есть ли пропуски в столбцах. Напишите вывод о том, какие столбцы содержат пропуски
```python
df.info()

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_3.png)
## Вывод
Вывел основную информацию с помощью метода info()

## Задание №4
### Удалите или замените пропуски известными вам методами. (Подсказка: `dropna()` или `fillna()`, выбор того или иного метода должен быть аргументирован).
```python
df['Type'] = df['Type'].fillna(df['Type'].mode()[0])
df['Content Rating'] = df['Content Rating'].fillna(df['Content Rating'].mode()[0])
df['Current Ver'] = df['Current Ver'].fillna(df['Current Ver'].mode()[0])
df['Android Ver'] = df['Android Ver'].fillna(df['Android Ver'].mode()[0])

print(f'Количество строк после замены пропусков: {df.shape[0]}')
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_4.png)
## Вывод
Для числовых столбцов замена пропусков на среднее или медиану помогает сохранить статистические свойства набора данных. Для категориальных столбцов использование моды позволяет заполнить наиболее распространенной категорией, сохраняя распределение.

## Задание №5
### Проверьте нет ли пропусков после произведенной обработки
```python
missing_values_after = df.isnull().sum()
print(missing_values_after[missing_values_after > 0])
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_5.png)
## Вывод
Проверил нет ли пропусков, после обработки 0 пропусков в столбцах

## Задание №6
### Выведите на экран минимум и максимум из столбца `Price`:
```python
df['Price'] = df['Price'].replace({'\$': '', '0': '', ' ': ''}, regex=True).astype(float)

min_price = df['Price'].min()
max_price = df['Price'].max()

print(f'Минимальная цена: {min_price}, Максимальная цена: {max_price}')
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_6.png)
## Вывод
Удалил символы и привел столбец к числовому формату.

## Задание №7
### Выведите на экран медиану и среднее арифметическое столбцов:
- Rating
- Reviews
```python
def convert_reviews(value):
    if 'M' in value:
        return int(float(value.replace('M', '').strip()) * 1_000_000)
    elif 'K' in value:
        return int(float(value.replace('K', '').strip()) * 1_000)
    else:
        return int(value)

df['Reviews'] = df['Reviews'].apply(convert_reviews)

rating_median = df['Rating'].median()
rating_mean = df['Rating'].mean()

reviews_median = df['Reviews'].median()
reviews_mean = df['Reviews'].mean()

print(f'Медиана Ratings: {rating_median}, Среднее Ratings: {rating_mean}')
print(f'Медиана Reviews: {reviews_median}, Среднее Reviews: {reviews_mean}')
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_7.png)
## Вывод
Преобразовал строки в числовые значения и вычислил медиану с средней.

## Задание №8
### Выведите на экран все уникальные значения категориального столбца Genres
```python
unique_genres = df['Genres'].unique()
print(unique_genres)
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_8.png)
## Вывод
Использовал встроенную функцию unique()

## Задание №9
### Сгруппируйте данные по столбцу `Genres` и посчитайте для каждого жанра средний и медианный рейтинг. Представьте результат в виде нового DataFrame,который будет сохранен в переменную `grouped_df`, где одна колонка будет содержать названия жарнов, а две другие буду содержать в себе средний и медианный рейтинги. Напишите краткий вывод.
```python
grouped_df = df.groupby('Genres')['Rating'].agg(['mean', 'median']).reset_index()
grouped_df.columns = ['Genres', 'Average Rating', 'Median Rating']
print(grouped_df)
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_9.png)
## Вывод
В результате получил таблицу, которая позволит быстро сравнить средние и медианные рейтинги различных жанров приложений в наборе данных. 

## Задание №10
### Из получившегося датафрейма выведите на экран только те жанры, чей медианный рейтинг больше 4.5. Напишите краткий вывод.
```python
high_rated_genres = grouped_df[grouped_df['Median Rating'] > 4.5]
print(high_rated_genres)
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_10.png)
## Вывод
Теперь можно определить, какие жанры приложений имеют высокий медианный рейтинг, что может указывать на их популярность.

## Задание №11
### Выведете кол-во дубликатов в основном DataFrame (df) и удалите их
```python
num_duplicates = df.duplicated().sum()
print(f'Количество дубликатов в DataFrame: {num_duplicates}')

df = df.drop_duplicates()

num_duplicates_after = df.duplicated().sum()
print(f'Количество дубликатов после удаления: {num_duplicates_after}')
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_11.png)
## Вывод
Посчитал количество дубликатов в основном датафрейме, далее удалил с помощью df.drop_duplicates().

## Задание №12
### Посчитатайте какое количество приложений содержится в каждом жанре (value_counts).В получившемся Series выведите на экран 10 строк с наибольшим количеством приложений отсортированных по убыванию.
```python
genre_counts = df['Genres'].value_counts()

top_10_genres = genre_counts.head(10)
print(top_10_genres)
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_12/theme_12/screen/lab12_12.png)
## Вывод
С помощью value_counts посчитал и далее вывел топ 10.

## Общие выводы по теме
Успешно загрузил данные из CSV-файла и провел предварительную обработку, включая удаление или замену пропусков. Провел статистический анализ, вычислив медиану и среднее арифметическое для рейтингов приложений.
