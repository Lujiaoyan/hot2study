'''我的主页'''
import streamlit as s

page = s.sidebar.radio('我的首页',['我的小说','我的留言板'])

def page_1():
    
    with open('music.mp3','rb') as q:
        b = q.read()
    s.audio(b,format = 'audio/mp3',start_time = 0)

    with open('时间.txt',encoding='utf-8')  as f:    
        a = f.read()
    s.write(f':blue{a}')
    
def page_2():
    pass

if page == '我的小说':
    page_1()
elif page == '我的留言板':
    page_2()