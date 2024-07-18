'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的主页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    st.write(":blue[我的兴趣推荐]")
    st.image("猫.png")

def page_2():
    st.write(":blue[我的图片处理工具]")

def page_3():
    st.write(":blue[我的智慧词典]")

def page_4():
    st.write(":blue[我的留言区]")


if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()