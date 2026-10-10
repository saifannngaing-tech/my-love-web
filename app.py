import streamlit as st
st.set_page_config(page_title="My Love 💖", page_icon="💝", layout="centered")
st.title("ချစ်သူလေးဖတ်ဖို့... 💌")
st.balloon_state = st.balloons()
st.subheader("ကို မင်းကို အရမ်းချစ်တယ်နော်... 💖")
st.write("ဒီကမ္ဘာပေါ်မှာ မင်းက ကိုယ့်အတွက် အလိုအပ်ဆုံးနဲ့ အချစ်ရဆုံးလူသားလေးပါ။")

st.write("---")
st.write("### ကိုယ့်ကို ပြန်ချစ်လား? 🥺")

col1, col2 = st.columns(2)

with col1:
    if st.button("💘 ချစ်တာပေါ့"):
        st.balloons() # ခလုတ်နှိပ်ရင် ပူဖောင်းထပ်တက်မယ်
        st.success("ဟေး! ကိုလည်း မင်းလေးကို အမြဲတမ်း ပိုပိုပြီး ချစ်သွားမှာပါ အသည်းလေးရေ 🥰✨")

with col2:
    if st.button("❌ မချစ်ဘူး"):
        st.error("ဟာ... စိတ်မကောင်းလိုက်တာ 😢 (ဒါပေမဲ့ ကိုကတော့ အတင်းလိုက်ချစ်နေမှာပဲ ဟွန့်!)")
