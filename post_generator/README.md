# 📱 Generador de Posts Automáticos

Microservicio que genera publicaciones personalizadas para Instagram, TikTok, Twitter, LinkedIn y más.

## 🚀 Instalación

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
uvicorn app:app --reload --port 8003
```

## 📡 Endpoints

### POST /generar_posts
Genera posts automáticos para redes sociales.

**Body:**
```json
{
  "tema": "Inteligencia Artificial",
  "cantidad": 5,
  "plataforma": "instagram"
}
```

**Respuesta:**
```json
{
  "posts_generados": [
    "✨ Inteligencia Artificial como nunca lo habías visto\n\n#Marketing #Emprendimiento",
    "🎯 La guía definitiva de Inteligencia Artificial\n\nGuarda este post 📌"
  ],
  "cantidad": 5,
  "tema": "Inteligencia Artificial",
  "plataforma": "instagram"
}
```

### GET /plataformas
Lista todas las plataformas disponibles.

## 🎯 Plataformas soportadas
- `instagram` - Posts visuales con emojis
- `tiktok` - Contenido viral y trendy
- `twitter` - Tweets y threads
- `linkedin` - Contenido profesional
- `general` - Posts genéricos

## 🧪 Ejemplo de uso con Python

```python
import requests

response = requests.post(
    "http://localhost:8003/generar_posts",
    json={
        "tema": "Marketing Digital",
        "cantidad": 3,
        "plataforma": "tiktok"
    }
)
print(response.json())
```