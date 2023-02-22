# muniDach
Prepare the env : 
1 - Install python via this link : https://www.python.org/downloads/
2- Install django : ouvre ton commande line "CMD" avec l'option 'Tant que admin', aprés lance cette commande : py -m pip install Django

Maitenant telecharge la version zip du git
extraire le .zip 
Navigue vers le dossier déja extrait
ouvre votre cmd "invite de commande " 
Ecrire cette commande pour que le projet se lance : python manage.py runserver

ouvre votre navigateur est ecrie cette adresse dans la barre de rechereche : http://127.0.0.1:8000/admin

Pour login en tant que super admin : 
Log : Parkinny
Password : Parkinny147

en cas d'erreur tu peut créer un nouvau compte comme suit: 
python manage.py createsuperuser (aprés tu fait la siasie des nouvelles info)
aprés tu fait : python manage.py makemigrations
                python manage.py migrate
                python manage.py runserver
                


