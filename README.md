# Leyifan AutoSign V2 (乐淘一番自动签到)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Stable-green)

A robust automation script for Leyifan (乐淘一番) daily check-ins with **Auto-Login** support.

## 🚀 New Features in V2.2
* **Auto-Login**: Automatically retrieves a fresh Token using your credentials. No more manual packet sniffing!
* **Smart Retry**: Handles session expiration gracefully.
* **Domain Fix**: Corrected API endpoints to `api.mall.leyifan.cn`.

## 🛠️ Configuration

1. Open `main.py`.
2. Add your accounts to the list:
```python
accounts = [
    ("my_email@gmail.com", "my_password_123"),
    ("another_account@qq.com", "password_456")
]