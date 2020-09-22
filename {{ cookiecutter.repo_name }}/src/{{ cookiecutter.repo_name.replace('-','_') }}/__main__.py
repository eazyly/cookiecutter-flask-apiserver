import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from {{ cookiecutter.repo_name.replace('-','_') }} import app

app.run(host=app.config['HOST'], port=app.config['PORT'], threaded=app.config['THREADED'])
