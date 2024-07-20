"'我的网络根据地'"
import streamlit as st
from PIL import Image

page = st.sidebar.radio("HOME PAGE", ['HOBBIES', "GAME", "COMPUTER", "TOOLBOX"])

def page_1():
    tab1, tab2 = st.tabs(["BOOK", "JNTM"])
    with tab1:
        st.header(":blue[三体三部曲，你值得拥有]")
        st.image("《三体》纪念版封面.png")
        #st.video()
        st.header("对你有帮助的书！")
        st.image("工具.jpg")
        #st.video()
    with tab2:
        st.title("成分复杂的我")
        tab3, tab4 = st.tabs(["OTHER", "JNTM"])
        with tab3:
            st.image("野比大雄.png")
            st.write("https://www.bilibili.com/video/BV15z421B7s9/?spm_id_from=333.1073.0.0&vd_source=504f4fdf95605216335d54ddaa2ac98a")
            st.image("nwd.png")
            st.write("https://bilibili.com/video/BV1rZ4y1M7CZ?spm_id_from=333.999.0.0")
        with tab4:
            st.header("2029春晚")
            st.image("jntm.png")
            st.write("https://www.bilibili.com/video/BV178411Y7QB/?spm_id_from=333.337.search-card.all.click&vd_source=504f4fdf95605216335d54ddaa2ac98a")
            st.image("jntm-1.png")
            st.header("鸡哥天下第一")
            st.image("jntm-2.png")
            st.write("https://www.bilibili.com/video/BV1am4y1175K/?spm_id_from=333.788.recommend_more_video.0&vd_source=504f4fdf95605216335d54ddaa2ac98a")
            

def page_2():
    st.title("米家全家桶，仅需300GB！！！超实惠的有没有！！！")
    st.image("崩坏3 .png")
    #st.video()
    st.image("原神.png")
    #st.video()
    st.image("绝区零zzz.png")
    #st.video()

def page_3():
    st.title("下面是一些我推荐的电脑，有电脑需求的考虑一下=）")
    tab1, tab2 = st.tabs(["联想", "华硕"])
    with tab1:
        st.header("联想：")
        tab5, tab6 = st.tabs(["ThinkPad", "ThinkBook"])
        with tab5:
            st.write("    thinkpad t14p:https://www.thinkpad.com/device/ThinkPad-T14p-2023")
            st.image("t14p.png")
        with tab6:
            st.write("    thinkbook 16p:https://www.thinkpad.com/device/thinkbook16-2023-i9?preview=true")
            st.image("16p.png")
    with tab2:
        st.header("ASUS:")
        tab3, tab4 = st.tabs(["天选", "ROG"])
        with tab3:
            st.subheader("    天选系列：")
            st.write("        天选5pro:https://www.asus.com.cn/laptops/for-gaming/tuf-gaming/asus-tuf-gaming-f16-2024/")
            st.image("tx5p.png")
        with tab4:
            st.subheader("    ROG系列：")
            st.write("        幻16:https://rog.asus.com.cn/laptops/rog-zephyrus/rog-zephyrus-g16-2023-series/")
            st.image("h16.png")


def page_4():
    st.header(":sunglasses:图片换色工具:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type = ["png", "jpg", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img)
        tab1, tab2, tab3= st.tabs([ "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img_change(img, 0,1,2))
        with tab2:
            st.image(img_change(img, 1,0,2))
        with tab3:
            st.image(img_change(img, 0,0,1))
    st.header(":sunglasses:小词典:sunglasses:")
    with open("words_space.txt","r", encoding="utf-8") as f:
        word_list = f.read().split("\n")
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split("#")
    word_dict = {}
    for i in word_list:
        word_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input("请输入要查的单词：")
    if word in word_dict:
        st.write(word_dict[word])
        if word == "python":
            st.code("print('hello world')")
        elif word == "zzz":
            st.image("绝区零zzz.png")
        elif word == "zhaohui":
            st.balloons()
            st.snow()
            
    
def img_change(img, rc, gc, bc):
    w, h = img.size
    img_array = img.load()
    for x in range(w):
        for y in range(h):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (b,g,r)
    return img
    

if page == 'HOBBIES':
    page_1()
elif page == 'GAME':
    page_2()
elif page == 'COMPUTER':
    page_3()
elif page == 'TOOLBOX':
    page_4()

#python -m streamlit run D:\workplace\营期\我的网络根据地\zhaohui_.py
