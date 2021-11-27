# Яндекс Геймификация

[Ссылка на рабочую версию](http://yandex-gamification.std-884.ist.mospolytech.ru)

[Ссылка на Figma](https://www.figma.com/file/sM5uZE2Cl2Kc94G7qO5XtE/Ya.Game?node-id=1%3A15)

[Ссылка на новую Figma](https://www.figma.com/file/3fkYWADZVM2hyMxWr6UwY0/%D1%80%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3?node-id=0%3A1)

[Ссылка на схему БД](https://drive.google.com/file/d/12doNF7ebLjCgTaV6Uq4hnegJmZVonzlp/view?usp=sharing)

Доступные учетные записи

| Тип пользователя | Логин   | Пароль                |
| ---------------- | ------- | --------------------- |
| Админ            | YGAdmin | VeryStrongPassword123 |
| Пользователь     | YGUser  | VeryStrongPassword123 |

# Установка

Для запуска на ПК должны быть установлены:
[Node.js](https://nodejs.org/);
[Yarn](https://yarnpkg.com/);
[Vue-CLI](https://cli.vuejs.org/guide/installation.html);
[Python 3.8](https://www.python.org/downloads/);
[Git](https://git-scm.com/);

Склонируйте репозиторий

```sh
$ git clone https://github.com/nikita220800/DjangoVueApp.git
```

### 1) Настройка Django

В корне проекта создайте виртуальное окружение и активируйте его

```sh
$ python -m venv “venv”
$ .\venv\Scripts\activate (для Linux: source ./venv/bin/activate)
```

#### Все последующие действия производить внутри виртуального окружения

Установите все необходимые зависимости для работы Django

```sh
$ pip install -r requirements.txt
```

#### В папке core скопируйте файл .env.example в .env

Установите все необходимые миграции, убедитесь, что был создан файл db.sqlite3

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Создайте суперпользователя для работы с админкой

```sh
$ python manage.py createsuperuser
```

Запустите проект

```sh
$ python manage.py runserver
```

### 2) Настройка Vue

Из корня проекта перейдите в папку frontend и сделайте установку необходимых зависимостей

```sh
$ cd ./frontend/
$ yarn install
```

Создайте файлы .env.production и .env.development и введите эти значения

```sh
Время жизни access токена (в минутах)
VUE_APP_ACCESS_TOKEN_EXPIRES=
Ссылка на backend api
API_BASE_URL=
Для development
API_BASE_URL=http://127.0.0.1:8000
Для production
API_BASE_URL=ссылка на рабочую версию
```

Убедитесь, что в редакторе (если у вас VS Code) установлены:
[Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode);
[ESlint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

Запустите проект

```sh
$ yarn serve
```

(Django и Vue нужно запускать в отдельных терминалах)

#### Перед загрузкой на github

Если вы устанавливали новые зависимости в Django, то сохраните их в requirenments.txt

```sh
$ pip freeze > requirements.txt
```
