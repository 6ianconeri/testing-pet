# Примерны тестов с SQL

def test_user_query(db_connection):
    db_connection.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                          ("John", "john@mail.com")
                        )
    cursor = db_connection.execute("SELECT * FROM users WHERE name = 'John'")
    result = cursor.fetchone()

    assert result[1] == "John"
    assert result[2] == "john@mail.com"