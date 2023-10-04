#ecrire un programme qui va lire les données d'un employer a partir du clavier
#identifiant, nom , salaire , adresse , marié
Id= input("veullez entrer votre identifiant\n")
nom = input("veullez entrer votre nom\n")
salaire = float( input("veullez entrer votre salaire\n"))
adresse = input("veullez entrer adresse\n")
status = bool(("est ce que vous ete marié ? : true/ false \n"))
print("[votre identifiant est: " , Id ,"]\n[votre nom est: ",nom ,"]\n[votre salaire est: " , str(salaire), "]\n[votre adresse est: " , adresse , "]\n[vous ete marie ?  ", status,"]" )
