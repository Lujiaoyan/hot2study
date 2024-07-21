'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('孙婧涵的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    tab1, tab2, tab3 = st.tabs(["听音乐", "阅读", "旅行+拍照"])
    with tab1:
        st.write(':blue[最喜欢的歌：《love story》]')
        with open('《love story》.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time = 0)
        st.write("""We were both young when I first saw you.
                 
I close my eyes and the flashback starts.
                 
I'm standing there on a balcony in summer air.
                 
See the lights, see the party, the ballgowns.
                 
See you make your way to the crowd.
                 
And say hello, little did I know.
                 
That you were Romeo, you were throwing pebbles.
                 
And my daddy said, Stay away from Juliet!
                 
And I was crying on the staircase.
                 
Begging you please don't go.
                 
And I said,
Romeo, take me somewhere we can be alone.
                 
I'll be waiting, all there's left to do is run.
                 
You'll be the prince and I'll be the princess.
                 
It's a love story, baby, just say yes.
                 
So I sneak out to the garden to see you.
                 
We keep quiet, 'cause we're dead if they knew.
                 
So close your eyes, escape this town for a little while.
                 
'Cause you were Romeo, I was a scarlet letter.
                 
And my daddy said, Stay away from Juliet!.
                 
But you were everything to me.
                 
I was begging you please don't go.
                 
And I said,
Romeo, take me somewhere we can be alone.
                 
I'll be waiting, all there's left to do is run.
                 
You'll be the prince and I'll be the princess.
                 
It's a love story, baby, just say yes.
                 
Romeo, save me, they're trying to tell me how to feel.
                 
This love is difficult, but it's real.
                 
Don't be afraid, we'll make it out of this mess.
                 
It's a love story, baby, just say yes.
                 
I got tired of waiting,
wondering if you were ever coming around.
                 
My faith in you was fading,
when I met you on the outskirts of town.
                 
And I said,
Romeo, save me, I've been feeling so alone.
                 
I keep waiting for you but you never come.
                 
Is this in my head, I don't know what to think.
                 
He knelt to the ground and pulled out a ring.
                 
And said,
Marry me, Juliet, you'll never have to be alone.
                 
I love you and that's all I really know.
                 
I talked to your dad, go pick out a white dress.
                 
It's a love story, baby, just say yes.
                 
We were both young when I first saw you.""")
    
    with tab2:
        st.write(':blue[①《简爱》]')
        st.write('简介：《简·爱》是英国女作家夏洛蒂·勃朗特创作的具有自传色彩的长篇小说，于1847年10月首次出版。该小说讲述了失去父母的女孩简被庄园主人罗切斯特暗恋，在偶然得知罗切斯特是有妇之夫，而且还向她隐瞒了惊人真相后，简陷入了迷茫、挣扎、苦痛的故事。本书暴露和批判了西方资本主义社会黑暗面。')
        st.image('简爱1.png')
        st.write('----------------------------')
        st.write(':blue[②《法医秦明》]')
        st.image('法医秦明.jpg')
    with tab3:
        st.write(':blue[北京之旅(天安门；天坛)]')
        st.image('北京1.jpg')
        st.image('北京2.jpg')
        st.write('----------------------------')
        st.write(':blue[恩施之旅（恩施大峡谷）]')
        st.image('恩施.jpg')
        st.write('----------------------------')
        st.write(':blue[长沙之旅(橘子洲)]')
        st.image('长沙.jpg')
        st.write('还有许多其他的美丽城市哦~（=^.^=)')

    
def page_2():
        st.write(":sunglasses:图片换色小程序:sunglasses:")
        uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img)
    
            tab1, tab2, tab3, tab4 = st.tabs(["原图","换色1", "换色2", "换色3"])

            with tab1:
                st.image(img)
    
            with tab2:
                st.image(img_change(img,0,2,1))
        
            with tab3:
                st.image(img_change(img,1,0,2))
        
            with tab4:
                st.image(img_change(img,2,0,1))
        
            
def page_3():
    st.write('智慧词典')
    tab1, tab2 = st.tabs(["英译中", "中译英"])
    with tab1:
        with open('words_space.txt', 'r', encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]
        with open('check_out_times.txt', 'r', encoding='utf-8') as f:
            times_list = f.read().split('\n')   
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
            
        word = st.text_input('请输入要查询的单词(英)：')
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt', 'w', encoding='utf-8') as f:
                message = '' 
                for k,v in times_dict.items():
                    message += str(k)+'#'+str(v)+'\n'
                message = message[:-1]
                f.write(message)
            st.write('查询次数：', times_dict[n])
            
            if word == 'python':
                st.snow()
                st.code('''print('hello word')''')
            if word == 'sunjinghan':
                st.balloons()
                st.write(':blue[(*^_^*) 嘻嘻……我最棒！]')
    with tab2:
        with open('words_space.txt', 'r', encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        words_dict = {}
        for i in words_list:
            words_dict[i[2]] = [int(i[0]), i[1]]
        word = st.text_input('请输入要查询的单词（中）：')        
        if word in words_dict:
            st.write(words_dict[word])


def page_4():
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '孙婧涵':
            with st.chat_message('😶'):
                st.write(i[1],':',i[2])
        elif i[1] == '绿巨人：':
            with st.chat_message('🤢'):
                st.text(i[1]+i[2])
        elif i[1] == '蜜汁微笑：':
            with st.chat_message('🙂'):
                st.text(i[1]+i[2])
    name = st.selectbox('我是……', ['孙婧涵', '绿巨人：', '蜜汁微笑：'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i [1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
        

def img_change(img,rc,gc,bc):
    width, height = img.size
    img_array = img.load()

    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]

            img_array[x,y] = (r,g,b)
            
    return img

        
if page == '我的兴趣推荐':
    page_1()

elif page == '我的图片处理工具':
    page_2()

elif page == '我的智慧词典':
    page_3()

elif page == '我的留言区':
    page_4()
