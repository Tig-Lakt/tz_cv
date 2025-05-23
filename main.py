import datetime

# Функция для получения текущего времени
def get_current_time() -> dict:
    now = datetime.datetime.now()
    iso_time = now.isoformat() + "Z"
    return {"utc": iso_time}

# Основная логика обработки сообщений
def handle_message(message: str) -> str:
    # Проверяем, спрашивает ли пользователь о времени
    if "время" in message.lower() or "time" in message.lower():
        current_time = get_current_time()
        return f"Текущее время (UTC): {current_time['utc']}"
    else:
        return 'Я могу сказать тебе текущее время. Запрос должен содержать слова "время" или "time"'

# Тестовый запуск
if __name__ == "__main__":
    while True:
        user_input = input("Пользователь: ")
        response = handle_message(user_input)
        print("Бот:", response)
