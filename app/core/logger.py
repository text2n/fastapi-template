import logging

logging.basicConfig(filename='storage/logs/app.log',level=logging.INFO , format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
