import requests
import random
import time
import os
from bs4 import BeautifulSoup
import g4f

# 1. واجـهة الـبـوت (Banner) لـلـمـحـتـرفـيـن
def show_banner():
    os.system('clear') 
    print("""
    ###########################################
    #       AMI SECURITY - ULTIMATE BOT       #
    #    ---------------------------------    #
    #    [+] Developer: mimimido6678-wq       #
    #    [+] Features: AI Comments + Warmup   #
    #    [+] System: Android (Pydroid 3)      #
    ###########################################
    """)

# 2. مـحـرك الـذكاء الـاصـطـنـاعـي (AI Engine)
def generate_smart_comment(post_text):
    print("[*] الـذكاء الـاصـطـنـاعـي كـيـفـكّر فـتـعـلـيـق...")
    # طـلـب مـن الـ AI يـكـتـب بـالـدارجـة بـاش يـبـان بـنادم حـقـيـقـي
    prompt = f"Write a short, natural Moroccan Darija comment for this post: '{post_text}'"
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": prompt}],
        )
        return response
    except:
        return "تـبارك الله عـلـيـك خـويـا، مـنـشـور مـفـيـد! ✨"

# 3. الـمـاكـيـنة الـرئـيـسـيـة لـلـتـسـخـيـن والـقـنـص
def start_ami_engine(accounts_file, target_url):
    show_banner()
    
    # الـتأكد مـن وجـود مـلـف الـحـسابات
    if not os.path.exists(accounts_file):
        print(f"[!] غـلـط: مـلـف {accounts_file} مـا لـقـيـتـوش!")
        return

    try:
        with open(accounts_file, "r") as f:
            accounts = f.readlines()
            
        with open("results.txt", "a") as report:
            report.write(f"\n--- جـولـة جـديـدة ({time.ctime()}) ---\n")

            for line in accounts:
                if ',' not in line: continue
                email, password = line.strip().split(",")
                print(f"\n[🚀] جـاري تـشـغيل الـحساب: {email}")
                
                # اسـتـخدام Session بـاش نـحـافـظو عـلى الـتـواصل (Cookies)
                session = requests.Session()
                # اسـتـخدام قـناع (User-Agent) كـأنـنـا داخـليـن مـن أندرويد
                session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A205U)...'})

                try:
                    # مرحلة البحث عن منشورات جديدة (Scraping)
                    res = session.get(target_url, timeout=10)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    posts = soup.find_all('div', limit=2) # قـنص أول جـوج بـوسـتات
                    
                    for post in posts:
                        text = post.text[:60]
                        comment = generate_smart_comment(text)
                        print(f"   [🎯] تـم تـولـيد رد ذكي: {comment[:40]}...")
                        
                        # تـقـييد الـنـتـيـجة فـالـتـقـرير
                        report.write(f"{email} | Post: {text[:20]} | Comment: {comment}\n")
                        
                        # تـوقف بـشكل عـشوائي بـاش مـا يـعـيقـوش بـالـبوت
                        time.sleep(random.randint(15, 30))

                    print(f"[✔] تـم تـسـخـيـن {email} بـنـجاح.")
                except Exception as e:
                    print(f"[!] مـشـكـل فـالـوصـول لـلـرابط: {e}")
                
                # وقـت مـسـتـقـل بـين الـحـسابات (Anti-Ban)
                time.sleep(random.randint(30, 60))

    except Exception as e:
        print(f"[!] وقـع مـشـكـل عـام: {e}")

# 4. تـشـغـيل الـبـوت
if __name__ == "__main__":
    # حـط رابـط الـنـيـش ديـالـك (مـثلا مـجـموعة فـيـسـبـوك مـهـمّـة لـلـ CPA)
    niche_link = "https://m.facebook.com/groups/morocco_deals" 
    start_ami_engine("accounts.txt", niche_link)
