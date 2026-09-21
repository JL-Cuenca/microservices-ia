from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import random

app = FastAPI(title="Generador de Posts Automáticos", version="1.0.0")

class PostRequest(BaseModel):
    tema: str = Field(..., min_length=1, description="Tema o keyword para los posts")
    cantidad: int = Field(default=5, ge=1, le=20, description="Cantidad de posts a generar (1-20)")
    plataforma: str = Field(default="general", description="Plataforma: instagram, tiktok, twitter, linkedin, general")

plantillas = {
    "general": [
        "¿Sabías que {tema}? Descúbrelo ahora 🚀",
        "Tips rápidos sobre {tema}: #IA #Productividad",
        "Transforma tu negocio con {tema} 💡",
        "El secreto detrás de {tema} revelado 🔥",
        "Domina {tema} en 3 pasos simples ✅"
    ],
    "instagram": [
        "✨ {tema} como nunca lo habías visto\n\n#Marketing #Emprendimiento",
        "🎯 La guía definitiva de {tema}\n\nGuarda este post 📌",
        "💎 {tema}: El cambio que tu negocio necesita",
        "🔥 Hablemos de {tema}\n\n¿Qué opinas? Comenta 👇",
        "⚡ {tema} explicado en 60 segundos"
    ],
    "tiktok": [
        "POV: Descubriste {tema} 😱 #fyp #viral",
        "¿{tema}? Te explico RÁPIDO ⚡ #tutorial",
        "Nadie habla de {tema} y es un ERROR 🚨",
        "3 cosas sobre {tema} que cambiarán tu vida 🤯",
        "{tema} antes vs después 💀 #trending"
    ],
    "twitter": [
        "🧵 Thread sobre {tema}:\n\n1/5",
        "Hot take: {tema} es el futuro 🚀",
        "Si no conoces {tema}, estás atrasado",
        "Quick tip sobre {tema} que nadie te dice:",
        "{tema} in 2024 be like: 📈"
    ],
    "linkedin": [
        "📊 Mi experiencia con {tema} en los últimos 6 meses:",
        "🎯 Lección aprendida: {tema} es clave para el crecimiento",
        "💼 Cómo {tema} transformó nuestra estrategia empresarial",
        "🚀 3 insights sobre {tema} que todo profesional debe conocer",
        "📈 Case study: Implementando {tema} en la empresa"
    ]
}

@app.post("/generar_posts")
def generar_posts(req: PostRequest):
    """
    Genera posts personalizados para redes sociales
    """
    try:
        if not req.tema.strip():
            raise HTTPException(status_code=400, detail="El tema no puede estar vacío")
        
        # Seleccionar plantillas según la plataforma
        plataforma_lower = req.plataforma.lower()
        if plataforma_lower not in plantillas:
            plataforma_lower = "general"
        
        templates = plantillas[plataforma_lower]
        
        # Generar posts únicos
        posts = []
        templates_disponibles = templates.copy()
        
        for _ in range(req.cantidad):
            if not templates_disponibles:
                templates_disponibles = templates.copy()
            
            template = random.choice(templates_disponibles)
            templates_disponibles.remove(template)
            posts.append(template.format(tema=req.tema))
        
        return {
            "posts_generados": posts,
            "cantidad": len(posts),
            "tema": req.tema,
            "plataforma": plataforma_lower
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar posts: {str(e)}")

@app.get("/plataformas")
def listar_plataformas():
    """
    Lista las plataformas disponibles
    """
    return {
        "plataformas": list(plantillas.keys()),
        "descripcion": "Usa estos valores en el campo 'plataforma'"
    }

@app.get("/")
async def root():
    return {
        "mensaje": "Generador de Posts Automáticos",
        "endpoints": ["/generar_posts", "/plataformas"]
    }