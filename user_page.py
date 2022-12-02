import streamlit as st
import requests
from streamlit_lottie import st_lottie


def app():

    # 设置格式
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    # 个人信息
    # import yaml
    # yaml_path = 'F:/OpenModelica-FmuList/login_data/config.yaml' # 从配置文件中获取数据
    #
    # def read_yaml(v):
    #     # 打开文件
    #     with open(yaml_path, "r", encoding="utf-8") as f:
    #         data = yaml.load(f, Loader=yaml.FullLoader)
    #         print(data)
    #         for v in data.values():
    #             print(v)

    with st.form("center"):

        st.subheader("个人信息"":pencil:")
        st.text_input("用户名", "18242095197")
        st.text_input("昵称","lily" )
        st.text_input("邮箱", "791496609@qq.com")
        submitted = st.form_submit_button("修改")
        if submitted:
           st.success("修改成功！")

    # 修改密码

    # 留言板
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")

    with st.container():
        st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_18QlHa.json"), height=102)
        st.header("留言板:loudspeaker:")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
                        <form action="https://formsubmit.co/791496609@qq.com" method="POST">
                            <input type="hidden" name="_captcha" value="false">
                            <input type="text" name="name" placeholder="昵称" required>                   
                            <textarea name="message" placeholder="留言内容" required></textarea>
                            <button type="submit">Send</button>
                        </form>
                        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ULeaW09pyz.json"), height=280)