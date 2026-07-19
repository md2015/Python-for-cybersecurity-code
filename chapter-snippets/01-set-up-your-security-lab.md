# 01 Set Up Your Security Lab

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 13

```text
Add Python to PATH
```

## PDF page 14

```text
python --version
python3 --version
python3 --version
```

## PDF page 15

```text
sudo apt update
sudo apt install python3 python3-pip -y
```

## PDF page 16

```python
# Windows - creates the folder on your Desktop
cd Desktop
mkdir security_tools
cd security_tools
# Mac or Linux - same result
cd ~/Desktop
mkdir security_tools
cd security_tools
```

## PDF page 17

```python
# Windows
python -m venv venv
# Mac or Linux
python3 -m venv venv
# Windows
venv\Scripts\activate
# Mac or Linux
source venv/bin/activate
```

## PDF page 18

```text
(venv) C:\Desktop\security_tools>
pip is Python's package installer. It downloads libraries from the Python 
Package Index, a public repository with hundreds of thousands of packages. 
pip comes bundled with Python so there is nothing extra to install.
requests
scapy
```

## PDF page 19

```python
pip install -r requirements.txt
pip list
print("My security lab is ready. Let's build something.")
```

## PDF page 20

```python
# Windows
python hello.py
# Mac or Linux
python3 hello.py
My security lab is ready. Let's build something.
```

## PDF page 21

```text
cd foldername: Change Directory. Moves your terminal into a specific 
folder. cd Desktop moves you to the Desktop. cd security_tools moves you 
into that project folder.
cd ..: Moves up one level. If you are inside security_tools, cd .. 
takes you back to Desktop.
python filename.py: Runs a Python script. Replace filename.py with 
the actual script name.
pip install library: Installs a Python library into the active 
virtual environment.
pip list: Shows all installed libraries in the current environment.
```

