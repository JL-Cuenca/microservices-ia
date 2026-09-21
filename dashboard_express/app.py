from fastapi import FastAPI, UploadFile, HTTPException
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Backend no interactivo para servidores

app = FastAPI(title="Dashboard Express", version="1.0.0")

@app.post("/dashboard")
async def generar_dashboard(file: UploadFile):
    """
    Genera un dashboard con estadísticas y gráficos a partir de un archivo CSV
    """
    try:
        # Validar que sea un archivo CSV
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Solo se aceptan archivos CSV")
        
        # Leer el CSV
        df = pd.read_csv(file.file)
        
        # Generar resumen estadístico
        resumen = df.describe().to_dict()
        
        # Crear gráficos
        fig = plt.figure(figsize=(10, 6))
        df.hist(bins=15, figsize=(10, 6))
        plt.tight_layout()
        plt.savefig("dashboard.png", dpi=100, bbox_inches='tight')
        plt.close(fig)  # Importante: cerrar la figura para liberar memoria
        
        return {
            "resumen": resumen,
            "grafico": "dashboard.png",
            "filas": len(df),
            "columnas": list(df.columns)
        }
    
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="El archivo CSV está vacío")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

@app.get("/")
async def root():
    return {"mensaje": "Dashboard Express API - Envía un CSV a /dashboard"}