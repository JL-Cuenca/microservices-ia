# 🚀 Portafolio de Microservicios IA – José Cuenca

Este repositorio contiene **3 microservicios desarrollados en Python con FastAPI**, diseñados para automatizar tareas comunes y ofrecer soluciones rápidas a emprendedores, freelancers y empresas.  
Todos los servicios están probados, documentados y listos para desplegar.

---

## 📌 Microservicios incluidos

### 1. 📱 Generador de Posts Automáticos
- **Función:** Genera publicaciones listas para Instagram, TikTok, Twitter y LinkedIn.  
- **Características:**
  - 25+ plantillas únicas por plataforma.
  - Validación de entrada con Pydantic.
  - Evita repetir plantillas en la misma solicitud.
  - Endpoint `/plataformas` para listar opciones disponibles.
- **Puerto:** 8003

---

### 2. 📊 Dashboard Express
- **Función:** Convierte archivos CSV en dashboards con KPIs y gráficos listos para presentar.  
- **Características:**
  - Validación de formato de archivo (solo CSV).
  - Manejo de errores robusto.
  - Gráficos generados con Matplotlib (sin fugas de memoria).
  - Retorna resumen de filas, columnas y estadísticas.
- **Puerto:** 8001

---

### 3. 🔤 Corrector y Traductor Automático
- **Función:** Corrige y traduce textos automáticamente.  
- **Características:**
  - 3 endpoints: corregir+traducir, solo corregir, solo traducir.
  - Validación de entrada (texto no vacío).
  - Manejo de errores con HTTPException.
  - Requiere instalación de corpus de TextBlob.
- **Puerto:** 8002

---

## ⚙️ Instalación y uso

### Requisitos previos
- Python 3.9+
- Pip instalado

### Pasos generales
1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU-USUARIO/microservices-ia.git
   cd microservices
