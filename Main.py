import requests
import random
import time
import os
from bs4 import BeautifulSoup
import g4f

# 1. واجـهة الـمبـرمـج الـمـحـتـرف (Banner)
def show_banner():
    os.system('clear') 
    banner = """
    ###########################################
    #       AMI SECURITY - ULTIMATE BOT       #
    #    ---------------------------------    #
    #    [+] Dev: mimimido6678-wq             #
    #    [+] Task: Warmup + AI Scraper        #
    #    [+] Status: Undetectable / Private   #
    ###########################################
    """
    print(banner)

# 2. مـحرك الـذكاء الاصـطـنـاعي لـلـتـعـلـيـقـات
def generate_ai_comment(post_text):
    print("[*] الـذكاء الاصـطـنـاعي كـيـحـلل الـمـنـشور...")
    prompt = f"Write a short, engaging comment in Moroccan Darija for this FB post: '{post_text}'. Keep it natural."
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": prompt}],
        )
        return response
    except:
        return "تـبارك الله عـلـيك خـويـا، مـنشور فـالـمستوى! ✨"

# 3. مـاكـيـنـة الـتـسـخـيـن والـتـنـقـيـب (The Engine)
def start_ami_engine(accounts_file, niche_url):
    show_banner()
    
    try:
        with open(accounts_file, "r") as f:
            accounts = f.readlines()
            
        with open("results.txt", "a") as report:
            report.write(f"\n--- جـولـة جـديـدة ({time.ctime()}) ---\n")

            for line in accounts:
                email, password = line.strip().split(",")
                print(f"\n[🚀] الـدخـول لـلـحساب: {email}")
                
                # إعـدادات الـحصة (Session) بـقـناع مـتـغـير
                session = requests.Session()
                ua = "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36..."
                session.headers.update({'User-Agent': ua})

                # محاكاة تسجيل الدخول (Simulation)
                time.sleep(random.randint(5, 10))
                
                # --- مـرحـلـة الـتـنـقـيـب عـن مـنـشـورات Fresh ---
                print(f"[*] الـبحث عـن أهداف فـي: {niche_url}")
                res = session.get(niche_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                
                # جـمع الـروابط لـي عـاد تـحطّات
                posts = soup.find_all('div', limit=3) # نـاخدو أول 3 بـوسـتات
                
                for post in posts:
                    post_text = post.text[:50] # نـاخدو طـرف مـن الـهدرة بـاش يـفـهمها الـ AI
                    smart_comment = generate_ai_comment(post_text)
                    
                    print(f"   [🎯] تـم تـوليد تـعليق ذكي: {smart_comment[:30]}...")
                    
                    # تـقـييد الـنـتـيجة فـالـتـقـرير
                    report.write(f"{email} | Post: {post_text[:20]} | Comment: {smart_comment}\n")
                    
                    # تـوقـف عـشـوائـي بـاش مـا يـعـيـقـوش بـيـنا
                    time.sleep(random.randint(15, 30))

                print(f"[✔] تـم تـسـخـيـن الـحـساب {email} بـنـجاح.")
                time.sleep(random.randint(20, 40)) # وقـت بـين حـساب وحـساب

    except Exception as e:
        print(f"[!] خـطأ فـالـتـنـفـيـذ: {e}")

# 4. تـشـغـيـل الـمـنـظـومـة
if __name__ == "__main__":
    # حـط رابـط الـصـفـحـة لـي بـغـيـتـي تـسـتـهـدفـهـا هـنـا
    target_niche = "https://m.facebook.com/groups/gaming_morocco" 
    start_ami_engine("accounts.txt", target_niche)
