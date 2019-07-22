'''
import json
import psycopg2

connection = psycopg2.connect("host=localhost dbname=test_users user=postgres password=11111111")
cursor = connection.cursor()

data = []
with open('C:/Users/NT Алекс/Desktop/21.07.19/users_postgres/tests\/fixtures/users_test_data.json') as f:
    for line in f:
        data.append(json.loads(line))

fields = [
    'id', #varchar
    'username', #BigInt
    'email', #BigInt Nullable
    'user_address', #JSONB
    'create_user_date'
]

for item in data:
    my_data = [item[field] for field in fields]
    for i, v in enumerate(my_data):
        if isinstance(v, dict):
            my_data[i] = json.dumps(v)
    insert_query = "INSERT INTO crm VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, tuple(my_data))
'''
