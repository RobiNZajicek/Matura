import logging
logging.basicConfig(level=logging.INFO,filename='myapp.log',filemode='w',format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
logger = logging.getLogger(__name__)
def main():
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('crit')
if __name__ == '__main__':
    main()  