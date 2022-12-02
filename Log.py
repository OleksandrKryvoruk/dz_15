"""
1. Використовуючи код домашнього завдання 1 лекції 11, додайте до
серверу чату систему логування рівня ІМЕРО, МАВМІМС і ЕБКОВ.
ЗАПУСК: СЕРВЕР - ЛОГ (КЛІЄНТ НЕ ЗАПУСКАТИ)
"""

import logging
import Client

def main():
    """
    The main entry point of the application
    """

    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("new_client.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = Client.add()
    logger.warning("Program finished")
    logger.error("Process finished without errors")

if __name__ == "__main__":
    main()