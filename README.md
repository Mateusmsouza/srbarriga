# Sr. Barriga

Cobra alugueis de spotify e é chato

<img
  src="https://aventurasnahistoria.uol.com.br/media/_versions/entretenimento/chaves_1_widelg.jpg"
  alt="Senhor Barriga"
  width="400"
/>

##  Development

### Local Development 
First you will need a mongodb instance. You may use docker compose to build a docker running mongo.

### Spinning up your environment
```bash
make build
```
Then export a environment variable to the database:
```bash
export MONGO_URI=mongodb://localhost:27017/dev # or any URI to an mongodb
``` 
And if you want to avoid sending notifications to Telegram group:
```bash
export SEND_NOTIFICATION=0
```
You will need some users on your database, so you may import the `people.json` on project root  file to the collection  `group.people`.

#### Running charge routine
```bash
make run-charge
```
  

###  Lint

  

####  **Useful commands**

  

Run lint:

  

```bash

make lint

```

  

Fix lint:

  

```bash

make fix
