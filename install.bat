@echo off
echo INSTALLING HMS....
python -m venv virt
call virt/Scripts/activate.bat
pip install -r requirements.txt
echo Done!

