#source me 
python3.10 -m venv .
source bin/activate.csh
pip install pip-tools
rehash
pip-compile
pip-sync
