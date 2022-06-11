from typing_extensions import Self
from psycopg2 import connect
from common.connectDb import ConnectServer
from psycopg2 import Error
connection = ConnectServer()


class MasterSuplier():
    def getDataSuplier():
        try:
            conn = connection.connectDb()
            query = """SELECT suplier_pk as suplier_id, suplier_name as suplier_name FROM samb.master_suplier"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def updateDataSuplier(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """UPDATE samb.master_suplier
                    SET suplier_name=%(editsupliername)s
                    WHERE suplier_pk=%(editsuplierid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataSuplier(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """INSERT INTO samb.master_suplier
                       (suplier_pk, suplier_name)
                       VALUES(%(inputsuplierid)s, %(inputsupliername)s);"""

            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def deleteDataSuplier(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """DELETE FROM samb.master_suplier
                    WHERE suplier_pk=%(suplierid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

class MasterCustomer():
    def getDataCustomer():
        try:
            conn = connection.connectDb()
            query = """SELECT customer_pk as customer_id, customer_name as customer_name FROM samb.master_customer"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def updateDataCustomer(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """UPDATE samb.master_customer
                    SET customer_name=%(editcustomername)s
                    WHERE customer_pk=%(editcustomerid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataCustomer(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """INSERT INTO samb.master_customer
                       (customer_pk, customer_name)
                       VALUES(%(inputcustomerid)s, %(inputcustomername)s);"""

            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def deleteDataCustomer(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """DELETE FROM samb.master_customer
                    WHERE customer_pk=%(customerid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

class MasterProduct():
    def getDataProduct():
        try:
            conn = connection.connectDb()
            query = """SELECT product_pk as product_id, product_name as product_name FROM samb.master_product"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def updateDataProduct(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """UPDATE samb.master_product
                    SET product_name=%(editproductname)s
                    WHERE product_pk=%(editproductid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataProduct(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """INSERT INTO samb.master_product
                       (product_pk, product_name)
                       VALUES(%(inputproductid)s, %(inputproductname)s);"""

            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def deleteDataProduct(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """DELETE FROM samb.master_product
                    WHERE product_pk=%(productid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

class MasterWarehouse():
    def getDataWarehouse():
        try:
            conn = connection.connectDb()
            query = """SELECT warehouse_pk as warehouse_id, warehouse_name as warehouse_name FROM samb.master_warehouse"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def updateDataWarehouse(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """UPDATE samb.master_warehouse
                    SET warehouse_name=%(editwarehousename)s
                    WHERE warehouse_pk=%(editwarehouseid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataWarehouse(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """INSERT INTO samb.master_warehouse
                       (warehouse_pk, warehouse_name)
                       VALUES(%(inputwarehouseid)s, %(inputwarehousename)s);"""

            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def deleteDataWarehouse(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """DELETE FROM samb.master_warehouse
                    WHERE warehouse_pk=%(warehouseid)s;"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

