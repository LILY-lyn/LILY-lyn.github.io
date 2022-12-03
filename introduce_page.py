import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def app():

    # # 侧边栏
    # st.sidebar.write(" ")
    # st.sidebar.write(" ")
    # sidebar = st.sidebar.radio(
    #      "请选择查看内容",
    #      ("建筑案例", "空调系统")
    #   )
    st.write("---")
    st.subheader("建筑案例")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                - 实验建筑背景如下：
                实验建筑案例位于山东省济南市，建筑类型为综合商厦。由于大空间商场建
                筑面积较大且空调系统设计困难，因此本文主要针对一层购物商场进行建筑模
                型建立，其中一层总面积1035m^2，层高为4m，外墙面积约为720m^2，
                内墙面积约为240m^2，外窗面积约为186m^2，建筑分区如图。
                """
            )
        with right_column:
            image = Image.open('images/building.jpg')
            st.image(image, caption='建筑一层平面示意图', use_column_width=True)
    # 空调系统
    st.write("---")
    st.subheader("空调系统")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            image = Image.open('images/system.jpg')
            st.image(image, caption='空调系统示意图', use_column_width=True)
        with right_column:
            st.write("##")
            st.write(
                """
                - 实验空调系统如下：
                本文研究案例是针对山东省济南市某综合建筑的一层商场的
                全空气定风量空调系统进行的，其中包含建筑、空调表冷器、
                风机、蓄能水箱、冷水机、冷冻水泵、冷却水泵、冷却塔。
                因建筑只模拟了一层商场，所以当空调系统启动时，只用一
                台冷水机组与一台冷却塔来运行。 

                冷水机设置额定容量为207kw。离开冷水机时的冷冻水温度Tset=7℃。
                冷却塔风扇功率为12kw，湿球温度为28℃。系统控制主要采用通断控制，
                其中冷水机的启停根据冷冻水回水温度进行控制，风机的启停根据室内
                温度进行控制。
                """
            )

    st.write("---")
    st.subheader("3D模型展示")
    # 载入bim模型
    components.html(
        """
        <html>
        <head>
        <meta charset="utf-8">
        </head>
        <body>
        <div id="domId" style="width:1000px; height: 500px"></div>
        <script src="https://static.bimface.com/api/BimfaceSDKLoader/BimfaceSDKLoader@latest-release.js" charset="utf-8"></script>
        <script>
            let viewer3D;
            let app;
            let viewToken = '04eda9b279d44243af2f0f7f52fda856';
            let loaderConfig = new BimfaceSDKLoaderConfig();
                loaderConfig.viewToken = viewToken;
                BimfaceSDKLoader.load(loaderConfig, successCallback, failureCallback);
                function successCallback(viewMetaData) {
                    let domShow = document.getElementById('domId');
                    let webAppConfig = new Glodon.Bimface.Application.WebApplication3DConfig();
                        webAppConfig.domElement = domShow;    
                    app = new Glodon.Bimface.Application.WebApplication3D(webAppConfig);    
                    app.addView(viewToken);
                    viewer3D = app.getViewer();    
                };

                function failureCallback(error) {
                    console.log(error);
                };
        </script>
      </body>
      </html>,
    """, width=1000, height=500, scrolling=False,  # 设置尺寸，是否有滑块
    )






