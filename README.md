# 🥕 Asistente Nutricional Personal con PYTHON FLASK e Integración de LLM mediante el API de GROQ

> **ES**: Proyecto desarrollado para explorar la integración de IA generativa basada en LLMs en una aplicación web como parte del MOOC: Introducción a la inteligencia artificial generativa a través de los grandes modelos de lenguaje

> **EN**: Project developed to explore the integration of generative AI based on LLMs into a web application, as part of the MOOC: Introduction to Generative Artificial Intelligence through Large Language Models.

---

## 📌 Descripción | Description

🟢 **ES:**  
Esta aplicación web basada en **Flask** implementa un asistente nutricional personal que recibe datos del usuario (edad, nivel de actividad física, comidas favoritas y alergias) para generar un plan de comidas personalizado. El sistema realiza una llamada al **API de GROQ** para obtener la recomendación de un LLM y la presenta al usuario en formato claro y adaptado.

🔵 **EN:**  
This web application built with **Flask** implements a personal nutrition assistant that takes user input (age, activity level, favorite foods, and allergies) to create a personalized nutrition plan. The system uses the **GROQ API** to obtain a recommendation from an LLM and displays it to the user in a structured, easy-to-read format.

---

## 🚀 Características | Features

✅ **ES:**  
✔️ Captura de datos de usuario mediante formulario (edad, actividad, comidas favoritas, alergias).  
✔️ Integración con el **GROQ API** para obtener un plan nutricional adaptado.  
✔️ Resultado mostrado en formato claro y marcado con Markdown para facilitar la lectura.   
✔️ Implementación basada en **Flask**, fácil de desplegar y ejecutar en local.

✅ **EN:**  
✔️ User input captured via form (age, activity level, favorite foods, allergies).  
✔️ Integrated with **GROQ API** to obtain a tailored nutrition plan.  
✔️ Results rendered clearly using Markdown for easy readability.   
✔️ Simple **Flask** implementation, easy to deploy and run locally.

---

## 🛠️ Tecnologías | Technologies Used

- 🐍 **Python / Flask** → Framework para crear la aplicación web.  
- ⚡ **GROQ API** → LLM para generación de planes nutricionales adaptados al usuario.  
- 🌐 **HTML/CSS/JavaScript** → Interfaz de usuario y lógica de interacción.  
- 🗄️ **Dotenv** → Carga de variables de entorno para la clave de la API.  

---

## 📦 Instalación | Installation

🟢 **ES:**  
Sigue estos pasos para instalar y ejecutar el proyecto:

Clonar el repositorio
```bash
git clone https://github.com/serguccierrez/MOOC_genai_llms_webapp
cd MOOC_genai_llms_webapp
```
Crear y activar un entorno virtual
```bash
[LINUX/MAC] > 'python3 -m venv venv' + 'source venv/bin/activate'
[WINDOWS] > 'py -m venv venv' + '.\venv\Scripts\activate'
```
Instalar dependencias
```bash
pip install -r requirements.txt
```
Crear un fichero .env con tu clave de la API de GROQ
```bash
GROQ_API_KEY=TU_API_KEY_AQUÍ
```
Por último, iniciar la aplicación y acceder a la misma:
```bash
py app.py
accede a la URL: http://localhost:5000
```
🔵 **EN:**  
Follow these steps to install and run the project:

Clone the repository
```bash
git clone https://github.com/serguccierrez/MOOC_genai_llms_webapp
cd MOOC_genai_llms_webapp
```
Create and activate a virtual environment
```bash
[LINUX/MAC] > 'python3 -m venv venv' + 'source venv/bin/activate'
[WINDOWS] > 'py -m venv venv' + '.\venv\Scripts\activate'
```
Install dependencies
```bash
pip install -r requirements.txt
```
Create a .env file with your GROQ API key
```bash
GROQ_API_KEY=TU_API_KEY_AQUÍ
```
Finally, start the application and access it at:
```bash
py app.py
open your browser at: http://localhost:5000
```

---

## 📂 Estructura del Proyecto | Project Structure
```bash
MOOC_LLMs_mod2_ejemplo/
├── app.py            # Lógica principal de la app en Flask
├── templates/
│   └── index.html    # Página HTML para capturar datos y mostrar resultados
├── static/
│   └── ...            # Archivos estáticos (CSS, JS)
├── .env               # Variable de entorno para clave de GROQ
├── requirements.txt    # Dependencias de Python
```

## ⚡️ Flujo de Trabajo | Workflow
🟢 **ES:** 
1. El usuario ingresa edad, nivel de actividad física, comidas favoritas y alergias en el formulario.

2. Al hacer clic en "Generar Plan Nutricional", los datos son enviados al servidor (POST /recommend).

3. El servidor construye un prompt para el LLM de GROQ con estos datos.

4. El LLM procesa la solicitud y retorna un plan nutricional en formato Markdown.

5. El usuario recibe y visualiza la recomendación en la misma pantalla.

🔵 **EN:**  
1. The user inputs age, activity level, favorite foods, and allergies into the form.

2. Upon clicking "Generate Nutrition Plan," the data is sent to the server (POST /recommend).

3. The server builds a prompt for the GROQ LLM based on the user inputs.

4. The LLM processes the request and returns a nutrition plan in Markdown format.

5. The user views the recommendation on the same page, displayed clearly and readably.

---
## 📬 Contacto | Contact

📩 **serguccierrez** → [GitHub Profile](https://github.com/serguccierrez)  
Si tienes preguntas o sugerencias, crea un **issue** en este repositorio.  

