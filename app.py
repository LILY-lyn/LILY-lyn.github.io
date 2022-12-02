import streamlit as st
import home_page, introduce_page, test_page, user_page
import datetime


def app():
    class MultiApp:

        def __init__(self):
            self.apps = []
            self.apps_dict = {}

        def add_app(self, header, func):
            if header not in self.apps:
                self.apps.append(header)
                self.apps_dict[header] = func

        st.sidebar.write("    ")
        st.sidebar.write("    ")

        def run(self):
            header = st.sidebar.radio('选择需要跳转的页面',
                                      self.apps, format_func=lambda header: str(header))
            self.apps_dict[header]()

    app = MultiApp()

    # 添加多页
    app.add_app("首 页", home_page.app)
    app.add_app("实验介绍", introduce_page.app)
    app.add_app("实验操作", test_page.app)
    app.add_app("用户中心", user_page.app)

    # 运行程序
    app.run()

    # 显示当前时间
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%X')
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(now_time)


def main():
    app()


if __name__ == '__main__':
    main()