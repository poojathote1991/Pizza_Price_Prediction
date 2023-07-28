from flask import Flask,render_template,request,jsonify,redirect,url_for
from utils import PizzaData
import config
import traceback
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('pizza_predict_price.html')

@app.route('/predicted_price',methods=['GET','POST'])
def predicted_price():
    try:
     
        if request.method =='GET':
            data=request.args.get
            print("data: ",data)
            diameter=data('diameter')
            topping=data('topping')
            variant=data('variant')
            size=data('size')
            extra_sauce=data('extra_sauce')
            extra_cheese=data('extra_cheese')
            extra_mushrooms=data('extra_mushrooms')
            company=data('company')
            pizza=PizzaData(diameter,topping,variant,size,extra_sauce,extra_cheese,extra_mushrooms,company)
            pred_price=pizza.get_predicted_price()

            return render_template("pizza_predict_price.html",prediction={pred_price})
        
        elif request.method =='POST':
                data=request.form.get
                print("data: ",data)
                diameter=data['diameter']
                topping=data['topping']
                variant=data['variant']
                size=data['size']
                extra_sauce=data['extra_sauce']
                extra_cheese=data['extra_cheese']
                extra_mushrooms=data['extra_mushrooms']
                company=data['company']
                pizza=PizzaData(diameter,topping,variant,size,extra_sauce,extra_cheese,extra_mushrooms,company)
                pred_price=pizza.get_predicted_price()

                return render_template("pizza_predict_price.html",prediction={pred_price})
    except:
         return print(traceback.print_exc())


if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)