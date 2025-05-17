# 📂 Древовидное меню на Django

Тестовое задание для Junior Python Backend Developer: реализовать древовидное меню с возможностью вложенности и подсветкой активного пункта.

---

## 🚀 Возможности

- Отображение древовидного меню с помощью `{% draw_menu 'menu_name' %}`
- Хранение меню в базе данных
- Редактирование через Django admin
- Подсветка активного пункта и автоматическое раскрытие родителей
- Поддержка нескольких меню на одной странице
- Только один SQL-запрос на меню
- Используется только Django и стандартная библиотека Python

---

## 🧱 Структура модели

Модель `MenuItem`:

- `title` — название пункта
- `url` — путь (например, `/about/`)
- `named_url` — альтернативно, путь по имени `url` из `urls.py`
- `parent` — родительский пункт меню (для вложенности)
- `menu_name` — имя меню (чтобы различать несколько меню на сайте)

---

## 🔧 Установка

```bash
git clone https://github.com/Kari230996/menu_project.git
cd menu_project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🧪 Тесты

```bash
python manage.py test
```

## 🗂 Пример пунктов меню в админке
| Название | URL          | Родитель | Название меню |
| -------- | ------------ | -------- | ------------- |
| Главная  | `/`          | —        | main\_menu    |
| О нас    | `/about/`    | —        | main\_menu    |
| Команда  | `/team/`     | О нас    | main\_menu    |
| Контакты | `/contacts/` | —        | main\_menu    |

## 📝 Автор
Разработано в рамках тестового задания Junior Python Backend Developer.
Связь: [karina.apaeva96@gmail.com]