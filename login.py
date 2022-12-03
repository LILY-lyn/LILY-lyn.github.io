import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import app

# 网页标题
st.set_page_config(page_title="实验小屋", page_icon=":house_with_garden:", layout="wide")
st.title('空调系统虚拟仿真实验平台')

# 侧边栏
st.sidebar.header("导航栏")
sidebar = st.sidebar.selectbox(
    "选择其他内容",
    ("用户登录", "用户注册")
)

# 打开数据文件
with open('login_data/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# 用户登录
if sidebar == "用户登录":
    name, authentication_status, username = authenticator.login('用户登录', 'main')
    if authentication_status:
        with st.container():
            cols1, cols2, cols3, cols4, cols5 = st.columns(5)
            with cols1.container():

                st.subheader(f'你好~ *{name}*:wave: ')
                with cols2.container():
                    st.write("                     ")
                    with cols3.container():
                        st.write("                   ")
                        with cols4.container():
                            st.write("                      ")
                            with cols5.container():
                                authenticator.logout('退出登录', 'main')
                                reset_password_button = st.button("修改密码")
        st.subheader('欢迎登录实验小屋，开启你的实验之旅吧！:sunflower:')
        # 修改密码
        if reset_password_button:
            try:
                if authenticator.reset_password('用户名', '修改密码', 'sidebar'):
                    st.success('Password modified successfully')
            except Exception as e:
                st.error(e)

        # 运行主页
        app.main()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

# 用户注册
if sidebar == "用户注册":
    try:
        if authenticator.register_user('用户注册', preauthorization=False):
            st.success('用户注册成功')
    except Exception as e:
        st.error(e)


# 保存到 yaml文件
with open('login_data/config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

