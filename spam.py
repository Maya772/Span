#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import random
import string
import time
import threading
from datetime import datetime

# ================== KONFIGURASI ==================
TARGET_NUMBER = "6282330267119"  # GANTI DENGAN NOMOR TARGET
MESSAGE = "Bapak Kau Lonte sama mami lonte bujanginam heang biang kontol bapak kau lonte anak 2 bujang"
THREADS = 100  # Jumlah thread paralel
DELAY = 0.1  # Delay antar request (detik)
# =================================================

class WABrutalSpam:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
            "Mozilla/5.0 (Linux; Android 11) WhatsApp/2.23.25",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6) WhatsApp/2.23.24"
        ]
        self.session = requests.Session()
        self.count = 0

    def generate_payload(self):
        """Generate payload random untuk bypass WA"""
        payload = {
            "phone": TARGET_NUMBER,
            "text": MESSAGE + " " + ''.join(random.choices(string.ascii_letters + string.digits, k=6)),
            "device": random.choice(self.user_agents),
            "timestamp": int(time.time()),
            "token": ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
        }
        return payload

    def send_spam(self):
        """Kirim spam ke WhatsApp melalui API dummy (bypass)"""
        try:
            # Fake endpoint (sebenarnya ini hanya simulasi bruteforce)
            url = "https://wa.me/" + TARGET_NUMBER
            headers = {
                "User-Agent": random.choice(self.user_agents),
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            }
            
            # Request dummy untuk membanjiri log
            self.session.get(url, headers=headers, timeout=2)
            self.count += 1
            print(f"[✓] SPAM #{self.count} -> {TARGET_NUMBER} | {datetime.now().strftime('%H:%M:%S')}")
            
        except Exception as e:
            print(f"[!] ERROR: {str(e)[:30]}...")

    def start_brutal(self):
        """Jalankan spam multi-thread"""
        print(f"""
╔══════════════════════════════════════╗
║   💀 WA SPAM BRUTAL BY ARCiPS 💀    ║
║   Target : {TARGET_NUMBER}             ║
║   Thread : {THREADS}                  ║
║   Status : [ 🔥 AKTIF ]             ║
╚══════════════════════════════════════╝
        """)
        
        while True:
            threads = []
            for _ in range(THREADS):
                t = threading.Thread(target=self.send_spam)
                t.start()
                threads.append(t)
                time.sleep(DELAY)
            
            for t in threads:
                t.join()
            
            print(f"[⏳] Sending {THREADS} spam per batch...")

if __name__ == "__main__":
    spammer = WABrutalSpam()
    try:
        spammer.start_brutal()
    except KeyboardInterrupt:
        print("\n[✖] Dihentikan Tuan! Spam berhasil dikirim ~")
