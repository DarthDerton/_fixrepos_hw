import telebot
from telebot import types
import requests
from datetime import datetime
import time
from bs4 import BeautifulSoup

"""API созданного бота"""
bot = telebot.TeleBot('6157744920:AAEcIepR896ltAoVxcExPsU-W4fbU1bC0-0')


@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id, f'Приветствуем, <b>{message.from_user.first_name} ' 
                                      f'{message.from_user.last_name}</b>!\n'
                                      'Вы находитесь в чат-боте "FTA".\n'
                                      'Он создан для упрощения Вашей деятельности в мире финансов.\n'
                                      'Для вызова графических кнопок нажмите /menu.\n'
                                      , parse_mode='html')


@bot.message_handler(commands=['menu'])
def menu_main(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton('Курсы валют ЦБ')
    button3 = types.KeyboardButton('Новости')
    button2 = types.KeyboardButton('Инвестиции')
    button4 = types.KeyboardButton('Совет')
    murkup.add(button1, button2, button3, button4, )
    bot.send_message(message.chat.id, 'Нажмите на желаемую кнопку: ', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Новости")
def news(message):
    url = 'https://1prime.ru/News/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    card_title = bs.find('h2', class_='rubric-list__article-title')
    card_url = card_title.find('a')['href']
    card_datetime = bs.find("time").get("datetime")
    dt = datetime.strptime(card_datetime, '%Y-%m-%dT%H:%M:%S%z')
    formatted_dt = dt.strftime('%Y-%m-%d %H:%M:%S')
    bot.send_message(message.chat.id, f'{card_title.text} https://1prime.ru{card_url} {formatted_dt}'
                     , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Курсы валют ЦБ")
def menu_rates(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    USD = types.KeyboardButton('$ Доллар США')
    GBP = types.KeyboardButton('£ Фунт стерлинга')
    EUR = types.KeyboardButton('€ Евро')
    JPY = types.KeyboardButton('¥ Японская иена')
    CNY = types.KeyboardButton('₩ Китайский юань')
    CAD = types.KeyboardButton('С$ Канадский доллар')
    CHF = types.KeyboardButton('₣ Швейцарский франк')
    AUD = types.KeyboardButton('A$ Австралийский доллар')
    back = types.KeyboardButton('⤝Вернуться в главное меню')
    murkup.add(USD, GBP, EUR, JPY, CNY, CAD, CHF, AUD, back)
    bot.send_message(message.chat.id, 'Выберите денежную единицу: Valute/RUB', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "$ Доллар США")
def dollar(message):
    data_0 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data0 = data_0['Valute']['USD']['Value']
    bot.send_message(message.chat.id, f'1 <b>Доллар США</b> = {data0} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "£ Фунт стерлинга")
def foont(message):
    data_1 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data1 = data_1['Valute']['GBP']['Value']
    bot.send_message(message.chat.id, f'1 <b>Фунт стерлингов СК</b> = {data1} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "€ Евро")
def euro(message):
    data_2 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data2 = data_2['Valute']['EUR']['Value']
    bot.send_message(message.chat.id, f'1 <b>Евро</b> = {data2} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "¥ Японская иена")
def yenna(message):
    data_3 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data3 = data_3['Valute']['JPY']['Value']
    bot.send_message(message.chat.id, f'100 <b>Японских иен</b> = {data3} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "₩ Китайский юань")
def yan(message):
    data_4 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data4 = data_4['Valute']['CNY']['Value']
    bot.send_message(message.chat.id, f'1 <b>Китайский юань</b> = {data4} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "С$ Канадский доллар")
def cad(message):
    data_5 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data5 = data_5['Valute']['CAD']['Value']
    bot.send_message(message.chat.id, f'1 <b>Канадский доллар</b> = {data5} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "₣ Швейцарский франк")
def chf(message):
    data_6 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data6 = data_6['Valute']['CHF']['Value']
    bot.send_message(message.chat.id, f'1 <b>Швейцарский франк</b> = {data6} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "A$ Австралийский доллар")
def aud(message):
    data_7 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data7 = data_7['Valute']['AUD']['Value']
    bot.send_message(message.chat.id, f'1 <b>Австралийский доллар</b> = {data7} ₽', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "⤝Вернуться в главное меню")
def back(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton('Курсы валют ЦБ')
    button3 = types.KeyboardButton('Новости')
    button2 = types.KeyboardButton('Инвестиции')
    button4 = types.KeyboardButton('Совет')
    murkup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, 'Нажмите на желаемую кнопку: ', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Инвестиции")
def deposits(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    bank_dep = types.KeyboardButton('% по вкладам в RUB и Valute')
    precious_meta = types.KeyboardButton('Учётные цены драгметаллов ЦБ')
    back = types.KeyboardButton('⤝Вернуться в главное меню')
    murkup.add(bank_dep, precious_meta, back)
    bot.send_message(message.chat.id, 'Выберите желаемую категорию', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "% по вкладам в RUB и Valute")
def advice(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    top = types.KeyboardButton('Топ 20 самых высоких ставок')
    din = types.KeyboardButton('Динамика максимальной ставки')
    back_2 = types.KeyboardButton('⤝Назад')
    murkup.add(top, din, back_2)
    bot.send_message(message.chat.id, 'Выберите желаемую категорию', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Топ 20 самых высоких ставок")
def top(message):
    bot.send_message(message.chat.id, 'Для сравнения процентных ставок по банкам, передите на сайт: '
                     , parse_mode='html')
    bot.send_message(message.chat.id, 'https://www.banki.ru/products/deposits/', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Учётные цены драгметаллов ЦБ")
def met_price(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    au = types.KeyboardButton('Золото')
    ag = types.KeyboardButton('Серебро')
    pt = types.KeyboardButton('Платина')
    pd = types.KeyboardButton('Палладий')
    din = types.KeyboardButton('Посмотреть динамику цен')
    back = types.KeyboardButton('⤝Назад')
    murkup.add(au, ag, pt, pd, din, back)
    bot.send_message(message.chat.id, f'Вы можете посмотреть учётную цену на выбранный металл за текущую дату, '
                                      f'либо посмотреть учётные цены за предыдущие временные периоды и сравнить их,' 
                                      f'перейдя на сайт ЦБ РФ. '
                                      f'Для этого нажмите на кнопку:\n' 
                                      f'"Посмотреть динамику цен"')
    bot.send_message(message.chat.id, 'Выберите желаемую категорию: ', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Золото")
def au(message):
    url = 'https://www.cbr.ru/hd_base/metall/metall_base_new/'
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/112.0.0.0 Safari/537.36"}
    html = requests.get(url, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    card = soup.findAll('td', {'class': 'right'})
    price = card[0].text.replace(' ', '').replace(',', '.')
    bot.send_message(message.chat.id, f'Учётная цена <b>Золота</b>: {price} руб./грамм', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Серебро")
def ag(message):
    url = 'https://www.cbr.ru/hd_base/metall/metall_base_new/'
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/112.0.0.0 Safari/537.36"}
    html = requests.get(url, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    card = soup.findAll('td', {'class': 'right'})
    price = card[1].text.replace(' ', '').replace(',', '.')
    bot.send_message(message.chat.id, f'Учётная цена <b>Серебра</b>: {price} руб./грамм', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Платина")
def pt(message):
    url = 'https://www.cbr.ru/hd_base/metall/metall_base_new/'
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/112.0.0.0 Safari/537.36"}
    html = requests.get(url, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    card = soup.findAll('td', {'class': 'right'})
    price = card[2].text.replace(' ', '').replace(',', '.')
    bot.send_message(message.chat.id, f'Учётная цена <b>Платины</b>: {price} руб./грамм', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Палладий")
def pd(message):
    url = 'https://www.cbr.ru/hd_base/metall/metall_base_new/'
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/112.0.0.0 Safari/537.36"}
    html = requests.get(url, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    card = soup.findAll('td', {'class': 'right'})
    price = card[3].text.replace(' ', '').replace(',', '.')
    bot.send_message(message.chat.id, f'Учётная цена <b>Палладия</b>: {price} руб./грамм', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Посмотреть динамику цен")
def din(message):
    bot.send_message(message.chat.id, 'Для просмотра динамики учётных цен на драгоценные металлы, '
                                      'перейдите на сайт Центрального Банка России')
    bot.send_message(message.chat.id, 'https://www.cbr.ru/hd_base/metall/metall_base_new/', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Динамика максимальной ставки")
def din(message):
    bot.send_message(message.chat.id, 'Просмотр средней процентной ставки поможет Вам провести '
                                      'анализ ставок по 3-м декадом каждого предыдущего месяца, '
                                      'и выбрать самую выгодную из них', parse_mode='html')
    bot.send_message(message.chat.id, 'Для просмотра динамики максимальной процентной ставки ' 
                                      '(по вкладам в российских рублях) '
                                      'десяти кредитных организаций, привлекающих наибольший '
                                      'объём депозитов физических лиц, перейдите на сайт ЦБ РФ', parse_mode='html')
    bot.send_message(message.chat.id, 'https://www.cbr.ru/statistics/avgprocstav/', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "⤝Назад")
def back_2(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    bank_dep = types.KeyboardButton('% по вкладам в RUB и Valute')
    precious_meta = types.KeyboardButton('Учётные цены драгметаллов ЦБ')
    back = types.KeyboardButton('⤝Вернуться в главное меню')
    murkup.add(bank_dep, precious_meta, back)
    bot.send_message(message.chat.id, 'Выберите желаемую категорию', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Совет")
def advice(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    fin_advice = types.KeyboardButton("Финансовый навигатор")
    bankcard_sec = types.KeyboardButton("Финансовая безопасность")
    back = types.KeyboardButton('⤝Вернуться в главное меню')
    murkup.add(fin_advice, bankcard_sec, back)
    bot.send_message(message.chat.id, 'Выберите желаемую категорию', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Финансовый навигатор")
def navigator(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    budjet = types.KeyboardButton('Составление бюджета')
    dolgi = types.KeyboardButton('Управление долгами')
    strahovanie = types.KeyboardButton('Страхование')
    nalogi = types.KeyboardButton('Налоговое планирование')
    krediti = types.KeyboardButton('Управление кредитом')
    nedvizhimost = types.KeyboardButton('Недвижимость')
    kariera = types.KeyboardButton('Карьерный рост')
    nazad = types.KeyboardButton('⤝ Назад')
    murkup.add(budjet, dolgi, strahovanie, nalogi, krediti, nedvizhimost, kariera, nazad)
    bot.send_message(message.chat.id, f'<b>Финансовый навигатор</b> представляет собой сборник советов, которые могут '
                                      f'помочь Вам получить информацию о конкретных продуктах и услугах, ' 
                                      f'а также советы и рекомендации по их выбору и использованию.', parse_mode='html')
    bot.send_message(message.chat.id, 'Выберите категорию совета:', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Составление бюджета")
def budjet(message):
    bot.send_message(message.chat.id, '<b>Составление бюджета:</b>\n' 
                                      '1. Определите свой доход и фиксируйте его.\n'
                                      '2. Оцените свои расходы, сократите ненужные траты.\n'
                                      '3. Создайте категории расходов и распределите свои деньги между ними.\n'
                                      '4. Отслеживайте свои расходы, используя приложения или таблицы Excel.\n'
                                      '5. Постоянно пересматривайте свой бюджет, чтобы увидеть, ' 
                                      'где можно сэкономить больше денег.\n'
                                      , parse_mode='html')
    bot.send_message(message.chat.id, f'<b>Инвестирование:</b>\n'
                                      '1. Изучите различные варианты инвестирования ' 
                                      'и выберите наиболее подходящий для вас.\n'
                                      '2. Диверсифицируйте свой портфель, распределив ' 
                                      'ваши инвестиции между различными активами.\n'
                                      '3. Управляйте своим риском, выбирая ' 
                                      'соответствующие инструменты для инвестирования.\n'
                                      '4. Не забывайте о долгосрочной перспективе ' 
                                      'и не делайте резких действий на основе краткосрочной волатильности.\n'
                                      '5. Следите за изменением рынка и общей экономической ситуацией, ' 
                                      'чтобы принимать информированные решения.\n'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Управление долгами")
def dolgi(message):
    bot.send_message(message.chat.id, '<b>1. Стратегии погашения долгов:</b>\n'
                                      '- Разработать бюджет и определить, '
                                      'сколько вы можете ежемесячно отложить для выплаты долгов.\n'
                                      '- Приоритезировать долги, начиная с тех, '
                                      'которые имеют наивысший процентный кредит, '
                                      'чтобы минимизировать общие затраты на проценты.\n'
                                      '- Рассмотреть варианты рефинансирования долгов с более низкой ' 
                                      'процентной ставкой или более гибкими условиями выплаты.\n'
                                      '<b>2. Переговоры с кредиторами:</b>\n'
                                      '- Обратиться к кредитору и сообщить о финансовых затруднениях, '
                                      'объяснить причины задержки выплаты.\n'
                                      '- Попросить у кредитора возможность реструктуризации или переноса ' 
                                      'выплаты долга на более длительный срок.\n'
                                      '- Рассмотреть возможность снижения процентных ставок, '
                                      'особенно если уже были заключены договоренности о возврате долгов.\n'
                                      '<b>3. Избежание кредитов с высокими процентами:</b>\n'
                                      '- Будьте осмотрительны при выборе кредитора и не соглашайтесь на условия, ' 
                                      'которые могут привести к большим затратам в будущем.\n'
                                      '- Рассмотреть возможность использования сбережений или других '
                                      'источников финансирования, прежде чем обращаться за кредитом.\n'
                                      '- Следить за своей кредитной историей и работать над улучшением ее показателей,' 
                                      'чтобы иметь более выгодные условия при получении кредита.\n', parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Страхование")
def strahovanie(message):
    bot.send_message(message.chat.id, f'<b>Как выбрать подходящее страховое покрытие?</b>\n'
                                      '1. Оценить свои потребности и риски\n'
                                      '2. Изучить условия и ограничения каждого вида страхования\n'
                                      '3. Сравнить предложения от разных страховых компаний по цене и условиям\n'
                                      '4. Обратить внимание на репутацию и финансовую стабильность страховой компании\n'
                                      '5. Рассмотреть возможность добавления дополнительных ' 
                                      'опций для более широкого покрытия\n'
                                      '6. Не забывать про переоценку и обновление страховки при '
                                      'изменении жизненной ситуации или значительных изменений в имуществе.'
                     , parse_mode='html')


@bot.message_handler(func = lambda message: message.text == "Налоговое планирование")
def nalogi(message):
    bot.send_message(message.chat.id, f'<b>Вот несколько пунктов, которые могут помочь</b> ' 
                                      f'<b>Вам минимизировать налоговые обязательства и</b> '
                                      f'<b>максимизировать налоговые вычеты:</b>'
                     , parse_mode='html')
    bot.send_message(message.chat.id, '<b>1. Используйте все доступные налоговые вычеты и льготы:</b> ' 
                                      'изучите налоговый кодекс вашей страны и '
                                      'ознакомьтесь со всеми возможными вычетами и льготами.\n'
                                      '<b>2. Планируйте свои расходы:</b> если вы знаете, '
                                      'что в этом году будете тратить определенную сумму денег на образование,' 
                                      'благотворительность или другие цели, то попробуйте сделать' 
                                      'это до конца налогового года,' 
                                      'чтобы получить соответствующие налоговые вычеты.\n'
                                      '<b>3. Общайтесь с профессионалами:</b> если у вас нет достаточной экспертизы ' 
                                      'в области налогового законодательства, обратитесь к налоговым консультантам '
                                      'или бухгалтерам для получения советов и помощи '
                                      'в минимизации налоговых обязательств.\n'
                                      '<b>4. Оптимизируйте свою структуру компании:</b> если '
                                      'вы являетесь предпринимателем, '
                                      'изучите налоговые законы, чтобы оптимизировать свою структуру компании '
                                      'и использовать все возможные вычеты.\n'
                                      '<b>5. Инвестируйте в пенсионные фонды:</b> внесения '
                                      'в пенсионные фонды могут помочь '
                                      'уменьшить вашу налогооблагаемую базу и '
                                      'получить дополнительные налоговые льготы.\n'
                                      '<b>6. Следите за изменениями в налоговом законодательстве:</b> '
                                      'налоговые законы постоянно меняются, поэтому не забывайте следить за '
                                      'новостями и изменениями, которые могут повлиять на вашу налоговую обязанность.\n'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Управление кредитом")
def krediti(message):
    bot.send_message(message.chat.id, f'<b>Советы по поддержанию хорошего кредитного рейтинга:</b>\n'
                                      '1. Своевременно оплачивайте все свои счета и кредиты.\n'
                                      '2. Старайтесь не использовать всю доступную вам кредитную линию.\n'
                                      '3. Не открывайте слишком много новых кредитных счетов за '
                                      'короткий период времени.\n'
                                      '4. Проверяйте свой кредитный отчет на предмет ошибок и неточностей.',
                     parse_mode='html')
    bot.send_message(message.chat.id, '<b>Советы по управлению задолженностью по кредитным картам:</b>\n'
                                      '1. Старайтесь оплачивать больше, чем минимальный платеж.\n'
                                      '2. Перенесите баланс с карты с '
                                      'высоким процентом на карту с более низким процентом.\n'
                                      '3. Разработайте план погашения долга и придерживайтесь его.\n'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Недвижимость")
def nedvizhimost(message):
    bot.send_message(message.chat.id, f'<b>Советы по покупке недвижимости:</b>\n'
                                      '1. Определите свой бюджет и возможности для '
                                      'получения кредита на жилье.\n'
                                      '2. Изучите рынок недвижимости в выбранном районе, '
                                      'чтобы оценить цены и состояние рынка.\n'
                                      '3. Наймите опытного агента по недвижимости для получения '
                                      'советов и помощи в процессе покупки.\n'
                                      '4. При осмотре недвижимости обращайте внимание на ее состояние, '
                                      'планировку, местоположение и инфраструктуру вокруг.\n'
                                      '5. Прежде чем заключать сделку, проверьте все необходимые документы '
                                      'и убедитесь, что объект свободен от обременений.\n'
                                      , parse_mode='html')
    bot.send_message(message.chat.id, f'<b>Советы по продаже недвижимости:</b>\n'
                                      '1. Подготовьте недвижимость к продаже: '
                                      'уберите и отремонтируйте всё, что нужно.\n'
                                      '2. Изучите рынок недвижимости, чтобы оценить цену своей недвижимости, '
                                      'и обратитесь за советом к агенту по недвижимости.\n'
                                      '3. Разместите объявление о продаже в различных источниках, '
                                      'таких как сайты недвижимости или газеты.\n'
                                      '4. Проведите показы недвижимости потенциальным покупателям '
                                      'и готовьтесь ответить на их вопросы.\n'
                                      '5. Проверьте, что все необходимые документы для продажи готовы.\n'
                                      , parse_mode='html')
    bot.send_message(message.chat.id, f'<b>Советы по аренде недвижимости:</b>\n'
                                      '1. Изучите рынок аренды недвижимости в выбранном районе, '
                                      'чтобы оценить стоимость аренды и конкуренцию на рынке.\n'
                                      '2. Выберите надежного арендодателя и заключите договор аренды.\n'
                                      '3. Убедитесь, что все условия аренды ясны и четко прописаны в договоре аренды.\n'
                                      '4. Следите за регулярностью выплаты арендных платежей и '
                                      'своевременно сообщайте об ущербе или неисправностях в съемной недвижимости.'
                                      , parse_mode='html')
    bot.send_message(message.chat.id, f'<b>Советы по ипотеке и кредитам на приобретение жилья:</b>\n'
                                      '1. Определите свою финансовую способность и сумму кредита, '
                                      'которую вы можете получить.\n'
                                      '2. Сравните различные предложения кредитных организаций '
                                      'и выберите наилучшие условия кредитования.\n'
                                      '3. Заключите договор кредитования и внимательно изучите все '
                                      'условия и требования, чтобы избежать непредвиденных затрат.\n'
                                      '4. Регулярно выплачивайте кредитные платежи и избегайте просрочек, '
                                      'чтобы избежать штрафных санкций и угрозы потери имущества.\n'
                     , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Карьерный рост")
def kariera(message):
    bot.send_message(message.chat.id, f'<b>Стратегии поиска работы:</b>\n'
                                      '1. Определите свои профессиональные цели и выберите '
                                      'соответствующую область деятельности.\n'
                                      '2. Составьте резюме и сопроводительное письмо, '
                                      'выделяющие ваши квалификации и достижения.\n'
                                      '3. Используйте различные ресурсы для поиска работы, '
                                      'включая онлайн-платформы, социальные сети, агентства '
                                      'по трудоустройству и конференции.\n'
                                      '4. Настраивайте оповещения о новых вакансиях, которые соответствуют '
                                      'вашим интересам и квалификациям.\n'
                                      '5. Подготовьтесь к собеседованиям, изучив информацию о компании, '
                                      'ее продуктах и услугах.\n'
                                      , parse_mode='html')
    bot.send_message(message.chat.id, f'<b>Стратегии ведения переговоров о зарплате:</b>\n'
                                      '1. Изучите уровень заработной платы в соответствующей отрасли и регионе.\n'
                                      '2. Определите минимальный уровень зарплаты, который вы готовы принять, '
                                      'и максимальную сумму, которую вы хотите получать.\n'
                                      '3. Подготовьтесь к диалогу с работодателем, чтобы убедительно '
                                      'представить свои достижения и квалификации.\n'
                                      '4. Обоснуйте свои требования, указав на свой опыт, '
                                      'специализацию и рыночные стандарты.\n'
                                      '5. Рассмотрите альтернативы, если работодатель не сможет предложить '
                                      'желаемый уровень заработной платы, например, возможности '
                                      'профессионального роста или другие бонусы.\n'
                                      , parse_mode='html')
    bot.send_message(message.chat.id, f'<b>Стратегии построения успешной карьеры:</b>\n'
                                      '1. Установите свои корпоративные цели и '
                                      'разработайте план действий для их достижения.\n'
                                      '2. Постоянно совершенствуйте свои профессиональные навыки, '
                                      'получая новые знания и подтверждения в виде сертификатов и лицензий.\n'
                                      '3. Найдите ментора или наставника, который поможет вам изучить отрасль, '
                                      'создать связи и расширить свои возможности.\n'
                                      '4. Проявляйте лидерские качества и общайтесь с коллегами, чтобы выстраивать '
                                      'отношения на основе доверия и уважения.\n'
                                      '5. Стремитесь к принятию ответственности за более сложные задачи и проекты, '
                                      'чтобы доказать свою ценность и получить возможности '
                                      'для профессионального роста.\n'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "⤝ Назад")
def back(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    fin_advice = types.KeyboardButton("Финансовый навигатор")
    bankcard_sec = types.KeyboardButton("Финансовая безопасность")
    back = types.KeyboardButton('⤝Вернуться в главное меню')
    murkup.add(fin_advice, bankcard_sec, back)
    bot.send_message(message.chat.id, 'Выберите желаемую категорию', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Финансовая безопасность")
def fin_sec(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    scheta = types.KeyboardButton('Счета')
    platezh = types.KeyboardButton('Онлайн платежи')
    dannie = types.KeyboardButton('Личные данные')
    bankomati = types.KeyboardButton('Использование банкоматов')
    kreditnistoria= types.KeyboardButton('Кредитная история')
    back = types.KeyboardButton('⤝ Назад')
    murkup.add(scheta, platezh, dannie, bankomati, kreditnistoria, back)
    bot.send_message(message.chat.id, f'<b>Финансовая безопасность</b> представляет собой '
                                      'сборник правил безопасности, которые могут '
                                      f'помочь Вам получить информацию об основных мерах защиты '
                                      'линчых данных или инструментов повседневго использвания, '
                                      , parse_mode='html')
    bot.send_message(message.chat.id, 'Выберите категорию совета:', reply_markup=murkup)


@bot.message_handler(func=lambda message: message.text == "Счета")
def scheta(message):
    bot.send_message(message.chat.id, f'<b>Есть несколько способов защитить свой банковский счет от мошенников:</b>\n'
                                      '1. Никогда не сообщайте свой пин-код, пароль или иные конфиденциальные '
                                      'данные по телефону, электронной почте или через социальные сети.\n'
                                      '2. Будьте внимательны при использовании общедоступных компьютеров и '
                                      'Wi-Fi сетей, чтобы избежать доступа к вашим персональным данным.\n'
                                      '3. Регулярно проверяйте свой банковский счет, чтобы быстро '
                                      'заметить любую подозрительную активность.\n'
                                      '4. Используйте сильные пароли и двухфакторную аутентификацию '
                                      'для защиты своих онлайн-аккаунтов, связанных с банковским счетом.\n'
                                      '5. Не отвечайте на подозрительные сообщения, которые запрашивают '
                                      'конфиденциальную информацию о вашем банковском счете.\n'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Онлайн платежи")
def platezh(message):
    bot.send_message(message.chat.id, f'<b>Несколько советов для безопасных онлайн платежей:</b>\n'
                                      '1. Используйте надежные и проверенные системы оплаты.\n'
                                      '2. Никогда не отправляйте свои личные данные или '
                                      'информацию о картах по электронной почте или сообщениям.\n'
                                      '3. Проверяйте URL-адрес сайта, чтобы убедиться, что он начинается '
                                      'с "https" и имеет зеленый значок замка.\n'
                                      '4. Используйте сложные пароли и активируйте двухфакторную аутентификацию.\n'
                                      '5. Будьте внимательны при открытии электронных писем и ссылок, '
                                      'особенно от незнакомых отправителей.\n'
                                      '6. Следите за вашими банковскими операциями и регулярно '
                                      'проверяйте свой банковский счет.\n'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Личные данные")
def dannie(message):
    bot.send_message(message.chat.id, f'<b>Чтобы избежать кражи личных данных при использовании '
                                      'банковских сервисов, необходимо принимать следующие меры:</b>\n'
                                      '1. Использовать надежный пароль и обновлять его периодически.\n'
                                      '2. Никогда не делиться своими учетными данными с посторонними.\n'
                                      '3. Использовать только безопасные подключения к Интернету '
                                      'при работе с онлайн-банком (SSL/TLS).\n'
                                      '4. Никогда не отвечать на электронные письма, которые запрашивают '
                                      'вашу конфиденциальную информацию.\n'
                                      '5. Не сообщайте свою основную электронную почту и номер телефона '
                                      'подозрительным личностям.\n'
                                      '6. Установить антивирусное программное обеспечение на свой '
                                      'компьютер и регулярно его обновлять.\n'
                                      '7. Проверять адрес веб-сайта банка перед вводом важной информации о себе.\n'
                                      '8. Используйте мессенджеры со сквозным шифрованием'
                                      '9. Проверьте настройки конфиденциальности в социальных сетях, '
                                      'исключите информацию которой может воспользоваться злоумышленник'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Использование банкоматов")
def bankomati(message):
    bot.send_message(message.chat.id, f'<b>Несколько основных принципов безопасности при '
                                      'использовании банкоматов:</b>\n'
                                      '1. Не давайте свой PIN-код другим людям и не записывайте '
                                      'его на карточку или в телефон.\n'
                                      '2. Проверяйте банкомат перед использованием на наличие подозрительных '
                                      'устройств или камер.\n'
                                      '3. Старайтесь использовать банкоматы в безопасных местах, например, внутри '
                                      'банковских отделений или супермаркетов.\n'
                                      '4. Закройте клавиатуру рукой при вводе PIN-кода, чтобы скрыть '
                                      'его от посторонних глаз.\n'
                                      '5. Не позволяйте никому помогать вам с использованием банкомата, если они не '
                                      'являются официальными представителями банка.\n'
                                      '6. Если вы заметили что-то подозрительное в работе банкомата, незамедлительно '
                                      'свяжитесь с банком и сообщите о проблеме.\n'
                                      , parse_mode='html')


@bot.message_handler(func=lambda message: message.text == "Кредитная история")
def kreditnistoria(message):
    bot.send_message(message.chat.id, f'<b>Как защитить свою кредитную историю от мошенников и ошибок банков?</b>\n'
                                      '1. Регулярно проверяйте свою кредитную отчетность на '
                                      'наличие ошибок и мошеннических действий.\n'
                                      '2. Защитите свои личные данные, такие как номера социального '
                                      'страхования и банковских счетов, от злоумышленников.\n'
                                      '3. Будьте внимательны при заполнении заявок на кредит и другие '
                                      'финансовые продукты, чтобы избежать ошибок.\n'
                                      '4. Если вы заметили ошибку или мошенническую активность, '
                                      'немедленно сообщите об этом своему банку или кредитному бюро.\n'
                                      '5. Установите пароли на свои банковские и финансовые аккаунты и не '
                                      'делитесь ими с никем.\n'
                                      '6. Поддерживайте свою кредитную историю в порядке и будьте бдительны '
                                      'для сохранения своих финансовых интересов.\n'
                                      , parse_mode='html')


bot.polling(non_stop=True)