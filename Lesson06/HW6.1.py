"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу можно
усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать
скрипт.
"""
from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def running(self):
        for color in self.__color.keys():
            print(f'Светофор включил: {color}')
            sleep(self.__color.get(color))


tr_light01 = TrafficLight()

tr_light01.running()