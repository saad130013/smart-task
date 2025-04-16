
import streamlit as st
from database import init_db, add_task, get_tasks
from ai_classifier import classify_task_text

st.set_page_config(page_title="نظام المهام الذكي", layout="centered")
st.title("🧠 نظام إدارة المهام بالذكاء الاصطناعي")

init_db()

with st.form("task_form"):
    title = st.text_input("عنوان المهمة")
    description = st.text_area("وصف المهمة")
    submitted = st.form_submit_button("➕ إضافة المهمة")

    if submitted:
        if title.strip():
            add_task(title, description)
            st.success("✅ تم حفظ المهمة بنجاح")
        else:
            st.warning("⚠️ العنوان مطلوب")

if st.button("🤖 اقتراح تصنيف بناءً على الوصف"):
    if description.strip():
        label, score = classify_task_text(description)
        st.info(f"التصنيف المقترح: {label} (دقة: {score:.2f})")
    else:
        st.warning("⚠️ يرجى إدخال وصف المهمة أولاً")

st.subheader("📋 قائمة المهام")
tasks = get_tasks()
for t in tasks:
    st.markdown(f"- **{t.title}**: {t.description}")
