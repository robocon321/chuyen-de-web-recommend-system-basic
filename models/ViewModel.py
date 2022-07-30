import numpy as np
from db.Connector import cursor

def getViewNumpy(type, user_id):
    cursor.execute("SELECT count(*) as view, user_id, object_id "
                   + "FROM `view` WHERE type = '"+ type + "' AND user_id IS NOT NULL AND user_id = " + user_id + " "
                   + "GROUP BY user_id, object_id, type")
    view = cursor.fetchall()
    viewNp = np.asarray(view)
    return viewNp


