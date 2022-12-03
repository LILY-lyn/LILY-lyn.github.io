import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def app():

    # 动图载入
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # 应用本地 css 风格
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # 应用设计格式
    local_css("style/style.css")
    # 下载动图 （ https://lottiefiles.com/featured ）
    lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_jyxnt8gq.json")

    # ---- 平台介绍 ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("平台功能")
            st.write("##")
            st.write(
                        """
                        空调系统虚拟仿真实验平台的主要功能如下：
                        - 针对一次回风的定风量空调系统的讲解以及3D模型的展示.
                        - 在这里可以进行空调系统的仿真实验.
                        - 通过实验进行数据分析，了解与学习空调系统知识.
                        希望在这里，你可以有所收获 O(∩_∩)O.
                        """
                    )
            st.write("[学习视频通道 >](https://www.bilibili.com/video/BV1Mz4y1S73w/?spm_id_from=333.337.search-card.all.click)")
        with right_column:
            st_lottie(lottie_coding, height=330, key="coding")

    with st.container():
        st.write("---")
        st.header("空调系统介绍")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write("##")
            image = Image.open('LILY-lyn.github.io/images/air1.jpg')
            st.image(image, caption='全空气系统示意图', use_column_width = True)
        with right_column:
            st.subheader(" 全空气空调系统 ")
            st.write(
                        """
                        中央空调系统在楼宇建筑中一直以来为人们舒适的工作和生活环境发挥着重要的作用。例如：
                        全空气空调系统设备集中，运行和管理相对便捷，系统简单，并且处理的空气品质较好，除湿
                        能力也相对较强，在过渡季节也可以实行全新风运行。
                        \n在大空间建筑中应用尤为广泛，例如:商场建筑就属于其中一种，因其人员密集、设备室内负
                        荷大、空气流通差等特点，在空调系统的选择上， 全空气定风量的空调系统在空气调节领域
                        是一种常用的形式。定风量空调系统主要组成部分有水系统与风系统，那么工作的原理就是通
                        过水系统与空气进行热量交换从而调节送风的状态，在风系统中通过温度传感器来控制室内空
                        气的温度、湿度来创造出舒适的室内环境从而满足人们的需求。
                        """
                    )
            st.markdown("[视频学习通道](https://www.bilibili.com/video/BV1Lf4y167GS/?spm_id_from=333.337.search-card.all.click)")
    st.write("##")
    # nano
    with st.container():
        st.write("##")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader(" 风机盘管加新风空调系统 ")
            st.write(
                """
                  风机盘管主要依靠风机的强制作用，使空气通过加热器表面时被加热，因而强化了
                  散热器与空气间的对流换热器，能够迅速加热房间的空气。新风系统是一种持续地、
                  能控制通风路径而无需管道的住宅通风方式。同时新鲜空气24小时不间断地经装有
                  过滤装置的平衡式进风器送入室内，这样，密闭空间的空气就得到了充分更新。新风
                  系统可以让你不用开窗也能享受大自然的新鲜空气，满足人体的健康需求，减少能源流失。
                  \n风机盘管加新风系统可以使建筑内各房间实现独立调节温湿度的功能，当房间无人
                  时可随意的关机并且不影响其他房间的使用，有利于节能；房间之间空气不串通，适
                  用于房间较多的建筑，但需要单独控制的场所，并且占用空间较小。可是风机盘管加
                  新风系统不能在过渡季节进行全新风运行，不适用于新风量需求较大的场所。
                """
            )
            st.markdown("[视频学习通道](https://www.bilibili.com/video/BV1Lf4y167GS/?spm_id_from=333.337.search-card.all.click&vd_source=ca7e0039fdbe4a9361a2b4f0f30df2ff)")
        with right_column:
            st.write("##")
            st.write("##")
            st.write("##")
            image = Image.open('LILY-lyn.github.io/images/air2.jpg')
            st.image(image, caption='空调系统房间末端示意图', use_column_width = True)




