# -*- coding: utf-8 -*-
"""
Leyifan Auto Sign-in Script V2.2
Updated: 2026-02-09
Features: 
  - Automatic Login (Token Refresh)
  - Domain Correction (api.mall.leyifan.cn)
  - 500 Error Handling for Duplicate Check-ins
"""

import requests
import time
import random

# ================= Configuration =================
# ⚠️ WARNING: Use Environment Variables or a local config file in production.
# DO NOT commit real passwords to GitHub!
accounts = [
    # Format: ("email/phone", "password")
    ("your_email_1@example.com", "your_password_1"),
    ("your_email_2@example.com", "your_password_2"),
]

# ================= Core Logic =================

def login_and_get_token(email, password, index):
    print(f"🔐 [Account {index}] Attempting auto-login...")
    
    # Official Login Endpoint
    login_url = "https://api.mall.leyifan.cn/api/front/login/leyifan"
    
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Origin": "https://letaoyifan.com",
        "Referer": "https://letaoyifan.com/",
        "Clientid": "cbdb7a7d-d6d8-4c2e-a398-534de34b449a6",
        "Appplatform": "other",
        "platform": "web"
    }
    
    payload = {
        "account": email,
        "password": password
    }
    
    try:
        resp = requests.post(login_url, json=payload, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("code") == 200 and "data" in data and "token" in data["data"]:
                token = data["data"]["token"]
                print(f"✅ [Account {index}] Login Success! Token refreshed.")
                return token
            else:
                print(f"❌ [Account {index}] Login Failed: {data.get('message')}")
        else:
            print(f"❌ [Account {index}] Network Error: {resp.status_code}")
    except Exception as e:
        print(f"❌ [Account {index}] Login Exception: {e}")
    return None

def sign_in(token, index):
    print(f"🚀 [Account {index}] Signing in...")
    
    # Corrected Endpoint for Sign-in
    sign_url = "https://api.mall.leyifan.cn/api/front/user/sign/integral"
    
    headers = {
        "Authori-zation": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Origin": "https://letaoyifan.com",
        "Referer": "https://letaoyifan.com/",
        "App-Version": "30361",
        "platform": "web"
    }
    
    try:
        # Note: API uses GET for write operation
        resp = requests.get(sign_url, headers=headers)
        
        if resp.status_code == 200:
            if "成功" in resp.text:
                print(f"✅ [Account {index}] Check-in Success! Points added.")
            else:
                print(f"ℹ️ [Account {index}] Response: {resp.text}")
        elif resp.status_code == 500:
            if "已签到" in resp.text:
                print(f"⚠️ [Account {index}] Already checked in today (Success).")
            else:
                print(f"❌ [Account {index}] Server Error: {resp.text}")
        else:
            print(f"❌ [Account {index}] Failed: {resp.status_code}")
            
    except Exception as e:
        print(f"❌ [Account {index}] Sign-in Exception: {e}")

# ================= Entry Point =================
if __name__ == "__main__":
    print(f"🤖 Leyifan Auto-Sign V2.2")
    
    for i, (email, pwd) in enumerate(accounts, 1):
        if "your_email" in email:
            print(f"⚠️ Skipping Account {i}: Please configure credentials.")
            continue
            
        token = login_and_get_token(email, pwd, i)
        if token:
            time.sleep(1)
            sign_in(token, i)
        
        if i < len(accounts):
            time.sleep(random.randint(3, 6))