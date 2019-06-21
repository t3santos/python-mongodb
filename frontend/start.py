
from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)


table = banco['deputados']

tablegastos = banco['gastos']

@app.route("/")
def deputados():
   list_dep = []
   for dep in table.find():
       list_dep.append(dep)
   return render_template('lista.html', listas=list_dep)

@app.route("/gastos/<id>")
def deputado(id):
   obj    = DadosAbertos()
   info   = obj.deputado_id(id)
   gastos = obj.deputado_despesas(id)
   datahoje = date.today()
   meshoje = datahoje.month
   valores = {}
   meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho"]
  
  # Labels data
   
   line_months = []

   for x in range(6):
      line_months.append(meses[meshoje])
      meshoje = meshoje - 1

   line_months.reverse()
   line_data = []
   for gasto in gastos:
       data = str(gasto['mes']) + '/' + str(gasto['ano'])
     
       

       if data in valores:
          line_data.append(gasto['valorLiquido']) 
       else:
          line_data.append(gasto['valorLiquido'])  

   
   line_labels = valores.keys()
   line_values = valores.values()
   line_data.append(random.randint(100,5000))
   line_data.append(random.randint(100,5000)) 

   return render_template('gastos.html', title='Grafico de Gastos', max=10000, labels=line_labels, values=line_data,
   meses = line_months, x = random.randint(100,5000), y =
   random.randint(100,5000))
