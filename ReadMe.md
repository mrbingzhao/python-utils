# Project
    .
    ├── LICENSE
    ├── ReadMe.md
    ├── bzutils
    │   ├── LogUtil.py
    │   └── __init__.py
    ├── dist
    │   ├── bzutil-1.0.6-py3-none-any.whl
    │   └── bzutil-1.0.6.tar.gz
    ├── pk.py
    └── setup.py

# Package
python pk.py
# Install
pip install bzutil
# Apply
    from bzutils import LogUtil
    
    logging = LogUtil.initLogConfig(__name__,'logs/eval.log',LogUtil.DEBUG)
    
    logging.debug('This is a debug message.')
    logging.info('This is an info message.')
    logging.error('This is an error message.')