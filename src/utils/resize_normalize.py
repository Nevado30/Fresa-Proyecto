from pathlib import Path
import json
from PIL import Image

# Rutas
ANNOTATIONS = Path("data/processed/coco_out/annotations_limpio.json")
IMAGES_RAW = Path("data/raw/images")
OUTPUT_IMAGES = Path("data/processed/images_640")
OUTPUT_JSON = Path("data/processed/coco_out/annotations_640.json")

# Crear carpeta de salida si no existe
OUTPUT_IMAGES.mkdir(parents=True, exist_ok=True)

TARGET_SIZE = (640, 640)  

def resize_and_update():
    # Leer JSON original
    data = json.loads(ANNOTATIONS.read_text(encoding="utf-8"))

    new_images = []
    new_annotations = []

    for im in data["images"]:
        file_name = im["file_name"]
        img_path = IMAGES_RAW / file_name

        if not img_path.exists():
            print(f" No existe {img_path}, se omite.")
            continue

        # Abrir y redimensionar
        with Image.open(img_path) as img:
            orig_w, orig_h = img.size
            resized = img.resize(TARGET_SIZE)
            resized.save(OUTPUT_IMAGES / file_name)

        # Escalas para ajustar bbox
        scale_x = TARGET_SIZE[0] / orig_w
        scale_y = TARGET_SIZE[1] / orig_h

        # Actualizar info de la imagen
        new_images.append({
            "id": im["id"],
            "file_name": file_name,
            "width": TARGET_SIZE[0],
            "height": TARGET_SIZE[1]
        })

        # Ajustar bboxes de anotaciones de esta imagen
        for ann in data["annotations"]:
            if ann["image_id"] == im["id"]:
                x, y, w, h = ann["bbox"]
                new_bbox = [
                    x * scale_x,
                    y * scale_y,
                    w * scale_x,
                    h * scale_y
                ]
                ann["bbox"] = new_bbox
                new_annotations.append(ann)

    # Guardar JSON actualizado
    new_data = {
        "images": new_images,
        "annotations": new_annotations,
        "categories": data["categories"]
    }

    OUTPUT_JSON.write_text(json.dumps(new_data, indent=2), encoding="utf-8")
    print(f" Dataset redimensionado guardado en {OUTPUT_JSON}")
    print(f" Imágenes redimensionadas guardadas en {OUTPUT_IMAGES}")


if __name__ == "__main__":
    resize_and_update()
