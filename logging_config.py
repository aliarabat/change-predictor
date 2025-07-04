import logging

# from rich.logging import RichHandler


def get_logger(name="change-predictor", level=logging.INFO, log_filename: str = "application"):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(name)s - %(message)s",
            # handlers=[RichHandler(markup=True)]
            filename=f"{log_filename}.log",
        )
        logger.info(f"{name} Logger has been initialized...")
    return logger