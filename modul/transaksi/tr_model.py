from typing_extensions import Self
from psycopg2 import connect
from common.connectDb import ConnectServer
from psycopg2 import Error
connection = ConnectServer()

class TransaksiPenerimaan():
    def getDataTransaksiPenerimaan():
        try:
            conn = connection.connectDb()
            query = """SELECT trx_in_pk as penerimaanid, trx_in_no as nomortransaksipenerimaan, warehouse_name as gudangasalpenerimaan, 
                        trx_in_date as tgllpenerimaan, suplier_name as suplierpenerimaan, trx_in_notes as notepenerimaan 
                        FROM samb.transaksi_penerimaan_barang_head,samb.master_warehouse, samb.master_suplier
                        WHERE trx_in_whs_idf = warehouse_pk and trx_in_supp_idf = suplier_pk"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def getDataGudangOption():
        try:
            conn = connection.connectDb()
            query = """SELECT warehouse_pk as id, warehouse_name as value FROM samb.master_warehouse"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def getDataSuplierOption():
        try:
            conn = connection.connectDb()
            query = """SELECT suplier_pk as id, suplier_name as value FROM samb.master_suplier"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def getDataProductOption():
        try:
            conn = connection.connectDb()
            query = """SELECT product_pk as id, product_name as value FROM samb.master_product"""
            result = connection.selectHeader(conn,query)
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataPenerimaanHead(param):
        try:
            conn = connection.connectDb()
            query = """INSERT INTO samb.transaksi_penerimaan_barang_head
                        (trx_in_no, trx_in_whs_idf, trx_in_date, trx_in_supp_idf, trx_in_notes)
                        VALUES(%(inputnomorpenerimaan)s, %(inputgudang)s, now() ,%(inputsuplier)s, %(inputpenerimaannote)s);"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def getDataTransaksiPenerimaanDetail(param):
        try:
            conn = connection.connectDb()
            query = """SELECT trx_in_d_pk as penerimaandetailiddetail, trx_in_d_idf as nomortransaksipenerimaandetail, product_name as namaproduct, trx_in_d_qty_dus as jumlahdus, trx_in_d_qty_pcs as jumlahpcs
                       FROM samb.transaksi_penerimaan_barang_detail,samb.master_product
                       WHERE trx_in_d_product_idf = product_pk and trx_in_d_idf=%(nomortransaksi)s;
                    """
            result = connection.selectDataHeader(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataPenerimaanDetail(param):
        try:
            conn = connection.connectDb()
            query = """INSERT INTO samb.transaksi_penerimaan_barang_detail
                        (trx_in_d_idf, trx_in_d_product_idf, trx_in_d_qty_dus, trx_in_d_qty_pcs)
                        VALUES(%(nomortransaksi)s, %(inputproductdetail)s, %(inputpenerimaandetaildus)s, %(inputpenerimaandetailpcs)s);"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def updateDataPenerimaanDetail(param):
        try:
            conn = connection.connectDb()
            query = """UPDATE samb.transaksi_penerimaan_barang_detail
                        SET trx_in_d_product_idf=%(editpenerimaandetailproduct)s, trx_in_d_qty_dus=%(editpenerimaandetaildus)s, trx_in_d_qty_pcs=%(editpenerimaandetailpcs)s
                        WHERE trx_in_d_pk=%(editpenerimaandetailid)s and trx_in_d_idf = %(editpenerimaandetailnomor)s;
                        """
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def deleteDataPenerimaanDetail(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """DELETE FROM samb.transaksi_penerimaan_barang_detail
                        WHERE trx_in_d_pk=%(penerimaandetailiddetail)s and trx_in_d_idf = %(nomortransaksipenerimaandetail)s;
                        """
            print(query%param)
            result = connection.executeData(conn,query,dict(param))
            print("askdjhaksjdhkajwhdk",result)
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

class TransaksiPengeluaran():
    def getDataTransaksiPengeluaran():
        try:
            conn = connection.connectDb()
            query = """SELECT trx_out_pk as pengeluaranid, trx_out_no as nomortransaksipengeluaran, warehouse_name as gudangasalpengeluaran, 
                        trx_out_date as tgllpengeluaran, suplier_name as suplierpengeluaran, trx_out_notes as notepengeluaran 
                        FROM samb.transaksi_pengeluaran_barang_head,samb.master_warehouse, samb.master_suplier
                        WHERE trx_out_whs_idf = warehouse_pk and trx_out_supp_idf = suplier_pk"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def getDataGudangOption():
        try:
            conn = connection.connectDb()
            query = """SELECT warehouse_pk as id, warehouse_name as value FROM samb.master_warehouse"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def getDataSuplierOption():
        try:
            conn = connection.connectDb()
            query = """SELECT suplier_pk as id, suplier_name as value FROM samb.master_suplier"""
            result = connection.selectHeader(conn,query)
            print("RESULT",result['data'])
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")
    
    def getDataProductOption():
        try:
            conn = connection.connectDb()
            query = """SELECT product_pk as id, product_name as value FROM samb.master_product"""
            result = connection.selectHeader(conn,query)
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataPengeluaranHead(param):
        try:
            conn = connection.connectDb()
            query = """INSERT INTO samb.transaksi_pengeluaran_barang_head
                        (trx_out_no, trx_out_whs_idf, trx_out_date, trx_out_supp_idf, trx_out_notes)
                        VALUES(%(inputnomorpengeluaran)s, %(inputgudang)s, now() ,%(inputsuplier)s, %(inputpengeluarannote)s);"""
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def getDataTransaksiPengeluaranDetail(param):
        try:
            conn = connection.connectDb()
            query = """SELECT trx_out_d_pk as pengeluarandetailiddetail, trx_out_d_idf as nomortransaksipengeluarandetail, product_name as namaproduct, trx_out_d_qty_dus as jumlahdus, trx_out_d_qty_pcs as jumlahpcs
                       FROM samb.transaksi_pengeluaran_barang_detail, samb.master_product
                       WHERE trx_out_d_product_idf = product_pk and trx_out_d_idf=%(nomortransaksi)s;
                    """
            result = connection.selectDataHeader(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def insertDataPengeluaranDetail(param):
        try:
            conn = connection.connectDb()
            query = """INSERT INTO samb.transaksi_pengeluaran_barang_detail
                        (trx_out_d_idf, trx_out_d_product_idf, trx_out_d_qty_dus, trx_out_d_qty_pcs)
                        VALUES(%(nomortransaksi)s, %(inputproductdetail)s, %(inputpengeluarandetaildus)s, %(inputpengeluarandetailpcs)s);"""
            result = connection.executeData(conn,query,dict(param))
            print(query%param)
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def updateDataPengeluaranDetail(param):
        try:
            conn = connection.connectDb()
            query = """UPDATE samb.transaksi_pengeluaran_barang_detail
                        SET trx_out_d_product_idf=%(editpengeluarandetailproduct)s, trx_out_d_qty_dus=%(editpengeluarandetaildus)s, trx_out_d_qty_pcs=%(editpengeluarandetailpcs)s
                        WHERE trx_out_d_pk=%(editpengeluarandetailid)s and trx_out_d_idf = %(editpengeluarandetailnomor)s;
                        """
            result = connection.executeData(conn,query,dict(param))
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")

    def deleteDataPengeluaranDetail(param):
        try:
            print("PARAM",param)
            conn = connection.connectDb()
            query = """DELETE FROM samb.transaksi_pengeluaran_barang_detail
                        WHERE trx_out_d_pk=%(pengeluarandetailiddetail)s and trx_out_d_idf = %(nomortransaksipengeluarandetail)s;
                        """
            print(query%param)
            result = connection.executeData(conn,query,dict(param))
            print("askdjhaksjdhkajwhdk",result)
            return result
        except (Exception,Error) as error:
            print("Sambungan database bermasalah")