"'我的网络根据地'"
import streamlit as st

page = st.sidebar.radio("HOME PAGE", ['BOOK', "GAME", "COMPUTER", "TOOLBOX"])

def page_1():
    st.write(":blue[三体三部曲，你值得拥有]")
    st.image("《三体》纪念版封面.png")

def page_2():
    st.write("米家全家桶，仅需300GB！！！超实惠的有没有！！！")
    st.image("D:\workplace\营期\我的网络根据地\崩坏3 .png")
    st.image("原神.png")
    st.image("绝区零zzz.png")

def page_3():
    st.write("下面是一些我推荐的电脑，有电脑需求的考虑一下=）")
    st.write("联想：")
    st.write("    thinkpad t14p:https://www.thinkpad.com/device/ThinkPad-T14p-2023")
    st.write("    thinkbook 16p:https://www.thinkpad.com/device/thinkbook16-2023-i9?preview=true")
    st.write("    thinkbook 16+:https://www.thinkpad.com/device/ThinkBook16-jia-2023-kurui")
    st.write("ASUS:")
    st.write("    天选系列：")
    st.write("        天选5pro:https://www.asus.com.cn/laptops/for-gaming/tuf-gaming/asus-tuf-gaming-f16-2024/")
    st.write("    ROG系列：")
    st.write("        幻16:https://rog.asus.com.cn/laptops/rog-zephyrus/rog-zephyrus-g16-2023-series/")

def page_4():
    st.write("对你有帮助的书！")
    st.image(r"D:\workplace\营期\我的网络根据地\工具.jpg")


if page == 'BOOK':
    page_1()
elif page == 'GAME':
    page_2()
elif page == 'COMPUTER':
    page_3()
elif page == 'TOOLBOX':
    page_4()