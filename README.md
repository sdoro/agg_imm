### Premessa ###

I tipi di dato della soluzione PostgreSQL sono stati
leggermente adattati quando il tipo PostgreSQL non trova
corrispondenze nel modello di Django.


### La prima prova di simulazione (1) ###

In ambiente c9.io autenticati con l'account github.com e seleziona il repository agg_imm.
Successivamente digita i comandi:

	virtualenv $HOME/.env
	source $HOME/.env/bin/activate
	pip install django==1.4.5

Verifica che Django funziona ad esempio lanciando il comando
di visualizzazione della versione:

	$ django-admin.py --version
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

	$ ./manage.py validate
	$ ./manage.py sqlall age_imm

Dopo aver verificato la correttezza si costruisce una
directory 'sql' e si inserisce tanti file corrispondenti
alle tabelle (class) con estensione '.sql' e contenenti
i comandi di insert. Alla fine si genera il db e si
genera anche la parte 'admin' (user/password=dba/dba):

	$ nano age_imm/admin.py
	$ ./manage.py syncdb

Il risultato si verifica attivando il server con:

	$ ./manage.py runserver $IP:$PORT

e con il browser all'indirizzo https://agg-imm-sdoro.c9users.io/

Per sperimentare l'interterfaccia amministrativa (admin)
punta invece il browser su https://agg-imm-sdoro.c9users.io/admin

