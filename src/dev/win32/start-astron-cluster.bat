@echo off
cd "../../dependencies/astron/"

title TTE Astron
:main
astrond --loglevel info --pretty config/cluster.yml
pause
goto :main
