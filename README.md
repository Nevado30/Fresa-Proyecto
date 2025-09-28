# Proyecto: Reconocimiento de etapas de crecimiento de la fresa
Este proyecto corresponde al curso **Percepción Computacional** 
El objetivo es aplicar técnicas de preprocesamiento de imágenes y preparar los datos para el entrenamiento de modelos que reconozcan las diferentes etapas de crecimiento de la fresa.

## 📦 Dataset 

### Por motivos de peso, **el dataset original no está incluido en este repositorio**.  
### Debe descargarse desde Kaggle:
### [Strawberry Growth Stage Dataset](https://www.kaggle.com/datasets/kotameyan/strawberry-growth-stage-datasets)
### Una vez descargado, ubica las carpetas en la siguiente estructura:
### data/raw/images/
### data/raw/labels/
### De esta forma, los scripts podrán ejecutarse sin cambios.

## Clonar el repositorio  
```markdown

```bash
git clone https://github.com/Nevado30/Fresa-Proyecto.git
cd Fresa-Proyecto
```

## Instalación y configuración
```bash
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar el entorno virtual 
.venv\Scripts\activate.bat

# 3. Instalar dependencias
pip install -r requirements.txt
```
## Uso de los scripts
### 1. Conversión YOLO -> COCO
### Ejecutar el script para convertir anotaciones en formato YOLO a COCO con
python src/utils/yolo_to_coco.py
### Genera:
data/processed/coco_out/annotations.json

### 2. Validación del JSON generado
### Revisa que las anotaciones del archivo COCO sean válidas con:
python src/utils/validation.py
### Ojo en mi caso me generaba errores y los mostraba como:
FALLA ['annotation 763 con bbox no positiva: [764.23, 1733.59, 0.0, 0.0]']

### 3. Limpieza de anotaciones inválidas
### Elimina automáticamente las anotaciones defectuosas detectadas en la validación con:
python src/utils/limpiar_json.py
### Genera:
data/processed/coco_out/annotations_limpio.json

### 4. Analisis del datasets incluye: 
### ✔ Verificación de integridad del JSON
### ✔ Consistencia de fresas detectadas
### ✔ Calidad de imágenes
### ✔ Distribución de clases
python src/utils/analisis.py

### 5. Redimensionamiento y Normalización
python src/utils/resize_normalize.py
### Genera imágenes de 640x640 normalizadas en:
data/processed/images_640/
### Y genera anotaciones ajustadas en:
annotations_640.json