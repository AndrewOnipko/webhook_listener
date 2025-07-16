import logging
import os
import sys
import asyncio
from functools import wraps

script_path = os.path.abspath(sys.argv[0])
file_directory = os.path.dirname(script_path)
log_file = os.path.join(file_directory, 'logs.log')

formatter = logging.Formatter('%(asctime)s - %(message)s')

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8', mode='w'),
        logging.StreamHandler()
    ]
)

for handler in logging.getLogger().handlers:
    handler.setFormatter(formatter)

logger = logging.getLogger("main_logger")

def simple_logger(func):
        if asyncio.iscoroutinefunction(func):
            @wraps(func)
            async def async_wrapper(self, *args, **kwargs):
                logger.debug(f'Запускаем функцию {func.__name__}()')
                try:
                    return await func(self, *args, **kwargs)
                except Exception as e:
                    logger.exception(f"Ошибка в {func.__name__}():\n {e}")
                    raise
            return async_wrapper
        else:
            @wraps(func)
            def sync_wrapper(self, *args, **kwargs):
                logger.debug(f'Запускаем функцию {func.__name__}()')
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    logger.exception(f"Ошибка в {func.__name__}():\n {e}")
                    raise
            return sync_wrapper
        

def get_logger():
    return logger