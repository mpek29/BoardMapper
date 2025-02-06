import os
import re
import cv2
import xml.etree.ElementTree as ET
from collections import defaultdict
from typing import Dict, Tuple

def extract_component_number(label: str) -> Tuple[str, int]:
    """Extracts the component type and number from its label (e.g., 'J1', 'R12')."""
    match = re.search(r'(\D+)(\d+)', label)
    return (match.group(1), int(match.group(2))) if match else (label, 0)

def draw_boxes(image_path: str, xml_path: str, output_path: str, counters: Dict[str, int]) -> Dict[str, int]:
    """Draws bounding boxes with labels on the given image based on XML annotations."""
    if not os.path.exists(image_path):
        print(f"Error: Image file not found - {image_path}")
        return counters
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Failed to load image - {image_path}")
        return counters

    if not os.path.exists(xml_path):
        print(f"Error: XML file not found - {xml_path}")
        return counters
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    components = []
    for obj in root.findall("object"):
        bbox = obj.find("bndbox")
        if bbox is None:
            continue

        try:
            xmin, ymin, xmax, ymax = (int(bbox.find(tag).text) for tag in ("xmin", "ymin", "xmax", "ymax"))
            label = obj.find("name").text
            components.append((label, xmin, ymin, xmax, ymax))
        except (AttributeError, TypeError, ValueError):
            print("Warning: Skipping invalid bounding box entry in XML.")
            continue

    for label, xmin, ymin, xmax, ymax in components:
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 255, 255), thickness=-1)
        component_type = label[0]  # First letter represents the component type
        counters[component_type] += 1
        num_label = f"{label}{counters[component_type]}"
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size, _ = cv2.getTextSize(num_label, font, 1.0, 1)
        text_width, text_height = text_size
        
        font_scale = min((xmax - xmin) / text_width, (ymax - ymin) / text_height)
        text_width, text_height = cv2.getTextSize(num_label, font, font_scale, 1)[0]
        text_x = xmin + (xmax - xmin - text_width) // 2
        text_y = ymin + (ymax - ymin + text_height) // 2
        
        cv2.putText(image, num_label, (text_x, text_y), font, font_scale, (0, 0, 0), 1, cv2.LINE_AA)
    
    cv2.imwrite(output_path, image)
    print(f"Annotated image saved: {output_path}")
    
    return counters

def process_images() -> None:
    """Processes top and bottom images with independent component counters."""
    counters = defaultdict(int)
    
    for position in ["top", "bottom"]:
        print(f"Processing {position}.png...")
        counters = draw_boxes(
            image_path=f"input/{position}.png",
            xml_path=f"input/{position}.xml",
            output_path=f"output/{position}_annotated.png",
            counters=counters
        )

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    process_images()
