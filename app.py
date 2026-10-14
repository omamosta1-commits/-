import streamlit as st
import cv2
import numpy as np
from datetime import datetime

# إعدادات صفحة لوحة التحكم
st.set_page_config(
    page_title="النظام الأمني الذكي للرصد والتحليل",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("إعدادات النظام الأمني")
app_mode = st.sidebar.selectbox("اختر القسم الرئيسي:", 
    ["لوحة الرصد المباشر والتحليل", "سجل الحوادث والتنبيهات", "إعدادات الذكاء الاصطناعي"])

st.sidebar.markdown("---")
st.sidebar.info("حالة النظام: متصل بالخادم الأمني 🟢")

# 1. قسم لوحة الرصد المباشر والتحليل المرتبط
if app_mode == "لوحة الرصد المباشر والتحليل":
    st.title("🛡️ لوحة الرصد المباشر والتحليل الذكي")
    st.markdown("نظام متكامل لكشف الأسلحة، المعادن، تعابير الوجه، والاشتباكات في الوقت الفعلي.")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("بث الكاميرا الحي مع التحليل")
        
        # زر تشغيل وإيقاف الكاميرا
        run_camera = st.checkbox("تشغيل بث الكاميرا الحي", value=False)
        camera_window = st.empty()

        if run_camera:
            # فتح الكاميرا الافتراضية
            cap = cv2.VideoCapture(0)
            
            while run_camera:
                ret, frame = cap.read()
                if not ret:
                    st.error("تعذر الوصول إلى الكاميرا الميدانية.")
                    break

                # --- [منطقة ربط نموذج الذكاء الاصطناعي] ---
                # هنا يتم تمرير الإطار (frame) إلى نموذج YOLO أو نماذج الرؤية الحاسوبية
                # مثال توضيحي لمعالجة الإطار:
                # results = yolo_model(frame)
                # frame = results.render() # رسم المربعات على الأسلحة أو الكائنات المكتشفة
                
                # كتابة تنبيه تجريبي على الشاشة مباشرة إذا تم رصد حدث
                cv2.putText(frame, "AI Monitoring Active - Safe", (30, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                # ----------------------------------------

                # تحويل الصورة من تنسيق OpenCV (BGR) إلى Streamlit (RGB)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                camera_window.image(frame, channels="RGB", use_container_width=True)
                
            cap.release()
        else:
            st.info("انقر على مربع 'تشغيل بث الكاميرا الحي' أعلاه لبدء المراقبة الميدانية.")

    with col2:
        st.subheader("⚠️ سجل التنبيهات الفورية")
        st.error("🚨 خطر: تم رصد حركة اشتباك في القطاع 02")
        st.warning("⚠️ تنبيه: رصد جسم معدني مشبوه في القطاع 01")
        st.success("🟢 استقرار عام في باقي القطاعات")

# 2. قسم سجل الحوادث
elif app_mode == "سجل الحوادث والتنبيهات":
    st.title("📋 سجل الحوادث والتحليلات التاريخية")
    
    data = {
        "التاريخ والوقت": [datetime.now().strftime("%Y-%m-%d %H:%M"), "2026-10-14 21:00"],
        "نوع التهديد المرصود": ["كشف سلاح / أداة حادة", "تعابير وجه تشير للهلع"],
        "مستوى الخطورة": ["حرج (عالي جداً)", "متوسط"],
        "القطاع": ["القطاع الشمالي", "القطاع الشرقي"],
        "الإجراء المتخذ": ["تم إطلاق الإنذار وتحويل البلاغ", "قيد المتابعة"]
    }
    st.dataframe(data, use_container_width=True)

# 3. إعدادات الذكاء الاصطناعي
elif app_mode == "إعدادات الذكاء الاصطناعي":
    st.title("⚙️ إعدادات النماذج وتحليل الرؤية")
    st.slider("حساسية نموذج كشف الأسلحة والمعادن (%)", 50, 99, 90)
    st.slider("حساسية نموذج رصد تعابير الوجه والاشتباكات (%)", 40, 95, 80)
    st.checkbox("تفعيل الإنذار الصوتي التلقائي عند الخطر", value=True)
    
    if st.button("حفظ إعدادات النماذج"):
        st.success("تم تحديث وتطبيق معايير الذكاء الاصطناعي بنجاح!")
