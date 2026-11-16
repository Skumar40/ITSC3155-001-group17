### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Upgrading an existing Part 1 database

For an existing database whose `orders` table predates Part 2, set
`MYSQL_PASSWORD` and run these commands from the repository root before serving
requests. The first command creates the new tables. The second adds the order
foreign keys and is run once per Part 1 database. Existing orders retain their
`customer_name` and start with empty customer and promotion links.

```sh
python -c 'from api.models.model_loader import index; index()'
mysql -h localhost -P 3306 -u root -p sandwich_maker_api < api/migrations/part2.sql
```

For a fresh database, normal application startup creates the complete schema.
