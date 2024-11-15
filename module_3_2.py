def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    domens = [".com", ".net", "ru"]
    is_valid1 = False
    is_valid2 = False

    for d in domens:
        if str(recipient).find(d) >= 0:
            is_valid1 = True

    for d in domens:
        if str(sender).find(d) >= 0:
            is_valid2 = True

    if not is_valid1 or not is_valid2:
        print("Невозможно отправить письмо с адреса {0} на адрес {1}".format(sender, recipient))
        return

    elif (sender == recipient):
        print("Нельзя отправить письмо самому себе!")
        return

    elif (sender == "university.help@gmail.com"):
        print("Письмо успешно отправлено с адреса {0} на адрес {1}".format(sender, recipient))
        return

    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {0} на адрес {1}".format(sender, recipient))
    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')