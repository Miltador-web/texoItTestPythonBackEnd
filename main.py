from fastapi import FastAPI
import sqlite3
import csv


app = FastAPI()

class SqlConsulta():
        max = '''
            WITH RankedAwards AS (
            SELECT
                year,
                producers,
                winner,
                ROW_NUMBER() OVER (PARTITION BY producers ORDER BY year) AS RowAsc,
                ROW_NUMBER() OVER (PARTITION BY producers ORDER BY year DESC) AS RowDesc
            FROM awards
            )

            SELECT
            producers AS Produtor,
            MAX(year) - MIN(year) AS Intervalo,
            (SELECT year FROM RankedAwards WHERE RowAsc = 1 AND producers = a.producers) AS AnoPrimeiroPremio,
            (SELECT year FROM RankedAwards WHERE RowDesc = 1 AND producers = a.producers) AS AnoSegundoPremio
            FROM RankedAwards a
            GROUP BY producers
            HAVING COUNT(*) >= 2
            ORDER BY Intervalo DESC
            LIMIT 2;
            '''
        min = '''
            WITH RankedAwards AS (
            SELECT
                year,
                producers,
                winner,
                ROW_NUMBER() OVER (PARTITION BY producers ORDER BY year) AS RowAsc,
                ROW_NUMBER() OVER (PARTITION BY producers ORDER BY year DESC) AS RowDesc
            FROM awards
            )

            SELECT
            producers AS Produtor,
            MAX(year) - MIN(year) AS Intervalo,
            (SELECT year FROM RankedAwards WHERE RowAsc = 1 AND producers = a.producers) AS AnoPrimeiroPremio,
            (SELECT year FROM RankedAwards WHERE RowDesc = 1 AND producers = a.producers) AS AnoSegundoPremio
            FROM RankedAwards a
            GROUP BY producers
            HAVING COUNT(*) >= 2
            ORDER BY Intervalo ASC
            LIMIT 2;
            '''

def create_awards_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE awards (
            year INTEGER,
            title TEXT,
            studios TEXT,
            producers TEXT,
            winner TEXT
        )
    ''')

    with open('movielist.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            cursor.execute('INSERT INTO awards VALUES (?, ?, ?, ?, ?)', 
                        (int(row['year']), row['title'], row['studios'], row['producers'], row['winner']))
            
    conn.commit()
    return conn, cursor

def fetch_data_and_transform_result(cursor, sql_query):
    cursor.execute(sql_query)
    result = cursor.fetchall()
    transformed_result = {
        "producer": result[0][0],
        "interval": result[0][1],
        "previousWin": result[0][2],
        "followingWin": result[0][3]
    }
    return transformed_result

@app.get('/producer_max_interval')
def get_producer_max_interval():
    try:
        conn, cursor = create_awards_database()
        result = fetch_data_and_transform_result(cursor, SqlConsulta.max)
        conn.close()
        return {"max": [result]}
    except sqlite3.Error as e:
        return {'error': f"Erro ao criar o banco de dados: {e}"}

@app.get('/producer_min_interval')
def get_producer_min_interval():
    try:
        conn, cursor = create_awards_database()
        result = fetch_data_and_transform_result(cursor, SqlConsulta.min)
        conn.close()
        return {"min": [result]}
    except sqlite3.Error as e:
        return {'error': f"Erro ao criar o banco de dados: {e}"}

@app.get('/awards_interval')
def get_awards_interval():
    try:
        conn, cursor = create_awards_database()
        result_min = fetch_data_and_transform_result(cursor, SqlConsulta.min)
        result_max = fetch_data_and_transform_result(cursor, SqlConsulta.max)
        conn.close()
        return {"min": [result_min], "max": [result_max]}
    except sqlite3.Error as e:
        return {'error': f"Erro ao criar o banco de dados: {e}"}
    
