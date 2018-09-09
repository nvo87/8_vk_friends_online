# Watcher of Friends Online

This script will request and output friends online list via vk python module.  
All you need is start script and type your login, password.  
Getpass module makes your password chars hidden.

# How to Install

Script requires vk module. You may download it wit pip.  
Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# How to run

Just type
```
python vk_friends_online.py
```
  
Then you have to input your login and password.

As a result, you'll get your online friends list:
```
Alex Petrov
Max Ivanov
Sergey Kozlov
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
