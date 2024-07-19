'我的主页'
import streamlit as st
from PIL import Image
from random import *
from collections import Counter

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','我的成分复杂的图鉴'])

def page_1():
    st.write('这是我的兴趣推荐')
    tab1,tab2,tab3 = st.tabs(['牢大','饮料涨价','老鼠会sing'])
    with tab1:
        with open('SeeYouAgain.mp3','rb') as f:
            my_mp3 = f.read()
        st.audio(my_mp3,format = 'audio/mp3',start_time = 0)
        st.write(':blue[牢大我想你了！]')
        st.image('冰红茶.jpg')
    with tab2:
        st.write(':orange[为什么最近总有东西要涨价？我的饮料怎么更贵了！]')
        st.image('生活.jpeg')
    with tab3:
        st.write(':red[震惊！老鼠会唱歌！]')
        st.image('悲伤鼠鼠.jpg')
        with open('悲伤鼠鼠唱歌.mp3','rb') as f:
            sad_mouse_mp3 = f.read()
        st.audio(sad_mouse_mp3,format = 'audio/mp3',start_time = 0)
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
    
def page_2():
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader('图片上传:sunglasses:',type=['png','jpeg','jpg'])
    tab1,tab2,tab3,tab4 = st.tabs(['随机色调','反色调','像素化','战损'])
    with tab1:
        if uploaded_file:
            nums= [0,1,2]
            img_1 = Image.open(uploaded_file)
            st.image(img_1)
            rc = choice(nums)
            nums.remove(rc)
            rg = choice(nums)
            nums.remove(rg)
            rb = choice(nums)
            nums.remove(rb)
            st.image(change_img(img_1,rc,rg,rb))
    with tab2:
        if uploaded_file:
            img_2 = Image.open(uploaded_file)
            st.image(img_2)
            st.image(fan_img(img_2))
    with tab3:
        if uploaded_file:
            img_3 = Image.open(uploaded_file)
            st.image(img_3)
            st.image(xiang_img(img_3))
    with tab4:
        if uploaded_file:
            img_4 = Image.open(uploaded_file)
            st.image(img_4)
            st.image(daxiao_img(img_4))
    
def page_3():
    st.write(':red[抱歉，你的内容丢失了]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_4():
    st.write(':red[抱歉，你的内容丢失了]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_5():
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['小坤佩奇','恶搞坤坤','冰红茶科比','劲凉冰红茶梅西','悲伤鼠鼠','新鲜哥猫','奸商','流浪栓绳'])
    st.write('———————————————————我是分界线———————————————————')
    tab9,tab10 = st.tabs(['废石三兄弟','臭猫'])
    with tab1:
        st.write(':blue[小坤佩奇]')
        st.image('小坤佩奇.png')
    with tab2:
        st.write('恶搞坤坤')
        st.image('恶搞坤坤.png')
    with tab3:
        st.write('冰红茶科比')
        st.image('冰红茶.jpg')
    with tab4:
        st.write('劲凉冰红茶梅西')
        st.image('劲凉冰红茶.png')
    with tab5:
        st.write(':blue[悲伤鼠鼠]')
        st.image('悲伤鼠鼠.jpg')
        st.write('它会唱会儿歌')
        with open('悲伤鼠鼠唱歌.mp3','rb') as f:
            sad_mouse_mp3 = f.read()
        st.audio(sad_mouse_mp3,format = 'audio/mp3',start_time = 0)
    with tab6:
        st.write('新鲜哥猫')
        st.image('新鲜哥猫.jpg')
    with tab7:
        st.write('奸商')
        st.image('Plains_Villager_Base.png')
        st.write(':red[打折扣吧，只要一组绿宝石就给两个甜菜根]')
    with tab8:
        st.write('流浪栓绳')
        st.image('Wandering_Trader_JE1_BE1.png')
        st.write(':red[我比上一个便宜，我两个绿宝石换一个苔藓块]')
    with tab9:
        st.write('废石三兄弟')
        st.image('废石三兄弟.png')
        st.write(':red[你的背包看起来还可以在装点]')
    with tab10:
        st.write('臭猫')
        st.image('臭猫.jpg')
        st.write(':red[我不会动，但我自带bgm]')
        with open('臭猫bgm.mp3','rb') as f:
            cat_mp3 = f.read()
        st.audio(cat_mp3,format = 'audio/mp3',start_time = 0)
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')

def change_img(img,rc,rb,rg):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][rg]
            b = img_array[x,y][rb]
            img_array[x,y] = (r,b,g)
    return img
def fan_img(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = 255- img_array[x,y][0]
            g = 255- img_array[x,y][1]
            b = 255- img_array[x,y][2]
            img_array[x,y] = (r,b,g)
    return img

def xiang_img(img):
    block=img.crop((0,0,10,10))

    s=5
    width=img.size[0]
    height=img.size[1]
    
    img_new=Image.new("RGB",img.size)
    for y in range(0,height,s):
        for x in range(0,width,s):
            block=img.crop((x,y,x+s,y+s))
    
            pixel_list=list(block.getdata())
            most_colors=Counter(pixel_list).most_common(1)[0][0]
            block_new=Image.new("RGB",block.size,most_colors)        
            
            img_new.paste(block_new,(x,y))

    return img_new
def daxiao_img(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][0]
            g = img_array[x,y][1]
            b = img_array[x,y][2]
            rgb= [r,g,b]
            r_n = max(r,g,b)
            g_n = min(r,g,b)
            b_n = randint(1,255)
            img_array[x,y] = (r_n,b_n,g_n)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的成分复杂的图鉴':
    page_5()
