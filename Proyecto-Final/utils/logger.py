import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Crear la carpeta de logs si no existe
        os.makedirs("logs", exist_ok=True)
        
        file_handler = logging.FileHandler("logs/execution.log", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger