from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
top_text = ""
bottom_text = ""
text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))
if text_type == 1:
  bottom_text = input("Введите нижний текст: ")
elif text_type == 2:
  top_text = input("Введите верхний текст: ")
  bottom_text = input("Введите нижний текст: ")
else:
  print("Ты вообще чёта не то пишешь, перезапусти программу и нормально введи на этот раз")
  quit()
print(top_text, bottom_text)

memes = ['Кот_в_очках.png', 'Кот_в_ресторане.png']

print('Выберите картинку для мема:')
for i in range(len(memes)):
  print(i, memes[i])

image = Image.open(memes[int(input('Введите номер картинки: '))])
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="black")
text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, (height - text[3] - 10)), bottom_text, font=font, fill="black")

image.save("memchik.png")