# Écrire un programme qui choisi le plus grand nombre parmi deux nombres saisies a partir du clavier
a= input("veullez entrer num 1\n")
b= input("veullez entrer num2\n")
c= input("veullez entrer num 3\n")

if a>b and a>c  :
     print( "le plus grand nombre est " ,a)
elif b>a and b>c  :
     print("le plus grand nombre est " ,b)
elif c>a and c>b :
     print("le plus grand nombre est ", c)

