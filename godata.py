import requests
import hashlib

print("Bienvenue dans l'outil de vérification d'adresse e-mail.")



print("                                                                 |---|   » GODATA V1 : Hoster") 
print("                                                                 |---|")
print("                                                                 |---|")
print("                                                             .---^ - ^---.")
print("                                                             :___________:")
print("                                                                |  |  |")
print("                                                                |  |  |")
print("                                                                |  |  |")
print("                                                                |  |  |")
print("                                                                |  |  |")
print("                                                                |  |  |")
print("                                                                |  |  |")
print("                                                                |.-'-_|")
print("                                                                 \***/")
print("                                                                  \*/")
print("                                                                   V")                                                                      
print("                                                                                ")
print("                                                              -.   ^   .-")
print("                                                          ______\'.|.'/________")

def run_application():
    email_to_check = input("Entrez l'adresse e-mail à vérifier : ")
    check_email(email_to_check)
 

def check_email(email):
    # Hash de l'adresse e-mail en SHA-1
    email_hash = hashlib.sha1(email.encode()).hexdigest().upper()

    # URL pour récupérer les données de fuite pour l'adresse e-mail
    url = f"https://api.github.com/repos/kilnapp/BreachCompilationData/contents/data/{email_hash}.json"


    # Effectue une requête GET à l'URL
    response = requests.get(url)

    # Vérifie le code de réponse
    if response.status_code == 200:
        # L'adresse e-mail a été compromise
        print(f"L'adresse e-mail {email} a été compromise dans les fuites de données suivantes:")
        data = response.json()
        for breach in data['breaches']:
            print(f"- {breach}")
    elif response.status_code == 404:
        # L'adresse e-mail n'a pas été compromise
        print(f"L'adresse e-mail {email} n'a pas été compromise dans les fuites de données.")
    else:
        # Erreur inattendue
        print(f"Une erreur est survenue lors de la vérification de l'adresse e-mail: {response.status_code}")

if __name__ == "__main__":
    email_to_check = input("Entrez l'adresse e-mail à vérifier : ")
    check_email(email_to_check)




