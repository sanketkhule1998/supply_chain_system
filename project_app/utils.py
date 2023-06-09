import pickle
import json
import numpy as np
import pandas as pd
import config
from sklearn.preprocessing import LabelEncoder

class SupplyChain():
    def __init__(self,Type, Days_for_shipping_real,Days_for_shipment_scheduled,
       Benefit_per_order, Sales_per_customer, Delivery_Status,
       Late_delivery_risk, Category_Id, Category_Name, Customer_City,
       Customer_Country, Customer_Fname, Customer_Id,Customer_Lname,
        Customer_Segment,Customer_State, Customer_Street, Customer_Zipcode,
       Department_Id, Department_Name, Latitude, Longitude, Market,
       Order_City, Order_Country, Order_Customer_Id,
       order_date_DateOrders, Order_Id, Order_Item_Cardprod_Id,
       Order_Item_Discount, Order_Item_Discount_Rate, Order_Item_Id,
       Order_Item_Product_Price, Order_Item_Profit_Ratio,
       Order_Item_Quantity, Sales, Order_Item_Total,
       Order_Profit_Per_Order, Order_State, Order_Status,
       Product_Card_Id, Product_Category_Id,
       Product_Name, Product_Price, Product_Status,
       shipping_date_DateOrders, Shipping_Mode):
        

        self.Type = Type
        self.Days_for_shipping_real = Days_for_shipping_real
        self.Days_for_shipment_scheduled = Days_for_shipment_scheduled
        self.Benefit_per_order = Benefit_per_order
        self.Sales_per_customer = Sales_per_customer
        self.Delivery_Status = Delivery_Status
        self.Late_delivery_risk = Late_delivery_risk
        self.Category_Id = Category_Id
        self.Category_Name = Category_Name
        self.Customer_City = Customer_City
        self.Customer_Country = Customer_Country
        self.Customer_Fname =  Customer_Fname
        self.Customer_Id = Customer_Id
        self.Customer_Lname = Customer_Lname
        self.Customer_Segment = Customer_Segment
        self.Customer_State = Customer_State
        self.Customer_Street = Customer_Street
        self.Customer_Zipcode = Customer_Zipcode
        self.Department_Id = Department_Id
        self.Department_Name = Department_Name
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Market = Market
        self.Order_City = Order_City
        self.Order_Country = Order_Country
        self.Order_Customer_Id = Order_Customer_Id
        self.order_date_DateOrders = order_date_DateOrders
        self.Order_Id = Order_Id
        self.Order_Item_Cardprod_Id = Order_Item_Cardprod_Id
        self.Order_Item_Discount = Order_Item_Discount
        
        self.Order_Item_Discount_Rate = Order_Item_Discount_Rate
        self.Order_Item_Id = Order_Item_Id
        self.Order_Item_Product_Price = Order_Item_Product_Price
        self.Order_Country = Order_Country
        self.Order_Item_Profit_Ratio = Order_Item_Profit_Ratio
        self.Order_Item_Quantity = Order_Item_Quantity
        self.Sales = Sales
        self.Order_Item_Total = Order_Item_Total
        self.Order_Profit_Per_Order = Order_Profit_Per_Order
        
        self.Order_State = Order_State
        self.Order_Status = Order_Status
        self.Product_Card_Id = Product_Card_Id
        self.Product_Category_Id = Product_Category_Id
        self.Product_Name = Product_Name
        self.Product_Price = Product_Price
        self.Product_Status = Product_Status
        self.shipping_date_DateOrders = shipping_date_DateOrders
        self.Shipping_Mode = Shipping_Mode
        

    def load_models(self):

        with open(config.MODEL_FILE_PATH,"rb") as f:
           self.model = pickle.load(f)


        with open(config.JSON_FILE_PATH,"r") as f:
           self.json_data = json.load(f)



    def get_predicted_sales(self):

        self.load_models()   # Creating instance of model and json_data

        
        
        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.json_data['Type'][self.Type]
        test_array[1] = self.Days_for_shipping_real
        test_array[2] = self.Days_for_shipment_scheduled
        test_array[3] = self.Benefit_per_order
        test_array[4] = self.Sales_per_customer
        test_array[5] = self.json_data['Delivery_Status'][self.Delivery_Status]
        test_array[6] = self.Late_delivery_risk
        test_array[7] = self.Category_Id
        test_array[8] = self.json_data['Category_Name'][self.Category_Name]
        test_array[9] = self.json_data['Customer_City'][self.Customer_City]
        test_array[10] = self.json_data['Customer_Country'][self.Customer_Country]
        test_array[11] = self.json_data['Customer_Fname'][self.Customer_Fname]
        test_array[12] = self.Customer_Id
        test_array[13] = self.json_data['Customer_Lname'][self.Customer_Lname]
        test_array[14] = self.json_data['Customer_Segment'][self.Customer_Segment]
        test_array[15] = self.json_data['Customer_State'][self.Customer_State]
        test_array[16] = self.json_data['Customer_Street'][self.Customer_Street]
        test_array[17] = self.Customer_Zipcode
        test_array[18] = self.Department_Id
        test_array[19] = self.json_data['Department_Name'][self.Department_Name]
        test_array[20] = self.Latitude
        test_array[21] = self.Longitude
        test_array[22] = self.json_data['Market'][self.Market]
        test_array[23] = self.json_data['Order_City'][self.Order_City]
        test_array[24] = self.json_data['Order_Country'][self.Order_Country]
        test_array[25] = self.Order_Customer_Id
        test_array[26] = self.order_date_DateOrders
        test_array[27] = self.Order_Id
        test_array[28] = self.Order_Item_Cardprod_Id
        test_array[29] = self.Order_Item_Discount
        test_array[30] = self.Order_Item_Discount_Rate
        test_array[31] = self.Order_Item_Id
        test_array[32] = self.Order_Item_Product_Price
        test_array[33] = self.Order_Item_Profit_Ratio
        test_array[34] = self.Order_Item_Quantity
        test_array[35] = self.Sales
        test_array[36] = self.Order_Item_Total
        test_array[37] = self.Order_Profit_Per_Order
        test_array[38] = self.json_data['Order_State'][self.Order_State]
        test_array[39] = self.json_data['Order_Status'][self.Order_Status]
        test_array[40] = self.Product_Card_Id
        test_array[41] = self.Product_Category_Id
        test_array[42] = self.json_data['Product_Name'][self.Product_Name]
        test_array[43] = self.Product_Price
        test_array[44] = self.Product_Status
        test_array[45] = self.shipping_date_DateOrders
        test_array[46] = self.json_data['Shipping_Mode'][self.Shipping_Mode]
        

        

        print("Test Array--->\n",test_array)

        vehicle = (self.model.predict([test_array])[0])

        return vehicle
    

