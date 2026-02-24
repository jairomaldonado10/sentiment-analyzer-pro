from textblob import TextBlob

def analizar_sentimiento(texto):
    # Creamos un objeto de TextBlob con el texto
    analisis = TextBlob(texto)
    
    # La polaridad va de -1 (muy negativo) a 1 (muy positivo)
    polaridad = analisis.sentiment.polarity
    
    if polaridad > 0:
        return "😊 Positivo"
    elif polaridad < 0:
        return "😡 Negativo"
    else:
        return "😐 Neutral"

if __name__ == "__main__":
    print("--- Analizador de Sentimiento Pro ---")
    frase = input("Escribe algo (en inglés por ahora): ")
    resultado = analizar_sentimiento(frase)
    print(f"El sentimiento es: {resultado}")