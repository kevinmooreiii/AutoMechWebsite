import os

# me
PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJ_PATH, 'static/')
print(PROJ_PATH)
print(STATIC_ROOT)

# rmg
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_PATH), 'static')
print(PROJECT_PATH)
print(STATIC_ROOT)

