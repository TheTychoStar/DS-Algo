import psycopg2
from configparser import ConfigParser


# set up connection to local db
def config(filename='database_hw2.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


# Set up cursor in PostgreSQL
def cursor_setup():
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # return current db connector
        return conn
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

# drop all 4 tables, vendor_parts, part_drawings, parts, vendors
def drop_table():
    conn = None
    try:
        conn = cursor_setup()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS vendor_parts, part_drawings, parts, vendors")
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None :
            conn.close()


# Execute sql command to create table, insert multi rows, update row
def execute_sql(sqlCommand):
    conn = None
    try:
        conn = cursor_setup()
        # Create a cursor
        cur = conn.cursor()
        # create table one by one
        cur.execute(sqlCommand)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Get result from sql query
def get_fetchresult(sqlCommand, fetchtype):
    conn = None
    try:
        conn = cursor_setup()
        # Create a cursor
        cur = conn.cursor()
        # create table one by one
        cur.execute(sqlCommand)
        #
        row = None
        rows = None
        if fetchtype == 1:
            row = cur.fetchone()
            while row is not None:
                print(row)
                row = cur.fetchone()
        elif fetchtype == 2:
            rows = cur.fetchall()
            for row in rows:
                print(row)
        elif fetchtype == 3:
            for row in iter_row(cur, 10):
                print(row)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#
def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

# Select the DVD with highest replacement cost from film table
def get_highestReplacement(sqlCommand):
    conn = None
    try :
        conn = cursor_setup()
        # Create a cursor
        cur = conn.cursor()
        # create table one by one
        cur.execute(sqlCommand)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        if conn is not None :
            conn.close()

if __name__ == '__main__':
    # drop all 4 tables if exists
    drop_table()

    # Create a new table 'vendors'
    # First, specify 'vendors" as the name of table
    # Second, create two columns in the vendors table.
    # Third, a primary key column uniquely identify rows in a table. A table can have one and only one primary key.
    # The primary key constraint allows you to define the primary key of a table.
    table_name = "vendors"
    commands = "CREATE TABLE IF NOT EXISTS " + table_name + " (" \
                                                            "VENDOR_ID  SERIAL PRIMARY KEY, " \
                                                            "VENDOR_NAME    VARCHAR(255) NOT NULL)"

    execute_sql(commands)
    table_name = "parts"
    commands = "CREATE TABLE IF NOT EXISTS " + table_name + " (" \
                                                            "PART_ID  SERIAL PRIMARY KEY, " \
                                                            "PART_NAME    VARCHAR(255) NOT NULL)"
    execute_sql(commands)
    # FOREIGN KEY – ensures values in a column or a group of columns from a table exists in a column or group
    # of columns in another table. Unlike the primary key, a table can have many foreign keys.
    # The table that contains the foreign key is called the referencing table or child table.
    # In below sample, part_drawing is child table.
    # The table referenced by the foreign key is called the referenced table or parent table.
    # In below sample, parts is parent table.
    # Here I specified part_drawings.part_id as foreign key columns
    # and specified parent table 'parts' and parent key column 'part_id' referenced by
    # the foreign key columns in the REFERENCES clause
    # Finally, the ON UPDATE determine the behaviors when the primary key in the parent table
    # is updated.
    # CASCADE, once the parts.part_id is updated, the part_drawings.part_id would
    # also be updated
    table_name = "part_drawings"
    commands = "CREATE TABLE IF NOT EXISTS " + table_name + " (" \
                                                           "PART_ID  INTEGER PRIMARY KEY, " \
                                                           "FILE_EXTENSION   VARCHAR(5) NOT NULL, " \
                                                           "DRAWING_DATA BYTEA NOT NULL, " \
                                                           "FOREIGN KEY(PART_ID) " \
                                                           "REFERENCES PARTS(PART_ID) " \
                                                           "ON UPDATE CASCADE ON DELETE CASCADE)"
    execute_sql(commands)

    table_name = "vendor_parts"
    commands = "CREATE TABLE IF NOT EXISTS " + table_name + " (" \
                                                            "VENDOR_ID    INTEGER NOT NULL, " \
                                                            "PART_ID  INTEGER NOT NULL, " \
                                                            "PRIMARY KEY(VENDOR_ID, PART_ID), " \
                                                            "FOREIGN KEY(VENDOR_ID) " \
                                                            "REFERENCES VENDORS(VENDOR_ID) " \
                                                            "ON UPDATE CASCADE ON DELETE CASCADE, " \
                                                            "FOREIGN KEY(PART_ID) " \
                                                            "REFERENCES PARTS(PART_ID) " \
                                                            "ON UPDATE CASCADE ON DELETE CASCADE)"
    execute_sql(commands)

    # Insert one row into table vendors
    # I added Geosoft Inc as new vendor
    vendor_name="'Geosoft Inc.'"
    commands = "INSERT INTO VENDORS(VENDOR_NAME) " \
               "VALUES("+vendor_name+") RETURNING VENDOR_ID;"
    execute_sql(commands)

    # Insert multi fows into vendors table
    commands = "INSERT INTO VENDORS(VENDOR_NAME) " \
               "VALUES('ASK SEIMICONDUCTOR INC.'), " \
               "('ASAKI GLASS CO LTD.'), " \
               "('DAIKIN INDUSTRIES LTD.'), " \
               "('DYNACAST INTERNATIONAL INC.'), " \
               "('FOSTER ELECTRIC CO. LTD.'), " \
               "('MURATA MANUFACTURING CO. LTD.')"
    execute_sql(commands)

    # Update the row in table vendors
    # I will update the record whose vendor is Geosoft Inc.
    commands = "UPDATE vendors SET vendor_name='Seequent Inc.' WHERE vendor_id=1"
    execute_sql(commands)

    # Query data using fetchone() method
    # The  fetchone() fetches the next row in the result set.
    # It returns a single tuple or None when no more row is available.
    commands = "SELECT VENDOR_ID, VENDOR_NAME FROM VENDORS " \
               "ORDER BY VENDOR_NAME"
    print("The result below is queried by fetchone() method.")
    get_fetchresult(commands, 1)
    # Query data using fetchall() method
    # The  fetchall() fetches all rows in the result set and returns a list of tuples.
    # If there are no rows to fetch, the  fetchall() method returns an empty list.
    print("The result below is queried by fetchall() method.")
    get_fetchresult(commands, 2)

    # Query data using fetchmany() method
    # The  fetchmany(size=cursor.arraysize) fetches the next set of rows specified by the size parameter.
    # If you omit this parameter, the arraysize will determine the number of rows to be fetched.
    # The  fetchmany() method returns a list of tuples or an empty list if no more rows available.
    commands = "SELECT VENDOR_ID, VENDOR_NAME FROM VENDORS " \
               "ORDER BY VENDOR_NAME"
    print("The result below is queried by fetchmany() method, size equals to 10")
    get_fetchresult(commands, 3)


    # Find the highest replacement_cost from film table
    print("The result below returns the DVD title which has highest replacement cost.")
    commands = "SELECT TITLE, REPLACEMENT_COST FROM FILM ORDER BY REPLACEMENT_COST DESC LIMIT 5"
    get_fetchresult(commands, 2)

    # Find the sum of replacement_cost of DVDs whose title start from B
    print("The result below returns the total cost of DVD from film table.")
    commands = "SELECT SUM(REPLACEMENT_COST) FROM FILM WHERE TITLE LIKE 'B%'"
    get_fetchresult(commands, 2)

    # Using Postgresql inner join to join customer and payment tables.
    # Whenever a customer makes a payment, a new row is inserted into the payment table. Each customer may have
    # many payments. Each payment belongs to one and only one customer. The customer_id column establishes the
    # relationship between the two tables
    print("The result below return INNER JOINT ")
    commands = "SELECT " \
               "customer.customer_id, " \
               "first_name, " \
               "last_name, " \
               "amount, " \
               "payment_date " \
               "FROM " \
               "customer " \
               "INNER JOIN payment " \
               "ON payment.customer_id = customer.customer_id " \
               "ORDER BY payment_date " \
               "LIMIT 5;"
    get_fetchresult(commands, 2)

    # Using Postgresql left join to join film and inventory table
    # Each row in the film table may have zero or many rows in the inventory table.
    # Each row in the inventory table has one and only one row in the film table.
    # The film_id column establishes the link between the film and inventory tables.
    # The following statement uses the LEFT JOIN clause to join film table with the inventory table
    print("LEFT JOIN , join film table with inventory table")
    commands = "SELECT " \
               "film.film_id, " \
               "title, " \
               "inventory_id " \
               "FROM " \
               "film " \
               "LEFT JOIN inventory " \
               "ON inventory.film_id = film.film_id " \
               "ORDER BY title " \
               "LIMIT 5;"
    get_fetchresult(commands, 2)

    print("RIGHT JOIN , join film table and inventory table")
    commands = "SELECT " \
               "inventory.last_update " \
               "FROM " \
               "inventory " \
               "RIGHT JOIN film " \
               "using (film_id)" \
               "LIMIT 5;"
    get_fetchresult(commands, 2)

    # UNION operation with table language and category
    print("The result below unions table language dna category.")
    commands = "SELECT * " \
               "FROM language " \
               "UNION ALL " \
               "SELECT * FROM category;"
    get_fetchresult(commands, 2)










