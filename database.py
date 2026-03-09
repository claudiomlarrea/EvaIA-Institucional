import sqlite3
import os

DB_PATH = "data/evaia.db"


def conectar():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)
