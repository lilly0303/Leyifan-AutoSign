# -*- coding: utf-8 -*-
import requests
import time
import random

# ================= 配置区 (Configuration) =================
# ⚠️ 请在下方填入你的 Authori-zation Token
# 获取方式: F12 -> Network -> 刷新页面 -> 找到 user 或 integral 请求 -> 复制 Request Headers 里的 Authori-zation
tokens = [
    "这里填入第一个账号的Token",
    "这里填入第二个账号的Token",
    # 可以无限添加...
]

# ================= 核心逻辑 (Core Logic) =================
def run_sign_in(token, index):
    print(f"\n🚀 [Account {index}] Start processing...")

    # 目标接口 (GET 请求)
    url = "https://api.mall.leyifan.com/api/front/user/sign/integral"

    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "App-Version": "30822",
        "Appplatform": "other",
        # 核心鉴权字段
        "Authori-zation": token,
        "Clientid": "2ce0790a-b7cf-4649-b970-5ec985bf07344",
        "Connection": "keep-alive",
        "Origin": "https://mall.leyifan.com",
        "Referer": "https://mall.leyifan.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "lang": "chs",
        "platform": "h5",
        "system": "windows"
    }

    try:
        # 随机延时 (Jitter)，防止并发风控
        delay = random.randint(2, 5)
        print(f"⏳ Waiting for {delay} seconds...")
        time.sleep(delay)

        # 发送请求
        response = requests.get(url, headers=headers)

        # 结果判定
        # 注意: 乐淘一番后端在重复签到时会返回 500 错误，这是正常的业务逻辑
        if response.status_code == 200:
            if "操作成功" in response.text:
                print(f"✅ [Account {index}] 签到成功 (Success)!")
                print(f"📝 {response.text}")
            else:
                print(f"ℹ️ [Account {index}] 状态正常: {response.text}")
        elif response.status_code == 500:
            if "已签到" in response.text:
                print(f"⚠️ [Account {index}] 今日已签到 (Already checked in).")
            else:
                print(f"❌ [Account {index}] 服务器错误: {response.text}")
        else:
            print(f"❌ [Account {index}] 未知错误: {response.status_code}")

    except Exception as e:
        print(f"❌ [Account {index}] 脚本执行报错: {e}")

# ================= 入口 (Main) =================
if __name__ == "__main__":
    print(f"📋 Loaded {len(tokens)} accounts.")
    print("-----------------------------------")
    
    for i, token in enumerate(tokens, 1):
        if "这里填" in token or len(token) < 10:
            print(f"⚠️ [Account {i}] Token 无效，请检查配置。")
            continue
            
        run_sign_in(token, i)
        
    print("\n🎉 All tasks completed.")
    # input("Press Enter to exit...") # 配合 Windows 任务计划程序时请注释此行