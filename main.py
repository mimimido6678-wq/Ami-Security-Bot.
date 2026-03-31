import requests  # 1. الـسـربـاي (لـي كـيـدق فـالـبـاب)
import random    # 2. مـول الـقـرعة (لـي كـيـخـتـار الـقـناع)
import time      # 3. الـمـكـلّـف بـالـوقـت (بـاش نـرتـاحـو)

# --- الـخـزنة ديـال الـأقـنـعـة (The Vault) ---
aqni3a = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", 
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)", 
    "Mozilla/5.0 (Linux; Android 14; SM-S918B)"
]

print("--- بـداية تـشـغـيل Ami-Security-Bot ---")

# --- الـمـاكـينة لـي مـا كـتـحـبـسـش (The Loop) ---
while True:
    # أ. الـقـرعة: هـز قـناع واحـد بـالـزهر
    qina3_lyoum = random.choice(aqni3a)
    
    # ب. الـكـسـوة: لـبـس الـبوت الـقـناع (Headers)
    kiswa = {
        "User-Agent": qina3_lyoum
    }
    
    # ج. الـهـجـوم: دق عـلى الـمـوقع (مـثـلا غـوغل بـاش نـجـربـو)
    try:
        talab = requests.get("https://www.google.com", headers=kiswa)
        
        # د. الـنـتـيـجة: طـبـع أش واقـع فـالـشـاشة الـسـوداء
        print(f"[*] الـقـناع لـي مـخـدمـيـن: {qina3_lyoum[:30]}...")
        print(f"[*] جـواب الـمـوقـع (Status): {talab.status_code}")
        
        if talab.status_code == 200:
            print("[+] الـبـاب مـحـلـول! الـبـوت خـدام بـنـجـاح.")
        else:
            print("[-] الـعـسّـاس عـاق بـيـنا.. جـرّب قـناع آخـر.")
            
    except:
        print("[!] كـايـن مـشـكـل فـالـكـونـيـكـسـيـون!")

    # هـ. الـراحـة: تـسـنّى 2 ثـوانـي بـاش نـبـانـو بـنـادم
    print("---------------------------------")
    time.sleep(2)
