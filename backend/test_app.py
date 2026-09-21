from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        database=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        port=5432
    )


@app.route("/")
def home():
    return "Hello from Backend!"


@app.route("/health")
def health():
    return "OK"


@app.route("/db-test")
def db_test():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT version();")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify({
            "status": "connected",
            "database": result[0]
        })

    except Exception as e:
        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)