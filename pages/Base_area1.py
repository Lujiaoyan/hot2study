'''我的主页'''
import streamlit as st
from PIL import Image
image = Image.open('image.jpg')

st.image(image, caption='Sunrise by the mountains',use_column_width=True)

#           python -m streamlit run C:\Users\Public\TurtleWorkspace\新的作品-4-副本\我的网路文件夹-副本\Base_area1.py





page = st.sidebar.radio('我的首页',["垃圾箱1","垃圾箱2","垃圾箱3"])

def db_1():
    pass
    
def db_2():
    st.write('秋叶的垃圾箱:http://qiuye.ysepan.com/?xzpd=1')
    
def db_3():
    st.image(image, caption='Sunrise by the mountains',use_column_width=True)


if page == '垃圾箱1':
    db_1()

elif page == '垃圾箱2':
    db_2()

elif page == '垃圾箱3':
    db_3()