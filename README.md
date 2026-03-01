# Random Compliment Generator

A beginner-friendly API built with [Sanic](https://sanic.dev) that returns a random compliment on every request.

## Endpoints

| Method | Route | Description |
|--------|-------------|----------------------------------|
| GET | `/` | Welcome message with usage hint |
| GET | `/compliment` | Returns a random compliment |

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:8000/compliment in your browser.

## Example Response

```json
{ "compliment": "You have a heart of gold." }
```
