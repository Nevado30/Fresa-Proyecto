import json
from pathlib import Path

# Ruta del archivo original
input_file = Path("data/processed/coco_out/annotations.json")
output_file = Path("data/processed/coco_out/annotations_limpio.json")

# Cargar JSON
with open(input_file, "r") as f:
    data = json.load(f)

# Filtrar anotaciones inválidas
n_invalid = 0
annotations_validas = []

for ann in data["annotations"]:
    bbox = ann["bbox"]
    if bbox[2] <= 0 or bbox[3] <= 0:
        print(f"Eliminada annotation {ann['id']} con bbox inválida: {bbox}")
        n_invalid += 1
        continue
    annotations_validas.append(ann)

# Reemplazar solo con válidas
data["annotations"] = annotations_validas

# Guardar limpio
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"Listo. Se eliminaron {n_invalid} anotaciones inválidas.")
print(f"Archivo limpio guardado en: {output_file}")
