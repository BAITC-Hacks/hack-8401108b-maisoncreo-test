from classifier import classify_message


def test_info_request():
    assert classify_message("Как получить справку о месте учёбы?") == "справка"


def test_complaint():
    assert classify_message("Пропал Wi-Fi в корпусе B.") == "жалоба"


def test_other():
    assert classify_message("Хочу записаться на консультацию завтра.") == "другое"