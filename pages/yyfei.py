'''F的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('F的首页',['F的兴趣推荐','F的图片处理工具','F的智慧词典','F的留言区'])

def page_1():
    st.write(':blue[F的兴趣推荐]')
    tab1,tab2,tab3,tab4 = st.tabs([':blue[电影]',':blue[音乐]',':blue[壁纸]',':blue[书籍]'])
    with tab1:
        st.image('默杀.jpg')
        st.write('《默杀》讲述了在校园霸凌事件横生的女子中学，在女子坠亡事件发生后，校园中的女学生相继失踪，在集体的沉默背后，正酝酿着充满仇恨与杀戮的复仇的故事。')
        st.image('云边有个小卖部.jpg')
        st.write('一心向往城市的刘十三，毕业后接连遭受爱情事业打击。醉酒后，外婆将他带回了故乡。为了回城逐梦，刘十三决心改造外婆的小卖部证明自己。而后困难重重，而他也随之转变')
    with tab2:
        st.write(':blue[JYJ - BACK SEAT]')
        with open('JYJ - BACK SEAT (网友改编).mp3','rb')as f:
            mymp3 = f.read()
        st.audio(mymp3,format='audio/mp3',start_time = 0)
        st.write(':blue[See You Later]')
        with open('GRAHAM - See You Later.mp3','rb')as f:
            mymp3_1 = f.read()
        st.audio(mymp3_1,format='audio/mp3',start_time = 0)
        st.write(':blue[小酒窝]')
        with open('林俊杰 - 小酒窝.mp3','rb')as f:
            mymp3_2 = f.read()
        st.audio(mymp3_2,format='audio/mp3',start_time = 0)
    with tab3:
        st.image('壁纸0.jpg')
        st.image('壁纸1.jpg')
        st.image('壁纸2.jpg')
        st.image('壁纸3.jpg')
    with tab4:
        st.write('《平凡的世界》——路遥')
        st.write('这是本能带给人向上向善的力量的书。孙少安与孙少平，他们都是平凡的人，生活在平凡的世界里，但却凭借勇气和坚毅的力量，创造了属于各自不平凡的人生。')
        st.write(':blue[生活不能等待别人来安排，要自己去争取和奋斗，不论结果是喜是悲，你总不枉在这世界上活了一场。]')
        st.image('《平凡的世界》.jpg')
        st.write('《我们仨》一一杨绛')
        st.write('这是本能教会我们珍惜当下的书。记录了前总书杨绛一家温暖而平凡的生活，从中我们可以看到世界上最美好的爱情，婚姻和家庭是什么样的。')
        st.write(':blue[人间不会有单纯的快乐，快乐总夹杂着烦恼和忧虑，人间也没有永远。]')
        st.image('《我们仨》.jpg')
        st.write('《岁月忽已晚，灯火要人归》一一丰子恺')
        st.write('这本书围绕家庭温景展开十分治愈，讲述成为父亲的感受和体悟，分享孩子和家长生活中的趣事，解读世间万物，领略世间的美好之处。')
        st.write(':blue[人要像大人一样生存，像孩子一样生活。]')
        st.image('《岁月忽已晚，灯火要人归》.jpg')
         
def page_2():
    '''F的图片处理工具'''
    st.write(':sunglasses:图片换色小程序:sunglasses:')
    uploaded_file = st.file_uploader("上传图片",type = ["png",'jpeg','jpg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
         
def page_3():
    pass
    
def page_4():
    pass

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
        
if page =='F的兴趣推荐':
    page_1()
elif page =='F的图片处理工具':
    page_2()
elif page =='F的智慧词典':
    page_3()
elif page =='F的留言区':
    page_4()
