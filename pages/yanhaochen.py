'''我的主页'''
import streamlit as s
from PIL import Image
import numpy as np
import random as r

e = []

page = s.sidebar.radio('我的首页',['我的小说','我的图片处理工具','我的词典','我的留言板'])

def page_1():
    
    with open('music.mp3','rb') as q:
        b = q.read()
    s.audio(b,format = 'audio/mp3',start_time = 0)

    with open('时间.txt',encoding='utf-8')  as f:    
        a = f.read()
    s.write(f':blue{a}')

    img1= Image.open('星空.png')
    s.image(img1)
    
def page_2():
    s.write(':sunglasses:图片换色小程序:sunglasses:')
    uploaded = s.file_uploader('上传图片',type = ['png','jpg','jpeg'])
    if uploaded:
        img= Image.open(uploaded)
        s.image(img)
        tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = s.tabs(['原图','改图1','改图2','改图3','改图4','改图5','改图6','改图7'])
        with tab1:
            s.image(img_change(img,0,1,2))
        with tab2:
            s.image(img_change(img,1,0,2))
        with tab3:
            s.image(img_change(img,1,2,0))
        with tab4:
            s.image(img_change(img,1,2,1))
        with tab5:
            s.image(img_change(img,2,2,1))
        with tab6:
            s.image(img_change(img,2,2,1))
        with tab7:
            s.image(img_change(img,0,2,2))
        with tab8:
            s.image(img_change(img,2,0,0))

def page_3():
    s.write('词典')
    with open('words_space.txt',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
        
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]

    word = s.text_input('请输入要查询的单词')
    if word in words_dict:
        if word != 'yuexiahanshuang':
            s.write(words_dict[word])
        else:
            s.write(words_dict[word])
            img1= Image.open('星空1.png')
            s.image(img1)
            s.code('别告诉别人哦~~')
            s.snow()

def page_4():
    pass

def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img

if page == '我的小说':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的词典':
    page_3()
elif page == '我的留言板':
    page_4()
