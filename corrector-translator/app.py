from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from textblob import TextBlob

app = FastAPI(title="Corrector y Traductor Automático", version="1.0.0")

class TextoEntrada(BaseModel):
    texto: str = Field(..., min_length=1, description="Texto a corregir y traducir")
    idioma: str = Field(default="es", description="Código del idioma destino (es, en, fr, de, etc.)")

@app.post("/corregir_traducir")
def corregir_traducir(data: TextoEntrada):
    """
    Corrige ortografía y traduce texto al idioma especificado
    """
    try:
        if not data.texto.strip():
            raise HTTPException(status_code=400, detail="El texto no puede estar vacío")
        
        blob = TextBlob(data.texto)
        
        # Corregir ortografía
        corregido = str(blob.correct())
        
        # Traducir al idioma destino
        try:
            traducido = str(blob.translate(to=data.idioma))
        except Exception as e:
            raise HTTPException(
                status_code=400, 
                detail=f"Error al traducir. Verifica el código de idioma: {data.idioma}"
            )
        
        return {
            "original": data.texto,
            "corregido": corregido,
            "traducido": traducido,
            "idioma_destino": data.idioma
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

@app.post("/solo_corregir")
def solo_corregir(texto: str):
    """
    Solo corrige ortografía sin traducir
    """
    try:
        blob = TextBlob(texto)
        corregido = str(blob.correct())
        return {"original": texto, "corregido": corregido}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/solo_traducir")
def solo_traducir(texto: str, idioma: str = "es"):
    """
    Solo traduce sin corregir
    """
    try:
        blob = TextBlob(texto)
        traducido = str(blob.translate(to=idioma))
        return {"original": texto, "traducido": traducido, "idioma": idioma}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al traducir: {str(e)}")

@app.get("/")
async def root():
    return {
        "mensaje": "API de Corrección y Traducción",
        "endpoints": ["/corregir_traducir", "/solo_corregir", "/solo_traducir"]
    }