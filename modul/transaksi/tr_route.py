from flask import Flask, Blueprint, render_template, redirect, request, url_for, jsonify
from modul.transaksi.tr_model import TransaksiPenerimaan,TransaksiPengeluaran
import json

appTransaksi = Blueprint('appTransaksi', __name__)
app = Flask(__name__)

@appTransaksi.route('/report', methods=['GET','POST'])
def report():
    return render_template('report.html')

@appTransaksi.route('/tr_penerimaan', methods=['GET','POST'])
def trPenerimaan():
    tr = TransaksiPenerimaan
    data = tr.getDataTransaksiPenerimaan()
    gudangOption = tr.getDataGudangOption()
    suplierOption= tr.getDataSuplierOption()
    return render_template('tr_penerimaan.html', data=data['data'], dataGudang = gudangOption['data'], dataSuplier =suplierOption['data'] )

@appTransaksi.route('/tr_penerimaan/input', methods=['GET','POST'])
def trPenerimaanInput():
    tr = TransaksiPenerimaan
    dataInsert = request.form
    result = tr.insertDataPenerimaanHead(dataInsert)
    data = tr.getDataTransaksiPenerimaan()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appTransaksi.route('/tr_penerimaan_detail', methods=['GET','POST'])
def trPenerimaanDetail():
    tr = TransaksiPenerimaan
    param = request.form
    data = tr.getDataTransaksiPenerimaanDetail(param)
    productOption = tr.getDataProductOption()
    return render_template('tr_penerimaan_detail.html', data=data['data'], dataProduct = productOption['data'], dataInsert = dict(param))

@appTransaksi.route('/tr_penerimaan_detail/input', methods=['GET','POST'])
def trPenerimaanInputDetail():
    tr = TransaksiPenerimaan
    dataInsert = request.form
    result = tr.insertDataPenerimaanDetail(dataInsert)
    data = tr.getDataTransaksiPenerimaanDetail(dataInsert)
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appTransaksi.route('/tr_penerimaan_detail/edit', methods=['GET','POST'])
def trPenerimaanEditDetail():
    tr = TransaksiPenerimaan
    dataUpdate = request.form
    param = {'nomortransaksi':dict(dataUpdate)['editpenerimaandetailnomor']}
    result = tr.updateDataPenerimaanDetail(dataUpdate)
    data = tr.getDataTransaksiPenerimaanDetail(param)
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appTransaksi.route('/tr_penerimaan_detail/delete', methods=['GET','POST'])
def trPenerimaanDeleteDetail():
    tr = TransaksiPenerimaan
    dataDelete = request.form
    param = {'nomortransaksi':dict(dataDelete)['nomortransaksipenerimaandetail']}
    result = tr.deleteDataPenerimaanDetail(dataDelete)
    data = tr.getDataTransaksiPenerimaanDetail(param)
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}
    




#  ======================================================= 
@appTransaksi.route('/tr_pengeluaran', methods=['GET','POST'])
def trPengeluaran():
    tr = TransaksiPengeluaran
    data = tr.getDataTransaksiPengeluaran()
    gudangOption = tr.getDataGudangOption()
    suplierOption= tr.getDataSuplierOption()
    return render_template('tr_pengeluaran.html', data=data['data'], dataGudang = gudangOption['data'], dataSuplier =suplierOption['data'] )

@appTransaksi.route('/tr_pengeluaran/input', methods=['GET','POST'])
def trPengeluaranInput():
    tr = TransaksiPengeluaran
    dataInsert = request.form
    result = tr.insertDataPengeluaranHead(dataInsert)
    data = tr.getDataTransaksiPengeluaran()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appTransaksi.route('/tr_pengeluaran_detail', methods=['GET','POST'])
def trPengeluaranDetail():
    tr = TransaksiPengeluaran
    param = request.form
    data = tr.getDataTransaksiPengeluaranDetail(param)
    productOption = tr.getDataProductOption()
    return render_template('tr_pengeluaran_detail.html', data=data['data'], dataProduct = productOption['data'], dataInsert=dict(param))

@appTransaksi.route('/tr_pengeluaran_detail/input', methods=['GET','POST'])
def trPengeluaranInputDetail():
    tr = TransaksiPengeluaran
    dataInsert = request.form
    result = tr.insertDataPengeluaranDetail(dataInsert)
    data = tr.getDataTransaksiPengeluaranDetail(dataInsert)
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appTransaksi.route('/tr_pengeluaran_detail/edit', methods=['GET','POST'])
def trPengeluaranEditDetail():
    tr = TransaksiPengeluaran
    dataUpdate = request.form
    param = {'nomortransaksi':dict(dataUpdate)['editpengeluarandetailnomor']}
    result = tr.updateDataPengeluaranDetail(dataUpdate)
    data = tr.getDataTransaksiPengeluaranDetail(param)
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appTransaksi.route('/tr_pengeluaran_detail/delete', methods=['GET','POST'])
def trPengeluaranDeleteDetail():
    tr = TransaksiPengeluaran
    dataDelete = request.form
    param = {'nomortransaksi':dict(dataDelete)['nomortransaksipengeluarandetail']}
    result = tr.deleteDataPengeluaranDetail(dataDelete)
    data = tr.getDataTransaksiPengeluaranDetail(param)
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}
      
    