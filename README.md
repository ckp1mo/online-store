# online-store

Проект онлайн магазина на мото тематику(без возможности покупки:D). 
Представляет из себя веб-приложение с использованием framework django. 
Будет доробатываться по мере получения новых знаний в течении всего курса. (завершен)

Пару слов о веб приложении. 
Доступ к функционалу и просмотру закрыт для не авторизованного пользователя. Регистрация на сайте требует электронной почты
а так же, нужно ее подтвердить посредством ввода кода из письма. Пока не будет верифицирована почта пользователь будет
считаться не активным и доступ на сайт запрещен. После авторизации доступен предпросмотр контента.
Для полного просмотра контента требуются права на просмотр, эти права можно выдать администратором в админке. 
Так же можно выдать права на удаление, изменение, создание и сделать не активным продукт/запись. 
Автор контента имеет полный набор прав над своим контентом и может удалить, просмотреть, имзенить..

Итак, в проекте используется связка pip + venv, база данных postgresql, для кэширования данных используется redis.
Если вы здесь, то определенно знакомы с порядком действий для запуска проекта, но позвольте мне внести свои пять копеек. 
Для начала нужно: 
1. Клонировать проект себе на устройство.
2. Создать виртуальное окружение внутри проекта. (командой "python -m venv venv")
3. Установить зависимости проекта из файла requirements.txt. (команда "pip install -r requirements.txt")
4. Настройка проекта, установка переменых окружения в файле ".env".
   1. Для поля "CACHE_ENABLED=" устанавливаем значение True, чтобы кэшировать данные с использование redis, 
    в противном случае устанавливаем False.
   2. Для поля "USER_POSTGRESQL=" прописываем имя пользователя для бд postgresql, по умолчанию имя "postgres".
   3. Для поля "PASSWORD_POSTGRESQL=" прописываем ваш пароль для доступа к бд postgresql.
   4. Для поля "EMAIL_HOST_USER=" прописываем почту, с которой будет производиться отправка писем.
   5. Для поля "EMAIL_HOST_PASSWORD=" прописываем пароль.
   6. Я использую почтовый сервис от Yandex, и если у вас такой же, то дополнительно менять ничего не надо. 
      Иначе нужно заглянуть в config/settings.py на 136 и 137 строчку и изменить хост и порт при необходимости.
   7. Дополнительно при желании можно кэшировать весь сайт, если в файле config/settings.py раскомментировать 46 и 47 строки.
5. Запуск проекта.
   1. Произвести миграции "python3 manage.py migrate"
   2. Для начала неплохо бы создать администратора, ну почему бы и нет, командой "python3 manage.py create_su"
      Данные для входа в админку email: "admin@skystore.com", пароль: "qwerty321".
   3. По желанию наполнить сайт контентом с помощью фикстур.
      1. Наполнить каталог товаров "python3 manage.py loaddata catalog_data.json"
      2. Наполнить блог записями "python3 manage.py loaddata blog_data.json"
   4. Запуск сервера командой "python3 manage.py runserver" и попасть на него по адресу http://127.0.0.1:8000 .

Вот в принципе и все)