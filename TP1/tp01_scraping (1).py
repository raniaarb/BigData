# type: ignore
import requests
from bs4 import BeautifulSoup
import pandas as pd

#  الرابط الأساسي للموقع
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

url = "https://books.toscrape.com/"
# إرسال طلب لجلب الصفحة
response = requests.get(url)

# طباعة كود HTML (المصدر)
print(response.text)


#  قائمة لتخزين كل العناوين
all_titles = []

#  حلقة تمر على كل الصفحات
for page in range(1, 51): 
    url = base_url.format(page)
    response = requests.get(url)
    
    # إذا لم يجد الصفحة (404)، نوقف الحلقة
    if response.status_code != 200:
        print(f" الصفحة {page} غير موجودة، تم التوقف.")
        break
    
    # تحليل الصفحة
    soup = BeautifulSoup(response.text, "html.parser")
    
    # استخراج كل العناصر <h3> التي تحتوي على عناوين الكتب
    books = soup.find_all("h3")
    
    # المرور على كل كتاب واستخراج العنوان
    for book in books:
        title = book.find("a")["title"]
        all_titles.append(title)
    
    print(f"✅ تم استخراج {len(books)} كتاب من الصفحة {page}")

#  إنشاء DataFrame وحفظ النتائج
df = pd.DataFrame({"Book Title": all_titles})
df.to_csv("all_books.csv", index=False)

print(f"\n تم استخراج {len(all_titles)} عنوان كتاب من جميع الصفحات!")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]  # التقييم مثل "One", "Two", "Three"...
    data.append({"Title": title, "Price": price, "Rating": rating})

# 6️⃣ تحويل القائمة إلى DataFrame
df = pd.DataFrame(data)

# 7️⃣ حفظ النتائج في ملف CSV
df.to_csv("books.csv", index=False, encoding="utf-8")

print("✅ Books data saved to books.csv")

