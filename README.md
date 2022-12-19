# README

# Sr. Barriga

Cobra alugueis de spotify e é chato

![https://aventurasnahistoria.uol.com.br/media/_versions/entretenimento/chaves_1_widelg.jpg](https://aventurasnahistoria.uol.com.br/media/_versions/entretenimento/chaves_1_widelg.jpg)

## Using Sr Barriga

Sr Barriga is an automation for splitting streamming services’s bill and notify about it monthly.

It runs a job using Github Actions and fires a script to send a message on a Telegram Group to remember people how much and when they should pay.

That means you don’t have to remember nor ask people to pay you by your Netflix or Disney +, Sr Barriga will take care for you 😊.

Currently supported features are:

- Charge monthly;
- Payment register script;
- Sends message on Telegram to remember the group.

<a href="https://www.buymeacoffee.com/msouza" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

**Here are useful commands:**

```bash
# Charges everyone in the group. It is runned monthly by Github Actions
make run-charge
```

## Development

### Local Development

First you will need a mongodb instance. You may use docker compose to build a docker running mongo.

```bash
# Spinning up your environment
make build
# Then export a environment variable to the database or any URI to a mongodb
export MONGO_URI=mongodb://localhost:27017/dev
# if you want to avoid sending notifications to Telegram group:
export SEND_NOTIFICATION=0
```

OBS: *You will need some users on your database, so you may import the `people.json` on project root file to the collection `group.people`.*

### **Useful commands**

```bash
# run lint on code base
$ make lint
# fix some lint problems
$ make fix
```