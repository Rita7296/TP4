import os


badhash = input("Entrez le hash du commit contenant le bogue (bad commit) : ")
goodhash = input("Entrez le hash d’un commit fonctionnel (good commit) : ")

# Démarrer le bisect entre les deux commits
os.system(f"git bisect start {badhash} {goodhash}")

# Lancer la commande de test automatique
os.system("git bisect run pytest")


