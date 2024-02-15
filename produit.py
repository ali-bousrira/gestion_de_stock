class crea_produit :
    def __init__(self):
        #si la db existe deja
        import mysql.connector
        try :
            self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2879",
            database="gestion_stocke"

            )

            self.cursor = self.db.cursor ()

        #conection pour la creation de la db avec def initialisation ()
        except :

            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2879"
                )

            self.cursor = self.connection.cursor ()

            self.initialisation ()

            self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2879",
            database="gestion_stocke"

            )

            self.cursor = self.db.cursor ()

    #creation de la db
    def initialisation (self) :
        import mysql.connector

        command = f"CREATE DATABASE gestion_stocke"

        self.cursor.execute (command)

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",
        database="gestion_stocke"

        )

        self.cursor = self.db.cursor ()
        
        self.db.commit()
        
        #a mettre dans la ceeation de category
        '''
        command = """
        CREATE TABLE IF NOT EXISTS category (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        );
        """
        self.cursor = self.db.cursor ()
        '''
    def crea_tables_produit (self) :

        command = """create table IF NOT EXISTS produit (
        id int auto_increment primary key,
        nom varchar (255),
        discription varchar (255),
        prix int,
        quantité int,
        id_category int,
        FOREIGN KEY (id_category) REFERENCES category(id)
        );"""

        self.cursor.execute(command)

        self.db.commit()

    #affichager des tables 
    def verif (self) :
        command = f"show tables;"

        self.cursor.execute (command)

        return (self.cursor.fetchall ())
    
    def crea_final (self, nom, discription, prix, quantité, id_category) :
        command = """insert into produit (nom, discription, prix, quantité, id_category)
        values
        (%s,%s,%s,%s,%s);
        """

        self.cursor.execute (command, (nom, discription, prix, quantité, id_category))

        self.db.commit()


    #modification
    def modif(self, nom, description, prix, quantite, id_category, id):
        command = """
        UPDATE produit
        SET nom = %s, discription = %s, prix = %s, quantité = %s, id_category = %s
        WHERE id = %s;
        """
        self.cursor.execute(command, (nom, description, prix, quantite, id_category, id))
        self.db.commit()

    def read (self) :
        command = f"select * from produit"

        self.cursor.execute(command)

        # Fetch all the rows
        rows = self.cursor.fetchall()

        return rows
        
class info_produit :
    def __init__(self):
        import mysql.connector

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",
        database="gestion_stocke"

        )

        self.cursor = self.db.cursor ()

    def read (self) :
        self.cursor.execute(f"SELECT * FROM produit")

        rows = self.cursor.fetchall()

        return rows

class suprime :
    def __init__(self):
        import mysql.connector

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",
        database="gestion_stocke"

        )

        self.cursor = self.db.cursor ()
    
    def run (self, id) :
        self.cursor.execute(f"delete from produit where id = {id}")

        self.db.commit()

"""test = crea_produit ()
test.crea_tables_produit ()
print (test.verif ())"""
