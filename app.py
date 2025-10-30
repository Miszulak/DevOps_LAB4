import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
# Używamy zmiennej środowiskowej do konfiguracji hosta Redis.
# Domyślnie ustawiamy 'localhost', jeśli zmienna nie jest dostępna.
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis = Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    try:
        # Spróbuj połączyć się i inkrementować licznik
        count = redis.incr('hits')
    except Exception as e:
        # Zwróć błąd, jeśli nie można połączyć się z Redis
        return f"Błąd połączenia z Redis ({redis_host}): {e}", 500
        
    return f'Witaj! Odwiedziłeś tę stronę {count} razy.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)