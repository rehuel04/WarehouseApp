import psycopg2
from common import globalVar
from psycopg2 import Error

class ConnectServer():
    def convertDictKeyVal(self,param):
        """
        :param :  [['LOVDIVISICODE', 'LOVDIVISIDESC'], [('Q0000', 'SMS OPERATIONAL')]]
        :type  :  list
        :return:  [{'lovdivisicode': 'Q0000', 'lovdivisidesc': 'SMS OPERATIONAL'}]
        
        
        """
        coll, data = param
        result = list()
        for value in data:
            new_item = {}
            for idx, key in enumerate(coll):
                key = key.lower().replace('_','')
                new_item.update({key: value[idx]})
            result.append(new_item)
        return result

    #================================================================#

    def connectDb(self):
        try:
            stringConnection = "user='{user}' password='{password}' host='{host}' port='{port}' dbname='{database}' ".format(**globalVar.connectionDb)
            conn = psycopg2.connect(stringConnection)
            return conn
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")



    def select(self,conn,query):
        status = False
        result = []
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            status = True
            return {'status':status,'data':result}
        except (Exception,Error) as error:
            return {'status':status,'data':result}

    def selectData(self,conn,query,param):
        status = False
        result = []
        try:
            cursor = conn.cursor()
            cursor.execute(query,param)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            status = True
            return {'status':status,'data':result}
        except (Exception,Error) as error:
            return {'status':status,'data':result}

    def selectHeader(self,conn,query):
        status = False
        result = []
        try:
            header = []
            cursor = conn.cursor()
            cursor.execute(query)
            for col in cursor.description:
                        header.append(col[0])
            data = cursor.fetchall()
            result.append(header)
            result.append(data)
            cursor.close()
            conn.close()
            result = self.convertDictKeyVal(result)
            status = True
            return {'status':status,'data':result}
        except (Exception,Error) as error:
            return {'status':status,'data':result}

    def selectDataHeader(self,conn,query,param):
        status = False
        result = []
        try:
            header = []
            cursor = conn.cursor()
            cursor.execute(query,param)
            for col in cursor.description:
                        header.append(col[0])
            data = cursor.fetchall()
            result.append(header)
            result.append(data)
            cursor.close()
            conn.close()
            result = self.convertDictKeyVal(result)
            status = True
            return {'status':status,'data':result}
        except (Exception,Error) as error:
            return {'status':status,'data':result}

    def execute(self,conn,query):
        status = False
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
            status = True
            return {'status':status,'msg':"Succes"}  
        except (Exception,Error) as error:
            return {'status':status,'msg':"Error Execute"}

    def executeData(self,conn,query,param):
        status = False
        try:
            cursor = conn.cursor()
            cursor.execute(query,param)
            conn.commit()
            cursor.close()
            conn.close()
            status = True
            return {'status':status,'msg':"Succes"}  
        except (Exception,Error) as error:
            return {'status':status,'msg':"Error Execute"}