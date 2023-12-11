import sys
from cx_Freeze import setup, Executable
from pathlib import Path

# Dependencies are automatically detected, but it might need fine tuning.
EXECUTALBEL_DIR_PATH = "build"

build_exe_options = {
    "packages": ["plyer"],
    "build_exe": EXECUTALBEL_DIR_PATH
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="notifier",
    version="0.4",
    description="notifier",
    options={"build_exe": build_exe_options},
    executables=[Executable("notifier.py", base=base)],
)

# writing file
# Settings file
with open("./settings.json") as source_setting_file:
    path_to_write = str(Path(build_exe_options["build_exe"], "settings.json"))

    with open(path_to_write, "w") as destination_setting_file:
        destination_setting_file.write(source_setting_file.read())
