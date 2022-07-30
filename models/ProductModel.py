import numpy as np
from db.Connector import cursor

def getProductNumpy():
    cursor.execute("SELECT * FROM product")
    product = cursor.fetchall()
    productNp = np.zeros(len(product))

    for index, x in enumerate(product):
        productNp[index] = x[0]

    return productNp


