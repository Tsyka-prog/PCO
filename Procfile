web:uvicorn app:app --host=0.0.0.0 --port=${PORT:8000}
heroku ps:scale --app index.html web=1
heroku ps:scale --app api/main.py worker=1
