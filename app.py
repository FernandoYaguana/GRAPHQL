from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema
import os


# Definimos el tipo de consulta
class Query(ObjectType):
    hello = String(description="A greeting to the world")
    
    def resolve_hello(self, info):
        return "Hola Mundo desde GraphQL"

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de GraphQL
schema = Schema(query=Query)

# Verifica si el entorno es producción o desarrollo
is_production = os.environ.get('FLASK_ENV') == 'production'

# Deshabilitar introspección solo en producción
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=not is_production))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')