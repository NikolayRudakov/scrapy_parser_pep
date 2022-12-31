# Асинхронный парсер информации о PEP

## 1. [Описание](#1)
## 2. [Запуск парсера](#2)
## 3. [Техническая информация](#3)
## 4. [Об авторе](#4)

---
## 1. Описание <a id=1></a>

Проект асинхронного парсера позволяет получать список всех PEP для Python
и информацию по статусам и количеству PEP, с записью полученной информации в файлы.

---
## 2. Запуск парсера <a id=2></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/NikolayRudakov/scrapy_parser_pep.git
SSH: git clone git@github.com:NikolayRudakov/scrapy_parser_pep.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

Для запуска парсера необходимо выполнить команду:
```bash
scrapy crawl pep
```

---
## 3. Техническая информация <a id=3></a>

Стек технологий: Python 3.8.0, Scrapy 2.5.1

Скачанная информация сохраняется в папке "results/" в файлах формата .csv с указанием даты и времени парсинга.

---
## 4. Об авторе <a id=4></a>

Рудаков Николай  
Python-разработчик плюс (Backend)  
E-mail: nrudakov@yandex.ru  
