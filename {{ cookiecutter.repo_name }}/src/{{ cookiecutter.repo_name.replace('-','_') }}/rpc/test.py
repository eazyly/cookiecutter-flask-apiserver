import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import json
from {{ cookiecutter.repo_name.replace('-','_') }} import app

@app.methods.add
def test():
    result = "test method"
    return result
