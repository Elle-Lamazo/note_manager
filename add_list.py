# Grade 1. Этап 1: Задание 4
#(несколько заметок)

username = input('Введите Ваше Имя:') #имя пользователя
title = [input('Введите заголовок заметки:\n1.'), input('2.'), input('3.')] #заголовок заметки

content = [input('Введите описание заметки:\n1.' + '"' + title[0] + '": '), input('2.' + '"' + title[1] + '": '),
           input('3.' + '"' + title[2] + '": ')] #описание заметки

status = [input('Укажите статус заметки:\n1.' + '"' + title[0] + '": '), input('2.' + '"' + title[1] + '": '),
           input('3.' + '"' + title[2] + '": ')] #статус заметки

created_date = input('Укажите дату начала заметки в формате ДД-ММ-ГГГГ:')
issue_date = input('Укажите дату истечения заметки в формате ДД-ММ-ГГГГ:')

print(username+',', 'Вы успешно создали заметку', '"' + title[2] + '"' + ',', '"' + title[0] + '"' + ',',
      '"'+title[1] + '"' + ',' '\nСрок выполнения до:',issue_date[:5],
      '\nЖелаем удачи!')
