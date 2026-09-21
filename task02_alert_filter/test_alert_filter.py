from alert_filter import filter_critical


def test_filter_critical():
    events = [
        {"level": "critical", "msg": "disk 90%"},
        {"level": "info", "msg": "user login"},
        {"level": "warn", "msg": "cache miss"},
        {"level": "critical", "msg": "db timeout"},
    ]

    result = filter_critical(events)

    assert len(result) == 2
    assert result[0]["msg"] == "disk 90%"
    assert result[1]["msg"] == "db timeout"