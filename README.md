# Proyecto Django - API de Usuarios por Género

Este proyecto es un ejemplo de cómo crear una API GraphQL simple con Django que separa usuarios por géneros. La API tiene dos queries que devuelven listas de nombres de usuarios masculinos y femeninos.


## Requisitos

- Python 3.x

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/mframosg/basic-graphql-django.git
    cd basic-rest-django
    ```

2. Crea un entorno virtual y actívalo:

    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias desde `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Paso a paso del código realizado

1. Añade las siguientes aplicaciones a tu proyecto Django:

    - `'graphene_django'`
    - `'users'`

    Abre el archivo `myproject/settings.py` y asegúrate de que las aplicaciones estén listadas en `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        ...
        'graphene_django',
        'users',
    ]
    ```

    Configura Graphene en `myproject/settings.py`:

    ```python
    GRAPHENE = {
        'SCHEMA': 'myproject.schema.schema'
    }
    ```

2. Configura las rutas del proyecto para incluir las rutas de la aplicación `users`. Abre `myproject/urls.py` y añade el siguiente código:

    ```python
    from django.contrib import admin
    from django.urls import path
    from graphene_django.views import GraphQLView
    from django.views.decorators.csrf import csrf_exempt

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    ]
    ```

3. Define el esquema GraphQL para la aplicación `users`. Crea un archivo `users/schema.py` y añade el siguiente código:

    ```python
    import graphene

    class Query(graphene.ObjectType):
        men = graphene.List(graphene.String)
        women = graphene.List(graphene.String)

        def resolve_men(self, info):
            return ["Juan", "Pedro", "Pablo", "Jose"]

        def resolve_women(self, info):
            return ["Maria"]

    schema = graphene.Schema(query=Query)
    ```

4. Define el esquema principal del proyecto. Crea un archivo `myproject/schema.py` y añade el siguiente código:

    ```python
    import graphene
    import users.schema

    class Query(users.schema.Query, graphene.ObjectType):
        pass

    schema = graphene.Schema(query=Query)
    ```

## Uso

1. Realiza las migraciones y crea la base de datos:

    ```sh
    python manage.py migrate
    ```

2. Ejecuta el servidor de desarrollo de Django:

    ```sh
    python manage.py runserver
    ```

3. Prueba las consultas GraphQL en tu navegador web o con una herramienta como GraphQL.

   - Consultar usuarios masculinos:

     ```graphql
     {
       men
     }
     ```

     Respuesta:

     ```json
     {
       "data": {
         "men": ["Juan", "Pedro", "Pablo", "Jose"]
       }
     }
     ```

   - Consultar usuarios femeninos:

     ```graphql
     {
       women
     }
     ```

     Respuesta:

     ```json
     {
       "data": {
         "women": ["Maria"]
       }
     }
     ```