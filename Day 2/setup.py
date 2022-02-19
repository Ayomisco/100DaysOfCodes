from cx_Freeze import *
import sys
includefiles=['calc.ico']
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Ayomisco Calc",
     "TARGETDIR",
     "[TARGETDIR]\Ayomisco calc.exe",
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
    description="This is a simple Desktop calculator",
    author="Ayomide Francis - Akinlolu",
    name="Ayomisco calc",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="calculator.py",
            base=base,
            icon='calc.ico',
        )
    ]
)
