class MySQLError(Exception):
    """For errors that occur with respect to the database"""

class ClientError(Exception):
    """For errors that occur with respect to the client"""

class ConnectionError(Exception):
    """Error related to the connection to the MySQL service. This could be cause by
    invalid hostname, username, password or database name."""

class NotConnected(MySQLError):
    """Error when there doesn't exist a connection to the database yet."""

    def __str__(self):
        return repr('No connection found to the database. Make a connection and try again.')

class AccessDenied(MySQLError):
    """The Host has denied access to the database. Username/Password must be wrong."""

class DatabaseNotExist(MySQLError):
    """The requested database doesn't exist. Create one/provide a new database name."""


class InvalidParameters(Exception):
    """The parameters sent are invalid."""

class NoConditionWarning(Warning):
    """No condition has been specified. All records will be affected"""

    def __str__(self):
        return repr('No Condition has been Specified. All records will be affected! \
Use \'\' as condition to overwrite.')
