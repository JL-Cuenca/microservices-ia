# 📊 Dashboard Express

Microservicio que convierte archivos CSV en dashboards con KPIs y gráficos estadísticos.

## 🚀 Instalación

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
uvicorn app:app --reload --port 8001
```

## 📡 Endpoints

### POST /dashboard
Genera un dashboard a partir de un archivo CSV.

**Ejemplo de uso con curl:**
```bash
curl -X POST "http://localhost:8001/dashboard" -F "file=@datos.csv"
```

**Respuesta:**
```json
{
  "resumen": {...},
  "grafico": "dashboard.png",
  "filas": 100,
  "columnas": ["col1", "col2"]
}
```

## 🧪 Prueba rápida

```python
import requests

with open("datos.csv", "rb") as f:
    response = requests.post("http://localhost:8001/dashboard", files={"file": f})
    print(response.json())
```