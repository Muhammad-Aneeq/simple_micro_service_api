from fastapi import FastAPI, Depends
from services import ProductService
from database import Product


app:FastAPI = FastAPI()


product_service = ProductService

# In FastAPI, when you include Depends in the function parameters, it acts as a dependency injection mechanism. The purpose of Depends is to execute the dependency function (TodoService in your case) and pass its return value (TodoService instance) to the corresponding path operation function (create_todos in your case).

# post method
@app.post("/api/products",tags=["product"])
async def create_products(product:Product,product_service:ProductService = Depends()):
   response = product_service.create_product(product)
   return response


# get method    
@app.get("/api/products",tags=["product"])
async def get_products(product_service:ProductService = Depends()):
   response = product_service.get_products()
   return response

@app.get("/api/products/{product_id}",tags=["product"])
async def get_product(product_id:int,product_service:ProductService = Depends()):
   response = product_service.get_product(product_id)
   return response
   
 
# put method
@app.put("/api/products/{product_id}",tags=["product"])
async def update_products(product_id:int,updated_product: Product,product_service:ProductService = Depends()):
   response = product_service.update_product(product_id,updated_product)
   return response

# delete method
@app.delete("/api/products/{product_id}", tags=["product"])
async def delete_products(product_id: int,product_service:ProductService = Depends()):
   response = product_service.delete_product(product_id)
   return response










    