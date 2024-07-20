'我的主页'
import streamlit as st
from PIL import Image
st.header("欢迎来到我的主页！")
page = st.sidebar.radio('我的主页',["兴趣推荐","图片处理工具","智慧词典","评论区"])

#功能区
def page_1():
    st.subheader("个人书法作品展示")
    st.image("书法作品1.jpg")
    st.image("书法作品2.jpg")
    st.image("书法作品3.jpg")
    st.image("书法作品4.jpg")

def page_2():
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img_change(img,0,1,2))
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))


def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y]= (r,g,b)
    return img
def page_3():
    st.write("智慧词典")
    with open("words_space.txt",encoding = "utf-8")as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    word = st.text_input("请输入要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        if word == "python":
            st.code('''print('hello world')''')
        
def page_4():
    pass



#运行区
if page =="兴趣推荐":
    page_1()
elif page == "图片处理工具":
    page_2()
elif page == "智慧词典":
    page_3()
elif page == "评论区":
    page_4()

    

    

