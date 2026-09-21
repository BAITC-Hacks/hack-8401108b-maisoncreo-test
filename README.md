
# hack-8401108b-maisoncreo-test

Hackathon team repository for Maisoncreo_test

## Task 01 — Request Classifier

Reads 5 Russian-language requests from `task01_classifier/messages.txt`, classifies each request into one of three categories:

- `справка`
- `жалоба`
- `другое`

and generates one draft response in Russian.

The classifier uses simple deterministic keyword-based rules and does not require an external API or LLM.

### Run

```bash
python task01_classifier/classifier.py task01_classifier/messages.txt
```

### Result

```text
1. Как получить справку о месте учёбы?
   Категория: справка

2. В столовой очередь, еда холодная.
   Категория: жалоба

3. Хочу записаться на консультацию завтра.
   Категория: другое

4. Пропал Wi-Fi в корпусе B.
   Категория: жалоба

5. Где парковка для гостей?
   Категория: справка
```

The program also prints one Russian draft response for every request.

## Task 02 — Alert Filter

Reads 8 events from `task02_alert_filter/events.json` and keeps only events whose `level` is `critical`.

### Run

```bash
python task02_alert_filter/alert_filter.py task02_alert_filter/events.json
```

### Result

```text
disk 90%
payment failed
db timeout
критичных 3
```

## Tests

The project uses `pytest` for simple automated checks.

Install it if necessary:

```bash
python -m pip install pytest
```

Run all tests:

```bash
python -m pytest -q
```

Expected result:

```text
4 passed
```
