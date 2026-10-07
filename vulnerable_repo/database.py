"""
Database Connection & Query Manager
CRITICAL SECURITY VULNERABILITIES:
- Hardcoded database passwords and secret API tokens
- Direct SQL Injection via f-strings and string concatenation
- Insecure deserialization using pickle.loads()
"""

import sqlite3
import pickle

# CRITICAL SECURITY RISK: Hardcoded production secrets & passwords
api_key = "sk-live-93821038102938102938"
password = "SuperSecretAdminPassword123!"


def get_user_account(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # CRITICAL: SQL Injection via f-string interpolation
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    
    return cursor.fetchone()


def delete_user_by_name(user_name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # CRITICAL: SQL Injection via string concatenation
    query = "DELETE FROM users WHERE username = '" + user_name + "'"
    cursor.execute(query)
    conn.commit()


def restore_user_session(session_blob):
    # CRITICAL: Insecure Deserialization via pickle.loads()
    return pickle.loads(session_blob)
