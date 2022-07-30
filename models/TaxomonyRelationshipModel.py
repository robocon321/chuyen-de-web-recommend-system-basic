import numpy as np
from db.Connector import cursor

def getTaxomonyRelationShipNumpy(type):
  cursor.execute("SELECT * FROM taxomony_relationship WHERE type = '" + type + "'")
  taxomonyRelationShip = cursor.fetchall()
  taxomonyRelationShipNp = np.asarray(taxomonyRelationShip)
  return taxomonyRelationShipNp


