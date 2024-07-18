'''我的主页'''
import streamlit as st

page  = st.sidebar.radio('我的首页', ['我的兴趣推荐','我的游戏推荐','我的智慧词典','我的留言区'])

def page_1():
    with open('萌果果大大 - Track in time.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write(':blue[跑步，哦豁豁]')
    st.image("跑步.png")
    pass
    
def page_2():
    with open('猫鼠主题曲.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write(':red [经典改编]')
    st.image("猫鼠.jpg")
    pass
    
def page_3():
    st.write('常用单词')
    st.image("单词.jpg")
    pass
    
def page_4():
    st.write(':red[留言]')
    pass

if page =='我的兴趣推荐':
    page_1()
elif page == '我的游戏推荐':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()