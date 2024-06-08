import mysql.connector


def connectToBDD():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
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


def updateActivity(id, id_parent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle,
                   reste_apres_projection, commentaires):
    db = connectToBDD()
    cursor = db.cursor()

    requete_update = """
        UPDATE activite
        SET id_parent = %s, libellé = %s, nom = %s, budget_initial = %s, budget_depense = %s, reste = %s, 
            projection_partielle = %s, reste_apres_projection = %s, commentaires = %s 
        WHERE id = %s
    """

    valeurs = (
        id_parent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection,
        commentaires, id
    )

    try:
        cursor.execute(requete_update, valeurs)
        db.commit()
        print("Activité modifiée avec succès !")
    except mysql.connector.Error as err:
        db.rollback()
        print("Erreur lors de l'enregistrement de l'activité :", err)
    finally:
        cursor.close()
        db.close()


def updateBudgetDepense(id, newBudgetDepense):
    db = connectToBDD()
    cursor = db.cursor()

    requete_update = "UPDATE activite SET budget_depense = %s WHERE id = %s"

    valeurs = (newBudgetDepense, id)

    try:
        cursor.execute(requete_update, valeurs)
        db.commit()
        print(f"Budget dépensé mis à jour pour l'id {id} : {newBudgetDepense}")
    except mysql.connector.Error as err:
        db.rollback()
        print("Erreur lors de la mise à jour du budget dépensé :", err)
    finally:
        cursor.close()
        db.close()


def updateReste(id, newReste):
    db = connectToBDD()
    cursor = db.cursor()

    requete_update = "UPDATE activite SET reste = %s WHERE id = %s"

    valeurs = (newReste, id)

    try:
        cursor.execute(requete_update, valeurs)
        db.commit()
        print(f"Reste mis à jour pour l'id {id} : {newReste}")
    except mysql.connector.Error as err:
        db.rollback()
        print("Erreur lors de la mise à jour du reste :", err)
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


def getActivityById(idActivity):
    db = connectToBDD()
    cursor = db.cursor()

    requete_select = "SELECT * FROM activite WHERE id = %s"

    cursor.execute(requete_select, (idActivity,))
    resultat = cursor.fetchall()

    cursor.close()
    db.close()

    return resultat


def getSubActivitiesByIdParent(idParent):
    db = connectToBDD()
    cursor = db.cursor()

    requete_select = "SELECT * FROM activite WHERE id_parent = %s"

    cursor.execute(requete_select, (idParent,))
    resultats = cursor.fetchall()

    cursor.close()
    db.close()

    return resultats


#nv