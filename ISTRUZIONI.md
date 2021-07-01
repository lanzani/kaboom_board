# Come eseguire l'applicazione
## Configurazione
Il programma è realizzato in python 3.8 utilizzando il framework django


Si consiglia l'utilizzo di un ambiente virtuale come [anaconda](https://www.anaconda.com/products/individual), 
[venv](https://docs.python.org/3/library/venv.html) o [pipenv](https://pypi.org/project/pipenv/), 
in alternativa installare python sul proprio sistema dal sito ufficiale ([python 3.8.10 download](https://www.python.org/downloads/release/python-3810/)).

### 1. Installare Python
- python version: 3.8.x 

### 2. Installare le dipendenze
Installare le dipendenze del progetto tramite il comando `pip`:

- Install Django:
`pip install django`

- Install Crispy Forms:
`pip install django-crispy-forms`

- Install Crispy Bootstrap5:
`pip install crispy-bootstrap5`

- Install Django Resized:
`pip install django_resized`

- Install Pillow:
`pip install Pillow`
  
  
## Avvio
**Nota**: Per utilizzare l'applicazione serve un account, quindi è possibile crearne uno direttamente dall'applicazione 
una volta avviata o fare il login con l'account demo con username:`demoUser`e password `SistemiDistribuiti2!`.

**Avvio applicazione**:
1. Da terminale andare nella root del progetto `kaboom_board`. (Dove è situato anche questo file)
2. Avviare il server con il comando `python manage.py runserver`
3. Andare con il proprio browser all'indirizzo del localhost porta 8000 (http://127.0.0.1:8000/)

