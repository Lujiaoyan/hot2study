'我的主页'
import streamlit as st
from PIL import Image
from random import *
from collections import Counter
from time import *

page = st.sidebar.radio(':orange[_我的首页:sunglasses:_]',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','我的成分复杂的图鉴','好用小工具'])
def page_1():
    st.title('_这是我的兴趣推荐👇_')
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
    st.title(":sunglasses:图片处理小程序:sunglasses:")
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
    st.title('awa_智慧词典📖_awa')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词：')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        a = str(times_dict[n])
        st.write(f':blue[_这个单词一共被查阅了{a}次_]')
        if word == 'Man':
            st.balloons()
            with open('SeeYouAgain.mp3','rb') as f:
                man_mp3 = f.read()
            st.audio(man_mp3,format = 'audio/mp3',start_time = 0)
        if word == 'python':
            st.snow()
            st.write(':red[_这是本网站的制作器_]')
            st.code('''这是一行Python代码
                    print('千万别输入Man')''')
        if word == 'ikun':
            st.balloons()
            st.write(':red[_你是真爱粉吗？_]')
            st.image('小坤佩奇.png')
        if word == 'oubeibei':
            st.write(':red[不是，你怎么知道的]')
            st.image('新鲜哥猫.jpg')
        if word == 'Kobe Bryant' or word == 'Kobe':
            st.balloons()
            st.image('冰红茶.jpg')
            with open('SeeYouAgain.mp3','rb') as f:
                man_mp3 = f.read()
            st.audio(man_mp3,format = 'audio/mp3',start_time = 0)
        if word == 'Technoblade':
            st.write(':red[_Technoblade never dies!_]')
        if word == 'dream':
            st.image('dream.png')
    elif word not in words_dict and word:
        st.write(':blue[_未找到该单词，请重新输入_]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_4():
    st.title('🪐我的留言区🪐')
    st.write(':red[_注意：在留言完后将留言人更改即可查看自己的留言_]')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '坤坤':
            with st.chat_message('🐥'):
                st.write(i[1],':',i[2])
        elif i[1] == '老八':
            with st.chat_message('💩'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '科比':
            with st.chat_message('🏀'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '贝贝':
            with st.chat_message('👌'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '小黑子':
            with st.chat_message('🐔'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '小老鼠':
            with st.chat_message('🐀'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '普通人':
            with st.chat_message('🙃'):
                st.text(i[1]+':'+i[2])
        elif i[1] == 'coke':
            with st.chat_message('😺'):
                st.text(i[1]+':'+i[2])
    name = st.selectbox('我是……',['坤坤','老八','科比','贝贝','小黑子','小老鼠','普通人','coke'])
    new_message = st.text_input('我想说的话……')
    if st.button('🪑留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
    with open('leave_messages.txt','w',encoding='utf-8') as f:
        message = ''
        for i in messages_list:
            message += i[0]+'#'+i[1]+'#'+i[2]+'\n'
        message = message[:-1]
        f.write(message)
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_5():
    st.title(':purple[我是个《正经》的图鉴🤪]')
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['小坤佩奇','恶搞坤坤','冰红茶科比','劲凉冰红茶梅西','悲伤鼠鼠','新鲜哥猫','奸商','流浪栓绳'])
    st.write('———————————————————我是分界线———————————————————')
    tab9,tab10,tab11,tab12 = st.tabs(['废石三兄弟','臭猫','《虾》','白色巨型僵尸'])
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
    with tab11:
        st.write('《虾》')
        st.image('虾.jpg')
    with tab12:
        st.write(':blue[白色巨型僵尸]')
        st.image('白色巨型僵尸.png')
        st.write(':red[《村庄祸害者，他永远不会还手》]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')

def page_6():
    st.title('_👏用过的人都说好！_')
    tab1,tab2,tab3,tab4 = st.tabs(['聪明的计算机','我会取名字！','不要点我！','猜身份'])
    with tab1:
        nums = st.text_input('请输入算式：')
        if nums:
            nl = [1,2,3]
            n = choice(nl)
            if n == 1:
                st.write(':red[我不会，长大后再来学吧]')
            elif n==2:
                st.write(':red[想偷懒？]')
            else:
                st.write(':red[（计算机跑路了）]')
    with tab2:
        father_name = None
        if not father_name:
            father_name = st.text_input('请输入父亲名字：')
        mother_name = None
        if not mother_name:
            mother_name = st.text_input('请输入母亲名字：')
        if father_name and mother_name:
            st.write('你们孩子的名字是：')
            st.subheader(father_name[0]+mother_name[0]+"!")
    with tab3:
        st.write('_加载ing_')
        bar_num = 0
        latest_iteration = st.empty()
        bar= st.progress(0)
        t = st.button('点我加载')
        if t:
            for i in range(99):
                latest_iteration.text(f'{i+1}%')
                bar.progress(i + 1)
                sleep(0.1)
            st.write(':red[_加载是个谎言！_]')
    st.write(' ')
    st.subheader(':blue[_👇评价一下！_]')
    if st.button('👍') or st.button('好') or st.button('好用') or st.button('太好用了') or st.button('这是我见过最好用的'):
        st.write(':blue[_谢谢评价，祝您生活愉快！_]')
    with tab4:
        job = st.text_input('请输入1—3条线索（写完再回车）：')
        if job:
            st.write(':red[我猜你是…………]')
            sleep(3)
            st.write(':red[生物！]')
            sleep(1)
            st.write(':red[得意ing……]')
    
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
elif page == '好用小工具':
    page_6()
