# Desafio Nível Socioeconômico (Inse)
Desafio proposto para a vaga de Analista de Sistemas Jr.

## Tecnologias utilizadas no frontend
O frontend foi construído em javascript com React.
  - `MUI` criação de componentes personalizados (input, divs, etc) e ícones. 
  - `Axios` realizar buscas (fetchs) no backend.
  - `React-router-dom` para navegar entre páginas usando parametros de busca.

## Tecnologia utilizada no backend
O backend foi todo construído em [python]()
  - `Flask` usado para construir uma API. 
  - `Flask RestX` para facilitar a construção de APIs Rest.
  - `Pandas` para o tratamento básico de dados.
  - `SQLAlchemy` para a criação dos models, conectors e consultas.
  - `Alembic` para a criação das migrações.

O banco de dados utilizado foi o Postgres

## Execução do backend com docker-compose
Tanto a API quanto o banco serão executadas utilizando docker-compose. Em um terminal, acesse a pasta do `backend`
<pre>$ cd backend
$ docker compose up --build
</pre>

## Execução do frontend
Em outro terminal, acesse a pasta do `frontend`
<pre>$ cd frontend
$ npm install
$ npm start
</pre>