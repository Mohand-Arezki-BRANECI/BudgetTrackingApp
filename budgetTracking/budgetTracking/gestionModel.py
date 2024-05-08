import mysql.connector


def connectToBDD():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="budget_tracking"
    )
    return mydb


def saveActivityToBDD(id_parent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle,
                      reste_apres_projection, commentaires):
    db = connectToBDD()
    cursor = db.cursor()

    requete_insert = "INSERT INTO activite (id_parent, libellé, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection, commentaires) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    valeurs = (
    id_parent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection,
    commentaires)

    try:
        cursor.execute(requete_insert, valeurs)
        db.commit()
        print("Activité enregistrée avec succès dans la base de données !")
    except mysql.connector.Error as err:
        db.rollback()
        print("Erreur lors de l'enregistrement de l'activité :", err)
    finally:
        cursor.close()
        db.close()


def getActivities():
    db = connectToBDD()
    cursor = db.cursor()

    requete_select = "SELECT * FROM activite WHERE id_parent = 0"

    cursor.execute(requete_select)
    resultats = cursor.fetchall()

    cursor.close()
    db.close()

    return resultats


def getSubActivities():
    db = connectToBDD()
    cursor = db.cursor()

    requete_select = "SELECT * FROM activite WHERE id_parent != 0"

    cursor.execute(requete_select)
    resultats = cursor.fetchall()

    cursor.close()
    db.close()

    return resultats

def getSubActivitiesByIdParent(idParent):
    db = connectToBDD()
    cursor = db.cursor()

    requete_select = "SELECT * FROM activite WHERE id_parent != %s"

    cursor.execute(requete_select, (idParent,))
    resultats = cursor.fetchall()

    cursor.close()
    db.close()

    return resultats