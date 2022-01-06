import qrcode
# пример данных
link  = "https://files.fm/f/qzvfsp9eg"
# имя конечного файла
filename = "aiprint1.png"
# генерируем qr код
img  = qrcode.make(link)
# сохраняем img в файл
img.save(filename)