# IZIRecord-case

The following steps will be presented for the local project usage.

> ## Prerequisites:
- Docker
- Docker-Compose

First, you need to identify the local directory where the project repository will be cloned.

Once the location is defined, run the following command to clone it:
```
$ git clone git@github.com:bereoff/IZIRecord-case.git
```

As the next step, you need to be in the project's root directory, where the docker-compose.yml file is located, and run the command:

<p align="center">
  <img src="https://github.com/bereoff/IZIRecord-case/blob/main/images/project-root.png" />
</p>

```
$ docker-compose up --build
```

This command will ensure that all necessary container images are downloaded to your computer and will start two services:
- Django
- Postgres

It will also install Python dependencies and perform other required routines for the process.

During the process, database migrations will be applied.

After this process is completed and the services are running, to access the Django admin and make requests to the documentation that comes with this API, you need to create a superuser.

Execute the following commands:
```
$ docker container ls
```

The following output will be displayed:

![List of containers](https://github.com/bereoff/IZIRecord-case/blob/main/images/docker-container-ls-command.png)

Use the container name referring to the Django application in the following command:
```
$ docker exec -it izirecord-case-django-1 bash
```

From this point on, you will be directly accessing the container in your terminal, and in this environment, you will create the user.

Perform the following test to confirm that the dependencies have been loaded:
```
$ ./manage.py --help
```

Additional commands to Django standards should be displayed.

Execute the following command to create a superuser:
```
$ ./manage.py createsuperuser --username=<your_username> --email=<your_email>
```

After executing this command, you will need to enter a password and confirm it. Avoid losing this password; otherwise, you will no longer have access to the user, and a new one will need to be created.

After these steps and with the services running, it will be possible to access the Django admin:
```
$ http://0.0.0.0:8000/admin/login/?next=/admin/
```
![Django Admin](https://github.com/bereoff/IZIRecord-case/blob/main/images/django-admin-login-page.png)

And the Swagger documentation for the application:
```
$ http://0.0.0.0:8000/api/schema/docs/
```
![API Swagger](https://github.com/bereoff/IZIRecord-case/blob/main/images/swagger-page.png)

---

> ## Test

To run the tests manually, it is necessary to have the services running and execute the following command:

```
$ docker-compose exec django python -m pytest
```

And whenever the services start, the test pipeline is executed.
