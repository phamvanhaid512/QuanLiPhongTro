# Dự án Quản Lý Phòng Trọ Django

## 1. Giới thiệu

Đây là dự án Web API quản lý phòng trọ được xây dựng bằng Python và Django.
Hệ thống hỗ trợ quản lý các nghiệp vụ cơ bản như tài khoản, phòng trọ, người thuê, hợp đồng, dịch vụ, chỉ số dịch vụ và hóa đơn.

Dự án sử dụng mô hình phân lớp gồm:

* Controller: tiếp nhận request từ client
* Service: xử lý nghiệp vụ
* Model: ánh xạ dữ liệu với database
* Utils: hỗ trợ response, phân quyền, serialize dữ liệu

---

## 2. Công nghệ sử dụng

* Python
* Django
* MySQL / MariaDB thông qua XAMPP
* Django ORM
* PowerShell
* Postman hoặc trình duyệt để test API

---

## 3. Cấu trúc thư mục chính

```text
DoAnPyThon/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── app/
│   ├── models.py
│   ├── urls.py
│   ├── controllers/
│   ├── services/
│   ├── utils/
│   └── migrations/
│
└── project/
    ├── settings.py
    └── urls.py
```

Tên thư mục có thể thay đổi tùy theo tên app trong project.

---

## 4. Cài đặt project

### Bước 1: Clone project

```powershell
git clone <link-repository>
cd DoAnPyThon
```

### Bước 2: Tạo môi trường ảo

```powershell
python -m venv .venv
```

Kích hoạt môi trường ảo:

```powershell
.venv\Scripts\activate
```

### Bước 3: Cài thư viện

```powershell
pip install -r requirements.txt
```

---

## 5. Cấu hình database MySQL XAMPP

Mở XAMPP và Start MySQL.

Đăng nhập MySQL bằng root:

```powershell
& "C:\xampp\mysql\bin\mysql.exe" -u root
```

Tạo database và user:

```sql
CREATE DATABASE IF NOT EXISTS quanlyphongtro_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'qlpt_user'@'localhost' IDENTIFIED BY '123456';

GRANT ALL PRIVILEGES ON quanlyphongtro_db.* TO 'qlpt_user'@'localhost';

FLUSH PRIVILEGES;
```

---

## 6. Cấu hình Django database

Trong file `settings.py`, cấu hình:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quanlyphongtro_db',
        'USER': 'qlpt_user',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Nếu MySQL XAMPP chạy port `3307`, đổi:

```python
'PORT': '3307'
```

---

## 7. Chạy migration

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

## 8. Chạy server

```powershell
python manage.py runserver
```

Sau khi chạy thành công, truy cập:

```text
http://127.0.0.1:8000/
```

---

## 9. Test API

Ví dụ gọi API danh sách tài khoản:

```http
GET /api/accounts/
Authorization: Token <token>
```

Một số API yêu cầu token đăng nhập và quyền phù hợp.

---

## 10. Ghi chú

* Không upload thư mục `.venv` lên GitHub.
* Không upload file database cục bộ.
* Khi tải project về máy khác, cần tạo lại database và chạy migration.
* Có thể dùng Postman để test các API.
