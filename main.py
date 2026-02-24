import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

def analizar_en_espanol(texto):
    try:
        blob = TextBlob(texto)
        traduccion = blob.translate(from_lang='es', to='en')
        polaridad = traduccion.sentiment.polarity
        if polaridad > 0.1: return "Positivo"
        elif polaridad < -0.1: return "Negativo"
        else: return "Neutral"
    except:
        return "Error"

# 1. Datos de prueba
data = {
    'Comentario': [
        "Increíble, me encanta", "Pésimo servicio", "Está bien", 
        "Una estafa total", "La mejor compra", "No me gustó mucho",
        "Funciona perfecto", "Llegó un poco tarde", "Calidad excelente"
    ]
}
df = pd.DataFrame(data)

# 2. Análisis
print("Analizando sentimientos...")
df['Resultado'] = df['Comentario'].apply(analizar_en_espanol)

# 3. GENERAR GRÁFICA (Lo nuevo)
plt.figure(figsize=(8, 6))
sns.countplot(x='Resultado', data=df, palette=['green', 'red', 'gray', 'yellow'])
plt.title('Resumen de Sentimientos de Clientes')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de Comentarios')

# Guardamos la gráfica como imagen
plt.savefig('reporte_visual.png')
print("¡Gráfica guardada como 'reporte_visual.png'!")

# 4. Guardar CSV
df.to_csv('reporte_final.csv', index=False)