if __name__ == "__main__":

    Type = "DEBIT"
    Days_for_shipping_real = 3
    Days_for_shipment_scheduled = 4
    Benefit_per_order = 91.25
    Sales_per_customer = 314.640015
    Delivery_Status = "Advance shipping"
    Late_delivery_risk = 0
    Category_Id = 73
    Category_Name = "Sporting Goods"
    Customer_City = "Caguas"
    Customer_Country = "Puerto Rico"
    Customer_Fname = "Cally"
    Customer_Id = 20755
    Customer_Lname = "Holloway"
    Customer_Segment= "Consumer"
    Customer_State = "PR"
    Customer_Street = "5365 Noble Nectar Island"
    Customer_Zipcode = 725.0
    Department_Id = 2
    Department_Name = "Fitness"
    Latitude = 18.251453
    Longitude = -66.037056
    Market = "Pacific Asia"
    Order_City = "Bekasi"
    Order_Country = "Indonesia"
    Order_Customer_Id = 20755
    order_date_DateOrders = 145286240
    Order_Id = 77202
    Order_Item_Cardprod_Id = 1360
    Order_Item_Discount = 13.11
    Order_Item_Discount_Rate = 0.04
    Order_Item_Id = 180517
    Order_Item_Product_Price = 327.75
    Order_Item_Profit_Ratio = 0.29
    Order_Item_Quantity = 1
    Sales = 327.75
    Order_Item_Total = 314.640015
    Order_Profit_Per_Order = 91.25
    Order_State = "Java Occidental"
    Order_Status = "COMPLETE"
    Product_Card_Id = 1360
    Product_Category_Id = 73
    Product_Name = "Smart watch "
    Product_Price = 327.75
    Product_Status = 0
    shipping_date_DateOrders = 145286240
    Shipping_Mode = "Standard Class"

    sales_predict = SupplyChain(Type, Days_for_shipping_real,Days_for_shipment_scheduled,Benefit_per_order, Sales_per_customer, Delivery_Status,
       Late_delivery_risk, Category_Id, Category_Name, Customer_City,Customer_Country, Customer_Fname, Customer_Id,Customer_Lname,
        Customer_Segment,Customer_State, Customer_Street, Customer_Zipcode,Department_Id, Department_Name, Latitude, Longitude, Market,
       Order_City, Order_Country, Order_Customer_Id,order_date_DateOrders, Order_Id, Order_Item_Cardprod_Id,
       Order_Item_Discount, Order_Item_Discount_Rate, Order_Item_Id,Order_Item_Product_Price, Order_Item_Profit_Ratio,
       Order_Item_Quantity, Sales, Order_Item_Total,Order_Profit_Per_Order, Order_State, Order_Status,
       Product_Card_Id, Product_Category_Id,Product_Name, Product_Price, Product_Status,
       shipping_date_DateOrders, Shipping_Mode)
    
    vehicle = sales_predict.get_predicted_sales()
    print("Predicted Region :",vehicle)
      