class category :
    def __init__(self):
        #si la db existe deja
        import mysql.connector

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",

        )

        self.cursor = self.db.cursor ()

        command = f"CREATE DATABASE IF NOT EXISTS gestion_stocke"

        self.cursor.execute (command)

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",
        database="gestion_stocke"

        )

        self.cursor = self.db.cursor ()
        
        self.db.commit()

        self.crea_table_category ()
        
    def crea_table_category (self) :
        command = """
        CREATE TABLE IF NOT EXISTS category (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        );
        """
        self.cursor.execute (command)

        self.db.commit()


    def crea_category(self, nom):
        command = f"""
        INSERT INTO category (name)
        VALUES
        ('{nom}');
        """
        self.cursor.execute(command)
        self.db.commit()


class manipulation_category :
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
        self.cursor.execute(f"SELECT * FROM category")

        rows = self.cursor.fetchall()

        return rows

class modification :
    def __init__(self) -> None:
        #conextion a la db
        import mysql.connector

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",
        database="gestion_stocke"

        )

        self.cursor = self.db.cursor ()

    #modification
    def modif(self, nom, id):
        command = """
        UPDATE category
        SET name = %s
        WHERE id = %s;
        """
        self.cursor.execute(command, (nom, id))
        self.db.commit()

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
        self.cursor.execute(f"delete from category where id = {id}")

        self.db.commit()

test = modification ()
test.modif ("test", 2)