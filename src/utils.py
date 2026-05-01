import json
import logging
from typing import Any


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_operations(file_path: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: путь до JSON-файла
    :return: список транзакций или пустой список
    """
    logger.info(f"Попытка чтения файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

            # проверка пустого файла
            if not content.strip():
                logger.warning("Файл пустой")
                return []

            data = json.loads(content)

            if isinstance(data, list):
                logger.info("Файл успешно прочитан")
                return data

            logger.warning("JSON не является списком")
            return []

    except FileNotFoundError:
        logger.error("Файл не найден")
        return []

    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return []
