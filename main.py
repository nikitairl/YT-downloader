from numpy import flatiter
import pafy as pf
import pydub as pd

url = input('Введите SHARE ссылку: ')
video = pf.new(url)
bestv = video.getbest()
besta = video.getbestaudio()
length = video.length/60
print(f'Название: {video.title}, Количество просмотров: {video.viewcount}, Автор: {video.author}, Длительность: {length}')
print(f'Лучшее качество V: {bestv}')
print(f'Лучшее качество A: {besta}')
last = input('V или A? ')
if last == 'V':
    bestv.download(quiet=False)
elif last == 'A':
    besta.download()