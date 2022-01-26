@echo off
cd "../../dependencies/astron/"

title TTEH Astron
:main
astrond --loglevel info --pretty config/cluster.yml
pause
goto :main
