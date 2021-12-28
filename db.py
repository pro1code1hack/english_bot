import mysql.connector

db = mysql.connector.connect(host='localhost', username='root', password='root', database='bot')
db.autocommit = True


def insert(table_name: str, column_values: dict) -> None:
    cursor = get_cursor()
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = '%s, ' * len(column_values.keys())
    placeholders = placeholders.rstrip(', ')
    sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.executemany(sql_statement, values)
    db.commit()


def get_cursor():
    return db.cursor(buffered=True)

def get_db():
    return db

