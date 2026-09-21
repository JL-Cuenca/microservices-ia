# 🔤 Corrector y Traductor Automático

Microservicio que corrige ortografía y traduce textos automáticamente usando TextBlob.

## 🚀 Instalación

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

**Nota importante:** Después de instalar las dependencias, debes descargar los datos de TextBlob ejecutando el segundo comando.

## ▶️ Ejecución

```bash
uvicorn app:app --reload --port 8002
```

## 📡 Endpoints

### POST /corregir_traducir
Corrige ortografía y traduce el texto.

**Body:**
```json
{
  "texto": "I havv a draem",
  "idioma": "es"
}
```

**Respuesta:**
```json
{
  "original": "I havv a draem",
  "corregido": "I have a dream",
  "traducido": "Tengo un sueño",
  "idioma_destino": "es"
}
```

### POST /solo_corregir
Solo corrige ortografía.

### POST /solo_traducir
Solo traduce el texto.

## 🌍 Códigos de idioma soportados
- `es` - Español
- `en` - Inglés
- `fr` - Francés
- `de` - Alemán
- `it` - Italiano
- Y muchos más...