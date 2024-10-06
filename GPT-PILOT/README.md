# GPT-PILOT

Antes de empezar asegurate de tener instalado `python +3.9` para que no tengas problemas

1. Clonar el repo `git clone https://github.com/Pythagora-io/gpt-pilot.git`
2. `cd .\gpt-pilot\`
3. Crear el ambiente `python3 -m venv venv` o `python -m virtualenv env`
4. Activar ambiente `source env/bin/activate/` o `.\env\Scripts\activate`
5. Instalar dependencias `pip install -r requirements.txt`
6. Crear una copia del archivo de config `cp example-config.json config.json`
7. Abre el archivo `config.json` ahora podras editar el provider de LLM 

```json
"llm": {
    "openai": {
      // Base url to the provider/server, omitting the trailing "chat/completions" part.
      "base_url": null,
      "api_key": null,
      "connect_timeout": 60.0,
      "read_timeout": 20.0
    },
    // Example config for Anthropic (see https://docs.anthropic.com/docs/api-reference)
    "anthropic": {
      "base_url": "https://api.anthropic.com",
      "api_key": "your-api-key",
      "connect_timeout": 60.0,
      "read_timeout": 20.0
    },
    // Example config for Azure OpenAI (see https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#chat-completions)
    "azure": {
      "base_url": "https://your-resource-name.openai.azure.com/",
      "api_key": "your-api-key",
      "connect_timeout": 60.0,
      "read_timeout": 20.0,
      "extra": {
        "azure_deployment": "your-azure-deployment-id",
        "api_version": "2024-02-01"
      }
    }
  }
```
Si quieres usar una API_KEY de OpenAI solo deberás agregar esto
```json
"openai": {
      "base_url": null,
      "api_key": "TU_API_KEY",
      "connect_timeout": 60.0,
      "read_timeout": 20.0
    },
```
Si tu API key esta en null, intentara leerla desde las variables de entorno

Por defecto la base de datos que se usa es sqlite pero también soporte PostgreSQL

8. Si estas en Windows en el archivo `gpt-pilot/core/agents/spec_writer.py`
Cambia esto entre las lineas 70-72:
```python
if len(user_description) < ANALYZE_THRESHOLD and complexity != Complexity.SIMPLE:
    initial_spec = await self.analyze_spec(user_description)
    reviewed_spec = await self.review_spec(desc=user_description, spec=initial_spec)
```

Por esto:

```python
initial_spec = await self.analyze_spec(user_description)
reviewed_spec = await self.review_spec(desc=user_description, spec=initial_spec)
```
8. Ahora solo deberás ejecutar el archivo `main.py` y tendras el asistente listo para andar
9. Algunos ejemplos de prueba simples

**Ejemplo 1: SwiftAccounts API**

<!-- 
Create a FastAPI project with Pydantic models for user accounts. Implement CRUD operations using POST, GET, PUT, DELETE, and PATCH endpoints for user management. The API should include: user registration (POST /users/), user login (POST /users/login), get all users (GET /users/), get user by ID (GET /users/{user_id}), update user (PUT /users/{user_id}), partial update user (PATCH /users/{user_id}), and delete user (DELETE /users/{user_id}). Use Pydantic for request/response models and input validation.
Utilize a local database using Python dictionaries and lists to store user data in memory. Implement proper error handling and status codes for all endpoints. Include input validation, password hashing, and basic authentication. Use FastAPI's dependency injection for shared logic. Ensure the API follows RESTful principles and includes appropriate documentation using FastAPI's built-in Swagger UI.
-->

**Ejemplo 2: CartsWheels**
<!-- 
Create a Flask application that simulates a car shopping cart. Implement a home page displaying a list of up to 25 pre-selected car models. Each car should have a name, price, and "Add to Cart" button. Create routes for adding items to the cart (POST /add_to_cart), viewing the cart (GET /cart), updating quantities (POST /update_cart), and removing items (POST /remove_from_cart). Use Flask-WTF for form handling and CSRF protection.
Implement a simple in-memory data structure (e.g., a list of dictionaries) to store the product catalog and another for the shopping cart. Use Flask's session to maintain cart state between requests. Create HTML templates with Jinja2 for the product list and cart pages, styling them with CSS. Include a checkout button on the cart page (without actual payment processing). Ensure proper error handling and user feedback for all actions. Add a navigation bar for easy movement between pages and display the current cart total on all pages.
-->

