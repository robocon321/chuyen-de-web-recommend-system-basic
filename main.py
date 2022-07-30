from models.ProductModel import getProductNumpy
from models.TaxomonyModel import getTaxomonyNumpy
from models.TaxomonyRelationshipModel import getTaxomonyRelationShipNumpy
from models.ViewModel import getViewNumpy
from models.PostModel import getPostNumpy
from services.ContentBase import ContentBase
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/products')
def index(user_id, amount : int):
    contentBase = ContentBase(item=getProductNumpy(),
                              subject=getTaxomonyNumpy("product"),
                              item_subject=getTaxomonyRelationShipNumpy("product"),
                              score=getViewNumpy("product", user_id))

    result = contentBase.calculate(amount)

    return result

@app.get('/posts')
def index(user_id, amount : int):
    contentBase = ContentBase(item=getPostNumpy(),
                              subject=getTaxomonyNumpy("post"),
                              item_subject=getTaxomonyRelationShipNumpy("post"),
                              score=getViewNumpy("product", user_id))

    result = contentBase.calculate(amount)

    return result
