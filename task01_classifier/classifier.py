import sys


def load_messages(path):
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def classify_message(message):
    text = message.lower()

    complaint_keywords = [
        "очередь",
        "холодная",
        "пропал",
        "не работает",
        "сломался",
        "проблема",
    ]

    info_keywords = [
        "как получить",
        "где",
    ]

    if any(keyword in text for keyword in complaint_keywords):
        return "жалоба"

    if any(keyword in text for keyword in info_keywords):
        return "справка"

    return "другое"


def generate_draft(message, category):
    if category == "жалоба":
        return (
            "Спасибо за сообщение. "
            "Передадим информацию ответственным сотрудникам для проверки."
        )

    if category == "справка":
        return (
            "Здравствуйте! Поможем вам с этим вопросом. "
            "Уточните, пожалуйста, необходимые детали."
        )

    return (
        "Здравствуйте! Спасибо за обращение. "
        "Уточните, пожалуйста, детали вашего запроса."
    )


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "messages.txt"

    messages = load_messages(path)

    for number, message in enumerate(messages, start=1):
        category = classify_message(message)
        draft = generate_draft(message, category)

        print(f"{number}. {message}")
        print(f"Категория: {category}")
        print(f"Ответ: {draft}")
        print()


if __name__ == "__main__":
    main()
    