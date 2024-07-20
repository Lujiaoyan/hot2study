'''我的主页'''
import streamlit as st
from PIL import Image

page  = st.sidebar.radio('我的首页', ['我的推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '''我的推荐'''
    st.write(':red 推荐榜')
    tab1, tab2, tab3, tab4= st.tabs(["兴趣推荐","游戏推荐","风景推荐", "书籍推荐"])
    with tab1:
        with open('萌果果大大 - Track in time.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.write(':blue, [跑步，哦豁豁]')
        st.image("跑步.png")
    with tab2:
        with open('猫鼠主题曲.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.write(':red 《猫和老鼠》经典改编')
        st.image("猫鼠.jpg")
    with tab3:
        st.write("猜猜这是哪~~")
        st.image("名胜.jpg")
    with tab4:
        st.write(':blue 想象奇特，震撼人心')
        st.image("三体.jpg")

    
def page_2():
    '''图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png','jpg','jpeg'])
    tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 1, 0, 2))
        with tab3:
            st.image(img_change(img, 0, 1, 2))
        with tab4:
            st.image(img_change(img, 1, 2, 0))
    pass
    
def page_3():
    '''我的智慧词典'''
    st.write("智慧词典")
    with open('words_space.txt','r', encoding='utf-8-sig') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    word = st.text_input('请输入查询单词')
    if word in words_dict:
        st.write(words_dict[word])
        if word =='python':
            st.code('''
                    #恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word =='luoxingzu':
            st.code('''
                    #恭喜你触发彩蛋，这是作者名字''')

    pass
    
def page_4():
    st.write(':red [留言]')
    pass

def img_change(img, rc, gc, bc):
    """图片处理"""
    width , height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x,y] = (b,g,r)
    return img

if page == '我的推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
