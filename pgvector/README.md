# pgvector

This demo repo is used to show how to install pgvector, load vector embeddings, and then search them.

To run with PostgreSQL docker:
* `docker pull ankane/pgvector`
* Connect to the server
* Create the database which is first line [scripts.sql](scripts.sql)
* Make sure that database is selected and execute the rest of [scripts.sql](scripts.sql)
* Copy `.env.template`
* Rename to `.env`
* Fill out required env variables
* Make sure to have jupyter notebook installed
* Run [pgvector_notebook.ipynb](pgvector_notebook.ipynb)