from flask import Flask,render_template,request,jsonify

from project_app.utils import SupplyChain


# Creating instance here
app = Flask(__name__)


@app.route("/")   # HOME API
def hello_Flask():
    print("Welcome to the Car Price Prediction System")   # console
    return render_template("index.html")     # for html
    #return "Success"                        # for postman

@app.route("/predict_sale",methods = ["POST","GET"])
def get_sales_data():
    if request.method == "GET":
        print("WE are in a GET method")



        
        Type = (request.args.get("Type"))
        Days_for_shipping_real = (request.args.get("Days_for_shipping_real"))
        Days_for_shipment_scheduled = (request.args.get("Days_for_shipment_scheduled"))
        Benefit_per_order = (request.args.get("Benefit_per_order"))
        Sales_per_customer = (request.args.get("Sales_per_customer"))
        Delivery_Status = (request.args.get("Delivery_Status"))
        Late_delivery_risk = (request.args.get("Late_delivery_risk"))
        Category_Id = (request.args.get("Category_Id"))
        Category_Name = (request.args.get("Category_Name"))
        Customer_City = (request.args.get("Customer_City"))
        Customer_Country = (request.args.get("Customer_Country"))
        Customer_Fname = (request.args.get("Customer_Fname"))
        Customer_Id = (request.args.get("Customer_Id"))
        Customer_Lname = (request.args.get("Customer_Lname"))
        Customer_Segment = (request.args.get("Customer_Segment"))

        Customer_State = (request.args.get("Customer_State"))
        Customer_Street = (request.args.get("Customer_Street"))
        Customer_Zipcode = (request.args.get("Customer_Zipcode"))
        Department_Id = (request.args.get("Department_Id"))
        Department_Name = (request.args.get("Department_Name"))
        Latitude = (request.args.get("Latitude"))
        Longitude = (request.args.get("Longitude"))
        Market = (request.args.get("Market"))
        Order_City = (request.args.get("Order_City"))
        Order_Country = (request.args.get("Order_Country"))
        Order_Customer_Id = (request.args.get("Order_Customer_Id"))

        order_date_DateOrders = (request.args.get("order_date_DateOrders"))
        Order_Id = (request.args.get("Order_Id"))
        Order_Item_Cardprod_Id = (request.args.get("Order_Item_Cardprod_Id"))
        Order_Item_Discount = (request.args.get("Order_Item_Discount"))
        Order_Item_Discount_Rate = (request.args.get("Order_Item_Discount_Rate"))
        Order_Item_Id = (request.args.get("Order_Item_Id"))
        Order_Item_Product_Price = (request.args.get("Order_Item_Product_Price"))
        Order_Item_Profit_Ratio = (request.args.get("Order_Item_Profit_Ratio"))
        Order_Item_Quantity = (request.args.get("Order_Item_Quantity"))
        Sales = (request.args.get("Sales"))
        Order_Item_Total = (request.args.get("Order_Item_Total"))

        Order_Profit_Per_Order = (request.args.get("Order_Profit_Per_Order"))
        Order_State = (request.args.get("Order_State"))
        Order_Status = (request.args.get("Order_Status"))
        Product_Card_Id = (request.args.get("Product_Card_Id"))
        Product_Category_Id = (request.args.get("Product_Category_Id"))
        Product_Name = (request.args.get("Product_Name"))
        Product_Price = (request.args.get("Product_Price"))
        Product_Status = (request.args.get("Product_Status"))
        shipping_date_DateOrders = (request.args.get("shipping_date_DateOrders"))
        Shipping_Mode = (request.args.get("Shipping_Mode"))
        


       
        sales_predict = SupplyChain(Type, Days_for_shipping_real,
                                    Days_for_shipment_scheduled,
                                    Benefit_per_order, Sales_per_customer,
                                      Delivery_Status,
        Late_delivery_risk, Category_Id, Category_Name, Customer_City,
        Customer_Country, Customer_Fname, Customer_Id,Customer_Lname,
        Customer_Segment,Customer_State, Customer_Street, Customer_Zipcode,
        Department_Id, Department_Name, Latitude, Longitude, Market,
       Order_City, Order_Country, Order_Customer_Id,order_date_DateOrders,
         Order_Id, Order_Item_Cardprod_Id,
       Order_Item_Discount, Order_Item_Discount_Rate, Order_Item_Id,
       Order_Item_Product_Price, Order_Item_Profit_Ratio,
       Order_Item_Quantity, Sales, Order_Item_Total,Order_Profit_Per_Order, 
       Order_State, Order_Status,
       Product_Card_Id, Product_Category_Id,Product_Name, Product_Price, 
       Product_Status,
       shipping_date_DateOrders, Shipping_Mode)
        
        vehicle = sales_predict.get_predicted_sales()
    
        return render_template("index.html",prediction = vehicle)

    # return jsonify({"Result":f"Predicted Charges is {charges}/- Rs."})
    

print("__name__ ---->",__name__)

if __name__ == "__main__":
    app.run()

