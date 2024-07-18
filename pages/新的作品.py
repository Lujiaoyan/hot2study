def page_1():
    pass

def page_2():
    pass

def page_3():
    pass

def page_4():
    pass


import streamlit as st

'我的主页'

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

if (page == '阿短的兴趣推荐'):
    page_1()
elif (page == '阿短的图片处理工具') :
    page_2()
elif (page == '阿短的智慧词典') :
    page_3()
elif (page == '阿短的留言区') :
    page_4()
else :
    pass

with open('天动万象.mp3', 'rb')as f:
