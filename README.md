# medical-exams

Projeto de exames médicos.

## Este projeto foi feito com:

* [Python 3.10.2](https://www.python.org/)
* [Django 4.0.4](https://www.djangoproject.com/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/mozartnp/medical-exams.git
cd medical-exams
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate

python manage.py createsuperuser

Email: admin@email.com
User type: PACI
Password: 
Password (again): 
```

## Docker

Leia [docker.md](docker.md)