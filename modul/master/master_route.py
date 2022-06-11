from flask import Flask, Blueprint, render_template, redirect, request, url_for, jsonify
import json
from modul.master.master_model import MasterSuplier,MasterCustomer,MasterProduct,MasterWarehouse

appMaster = Blueprint('appMaster', __name__)
app = Flask(__name__)


@appMaster.route('/master_suplier', methods=['GET','POST'])
def masterSuplier():
    master = MasterSuplier
    data = master.getDataSuplier()
    print(data['data'])
    return render_template('master_suplier.html', data=data['data'])

    
@appMaster.route('/master_suplier/edit', methods=['GET','POST'])
def masterSuplierEdit():
    master = MasterSuplier
    dataUpdate = request.form
    result = master.updateDataSuplier(dataUpdate)
    data = master.getDataSuplier()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_suplier/input', methods=['GET','POST'])
def masterSuplierInput():
    master = MasterSuplier
    dataInsert = request.form
    result = master.insertDataSuplier(dataInsert)
    data = master.getDataSuplier()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_suplier/delete', methods=['GET','POST'])
def masterSuplierDelete():
    master = MasterSuplier
    dataInsert = request.form
    result = master.deleteDataSuplier(dataInsert)
    data = master.getDataSuplier()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}


@appMaster.route('/master_customer', methods=['GET','POST'])
def masterCustomer():
    master = MasterCustomer
    data = master.getDataCustomer()
    print(data['data'])
    return render_template('master_customer.html', data=data['data'])

    
@appMaster.route('/master_customer/edit', methods=['GET','POST'])
def masterCustomerEdit():
    master = MasterCustomer
    dataUpdate = request.form
    result = master.updateDataCustomer(dataUpdate)
    data = master.getDataCustomer()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_customer/input', methods=['GET','POST'])
def masterCustomerInput():
    master = MasterCustomer
    dataInsert = request.form
    result = master.insertDataCustomer(dataInsert)
    data = master.getDataCustomer()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_customer/delete', methods=['GET','POST'])
def masterCustomerDelete():
    master = MasterCustomer
    dataInsert = request.form
    result = master.deleteDataCustomer(dataInsert)
    data = master.getDataCustomer()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_product', methods=['GET','POST'])
def masterProduct():
    master = MasterProduct
    data = master.getDataProduct()
    print(data['data'])
    return render_template('master_product.html', data=data['data'])

    
@appMaster.route('/master_product/edit', methods=['GET','POST'])
def masterProductEdit():
    master = MasterProduct
    dataUpdate = request.form
    result = master.updateDataProduct(dataUpdate)
    data = master.getDataProduct()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_product/input', methods=['GET','POST'])
def masterProductInput():
    master = MasterProduct
    dataInsert = request.form
    result = master.insertDataProduct(dataInsert)
    data = master.getDataProduct()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_product/delete', methods=['GET','POST'])
def masterProductDelete():
    master = MasterProduct
    dataInsert = request.form
    result = master.deleteDataProduct(dataInsert)
    data = master.getDataProduct()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_warehouse', methods=['GET','POST'])
def masterWarehouse():
    master = MasterWarehouse
    data = master.getDataWarehouse()
    print(data['data'])
    return render_template('master_warehouse.html', data=data['data'])

    
@appMaster.route('/master_warehouse/edit', methods=['GET','POST'])
def masterWarehouseEdit():
    master = MasterWarehouse
    dataUpdate = request.form
    result = master.updateDataWarehouse(dataUpdate)
    data = master.getDataWarehouse()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_warehouse/input', methods=['GET','POST'])
def masterWarehouseInput():
    master = MasterWarehouse
    dataInsert = request.form
    result = master.insertDataWarehouse(dataInsert)
    data = master.getDataWarehouse()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}

@appMaster.route('/master_warehouse/delete', methods=['GET','POST'])
def masterWarehouseDelete():
    master = MasterWarehouse
    dataInsert = request.form
    result = master.deleteDataWarehouse(dataInsert)
    data = master.getDataWarehouse()
    return  {'data':data['data'], 'status':result['status'], 'msg':result['msg']}