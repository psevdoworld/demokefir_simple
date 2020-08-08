# demokefir_simple
#### Задание было следующим:
>*Сервис на python, планировщик задач по экспорту статей с сайта habr.ru.  Несколько раз в день ежедневно (конкретные временные точки не принципиальны), просыпается джоб,  вытаскивает из json-файла (формат файла произвольный) список URL со статьями для экспорта, затем получает их посредством get-запроса, парсит ответ, сохраняет в базу текст статьи, засыпает.  http-запросы необходимо выполнять асинхронно (asyncio/aiohttp или производные). Отсутствуют ограничения на использование библиотек.*

я зацепился за слово сервис и провозился большую часть времени, собирая апи и клиент к нему. Наконец поняв, что занимаюсь совсем не тем, и попросту закапываюсь - решил быстро собрать прототип, который берет данные из json и отдает их в БД.

В качестве БД была выбрана postgresql и работу начал снизу.

Сначала был utils.py в который постепенно собирался функционал и выносился в другие файлы, его же и запускал при разработке и отладке. В итоге он работает с json, а также запускает код на тестовой выборке, как маленький кусочек легаси.

Затем нырнул в aiohttp. До этого никогда не работал с ней, но опыт асинхронной магии есть по комплексным проектам. Невольно даже вспомнились несколько библиотек для фронта и мобильной разработки, где тоже было весело. 

К сожалению, работа с aiohttp ограничилась сборкой кода из гайдов и легкой допилкой их напильником. Весь код в aiohttp_stuff.py.

В функции fetch несколько неловко вызывается парсинг, тоже взятый откуда-то, он на bs4, с которым у меня не очень много опыта (коллега любил такие задачи) но я справился.

Далее полученные странички возвращаются в главный файл, где превращаются в список и отправляются в бд.

Работа с БД получилась также несколько неловкой, ибо до этого я работал с БД только через инструменты Django или Flask, потому я не стал сильно усложнять себе задачу и собрал код по туториалам psycopg2
Этот код можно найти в файле db_stuff.py. Код я не чистил, но честно скажу что мною там написанно скорее всего только SQL запросы.

Запускается это все в файле main.py

Для запуска же всего несколько раз в день использовал crontab
получилось больно. а результат вот такой:
0 1,13 * * * env -i bash -c 'export WORKON_HOME=~/.virtualenvs && source ~/.virtualenvs/demokefir/bin/activate && cd  ~/dev/demokefir_simple/ && ~/.virtualenvs/demokefir/bin/python3 ~/dev/demokefir_simple/main.py' >> log.txt 2>&1

Для запуска понадобится создать БД и пользователя, я делал это через psql. данные надо будет записать в database.ini.
в файле requirements.txt есть куча библиотек, часть из которых нужны. Решил не делать dry run, чтобы выяснить что точно нужно и уточнить инструкцию по запуску, но если нужно - могу.
что насчет crontab - тут все сильно зависит от того как вы будете ставить. Как можете видеть, любовь к виртуальным окружениям дорого мне обошлась.
