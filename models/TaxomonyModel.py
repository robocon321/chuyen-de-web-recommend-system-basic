import numpy as np
from db.Connector import cursor

def getTaxomonyNumpy(type):
  cursor.execute("SELECT * FROM taxomony WHERE type = '" + type + "'")
  taxomony = cursor.fetchall()
  taxomonyNp = np.zeros(len(taxomony))

  for index, x in enumerate(taxomony):
    taxomonyNp[index] = x[0]

  return taxomonyNp
