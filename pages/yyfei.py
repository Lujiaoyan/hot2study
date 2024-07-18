'''F的主页'''
import streamlit as st
page = st.sidebar.radio('F的首页',['F的兴趣推荐','F的图片处理工具','F的智慧词典','F的留言区'])

def page_1():
    st.write(':blue[F的兴趣推荐]')
    st.write(':blue[电影]')
    st.image('默杀.jpg')
    st.image('云边有个小卖部.jpg')
    st.write(':blue[音乐]')
    st.write(':blue[JYJ - BACK SEAT]')
    with open('JYJ - BACK SEAT (网友改编).mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time = 0)
    st.write(':blue[See You Later]')
    with open('GRAHAM - See You Later.mp3','rb')as f:
        mymp3_1 = f.read()
    st.audio(mymp3_1,format='audio/mp3',start_time = 0)
        
    
def page_2():
    pass
    
def page_3():
    pass
    
def page_4():
    pass
 
if page =='F的兴趣推荐':
    page_1()
elif page =='F的图片处理工具':
    page_2()
elif page =='F的智慧词典':
    page_3()
elif page =='F的留言区':
    page_4()
