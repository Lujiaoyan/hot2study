'我的主页'

import streamlit as st

from PIL import Image

page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])
tab4,tab5,tab6=st.tabs(["最爱游戏","图片","音乐"])

def page_1():
    with tab4:
        st.write("最爱的游戏")
        st.write(':green[我的世界]')    
    with tab6:
        with open('111.mp3','rb') as f:
            mymp3=f.read()
        st.audio(mymp3,format="audio/mp3",start_time=0)
    with tab5:
        st.image('down.jpeg')
        st.image('icon.png')

def page_2():
    st.write(":sunglasses:图片/音频处理小程序：sunglasses")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg','gif'])
    uploaded_file1=st.file_uploader("上传音频mp3",type=['mp3'])

    if uploaded_file:
        img=Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img,0,2,1))
        tab1,tab2,tab3,tab4=st.tabs(["原图","改色001","改色002","改色003"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,0,2))
        with tab4:
            st.image(img_change(img,1,2,0))

def page_3():
    st.write("智慧词典")
    with open('words_space.txt',encoding='utf-8')as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')


    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]

    word=st.text_input("请输入查询单词：(里面有亿堆彩蛋)")
    if word in words_dict:
        st.write(words_dict[word])
        if word == 'mini' :
            st.code('''竟敢输入我最痛恨的游戏英文缩写！！！他是mc的敌对游戏''')
        if word == 'mc' :
            st.code('''这是mo款游戏缩写，猜猜它的全称吧''')
        if word == 'minecraft' :
            st.code('''恭喜你输入了我最爱的游戏我的世界的全称''')

        if word == 'unikun' :
            st.code('''请看下面''')
            st.image("1234.png")
        if word == 'zhangruixuan':
            st.balloons()
        if word== 'python':
            st.snow()

        if word== 'jietu4':
            st.image("jt4.png")

        if word =='mcupdate':
            st.image('114.png')
            

def page_4():
    pass

def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

if page=='我的兴趣推荐':
    page_1()

if page=='我的图片处理工具':
    page_2()

if page=='我的智慧词典':
    page_3()

if page=='我的留言区':
    page_4()
