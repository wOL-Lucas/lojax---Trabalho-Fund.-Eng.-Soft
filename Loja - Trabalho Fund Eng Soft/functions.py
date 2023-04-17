import dbconn

def getProductsFromDb():
    
    productsList = []

    cursor = dbconn.dbConnect()
    query = cursor.execute('SELECT nomeProduto FROM estoque')

    for produto in query:
        product = str(produto).replace(',','').replace('(','').replace(')','').replace("'",'')
        productsList.append(product)

    return productsList


def getChoiceSetValue(var):
    return(var.get())
