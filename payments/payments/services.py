from sqlmodel import Session,select
from fastapi import Depends,HTTPException
from database import SessionLocal,Order
from fastapi.background import BackgroundTasks
import requests, time,json

# Dependency
def get_db():
  db:Session =SessionLocal
  try:
    yield db
  finally:
    db.close()



class OrderService:
  def __init__(self,db:Session = Depends(get_db)) -> None:
    self.db = db

# create Order
  def create_order(self,product_id,order_quantity):
    req = requests.get(f'http://127.0.0.1:8000/api/products/{product_id}')
    product = req.json()
    product_data = product['data']

    new_order =Order(
     name = product_data['name'],
     price = product_data['price'],
     quantity = order_quantity,
     fee = 0.2 * int(product_data['price']),
     status="completed" 
    )

    self.db.add(new_order)
    self.db.commit()
    self.db.refresh(new_order)
    # background_tasks.add_task(self.update_product_quantity, product_data,new_order)
    return Order(**new_order.__dict__)
 
# get orders
  
  def get_orders(self):
    statement = select(Order)
    orders = self.db.exec(statement).all()
    return {"message" : "orders fetched successfully","data":orders}


 # updating product and order
  def update_product_quantity(self,product,order):
     payload = {
       'name':product['name'],
       'price':product['price'],
       'quantity':int(product['quantity']) - (order['quantity']) 
     }
     json_payload = json.dumps(payload)
     req = requests.put(f'http://127.0.0.1:8000/api/products/{product.id}',data=json_payload)
     respone = req.json()
     print("respone>>>.",respone)


