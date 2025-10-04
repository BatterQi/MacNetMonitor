"""
setup.py for NetMonitor
打包 macOS 菜单栏应用（使用 py2app）
"""

from setuptools import setup

# 主程序入口（相对于 setup.py 的路径）
APP = ['NetMonitor.py']

# 额外资源文件（如图标、配置等，目前为空）
DATA_FILES = []

# py2app 打包选项
OPTIONS = {
    'argv_emulation': False,  # 允许模拟命令行参数（双击运行兼容）
    'plist': {
        'LSUIElement': True,  # 关键！隐藏 Dock 图标，仅显示菜单栏
    },
    # 显式包含依赖包（避免打包后找不到模块）
    'packages': ['rumps', 'psutil'],
    # 可选：排除不需要的模块以减小体积
    # 'excludes': ['tkinter', 'unittest', 'email', 'xml'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],  # 构建时需要 py2app
)