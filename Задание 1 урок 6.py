# видео урок 4, конец
from time import sleep

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']
    def running(self):
        i = 0
        while i < 3:
            print('Светофор переключается\n'
                f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(2)
            elif i == 1:
                sleep(1)
            elif i == 2:
                sleep(2)
                i = -1
            i += 1+


TrafficLight = TrafficLight()
TrafficLight.running()