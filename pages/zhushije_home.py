'我的主页'
import streamlit as st
st.header("欢迎来到我的主页！")
tab1,tab2,tab3,tab4,tab5 = st.tabs(['时政新闻','今日天气','个人简介','照片墙','留言板'])

#功能区
def page_1():
    answer = st.selectbox("请选择你想要浏览的文章",["1",'现场发生了什么？直击特朗普竞选集会现场枪击事件','3'])
    if answer == "1":
        st.write('1')
    elif answer == "现场发生了什么？直击特朗普竞选集会现场枪击事件":
        st.video("视频.mp4")
        st.caption("据美国媒体13日报道，美国前总统特朗普当天在宾夕法尼亚州巴特勒市举行的竞选集会现场发生枪击事件，特朗普被特勤局人员护送离开。视频来源：新华社(00:23)")
        st.write("当地时间13日下午，特朗普在美国宾夕法尼亚州举行竞选集会发表演讲时，现场响起枪声。他在特勤人员保护下立即撤离了演讲台。社交媒体上公布的视频显示，事发时特朗普被特勤局人员团团围住，他被紧急护送离开现场，特朗普右耳有血迹，并向人群挥舞拳头。随后，特朗普在发表声明中称，自己的“右耳上部被一颗子弹击穿”，“流了很多血”。")
        st.image("trump.png")
        st.caption("特朗普在特勤人员保护下撤离演讲台，并向人群挥舞拳头。")
    else:
        pass

def page_2():
    pass

def page_3():
    pass

def page_4():
    pass

def page_5():
    pass

#运行区
with tab1:
    page_1()
with tab2:
    page_2()
with tab3:
    page_3()
with tab4:
    page_4()
with tab5:
    page_5()
    

    

