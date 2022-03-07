import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"include_files": ["C:/Users/marli/AppData/Local/Programs/Python/Python39/Lib/_strptime.py"],
                     "packages": ["os", "configparser", "binance", "binance.client", "binance.enums"],
                     "includes": ["configparser", "binance", "binance.client", "binance.enums", "time"],
                     "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
#base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

setup(
    name="Binance API",
    version="0.1",
    description="Gestão de carteira Binance automatizada",
    options={"build_exe": build_exe_options},
    executables=[Executable("Binance_API.py", )]
)