<div>
# API 2022 
</div>

## Quickstart

- python3 -m pip install --user virtualenv

- python3 -m venv venv

- python3 -m pip install --upgrade pip

- source venv/bin/activate

- pip3 install -r requirements.txt

// ubuntu error install psycopg2
sudo apt install python3-dev libpq-dev
pip3 install psycopg2

- python3 manage.py runserver

- psql api -c "GRANT ALL ON ALL TABLES IN SCHEMA public to aminhp93;"

- psql api -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to aminhp93;"

- psql api -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to aminhp93;"

## Use cases

## How it works

## Limitations

## Advanced features

## Status

## Acknowledgements

## Licences

This project is licensed under the [MIT license](LICENSE).

It contains code that is copied and adapted from transformers (<https://github.com/huggingface/transformers>),
which is [Apache 2.0 licensed](http://www.apache.org/licenses/LICENSE-2.0). Files containing this code have
been marked as such in their comments.

export PG_HOME=/usr/lib/postgresql/14/bin/pg_config
export PATH=$PATH:$PG_HOME/bin
