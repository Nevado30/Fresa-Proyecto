# Proyecto: Reconocimiento de etapas de crecimiento de la fresa
Este proyecto corresponde al curso **Percepción Computacional** 
El objetivo es aplicar técnicas de preprocesamiento de imágenes y preparar los datos para el entrenamiento de modelos que reconozcan las diferentes etapas de crecimiento de la fresa.
## Instalación y configuración
### 1. Crear entorno virtual
python -m venv .venv

### 2. Activar el entorno virtual 
.venv\Scripts\activate.bat

### 3. Instalar dependencias
pip install -r requirements.txt

## Uso de los scripts
### 1. Conversión YOLO -> COCO
### Ejecutar el script para convertir anotaciones en formato YOLO a COCO con
python yolo_to_coco.py
### Genera:
data/processed/coco_out/annotations.json

### 2. Validación del JSON generado
python validation.py
