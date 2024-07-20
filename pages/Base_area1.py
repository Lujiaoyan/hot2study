'''我的主页'''
import streamlit as st
from PIL import Image


#          .-.. .-.. --- ...- . .--. . .- -.-. . -.- . . .--. . .-.





#           python -m 
sss = Image.open('sss.jpg')
w = Image.open('world.jpg')
BFG = Image.open('BFG.jpg')

page = st.sidebar.radio('我的首页',["垃圾箱1","垃圾箱2","垃圾箱3"])

def db_1():
    st.image(sss)
    st.write('-----------------------------------------------------------------分割线------------------------------------------------------------------')
    st.write('                                                                                                                                         ')
    st.image(BFG)
    
def db_2():
    st.write('图片处理工具')
    uploaded_file = st.file_uploader('上传图片',type=['png', 'jpeg', 'jpg'])

    if uploaded_file:
        img = Image.open(uploaded_file)
        tab1, tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1: 
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab2:
            st.image(img_change(img,1,2,0))
        with tab2:
            st.image(img_change(img,1,0,2))
#st.image(img_change(img,0,2,1))  
    
def db_3():
    st.write('秋叶的垃圾箱:http://qiuye.ysepan.com/?xzpd=1')
    st.image(w,caption='一张游戏中的世界地图')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict ={}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]

    word  = st.text_input('请输入要查询的单词')
    
    if word in words_dict:
        st.write(words_dict[word])
        if word == '.-.. .-.. --- ...- . .--. . .- -.-. . -.- . . .--. . .-.':
            st.write('!')

        
    print(words_list)
    print(words_dict)


def img_change(img,rc,gc,bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x, y] = (b, g, r)
            
    return img





if page == '垃圾箱1':
    db_1()

elif page == '垃圾箱2':
    db_2()

elif page == '垃圾箱3':
    db_3()
