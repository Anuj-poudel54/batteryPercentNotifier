import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["plyer"]
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="notifier",
    version="0.1",
    description="Program to notify whether to plug or unplug the charger!",
    options={"build_exe": build_exe_options},
    executables=[Executable("notifier.py", base=base)],
)