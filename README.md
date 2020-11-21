# Яндекс Геймификация

[Ссылка на рабочую версию](http://yandex-gamification.std-884.ist.mospolytech.ru)

[Ссылка на Figma](https://www.figma.com/file/sM5uZE2Cl2Kc94G7qO5XtE/Ya.Game?node-id=1%3A15)

[Ссылка на схему БД](https://drive.google.com/file/d/12doNF7ebLjCgTaV6Uq4hnegJmZVonzlp/view?usp=sharing)

Доступные учетные записи

| Тип пользователя | Логин   | Пароль                |
| ---------------- | ------- | --------------------- |
| Админ            | YGAdmin | VeryStrongPassword123 |

# Установка

Для запуска на ПК должны быть установлены:
[Node.js](https://nodejs.org/);
[Yarn](https://yarnpkg.com/);
[Vue-CLI](https://cli.vuejs.org/guide/installation.html)
[Python 3.8](https://www.python.org/downloads/)

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
