#!/usr/bin/python3
import sys
import os
import csv
import mysql.connector

def connect_db():
    """
    connect to a mysql server
    """
    try:
        conx = mysql.connector.connect(
                host= "127.0.0.1",
                port=3306,
                user="root",
                password="mypass")
        # get a cursor
        # A cursor is the object go after a succesful connection
        # The cursor is used to run SQL commands
        cur = conx.cursor()
        cur.execute("SELECT CURDATE()")
        date_result = cur.fetchone()

        return conx

    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        return None
def create_database(connection):
    """
    Create database and table 
    """
    cur = connection.cursor()
    try:
        cur.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("Database 'ALX_prodev created successfully")

        return True

    except mysql.connector.Error as e:
        print(f"Error creating database:{e}")
        return False

def connect_to_prodev():
    """
    connnet to prodev database
    """
    try:
        db_to_use= mysql.connector.connect(
                host= 'localhost', 
                port=3306,
                user='root',
                password='mypass',
                database='ALX_prodev')
        print("Succesfully seleted the 'ALX_prodev' DB")
        return db_to_use
    except mysql.connector.Error as e:
        print(f"Error conecting to the database 'ALX_prodev': {e}")
        return None

def create_table(connection):
    """ creates the table 'user_data' if it does not exist
    """
    cur = None
    cur = connection.cursor()
    create_table_query="""
        CREATE TABLE IF NOT EXISTS user_data
        (user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3,0) NOT NULL)
        """
    try:
        cur.execute(create_table_query)
        print("successfully created user_data table")
    except mysql.connector.Error as e:
        print(f"Unable to create database:{e}")
    finally:
        if cur:
            cur.close()


def insert_data(connection, data):
    """
    insert data into the db if it does not exist
    The function takes input from the connection created and data which is our file
    """
    # data insertion
    cur = None
    insert_query="""
    INSERT IGNORE INTO user_data
    (user_id, name, email, age) VALUES
    (UUID(), %s, %s, %s)
    """
    try:
        cur = connection.cursor()
        with open(data, 'r') as csvfile:
            read_data = csv.reader(csvfile)
            next(read_data) # skip the first line of data that contains column names
            # convert items to a list
            list_of_rows_for_db = list(read_data)

            # do a quick check to confirm that the items we are working with are in a list
            if list_of_rows_for_db:
                cur.executemany(insert_query, list_of_rows_for_db)
            else:
                print("No data found in the CSV file")

        connection.commit()
        print("Data written to the table 'user_data'")
    except mysql.connector.Error as e:
        print(f"Unable to add data into the table 'user_data':{e}")
    except FileNotFoundError:
        print(f"Error: {data} not found")
    finally:
        if cur:
            cur.close()


#if __name__ == "__main__":
#     final = connect_db()
#     db_creation = create_database(final)
 #    tb_selection = connect_to_prodev()
 #    tb_creation = create_table(tb_selection)
 #    insert_data(tb_selection, 'user_data.csv')
