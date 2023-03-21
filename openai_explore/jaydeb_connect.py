import jaydebeapi

# Set the connection parameters
dsn_database = "database_name"
dsn_hostname = "hostname"
dsn_port = "port_number"
dsn_uid = "username"
dsn_pwd = "password"

# Set the JDBC driver class and connection string
jdbc_driver_class = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
jdbc_connection_string = f"jdbc:sqlserver://{dsn_hostname}:{dsn_port};databaseName={dsn_database}"

# Establish the connection using JayDeBeApi
conn = jaydebeapi.connect(jdbc_driver_class,
                          jdbc_connection_string,
                          [dsn_uid, dsn_pwd],
                          jars="path/to/sqljdbc42.jar")

# Execute SQL statement
cursor = conn.cursor()
cursor.execute("SELECT * FROM table_name")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

"""
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'"""

