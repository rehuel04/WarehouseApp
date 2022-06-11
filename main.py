from flask import Flask, render_template, request
from modul.master.master_route import appMaster
from modul.transaksi.tr_route import appTransaksi

app = Flask(__name__)
app.register_blueprint(appMaster)
app.register_blueprint(appTransaksi)

    
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(port=8080, debug=True)