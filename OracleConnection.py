"""
    OracleConnection Class Description:
    Create/Pass connection to
    execute sql statements

"""
import sys
import cx_Oracle
from AppendStringToFile import *


class OracleConnection(object):
    """
        Create/Pass connection class

    """

    def __init__(self):
        print('Initiating Connection')

    @staticmethod
    def connect(filename):
        username = 'query'
        password = 'query1'
        a = AppendStringToFile()

        # Connect to oracle and run a function and procedure.
        try:
            conn = cx_Oracle.Connection(username + '/' + password + '@172.16.0.35:1521/prd11g.cashco.com')
        except cx_Oracle.DatabaseError:
            print('Oracle Error: ')
            a.to_file(filename, 'Login Error: Program will Close.\n', 1).to_file()
            sys.exit()

        return conn
