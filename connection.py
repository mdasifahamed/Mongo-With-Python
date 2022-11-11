import pymongo as mongo #pymongo is module to connet python with mongdb



"""
to coonect mongo we need an object of pymongo.MongoClient() class
in the MongoCilent() parameter should be passed coonection uri gotten from the mongo atlas cluster conection page
"""
mongo_client = mongo.MongoClient("mongodb+srv://asif:helloasif123@pyhtonandmongo.sjlwv8r.mongodb.net/?retryWrites=true&w=majority")



"""
after Coonecting The Client We Can Create Dtatabase From pyhton code editor 

Note To Create Data Create DataBase in Mongo We Have to Speciy The Tab;e Or in Mongo Word Collection for the database And Awe Have Also insert atlist one dummy datat
to it run it Otherwidse no databse will be created it is default by the mongo
folllow bellow lines of code
"""
store_db = mongo_client["Store_Database"]#creating DataBase
customer_table = store_db["Customer"] #Creating Collection Or Table To The DataBase
cus = {
    'name': "Asif",
    'Age': 27,
    'E-mail': "madasifahamedfahim@gmail.com",
}
cus1 = customer_table.insert_one(cus)# Inserting Data to The Table or in Mongo Word Collection

for names in mongo_client.list_database_names():
    print(names,'\n')
    for tables in store_db.list_collection_names():
        print(tables)

