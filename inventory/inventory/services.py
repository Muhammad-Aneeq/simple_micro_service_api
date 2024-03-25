from sqlmodel import Session,select
from fastapi import Depends,HTTPException
from database import SessionLocal,Product

# Dependency
def get_db():
  db:Session =SessionLocal
  try:
    yield db
  finally:
    db.close()



class ProductService:
  def __init__(self,db:Session = Depends(get_db)) -> None:
    self.db = db

  # create Product
  def create_product(self,product_create):
    new_product = Product(
      name = product_create.name,
      price = product_create.price,
      quantity = product_create.quantity
    ) 

    self.db.add(new_product)
    self.db.commit()
    self.db.refresh(new_product)
    return Product(**new_product.__dict__)
  

  def get_product(self,product_id):
    statement = select(Product).filter(Product.id == product_id)
    product = self.db.exec(statement).first()
    return {"message" : "product fetched successfully","data":product}


  # get products
  def get_products(self):
    statement = select(Product)
    products = self.db.exec(statement).all()
    return {"message" : "products fetched successfully","data":products}


  # updating product
  def update_product(self,product_id,updated_product):
    statement = select(Product).filter(Product.id == product_id)
    db_product = self.db.exec(statement).first()
    if db_product is None:
      raise HTTPException(status_code=404,detail="Product not found")
     # Remove 'id' from updated_product fields
    updated_fields = updated_product.dict(exclude={'id'})
    for key , value in updated_fields.items():
      setattr(db_product,key,value)
    self.db.commit()
    return {"message": "Product updated successfully"}
    
  # deleting product
  def delete_product(self,product_id):
    statement = select(Product).filter(Product.id == product_id)
    db_product = self.db.exec(statement).first()
    if db_product is None:
      raise HTTPException(status_code=404,detail="Product not found")
    self.db.delete(db_product)
    self.db.commit()
    return {"message": "Product deleted successfully"}




