import requests
import random
import time

def warmup_factory(file_path):
    print(f"--- [ 🚀 بـداية مـصـنع الـتسخين Ami-Security ] ---")
    
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            email, password = line.strip().split(',')
            print(f"\n[*] جـاري الـتـواصل مـع الـحساب: {email}")
            
            # --- هـنا كـتـكـون عـملية الـربط بـفـيسبوك (Requests) ---
            session = requests.Session()
            session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A205U)...'})
            
            # مـحاكاة الـتـسخين (سكرول وتفاعل)
            for i in range(1, 4):
                wait = random.randint(5, 12)
                print(f"   - الـخـطوة {i}: الـبوت كـيـتـحرّك.. تـسنى {wait} ثـانية.")
                time.sleep(wait)
                
            print(f"[✔] الـحساب {email} سـخـان ونـاضـي!")
            
            # تـسـنّى شـويّة قـبل مـا تـدوز لـلـحساب لـي مـوراه بـاش مـا يـعـيقـوش بـيك
            time.sleep(random.randint(10, 20))

    except FileNotFoundError:
        print("[!] الـغـلـط: مـلـف accounts.txt مـا لـقـيـتـوش!")
    except Exception as e:
        print(f"[!] وقـع مـشـكل: {e}")

# تـخديـم الـمـصـنع
warmup_factory("accounts.txt")
