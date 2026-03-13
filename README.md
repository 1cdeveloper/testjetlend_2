### Импорт рассылок из XLSX и отправка писем

Этот проект реализует Django‑команду для импорта рассылок из XLSX‑файла и последующей отправки писем (эмулируется задержкой и записью в лог).

#### Требования

- **Python**: 3.10+
- **Django**: 4.2+
- **База данных**: SQLite 

#### Установка и запуск

1. **Клонировать репозиторий**

```bash
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd testjetlend_2
```

2. **Создать виртуальное окружение и установить зависимости**

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. **Применить миграции**

```bash
python manage.py makemigrations mailings
python manage.py migrate
```

4. **Запустить импорт**

```bash
python manage.py import_mailings path\to\file.xlsx
```

Где `file.xlsx` содержит колонки:

- `external_id`
- `user_id`
- `email`
- `subject`
- `message`

Первая строка — заголовки колонок.

#### Пример вывода команды

```text
Начинаю обработку файла: path\to\file.xlsx

Импорт завершён.
Количество обработанных строк: 10
Количество созданных записей: 8
Количество пропущенных записей: 1
Количество ошибочных строк: 1
```

#### Тесты

```bash
pytest
```

