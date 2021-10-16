import os

os.system("sudo apt-get install python3-dev")
os.system("sudo apt-get install -y libpq-dev")
os.system("sudo apt-get install -y gcc-x86-64-linux-gnu")

os.system("python3 setup.py bdist_wheel")
os.system("pip install -e .[all,dev]")
os.system("./demo/start.sh")
