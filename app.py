# app.py
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

@app.route('/', methods=['GET'])
def index():
    # Niveles de actividad
    niveles_actividad = [
        'Sedentario (Poco o ningún ejercicio)',
         'Poco Activo (1-3 días/semana)',
        'Moderadamente Activo (3-5 días/semana)',
         'Muy Activo (6-7 días/semana)',
         'Super Activo (Atleta profesional/2x entrenamientos)'
    ]

    return render_template('index.html', activity_level=niveles_actividad)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get form data
    edad = request.form.get('age')
    nivel_actividad = request.form.get('activity_level')
    comidas_favoritas = request.form.get('favourite_foods')
    restricciones = request.form.get('alergies')

    # Construcción del prompt mejorado por un propio LLM 
    prompt = f"""Como nutricionista profesional especializado en nutrición personalizada, crea un plan nutricional detallado para una persona con el siguiente perfil:
    Edad: {edad} años
    Nivel de actividad física: {nivel_actividad}
    Comidas favoritas: {comidas_favoritas}
    Restricciones dietéticas y alergias: {restricciones}

    Por favor, elabora un plan que incluya:
    1. Estimación de sus necesidades calóricas diarias, teniendo en cuenta su edad, nivel de actividad y restricciones.
    2. Distribución recomendada de macronutrientes (carbohidratos, proteínas, grasas) expresada en porcentaje y gramos aproximados.
    3. Plan de comidas diario de ejemplo (desayuno, almuerzo, cena y snacks), incorporando sus comidas favoritas siempre que sea posible y adaptándolas a sus necesidades.
    4. Consideraciones nutricionales específicas para su grupo de edad, como vitaminas o minerales clave.
    5. Recomendaciones concretas según su nivel de actividad física, como tiempos ideales de ingesta o alimentos para recuperación.
    6. Alternativas seguras y equilibradas para cualquier alimento restringido o alérgeno.
    7. 2 o 3 sugerencias de snacks saludables fáciles de preparar o conseguir.

    Elabora la respuesta con encabezados claros y estructura con listas o puntos para facilitar la lectura. Mantén un tono profesional y cercano, y prioriza la salud y la seguridad, especialmente en lo que respecta a las restricciones y alergias mencionadas. Redacta en español neutro y de forma clara.
    Asegurate de que los dos primeros puntos no sean extensos ni aburridos asi como tu respuesta en general.
    No incluyas información innecesaria o redundante, y evita el uso de jerga técnica compleja que pueda dificultar la comprensión del plan nutricional.
    Además, si lo crees conveniente puedes ayudarte también de tablas e imagenes
    Por último, ten en cuenta que solo puedes usar 1000 tokens en total para toda la respuesta, incluyendo los encabezados y las listas.
    """

    print("Prompt que vamos a enviar a Groq:")
    print("-----------------------------")
    print(prompt)
    print("-----------------------------")

    try:
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="mistral-saba-24b",
            temperature=0.7,
            max_tokens=10000,
        )
        
        recommendation = completion.choices[0].message.content
        return jsonify({'success': True, 'recommendation': recommendation})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)