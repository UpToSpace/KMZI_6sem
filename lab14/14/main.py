import stegoimage
import stegosound


name = 'slavnikov mikhail alexandrovich'
with open('report.txt', encoding="utf8") as f:
    report = f.read()


stegoimage.encode(name, 'cat.bmp', 'name.bmp')
decoded = stegoimage.decode('name.bmp')
print(f'Decoded image: {decoded}\n')

stegoimage.encode(report, 'cat.bmp', 'report.bmp')
decoded = stegoimage.decode('report.bmp')
print(f'Decoded image: {decoded}\n\n')


stegosound.encode(name, 'mario.wav', 'name.wav')
decoded = stegosound.decode('name.wav')
print(f'Decoded sound: {decoded}\n')
stegosound.encode(report, 'mario.wav', 'report.wav')
decoded = stegosound.decode('report.wav')
print(f'Decoded sound: {decoded}\n')
