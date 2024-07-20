'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的主页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    st.write(":blue[我的兴趣推荐]")
    tab1,tab2,tab3 = st.tabs(['动物推荐', '游戏推荐', '水果推荐'])
    with tab1:
        st.image("猫.png")
    with tab2:
        st.image("gy.jpg")
    with tab3:
        st.image("蓝莓.jpg")
        

def page_2():
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原图', '改色1', '改色2', '改色3',])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
        
def page_3():
    st.write(":blue[智慧词典]")
    with open('words_space.txt',encoding='utf-8')as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')

    words_dict = {}
    for i in word_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    
    word = st.text_input('请输入查询单词')

    if word in words_dict:
        st.write(words_dict[word])
        if word == 'python':
            st.balloons()
            st.code('''
                    #恭喜你触发彩蛋，这是一行python代码
                    print('hello world!')
                    ''')
        if word == 'xingsiyue':
            st.snow()
        if word == 'ikun':
            st.code('''
                    。。。竟然被你发现了
                    你是我家哥哥的真爱粉吗？''')
            st.image("ikun.jpeg")
    

def page_4():
    st.write(":blue[我的留言区]")

def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (b,g,r)
    return img 

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
