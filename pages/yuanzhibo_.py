
import streamlit as st
from PIL import Image

'我的主页'

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])
def page_1():
    with open('天动万象.mp3', 'rb')as f:
        st.audio(f)
    tab1, tab2, tab3, tab4 = st.tabs(['我的电影推荐', '我的游戏推荐', '我的书籍推荐', '我的习题集推荐'])
    with tab1:
        st.write('         我的电影推荐')
        st.write('-----------------------------')
    with tab2:
        st.write('         我的游戏推荐')
        st.write('https://supermario-game.com/')
    with tab3:
        st.write('         我的书籍推荐')
        st.write('-----------------------------')
    with tab4:
        st.write('         我的习题集推荐')
        st.write('-----------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))

def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    #从本地文件中将词典信息读取出来，并存储在列表中
    with open('。com.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]= words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    word = st.text_input('请输入查询单词')
    if word in words_dict:
        st.write(words_dict[word])
def page_4():
    '''我的留言区'''
    pass
def img_change(img, rc , gc, bc):
    '''图片处理'''
    width,height =img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB
            r = img_array[x,y][rc]
            g= img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y]=(b,g,r)
    return img





if (page == '我的兴趣推荐'):
    page_1()
elif (page == '我的图片处理工具') :
    page_2()
elif (page == '我的智慧词典') :
    page_3()
elif (page == '我的留言区') :
    page_4()
else :
    pass
