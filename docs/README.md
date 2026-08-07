### PASSO 1: Installare Django
da terminale usare la seguente riga:

```
pip install django
```

### PASSO 2: Creare un progetto Django
da terminale usare la seguente riga:

```
django-admin startproject nome_progetto
```

creato il progetto, abbiamo una cartella con i file con estenzione .py

### PASSO 3: Creare un'app
dopo aver creato il progetto, spostarsi dentro la cartella del progetto, dentro c'é un file chiamato manage.py
da terminale usare la seguente riga per creare un'applicazione:

```
python manage.py startapp nome_applicazione
```

dopo aver digitato quella riga avrá creato una cartella con altri file con estenzione .py

### PASSO 4: Aggiunzione dell'applicazione
entrare su settings.py, andare nella sezione INSTALLED_APPS e scrivere la seguente riga di codice per aggiungerla:
'nomeapp.apps.NomeappConfig',
esattamente cosí.

### PASSO 5: L'esecuzione del server
Per eseguire il server, bisogna aprire il terminale e stare nel percorso file dove si trova il file manage.py e scrivere la seguente riga:

```
python manage.py runserver
```

aprirá un server, se vuoi aprire una specifica porta digitare il numero della porta dopo runserver quindi:

```
python manage.py runserver 9876
```

adesso si puó visualizzare il server quando si vuole ma momentaneamente abbiamo solo il path di admin e il congratulazioni per aver aperto un server django

### PASSO 6: Aggiunzione di un file frontend
mettere nella cartella nomeapp un'altra cartella chiamata "template" e mettergli dentro un ulteriore cartella chiamata "nomeapp" e si puó mettere all'interno il file.html

### PASSO 7: View
entarare nella cartella nomeapp dove ci sono dei file .py in particolare "views.py", in quel file scrivere una funzione chiama view dove all'ingresso deve esserci la request e deve ritornare una response che jango ci fornisce la funzione render():

```
def view(request):
    return render(request, nomeapp/file.html)
```

### PASSO 8: Models
nella stessa cartella della view c'é anche models.py, dentro bisogna metterci una classe del modello, come nell'esempio:

```
class Joint(models.Model):
    name = models.CharField(max_lenght=20)
    degree = models.IntegerFiend()

    def __str__(self):
        return self.name
```

str é importante se vuoi fare visualizzare il nome specifico di quel modello.

### PASSO 9: Migrazioni
ogni volta che si modifica il model bisogna fare delle migrazioni con le seguenti righe nel terminale:

(leggere i models)
```
python manage.py makemigrations
```

(applica le migrazioni al database)
```
python manage.py migrate
```

### PASSO 10: Registrazioni
bisogna registrarsi come admin nel seguente riga sul terminale:

```
python manage.py createsuperuser
```
bisogna mettere il nome dell'user, una email e una password

### PASSO 11: Login
adesso andare sul motore di ricerca e scrivere l'url (con il server aperto) localhost:9876/admin e fare il login

### PASSO 12: get_object_or_404()
È una funzione shortcut di Django che tenta di recuperare un oggetto dal database — se non esiste, invece di far crashare il server con un errore 500, restituisce automaticamente una risposta HTTP 404 (Not Found)

bisogna metterlo vicino all'import del render

```
from django.shortcuts import get_object_or_404, render
```

### PASSO 13: Creare Urls
entrare nella cartella vicino alla cartella nomeapp e crare file urls.py e mettere le seguenti righe:

```
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.nomemodel, name="list_nomemodel"),
    # path("change/<int:id>/", views.funzione, name="funzione")
]
```

path é la funzione che associa un URL a una view e ha i seguenti parametri: route	La stringa dell'URL da intercettare, view	La funzione/classe view da chiamare, kwargs	Argomenti extra da passare alla view (opzionale), name	Nome univoco dell'URL, usato nei template con {% url %} (opzionale)

### PASSO 14: urls
aprire urls su nomeapp e inserire sotto alla riga del path di admin mettere:

```
path('nome/', include('nome.urls')),
```

vicino all'import del path mettere include, in questo modo:

```
from django.urls import path, include
```

### Riepilogo di comandi + comandi utili
comandi con manage.py

```
python manage.py runserver          # Avvia server di sviluppo
python manage.py startapp nomeapp   # Crea nuova app
python manage.py makemigrations     # Genera migrazioni
python manage.py migrate            # Applica migrazioni
python manage.py createsuperuser    # Crea admin
python manage.py shell              # Shell Python con Django loaded
python manage.py test               # Esegue i test
python manage.py collectstatic      # Raccoglie i file statici (produzione)
python manage.py showmigrations     # Lista stato migrazioni
python manage.py dbshell            # Shell SQL diretta al database
```

```
Tipi di campo più comuni:

Campo	        Utilizzo

CharField	    Stringa breve (con max_length)
TextField	    Testo lungo
IntegerField	Intero
FloatField	    Float
BooleanField	True/False
DateTimeField	Data e ora
ForeignKey	    Relazione molti-a-uno
ManyToManyField	Relazione molti-a-molti
ImageField	    Upload immagini
FileField	    Upload file generici
```

```
Sintassi template Django:

Sintassi	                Significato

{{ variabile }}	            Stampa una variabile
{% tag %}	                Tag logico (for, if, block…)
{% url 'nome' %}	        Genera URL da nome
{% extends 'base.html' %}	Eredita un template
{% block contenuto %}	    Definisce un blocco
{% static 'file.css' %}	    File statici
```