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

# altere o valor de USE_DOCKER para False
sed -i "s/USE_DOCKER=True/USE_DOCKER=False/" .env

# migração
python manage.py migrate

# crie super usuários
python manage.py createsuperuser --email="admin@email.com" --user_type="MEDI"
```

http://localhost:8000/


## Docker

Leia [docker.md](docker.md)

```
# altere o valor de USE_DOCKER para True
sed -i "s/USE_DOCKER=False/USE_DOCKER=True/" .env

# suba os containers
docker-compose up --build -d

# migração
docker container exec -it app python manage.py migrate

# crie super usuários
docker container exec -it app python manage.py createsuperuser --email="admin@email.com" --user_type="MEDI"
docker container exec -it app python manage.py createsuperuser --email="mozart@email.com" --user_type="PACI"
```

Com Docker o projeto roda na porta

http://0.0.0.0:8001/

