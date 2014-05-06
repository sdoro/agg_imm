### Premessa ###

I tipi di dato della soluzione PostgreSQL sono stati
leggermente addattati quando il tipo PostgreSQL non trova
corrispondenze nel models di Django.


### La prima prova di simulazione (1) ###

Versione utilizzata:

	$ django-admin --version
	1.4.5

Costruzione del progetto 'age_imm'

	$ django-admin startproject age_imm
	$ cd age_imm/

Editing del file 'setting.py':

	$ nano age_imm/settings.py

Editing del file 'urls.py':

	$ nano age_imm/urls.py 

Editing del file 'models.py':

	$ nano age_imm/models.py

Validazione del modello e test output in SQL:

	$ /manage.py validate
	$ /manage.py sqlall age_imm

Dopo aver verificato la correttezza si costruisce una
directory 'sql' e si inserisce tanti file corrispondenti
alle tabelle (class) con estensione '.sql' e contenenti
i comandi di insert. Alla fine si genera il db e si
genera anche la parte 'admin':

	$ nano age_imm/admin.py
	$ ./manage.py syncdb

Il risultato si verifica andando con un browser all'indirizzo
http://127.0.0.1:8000.

