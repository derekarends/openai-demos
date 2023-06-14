# pgvector

This demo repo is used to show how to install pgvector, load vector embeddings, and then search them.

To run with PostgreSQL docker:
* `docker pull ankane/pgvector`
* Connect to the server
  * Execute the following 
  * ```create extension if not exists vector;```
* Copy `.env.template`
* Rename to `.env`
* Fill out required env variables
* Make sure to have jupyter notebook installed
* Run [pgvector_notebook.ipynb](pgvector_notebook.ipynb)
