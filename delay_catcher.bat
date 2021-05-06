@echo off
set /p port="Delay_Catcher.py - Insert port: "
python src/delay_catcher/main.py -p %port%