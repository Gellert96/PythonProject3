import logging


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")

file_formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX"""
    logger.info("Начато маскирование номера карты")

    try:
        if not card_number or len(card_number) < 16:
            logger.error("Некорректный номер карты")
            return ""

        first_six = card_number[:6]
        last_four = card_number[-4:]
        masked = first_six + "**" + "****" + last_four

        result = f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:16]}"

        logger.info(f"Маскирование завершено: {result}")

        return result

    except Exception as e:
        logger.error(f"Ошибка при маскировании карты: {e}")
        return ""


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формате **XXXX"""
    logger.info("Начато маскирование счета")

    try:
        if not account_number or len(account_number) < 4:
            logger.error("Некорректный номер счета")
            return ""

        result = f"**{account_number[-4:]}"

        logger.info(f"Маскирование завершено: {result}")

        return result

    except Exception as e:
        logger.error(f"Ошибка при маскировании счета: {e}")
        return ""
