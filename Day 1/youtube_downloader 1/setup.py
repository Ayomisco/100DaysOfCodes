from cx_Freeze import *
import sys
includefiles=['ytd.ico']
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "YouTube Downloader",
     "TARGETDIR",
     "[TARGETDIR]\youtube_downloader.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="This is a free YouTube Downloader",
    author="Ayomide Francis - Akinlolu",
    name="YouTube Downloader",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="youtube_downloader.py",
            base=base,
            icon='ytd.ico',
        )
    ]
)
