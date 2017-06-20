import pymysql
import error
from config import config

class MySQL(object):
    """Handles the MySQL database using mysql connector/ Python"""

    def __init__(self, **kwargs):
        """Creates an instance of the MySQL Database Object"""

        config.update(**kwargs)

        self.connection = pymysql.connect(**config)

    def __str__(self):
        return """
MySQL Database
Connected to: {host}
User: {user}
Database: {database}
""".format(host=config['host'], user=config['user'], database=config['database'])

    def create_db(self, db_name):
        """Function to Create a database give database name"""
        if not self.connection:
            raise error.NotConnected
        elif db_name == '':
            raise error.InvalidParameters
        else:
            query = "CREATE DATABASE " + db_name

            with self.connection.cursor() as cursor:
                cursor.execute(query)

    def drop_db(self, db_name):
        """Function to Drop a database given its name"""
        if not self.connection:
            raise error.NotConnected
        elif db_name == '':
            raise error.InvalidParameters
        else:
            query = "DROP DATABASE " + db_name

            with self.connection.cursor() as cursor:
                cursor.execute(query)

    def use(self, db_name):
        """Function to change to another database"""
        query = "USE " + db_name

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            config.update({'database' : db_name})

    def create_table(self, table_name, columns, data_types, additional_params=None,
                     table_config=''):
        """Function to create a table."""

        if not self.connection:
            raise error.NotConnected
        elif len(columns) != len(data_types):
            raise error.InvalidParameters
        else:
            params = []
            for iterator in range(0, len(columns)):
                params.append('`' + columns[iterator] + '` ' + data_types[iterator])

            for iterator in additional_params:
                params.append(iterator)
            params = ', '.join(params)

            query = "CREATE TABLE `" + table_name + "` ( " + params + ")" + table_config + ";"

            with self.connection.cursor() as cursor:
                cursor.execute(query)
                cursor.close()

    def desc_table(self, table_name):
        """Function that gives a Description of the table"""
        if not self.connection:
            raise error.NotConnected
        else:
            query = "DESC " + table_name

            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                print result
                cursor.close()

    def insert(self, table_name='', fields=None, values=None):
        """Function to insert a record into the given table"""

        if not self.connection:
            raise error.NotConnected
        else:
            for iterator in range(0, len(values)):
                values[iterator] = str(values[iterator])

            if len(fields) == len(values):
                query = "INSERT" + " INTO `" + table_name + "` (`" + '`, `'.join(fields) + '`)' + \
                        " VALUES (" + ', '.join(values) + ");"
            elif len(fields) == 0:
                query = "INSERT " + " INTO " + table_name + " VALUES (" + ', '.join(values) + ");"

            else:
                raise error.InvalidParameters

            with self.connection.cursor() as cursor:
                print query
                cursor.execute(query)
                #self.connection.commit()
                cursor.close()

    def get_record(self, table_name, columns, condition='',
                   orderby=None, ascending=True, distinct=False):
        """Function that gets a record based on the arguments specified"""
        if not self.connection:
            raise error.NotConnected
        else:
            if len(columns) != 0:
                params = '`, `'.join(columns)
                if condition != '':
                    query = "SELECT" + ("DISTINCT" if distinct else "")\
                            + " `" + params + "` FROM " + table_name + " WHERE " + condition\
                            + (" ORDER BY `" + '`, `'.join(orderby) + "`" if orderby else "")\
                            + (" ASC " if ascending else " DSC ")

                else:
                    query = "SELECT" + ("DISTINCT" if distinct else "")\
                            + " `" + params + "` FROM " + table_name\
                            + (" ORDER BY `" + '`, `'.join(orderby) + "`" if orderby else "")\
                            + (" ASC " if ascending else " DSC ")
                print query

                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    data = zip(*result)
                    records = []
                    for iterator_1 in range(0, len(data[0])):
                        record = []
                        for iterator_2 in range(0, len(data)):
                            record.append(data[iterator_2][iterator_1])

                        records.append(record)
                    cursor.close()
                    return records

    def update(self, table_name, columns, values, condition=''):
        """Function to update records in the given Table"""
        if not self.connection:
            raise error.NotConnected
        else:
            if len(columns) != 0:
                if condition == '':
                    raise error.NoConditionWarning

                params = []
                for iterator in range(0, len(columns)):
                    params.append('`' + columns[iterator] + '` = ' + str(values[iterator]))
                params = ', '.join(params)
                query = ''
                if condition != '':
                    query = "UPDATE `" + table_name + "` SET " + params + " WHERE " + condition
                else:
                    query = "UPDATE `" + table_name + "` SET " + params

                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    self.connection.commit()
                    cursor.close()

    def delete(self, table_name, condition=''):
        """Function to delete records in the given Table"""

        if not self.connection:
            raise error.NotConnected
        else:
            if condition == '':
                raise error.NoConditionWarning
            else:
                query = "DELETE FROM `" + table_name + "` WHERE " + condition

                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    self.connection.commit()
                    cursor.close()

    def execute(self, query):
        """Function to execute any other/ custom SQL Command"""

        if not self.connection:
            raise error.NotConnected
        else:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                cursor.close()
                self.connection.commit()

    def close(self):
        """Function to close a connection if present"""

        if not self.connection:
            raise error.NotConnected
        else:
            self.connection.close()

    def __del__(self):
        self.connection.close()
