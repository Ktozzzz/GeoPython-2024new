"""
Функция для преобразования температуры из Фаренгейтов в Цельсии.

Параметры 
---------
temp_fahrenheit: <числовое значение>
Температура в Фаренгейтах
convert_to: <int>

Возвращает
----------
<float>
Температура в Цельсиях
"""


def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit-32)*5/9
   
"""
Функция для классификации температуры в Цельсиях.

Параметры 
---------
temp_celsius: <числовое значение>
Температура в Wtkmcbz[
convert_to: <int>

Возвращает
----------
<f>
Температура в Цельсиях
"""

def temp_classifier(temp_celsius):
    if temp_celsius<-2:
        return 0
    elif temp_celsius>=-2 and temp_celsius<2:
        return 1
    elif temp_celsius>=2 and temp_celsius<15:
        return 2
    elif temp_celsius>=15:
        return 3