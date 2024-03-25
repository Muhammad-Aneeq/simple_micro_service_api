from fastapi import FastAPI, Depends
from services import OrderService
from database import Order
from fastapi.background import BackgroundTasks


app:FastAPI = FastAPI()


order_service = OrderService

# In FastAPI, when you include Depends in the function parameters, it acts as a dependency injection mechanism. The purpose of Depends is to execute the dependency function (TodoService in your case) and pass its return value (TodoService instance) to the corresponding path operation function (create_todos in your case).

# post method
@app.post("/api/orders/{product_id}/{order_quantity}",tags=["order"])
async def create_orders(product_id:int,order_quantity:int,order_service:OrderService =Depends()):
   response = order_service.create_order(product_id,order_quantity)
   return response



# get method    
@app.get("/api/orders",tags=["order"])
async def get_orders(order_service:OrderService =Depends()):
   response = order_service.get_orders()
   return response


 








    