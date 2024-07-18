'''我的主页'''
import streamlit as st

page = st.sidebar.radio('孙婧涵的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    st.write(':blue[①听音乐]')
    st.write('----------------------------'+'\n'+'最喜欢的歌：《love story》')
    with open('《love story》.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time = 0)

    st.write('----------------------------')
    st.write(':blue[②阅读]')
    st.write('----------------------------'+'\n'+'最喜欢的书：《简爱》')
    st.write('简介：《简·爱》是英国女作家夏洛蒂·勃朗特创作的具有自传色彩的长篇小说，于1847年10月首次出版。该小说讲述了失去父母的女孩简被庄园主人罗切斯特暗恋，在偶然得知罗切斯特是有妇之夫，而且还向她隐瞒了惊人真相后，简陷入了迷茫、挣扎、苦痛的故事。本书暴露和批判了西方资本主义社会黑暗面。')
    
    st.write('----------------------------')
    st.write(':blue[③旅行+拍照]')
    st.write('----------------------------'+'\n'+'北京之旅(天安门；天坛)')
    st.image('北京1.jpg')
    st.image('北京2.jpg')
    st.write('----------------------------'+'\n'+'恩施之旅(恩施大峡谷)')
    st.image('恩施.jpg')
    st.write('----------------------------'+'\n'+'长沙之旅(橘子洲)')
    st.image('长沙.jpg')
    st.write('还有许多其他的美丽城市哦~（=^.^=)')

    
def page_2():
    pass

def page_3():
    pass

def page_4():
    pass

if page == '我的兴趣推荐':
    page_1()

elif page == '我的图片处理工具':
    page_2()

elif page == '我的智慧词典':
    page_3()

elif page == '我的留言区':
    page_4()