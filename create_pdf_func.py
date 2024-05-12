#!pip install reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_pdf(photo, file_name, name, surname, age, sex, country, city, date, time, probability_prediction, binary_prediction) :
    c = canvas.Canvas(file_name, pagesize=letter)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont('FreeSans', 22)
    c.drawString(160, 750, 'Медицинское заключение')
    c.setFont('FreeSans', 15)
    c.drawImage(photo, 150, 400, width=300, height=300)
    if binary_prediction :
        prediction='Высокая вероятность пневмонии'
    else :
        prediction='Низкая вероятность пневмонии'
    text_lines = ["Имя: "+str(name), "Фамилия: "+str(surname), 'Возраст: '+str(age), 'Пол: '+str(sex), 'Страна: '+str(country), 'Город: '+str(city), 'Дата: '+str(date), 
                  'Время: '+str(time), 'Вероятность предсказания: '+str(probability_prediction), str(prediction)]
    y = 340  
    for line in text_lines:
        c.drawString(50, y, line)
        y -= 25  
    c.save()



#Пример
#create_pdf('008b69b2-446a-43dd-9ba2-9ccff8f3da41.jpg', "report.pdf", 'Иван', 'Иванов', 30, 'Мужчина', 'Россия', 'Москва', '20 April 2024 года', '22 часов 56 минут', 0.86, 1)
