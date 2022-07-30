from models.TaxomonyModel import getTaxomonyNumpy
from models.TaxomonyRelationshipModel import getTaxomonyRelationShipNumpy
from models.ViewModel import getViewNumpy
from models.PostModel import getPostNumpy
from models.ProductModel import getProductNumpy
from services.ContentBase import ContentBase

contentBase = ContentBase(item=getPostNumpy(),
                          subject=getTaxomonyNumpy("post"),
                          item_subject=getTaxomonyRelationShipNumpy("post"),
                          score=getViewNumpy(type="post", user_id="19"))

result = contentBase.calculate()
print(result)
