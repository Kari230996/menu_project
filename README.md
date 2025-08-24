# 📂 Tree Menu in Django

Test task for Junior Python Backend Developer: implement a tree-like menu with nesting support and highlighting of the active item.

---

## 🚀 Features

* Display a tree menu using `{% draw_menu 'menu_name' %}`
* Store menus in the database
* Edit through Django admin
* Highlight active item and automatically expand parent items
* Support multiple menus on one page
* Only one SQL query per menu
* Uses only Django and Python standard library

---

## 🧱 Model Structure

Model `MenuItem`:

* `title` — item name
* `url` — path (e.g., `/about/`)
* `named_url` — alternatively, path by `url` name from `urls.py`
* `parent` — parent menu item (for nesting)
* `menu_name` — menu name (to distinguish multiple menus on the site)

---

## 🔧 Installation

```bash
git clone https://github.com/Kari230996/menu_project.git
cd menu_project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🧪 Tests

```bash
python manage.py test
```

---

## 🗂 Example Menu Items in Admin

| Title    | URL          | Parent | Menu Name  |
| -------- | ------------ | ------ | ---------- |
| Home     | `/`          | —      | main\_menu |
| About    | `/about/`    | —      | main\_menu |
| Team     | `/team/`     | About  | main\_menu |
| Contacts | `/contacts/` | —      | main\_menu |

---

## 📝 Author

Developed as part of a test task for Junior Python Backend Developer.
Contact: [karina.apaeva96@gmail.com](mailto:karina.apaeva96@gmail.com)
