import numpy as np
from db.Connector import cursor

def getPostNumpy():
    cursor.execute("SELECT * FROM post WHERE type = 'post'")
    post = cursor.fetchall()
    postNp = np.zeros(len(post))

    for index, x in enumerate(post):
        postNp[index] = x[0]

    return postNp
