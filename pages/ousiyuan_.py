'我的主页'
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','我的成分复杂的图鉴'])

def page_1():
    st.write('这是我的兴趣推荐')
    with open('SeeYouAgain.mp3','rb') as f:
        my_mp3 = f.read()
    st.audio(my_mp3,format = 'audio/mp3',start_time = 0)
    st.write(':blue[牢大我想你了！]')
    st.image('冰红茶.jpg')
    st.write('——————————————————我是分界线——————————————————')
    st.write(':orange[为什么最近总有东西要涨价？我的饮料怎么更贵了！]')
    st.image('生活.jpeg')
    st.write('——————————————————我是分界线——————————————————')
    st.write(':red[震惊！老鼠会唱歌！]')
    st.image('悲伤鼠鼠.jpg')
    with open('悲伤鼠鼠唱歌.mp3','rb') as f:
        sad_mouse_mp3 = f.read()
    st.audio(sad_mouse_mp3,format = 'audio/mp3',start_time = 0)
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
    
def page_2():
    st.write(':red[抱歉，你的内容丢失了]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_3():
    st.write(':red[抱歉，你的内容丢失了]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_4():
    st.write(':red[抱歉，你的内容丢失了]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_5():
    st.write(':blue[小坤佩奇]')
    st.image('小坤佩奇.png')
    st.write('——————————————————我是分界线——————————————————')
    st.write('恶搞坤坤')
    st.image('恶搞坤坤.png')
    st.write('——————————————————我是分界线——————————————————')
    st.write('冰红茶科比')
    st.image('冰红茶.jpg')
    st.write('——————————————————我是分界线——————————————————')
    st.write('劲凉冰红茶梅西')
    st.image('劲凉冰红茶.png')
    st.write('——————————————————我是分界线——————————————————')
    st.write(':blue[悲伤鼠鼠]')
    st.image('悲伤鼠鼠.jpg')
    st.write('它会唱会儿歌')
    with open('悲伤鼠鼠唱歌.mp3','rb') as f:
        sad_mouse_mp3 = f.read()
    st.audio(sad_mouse_mp3,format = 'audio/mp3',start_time = 0)
    st.write('——————————————————我是分界线——————————————————')
    st.write('新鲜哥猫')
    st.image('新鲜哥猫.jpg')
    st.write('——————————————————我是分界线——————————————————')
    st.write('奸商')
    st.image('Plains_Villager_Base.png')
    st.write(':red[打折扣吧，只要一组绿宝石就给两个甜菜根]')
    st.write('——————————————————我是分界线——————————————————')
    st.write('流浪栓绳')
    st.image('Wandering_Trader_JE1_BE1.png')
    st.write(':red[我比上一个便宜，我两个绿宝石换一个苔藓块]')
    st.write('——————————————————我是分界线——————————————————')
    st.write('废石三兄弟')
    st.image('废石三兄弟.png')
    st.write(':red[你的背包看起来还可以在装点]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
    

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