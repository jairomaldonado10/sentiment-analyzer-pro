import pandas as pd
from textblob import TextBlob

def analizar_en_espanol(texto):
    try:
        # Traducimos al inglés para que TextBlob sea 100% preciso
        blob = TextBlob(texto)
        traduccion = blob.translate(from_lang='es', to='en')
        polaridad = traduccion.sentiment.polarity
        
        if polaridad > 0.1: return "😊 Positivo"
        elif polaridad < -0.1: return "😡 Negativo"
        else: return "😐 Neutral"
    except:
        return "❓ Error al traducir"

# 1. Crear datos de prueba (Simulamos un Excel/CSV)
data = {
    'Comentario': [
        "Este producto es increíble, me encanta",
        "Pésimo servicio, no lo recomiendo para nada",
        "Está bien, cumple con lo que dice",
        "Me llegó roto y tarde, una estafa",
        "La mejor compra que he hecho este año"
    ]
}

df = pd.DataFrame(data)

# 2. Aplicar el análisis
print("--- Analizando sentimientos en español... ---")
df['Resultado'] = df['Comentario'].apply(analizar_en_espanol)

# 3. Guardar el resultado
df.to_csv('reporte_sentimientos.csv', index=False)
print("¡Listo! Revisa el archivo 'reporte_sentimientos.csv'")
print(df) 