templates = {'forecast':'''Прогноз на 3 дня для *{place}*:
                        ''',
             'forecast_component': '''\n*{date}*:
\U000026C5 _Погода: _ *{weather}*
\U0001F321 _Температура: _ *{temp} °C*
\U0001F343 _Ветер: _ *{wind} м/с*
\U00002601 _Облака: _ *{clouds} %*
''',
             'geoposition': 'Отправь мне название или геопозицию местности, погода в которой тебя интересует',
             'help':
'''Если ты здесь, то ты не смог поладить со мной, но в этом нет ничего страшного \U0001F60A
Я могу прислать тебе погоду на данный момент и прогноз, для этого:
	1. Выбери на клавиатуре соответствующий пункт меню: \U000026C5 или \U0001F4C5
	2. Введи название города, который тебя интересует (в любом формате: Россия, Москва; Москва, Moscow)
Надеюсь, я смог тебе помочь \U0001F609
''',
             'info':
'''Интересует погода?
Просто отправь мне одну из этих команд:

- *Погода* \U000026C5 на текущую дату и время
- *Прогноз* \U0001F4C5 на следующие 3 дня
- *Помощь* \U00002753''',
             'weather':'''Погода на сегодня для *{place}*:

\U000026C5 _Погода: _ *{weather}*
\U0001F321 _Температура: _ *{temp} °C*
\U0001F343 _Ветер: _ *{wind} м/с*
\U00002601 _Облака: _ *{clouds} %*
''',
             'error':'''Место не найдено \U0000274C
Попробуй еще раз \U0001F609'''}