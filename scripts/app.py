from datetime import datetime
from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
import mysql.connector as mysql


# modèle fine-tuné utilisé
modele = os.getenv("MODEL_FINETUNE")

# Initialisation de la connexion avec OpenAI
def connexion_openai():
    load_dotenv()
    client = OpenAI()
    return client

def phrase_accueil():
    return f"LexyBot : Bonjour, comment puis-je vous aider ?"

# On interroge le modèle fine-tuné
def demander_au_modele_finetune(question):
    try:
        response = openai.ChatCompletion.create(
            model = modele,
            messages = [
                {"role": "system", "content": "Tu es un assistant amical et spécialisé."},
                {"role": "user", "content": question}
            ]
        )
        reponse = response.choices[0].message['content']
        return 1, reponse # succès
        # on récupère le texte généré par le modèle et on le renvoie en sortie de la fonction
    except openai.error.OpenAIError as e:
         return 2, f"Erreur innatendue : {str(e)}"# échec

# Sauvegarde des échanges dans la base de données
def sauvegarder_echange(prompt, reponse, date, statut):
        # Connexion à la base de données
        connexion = mysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),       
            password=os.getenv("DB_PASSWORD"),  
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT", 3306)        
        )

        curseur = connexion.cursor()
        requete = """
                INSERT INTO echanges (conversation, prompt, reponse, date, statut)
                VALUES (1, %s, %s, %s, %s)
            """
        valeurs = (prompt, reponse, date, statut)
        curseur.execute(requete, valeurs)
        connexion.commit()
        # ferme les connecxions à la base de données
        curseur.close()
        connexion.close()

# Boucle principale du chatbot
def main():
     client = connexion_openai()
     print(phrase_accueil())
     while True:
        user_input = input("Vous : ")
        if user_input.lower() in ['exit']:
             print("LexyBot : A bientôt !")
             break
        reponse, statut = demander_au_modele_finetune(user_input)
        print(f"LexyBot : {reponse}")
        sauvegarder_echange(user_input, reponse, datetime.now(), statut)

if __name__ == "__main__":
     main()