import cx_Freeze
import sys

base = None

if sys.platform == 'win64':
    base = "Win64GUI"

executables = [cx_Freeze.Executable("manageacc.py", base=base, icon="maicon.png")]

cx_Freeze.setup(
    name = "manageacc",
    options = {"build_exe": {"packages":["tkinter","sqlite3","tkcalendar","datetime"], "include_files":["accdatabase.py","exp.py","placeholder.py","manageaccountsdb"]}},
    version = "0.01",
    description = "Account Management application",
    executables = executables
    )