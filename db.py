import sqlite3

# Connect to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('BAA_1.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table (if not exists)
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL,
#         password1 TEXT NOT NULL,
#         first_name TEXT NOT NULL,
#         other_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         phone_no TEXT NOT NULL,
#         id_no TEXT NOT NULL
#     )
# ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS B1_DATA (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        other_name TEXT NOT NULL,
        name_of_the_father TEXT NOT NULL,
        sex TEXT NOT NULL,
        DOB DATETIME NOT NULL,
        nature_of_birth TEXT NOT NULL,
        weigth_of_birth TEXT,
        type_of_birth TEXT,
        facility TEXT NOT NULL,
        sub_county TEXT NOT NULL,
        notification_issued_to TEXT,
        NATIONALITY TEXT,
        NATIONAL_ID_NO INT
    )
''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS D1_DATA (
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL,
#         password1 TEXT NOT NULL,
#         first_name TEXT NOT NULL,
#         other_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         phone_no TEXT NOT NULL,
#         id_no TEXT NOT NULL
#     )
# ''')

# Insert data into the table
# cursor.execute('''
#     INSERT INTO users (username, password, password1, first_name, other_name, last_name, phone_no, id_no) 
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', 

#     # ('Janepher', '123456','123456', 'janepher', 'janny', 'janipher', '0745698043', '35629696')
#     # ('lilian', 'password','password', 'lilian', 'mapesa', 'obonyo', '0745698042', '35629695')
#     # ('naomi', 'password','password', 'bukutsa', 'naomi', 'obonyo', '0745698042', '35629695')
# )

cursor.execute('''
    INSERT INTO B1_DATA (first_name, other_name, name_of_the_father, sex, DOB, nature_of_birth,
    weigth_of_birth, facility, sub_county, type_of_birth, NATIONALITY,NATIONAL_ID_NO
    ) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', 
    ('bless','blessing','juma','male','2/4/2012','3kg','butere','normal','kenya',122345)
)

# Commit the changes
conn.commit()

# Query data from the table
cursor.execute('SELECT * FROM users')
result = cursor.fetchall()
print("User data:")
for row in result:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
