# containerized_airflow

Airflow in a docker container by following the instructions outlined in [Airflow Docker image extension quickstart](https://airflow.apache.org/docs/docker-stack/build.html#build-build-image) and [Running Airflow in Docker how to guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

---
### OVERVEIW:
---

 This repo should only be used to jump start a development enviornment or as a training method to become more familar with writing DAGs in Airflow.

---
## Initializing Environment
---
Before starting Airflow for the first time, you need to prepare your environment, i.e. create the necessary files, directories and initialize the database.

- Create a **`.env`** file in the same directory as the **`compose.yaml`** file to add the [Airflow specific Docker compose enviornmental variables](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#docker-compose-env-variables).

For our simple example we will just use the following ENV Variables.
```
AIRFLOW_VERSION=3.1.8
AIRFLOW_UID=50000
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow
```
---
## Build the Airflow Image
Because we are creating a custom image and installing other dependencies via the
requirements.txt file we will need to build the image first.

```
docker compose build
```
---
## Initialize the database
---
On all operating systems, you need to run database migrations and create the first user account. To do this, run.

```
docker compose up airflow-init
```

After initialization is complete, you should see a message like this:
```
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 3.1.8
start_airflow-init_1 exited with code 0
```
The account created has the login **`airflow`** and the password **`airflow`**
---
## Running Airflow
---
Now you can start all services:

```
docker compose up
```
---