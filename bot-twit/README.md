Requiremens:
- virtualenv
- direnv

How To Start:
- create a python `virtualenv venv`.
- clone this repository `git clone <repo> && cd <repo>`.
- change `source $HOME/Dev/py/py3/bin/activate` to `source path/to/venv` in `<repo>.envrc`.
- set value of `T_CONSUMER_KEY`, `T_CONSUMER_SEC=`, `T_ACCESS_TOKEN` & `T_ACCESS_TOKEN_SEC` from [Twitter Developer](https://developer.twitter.com/en/apps).
- run python script `python main.py`.
