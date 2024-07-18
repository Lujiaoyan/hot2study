'我的主页'

import streamlit as st

page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    with open('111.mp3','rb') as f:
        mymp3=f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.write("最爱的游戏")
    st.write(':green[我的世界]')
    st.image('down.jpeg')
    st.image('icon.png')

def page_2():
    pass

def page_3():
    pass

def page_4():
    pass

if page=='我的兴趣推荐':
    page_1()

if page=='我的图片处理工具':
    page_2()

if page=='我的智慧词典':
    page_3()

if page=='我的留言区':
    page_4()
