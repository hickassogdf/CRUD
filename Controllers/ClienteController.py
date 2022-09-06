import services.database as db;


def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO crud (name, age, occupation) 
    VALUES (?,?,?)""",
    cliente.name, cliente.age, cliente.occupation).rowcount
    db.cnxn.commit()
