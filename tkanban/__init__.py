"""
File         : __init__.py
Description  : 

Author       : MrChuckomo
Version      : v0.1.0
Creation Date: 01-Jun-2021
"""

import os

# ---------------------------------------------------------------------------------------------------------------------

CTX = os.path.abspath(os.path.dirname(__file__))

RES_FOLDER = f'{CTX}{os.sep}..{os.sep}res{os.sep}'
DB_FILE = f'{RES_FOLDER}kanban.db'
