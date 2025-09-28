import json, os
from pathlib import Path

def validate_coco(json_path, images_root=None, num_categories=None):
    p = Path(json_path)
    data = json.loads(p.read_text(encoding="utf-8"))
    errors = []

    # 1) Estructura básica
    for k in ("images", "annotations", "categories"):
        if k not in data or not isinstance(data[k], list):
            errors.append(f"Falta sección '{k}' o no es lista")

    if errors:
        return False, errors

    # 2) Categories
    cat_ids = {c.get("id") for c in data["categories"]}
    if None in cat_ids:
        errors.append("Alguna categoría no tiene 'id'")
    if num_categories and len(cat_ids) != num_categories:
        errors.append(f"Se esperaban {num_categories} categorías, hay {len(cat_ids)}")

    # 3) Images
    img_ids = set()
    for im in data["images"]:
        if "id" not in im or "file_name" not in im or "width" not in im or "height" not in im:
            errors.append(f"Imagen inválida: {im}")
        img_ids.add(im["id"])
        if images_root:
            if not Path(images_root, im["file_name"]).exists():
                errors.append(f"No existe archivo de imagen: {im['file_name']}")

    # 4) Annotations
    for ann in data["annotations"]:
        if "image_id" not in ann or ann["image_id"] not in img_ids:
            errors.append(f"annotation {ann.get('id')} con image_id inválido")
        if "category_id" not in ann or ann["category_id"] not in cat_ids:
            errors.append(f"annotation {ann.get('id')} con category_id inválido")
        bbox = ann.get("bbox")
        if (not isinstance(bbox, list)) or len(bbox) != 4 or any((not isinstance(v,(int,float))) for v in bbox):
            errors.append(f"annotation {ann.get('id')} con bbox inválido: {bbox}")
        if bbox and (bbox[2] <= 0 or bbox[3] <= 0):
            errors.append(f"annotation {ann.get('id')} con bbox no positiva: {bbox}")

    return (len(errors) == 0), errors


ok, errs = validate_coco("data/processed/coco_out/annotations.json", images_root="data/raw/images", num_categories=5)
print("OK" if ok else "FALLA", errs[:10])