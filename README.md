# Installation

```
git clone git@gitlab.com:ai-python-django/hr-utilities.git
cd hr_utilities
```

# ENV FILE
- Keep the environment file .env in project root directory

- For Developoment Environment:
    - Setup .env as following:
    ```
    DEBUG=True
    TEMPLATE_DEBUG=True
    ENVIRONMENT=development
    SECRET_KEY=django-insecure-_8t6=8t#&c5wo+7p2r28k_t0+5ahkordrwe2#_+)bo@252xg8v

    #DB
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=hr_utilities
    DB_USER=postgres
    DB_PASSWORD=admin#123
    DB_HOST=db
    DB_PORT=5432
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=admin#123

    #EMAIL
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_USE_TLS=True
    EMAIL_PORT=587
    EMAIL_HOST_USER=djangomail3000@gmail.com
    EMAIL_HOST_PASSWORD=djangotestingmail
    EMAIL_USE_SSL=False
    EMAIL_TO_ALL_STAFF=meeting_all_staff@yopmail.com

    #KEYCLOAK
    KEYCLOAK_REALM=InfoDevelopers
    KEYCLOAK_CLIENT_ID=hr-utility
    KEYCLOAK_DEFAULT_ACCESS=ALLOW
    KEYCLOAK_METHOD_VALIDATE_TOKEN=DECODE
    KEYCLOAK_SERVER_URL=http://192.168.50.140:9001/auth/
    KEYCLOAK_CLIENT_SECRET_KEY=a18e357e-7372-4e0e-ad4e-8c62225fea0c


    #CELERY
    RABBITMQ_DEFAULT_USER=admin
    RABBITMQ_DEFAULT_PASS=password
    CELERY_BROKER_URL=amqp://admin:password@rabbit:5672
    CELERY_SETTINGS_MODULE=hr_utilities.settings.development

    #SMIS ALL PROJECTS
    SMIS_ALL_PROJECTS=https://smis.infodev.com.np/smartmis/overall/get/project-product/list

    #HR ALL USERS
    HR_ALL_USERS=http://192.168.50.140:9001/customer/users

    # OPENID URL
    SSO_URI=https://idnhris.infodev.com.np

    # EMPLOYEE DETAIL API
    EMPLOYEE_DETAIL_API_URL=http://172.23.1.130:1902/api/User/getEmployeeListByEmpCode

    # ALL EMPLOYEE LIST
    HRIS_ALL_EMPLOYEE_LIST=http://172.23.1.130:1902/api/User/getEmployeeNameList


    ```

- For Production Environment:
    - Setup .env.prod as follows:
    ```
    DEBUG=False
    TEMPLATE_DEBUG=False
    ENVIRONMENT=production
    SECRET_KEY=django-insecure-_8t6=8t#&c5wo+7p2r28k_t0+5ahkordrwe2#_+)bo@252xg8v

    #DB
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=hr_utilities
    DB_USER=postgres
    DB_PASSWORD=admin#123
    DB_HOST=db
    DB_PORT=5432
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=admin#123
    POSTGRES_DB=hr_utilities

    #EMAIL
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_USE_TLS=True
    EMAIL_PORT=587
    EMAIL_HOST_USER=noreply@infodev.com.np
    EMAIL_HOST_PASSWORD=Nepal999
    EMAIL_USE_SSL=False
    EMAIL_TO_ALL_STAFF=allstaff@infodevelopers.com

    #KEYCLOAK
    KEYCLOAK_REALM=InfoDeveloper
    KEYCLOAK_CLIENT_ID=hr-utility
    KEYCLOAK_DEFAULT_ACCESS=ALLOW 
    KEYCLOAK_METHOD_VALIDATE_TOKEN=DECODE
    KEYCLOAK_SERVER_URL=https://sinfra.infodev.com.np/auth/
    KEYCLOAK_CLIENT_SECRET_KEY=2afa2d92-de26-4aaa-a4a7-da7075d4b5a4

    #CELERY
    RABBITMQ_DEFAULT_USER=admin
    RABBITMQ_DEFAULT_PASS=password
    CELERY_BROKER_URL=amqp://admin:password@rabbit:5672
    CELERY_SETTINGS_MODULE=hr_utilities.settings.production

    #SMIS ALL PROJECTS
    SMIS_ALL_PROJECTS=https://smis.infodev.com.np/smartmis/overall/get/project-product/list

    #HR ALL USERS
    HR_ALL_USERS=https://sinfra.infodev.com.np/auth/customer/users/

    # OPENID URL
    SSO_URI=https://idnhris.infodev.com.np/

    # EMPLOYEE DETAIL API
    EMPLOYEE_DETAIL_API_URL=https://hris.infodev.com.np/api/User/getEmployeeListByEmpCode

    # ALL EMPLOYEE LIST
    HRIS_ALL_EMPLOYEE_LIST=https://hris.infodev.com.np/api/User/getEmployeeNameList
    

    #sentry key
    DSN_KEY=sentry_key

    ```

    - Setup .env.prod.db as follows:
    ```
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=admin#123
    POSTGRES_DB=hr_utilities
    ```

# Configuring The Project 

    - Install docker and docker-compose

    - run these commands in order:

        docker-compose up -d --build
        docker-compose exec web python manage.py migrate --noinput

    - use this command to create superuser
        docker-compose run web python manage.py createsuperuser

- Project will run on ```http://127.0.0.1:8000```

# Management Command
Create Management Command Using the command:
```
docker-compose run web python manage.py create_all_commands
```



# Swagger Documentation

- To use swagger documentation, {{baseurl}}/swagger/ can be used
- To access the doucmentation,
    1. Download `ModHeader` extension in your browser. 
    2. Add request header as
    | Authentication | Bearer token_from_keycloak |


# Redoc Documentation

- To use recod documentation, {{baseurl}}/redoc/ can be used
- To access the doucmentation,
    1. Download `ModHeader` extension in your browser. 
    2. Add request header as
    | Authentication | Bearer token_from_keycloak |

