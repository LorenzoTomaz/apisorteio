import random
import mysql.connector

def sorteio_vendedor():
   L = []
   G = []
   cnx = mysql.connector.connect(#insira os dados do seu db)
   cursor = cnx.cursor()
   query = "select * from teste.sorteio_troco"
   cursor.execute(query)
   for x in cursor:
     L.append(x[0])

   secure_random = random.SystemRandom()
   sort = secure_random.choice(L)
   return sort

def sort():

    G = ""
    sort = sorteio_vendedor()
    cnx = mysql.connector.connect(#insira os dados do seu db)
    cursor = cnx.cursor()
    query_1 = "select loja from teste.sorteio_troco where vendedor like '{}' order by loja ASC limit 1".format(sort)
    cursor.execute(query_1)
    for i in cursor:
     G = str(i)
    dic_sort = {'vendedor': sort, 'loja': G}
    return dic_sort


def sorteio_loja():
 L = []
 G = []
 cnx = mysql.connector.connect()
 cursor = cnx.cursor()
 query = "select * from teste.sorteio_troco_loja"
 cursor.execute(query)
 for x in cursor:
  L.append(x[0])

 secure_random = random.SystemRandom()
 sort = secure_random.choice(L)
 return sort
