import logging

def get_logger():
    logging.basicConfig(
        filename='logs/bot.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger("Omni-B0T")
