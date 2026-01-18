from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "comments.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            comment TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        comment = request.form.get("comment", "").strip()

        if not name or not comment:
            return jsonify({"status": "error", "message": "Invalid input"}), 400

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO comments (name, comment) VALUES (?, ?)",
            (name, comment)
        )
        conn.commit()
        conn.close()

        # Support both AJAX and normal form submit
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"status": "success"})

        return redirect(url_for("index"))

    conn = get_db_connection()
    comments = conn.execute(
        "SELECT name, comment FROM comments ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template("index.html", comments=comments)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
