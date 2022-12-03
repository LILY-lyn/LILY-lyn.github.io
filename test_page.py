from pyfmi import load_fmu
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests
from streamlit_lottie import st_lottie


def app():

    # 动图载入
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # 载入fmu模型
    model = load_fmu('LILY-lyn.github.io/model/AirConditionSystem.fmu')
    model.get_model_variables()

    # 侧边栏
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    sidebar = st.sidebar.radio(
        "请选择实验项目",
        ("实验一", "实验二")
    )
    st.write("---")
    if sidebar == "实验一":
        st.subheader("实验一：风机控制实验")
        with st.form("fan_set"):
            st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_4m0f2coq.json"), height=80)
            st.info("参数设置")
            # 设置参数
            fancon_ulow = st.slider('风机控制最低温度(℃):', 25.0, 26.0, 25.5)
            fancon_uhigh = st.slider('风机控制最高温度(℃):', 26.0, 27.0, 26.5)
            st.write("当前风机控制温度(Tset)的范围：", fancon_ulow, "℃ <"  "Tset  <", fancon_uhigh, "℃")
            model.set('FanCon.uLow', fancon_ulow + 273.15)
            model.set('FanCon.uHigh', fancon_uhigh + 273.15)
            # 数值选择范围
            st.info("仿真时间")

            # 定义函数
            def f(n):
                if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
                    return True
                else:
                    return False
            # 开始时间
            d = st.date_input("请输入开始时间（天）", datetime.date(2019, 7, 22))
            date_string = d.strftime('%Y-%m-%d')
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            start_t = 0
            for i in range(1, l[1]):
                start_t += month[i]
            start_t += l[2]
            st.write(f"当前开始仿真天数为第{start_t}天")
            # 结束时间
            d = st.date_input("请输入结束时间（天）", datetime.date(2019, 7, 23))
            date_string = d.strftime('%Y-%m-%d')
            # print(date_string)
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            final_t = 0
            for i in range(1, l[1]):
                final_t += month[i]
            final_t += l[2]
            st.write(f"当前结束仿真天数为第{final_t}天")
            model_data = st.selectbox(
                "请选择展示数据",
                ("室外温度与室内温度", "送风温度", "风机功率")
            )
            submitted = st.form_submit_button("提交")
            if submitted:
                # 这里添加提交的信息
                st.success("提交成功")
                res = model.simulate(start_time=start_t * 86400, final_time=final_t * 86400)
                st.info("结果数据")
                if model_data == "室外温度与室内温度":
                    # 运行参数
                    model.get("WeaBus.TDryBul")
                    res.final("WeaBus.TDryBul")
                    model.get("Zone.Troom")
                    res.final("Zone.Troom")
                    # 结果绘制
                    fig = plt.figure()
                    x = res['time'] / 86400
                    y1 = res["WeaBus.TDryBul"] - 273.15
                    y2= res["Zone.Troom"] - 273.15
                    plt.xlabel('时间(天)')
                    plt.ylabel('温度(℃)')
                    plt.plot(x, y1, label='室外干球温度', color="red")
                    plt.plot(x, y2, label='室内空气温度', color="blue")
                    st.plotly_chart(fig, use_container_width=True)
                if model_data == "送风温度":
                    # 运行参数
                    model.get("WeaBus.TDryBul")
                    res.final("WeaBus.TDryBul")
                    model.get("Zone.Troom")
                    res.final("Zone.Troom")
                    model.get("TsuAir.T")
                    res.final("TsuAir.T")
                    fig = plt.figure()
                    x = res['time'] / 86400
                    y1 = res["WeaBus.TDryBul"] - 273.15
                    y2 = res["Zone.Troom"] - 273.15
                    y3 = res["TsuAir.T"]-273.15
                    plt.xlabel('时间(天)')
                    plt.ylabel('温度(℃)')
                    plt.plot(x, y1, label='室外干球温度', color="red")
                    plt.plot(x, y2, label='室内空气温度', color="blue")
                    plt.plot(x, y3, label='送风温度',color="green")
                    st.plotly_chart(fig, use_container_width=True)
                if model_data == "风机功率":
                    # 参数运行
                    model.get("Fan.P")
                    res.final("Fan.P")
                    fig = plt.figure()
                    x = res['time'] / 86400
                    y = res["Fan.P"]
                    plt.xlabel('时间(天)')
                    plt.ylabel('功率(W)')
                    plt.plot(x, y, label='风机功率',color="m")
                    st.plotly_chart(fig, use_container_width=True)

    if sidebar == "实验二":
        st.subheader("实验二：风机控制实验")
        with st.form("fan_set"):
            st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_4m0f2coq.json"),height=80)
            st.info("参数设置")
            # 设置参数
            fancon_ulow = st.slider('风机控制最低温度(℃):', 25.0, 26.0, 25.5)
            fancon_uhigh = st.slider('风机控制最高温度(℃):', 26.0, 27.0, 26.5)
            st.write("当前风机控制温度(Tset)的范围：", fancon_ulow, "℃ <"  "Tset  <", fancon_uhigh, "℃")
            model.set('FanCon.uLow', fancon_ulow + 273.15)
            model.set('FanCon.uHigh', fancon_uhigh + 273.15)
            # 数值选择范围
            st.info("仿真时间")
            # 定义函数
            def f(n):
                if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
                    return True
                else:
                    return False
            # 开始时间
            d = st.date_input("请输入开始时间（天）", datetime.date(2019, 7, 22))
            date_string = d.strftime('%Y-%m-%d')
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            start_t = 0
            for i in range(1, l[1]):
                start_t += month[i]
            start_t += l[2]
            st.write(f"当前开始仿真天数为第{start_t}天")
            # 结束时间
            d = st.date_input("请输入结束时间（天）", datetime.date(2019, 7, 23))
            date_string = d.strftime('%Y-%m-%d')
            # print(date_string)
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            final_t = 0
            for i in range(1, l[1]):
                final_t += month[i]
            final_t += l[2]
            st.write(f"当前结束仿真天数为第{final_t}天")
            submitted = st.form_submit_button("提交")
            if submitted:
                # 这里添加提交的信息
                st.success("提交成功")
                res = model.simulate(start_time=start_t * 86400, final_time=final_t * 86400)
                # 重新运行参数
                model.get("WeaBus.TDryBul")
                res.final("WeaBus.TDryBul")
                model.get("Zone.Troom")
                res.final("Zone.Troom")
                # 结果绘制
                st.info("结果数据")
                fig = plt.figure()
                x = res['time'] / 86400
                y1 = res["Zone.Troom"] - 273.15
                y2 = res["WeaBus.TDryBul"] - 273.15
                plt.xlabel('时间(天)')
                plt.ylabel('温度(℃)')
                plt.plot(x, y1, label='室内温度')
                plt.plot(x, y2, label='室外温度')

                st.plotly_chart(fig, use_container_width=True)

    if sidebar == "实验三":
        st.subheader("实验三：风机控制实验")
        with st.form("fan_set"):
            st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_4m0f2coq.json"),height=80)
            st.info("参数设置")
            # 设置参数
            fancon_ulow = st.slider('风机控制最低温度(℃):', 25.0, 26.0, 25.5)
            fancon_uhigh = st.slider('风机控制最高温度(℃):', 26.0, 27.0, 26.5)
            st.write("当前风机控制温度(Tset)的范围：", fancon_ulow, "℃ <"  "Tset  <", fancon_uhigh, "℃")
            model.set('FanCon.uLow', fancon_ulow + 273.15)
            model.set('FanCon.uHigh', fancon_uhigh + 273.15)
            # 数值选择范围
            st.info("仿真时间")
            # 定义函数
            def f(n):
                if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
                    return True
                else:
                    return False
            # 开始时间
            d = st.date_input("请输入开始时间（天）", datetime.date(2019, 7, 22))
            date_string = d.strftime('%Y-%m-%d')
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            start_t = 0
            for i in range(1, l[1]):
                start_t += month[i]
            start_t += l[2]
            st.write(f"当前开始仿真天数为第{start_t}天")
            # 结束时间
            d = st.date_input("请输入结束时间（天）", datetime.date(2019, 7, 23))
            date_string = d.strftime('%Y-%m-%d')
            # print(date_string)
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            final_t = 0
            for i in range(1, l[1]):
                final_t += month[i]
            final_t += l[2]
            st.write(f"当前结束仿真天数为第{final_t}天")
            submitted = st.form_submit_button("提交")
            if submitted:
                # 这里添加提交的信息
                st.success("提交成功")
                res = model.simulate(start_time=start_t * 86400, final_time=final_t * 86400)
                # 重新运行参数
                model.get("WeaBus.TDryBul")
                res.final("WeaBus.TDryBul")
                model.get("Zone.Troom")
                res.final("Zone.Troom")
                # 结果绘制
                st.info("结果数据")
                fig = plt.figure()
                x = res['time'] / 86400
                y1 = res["Zone.Troom"] - 273.15
                y2 = res["WeaBus.TDryBul"] - 273.15
                plt.xlabel('时间(天)')
                plt.ylabel('温度(℃)')
                plt.plot(x, y1, label='室内温度')
                plt.plot(x, y2, label='室外温度')

                st.plotly_chart(fig, use_container_width=True)
    if sidebar == "实验四":
        st.subheader("实验四：风机控制实验")
        with st.form("fan_set"):
            st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_4m0f2coq.json"),height=80)
            st.info("参数设置")
            # 设置参数
            fancon_ulow = st.slider('风机控制最低温度(℃):', 25.0, 26.0, 25.5)
            fancon_uhigh = st.slider('风机控制最高温度(℃):', 26.0, 27.0, 26.5)
            st.write("当前风机控制温度(Tset)的范围：", fancon_ulow, "℃ <"  "Tset  <", fancon_uhigh, "℃")
            model.set('FanCon.uLow', fancon_ulow + 273.15)
            model.set('FanCon.uHigh', fancon_uhigh + 273.15)
            # 数值选择范围
            st.info("仿真时间")
            # 定义函数
            def f(n):
                if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
                    return True
                else:
                    return False
            # 开始时间
            d = st.date_input("请输入开始时间（天）", datetime.date(2019, 7, 22))
            date_string = d.strftime('%Y-%m-%d')
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            start_t = 0
            for i in range(1, l[1]):
                start_t += month[i]
            start_t += l[2]
            st.write(f"当前开始仿真天数为第{start_t}天")
            # 结束时间
            d = st.date_input("请输入结束时间（天）", datetime.date(2019, 7, 23))
            date_string = d.strftime('%Y-%m-%d')
            # print(date_string)
            s = date_string.split('-')
            l = [int(x) for x in s]
            month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if f(l[0]):
                month[2] = 29
            else:
                month[2] = 28
            final_t = 0
            for i in range(1, l[1]):
                final_t += month[i]
            final_t += l[2]
            st.write(f"当前结束仿真天数为第{final_t}天")
            submitted = st.form_submit_button("提交")
            if submitted:
                # 这里添加提交的信息
                st.success("提交成功")
                res = model.simulate(start_time=start_t * 86400, final_time=final_t * 86400)
                # 重新运行参数
                model.get("WeaBus.TDryBul")
                res.final("WeaBus.TDryBul")
                model.get("Zone.Troom")
                res.final("Zone.Troom")
                # 结果绘制
                st.info("结果数据")
                fig = plt.figure()
                x = res['time'] / 86400
                y1 = res["Zone.Troom"] - 273.15
                y2 = res["WeaBus.TDryBul"] - 273.15
                plt.xlabel('时间(天)')
                plt.ylabel('温度(℃)')
                plt.plot(x, y1, label='室内温度')
                plt.plot(x, y2, label='室外温度')

                st.plotly_chart(fig, use_container_width=True)