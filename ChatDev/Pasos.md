# Crear software con Chat Dev

1. Ir a tu ruta de trabajo
2. Clonar el repositorio
    ```bash
    git clone https://github.com/OpenBMB/ChatDev.git
    ```
3. Navegar al directorio clonado
    ```bash
    cd ChatDev
    ```
4. Configurar tu clave de API como variable de entorno
    ```bash
    $env:OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXX"
    ```
5. Crear un entorno virtual aislado
    ```bash
    python -m venv myenv
    ```
6. Activar el entorno virtual
    ```bash
    .\myenv\Scripts\activate
    ```
7. Instalar las dependencias
    ```bash
    python -m pip install -r .\requirements.txt
    ```
8. Iniciar el proceso de desarrollo
    ```bash
    python run.py --task "una aplicación de contraseñas donde los usuarios pueden crear, cambiar y eliminar contraseñas" --name "password"
    ```
9. Esperar a que termine; al final, dentro de la carpeta `Warehouse`, podrás visualizar tu proyecto.
10. Ahora podrás ver el flujo de conversaciones con:
    ```bash
    python .\visualizer\app.py
    ```
