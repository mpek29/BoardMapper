import cv2
import xml.etree.ElementTree as ET
import os
import re

def extract_component_number(label):
    """ Extraire le numéro d'un composant à partir de son label (par exemple 'J1', 'R12') """
    match = re.search(r'(\D+)(\d+)', label)
    if match:
        return match.group(1), int(match.group(2))  # Retourne la partie lettres et la partie numérique
    return label, 0  # Si le format est incorrect, retourner un label sans numéro

def draw_boxes(image_path, xml_path, output_path):
    # Charger l'image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erreur : Impossible de charger l'image {image_path}")
        return
    
    # Lire le fichier XML
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Liste pour stocker les composants avec leurs informations (type, numéro, bbox)
    components = []
    
    # Parcourir les objets annotés
    for obj in root.findall("object"):
        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)
        label = obj.find("name").text  # Récupérer le type de composant
        
        # Ajouter le composant à la liste avec son label et ses coordonnées
        components.append((label, xmin, ymin, xmax, ymax))
    
    # Trier les composants par numéro extrait du label (par exemple 'J1' -> 'J', 1)
    components.sort(key=lambda x: extract_component_number(x[0])[1])

    # Parcourir les composants triés pour les afficher avec la numérotation
    for idx, (label, xmin, ymin, xmax, ymax) in enumerate(components, 1):
        # Dessiner un rectangle blanc plein
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 255, 255), thickness=-1)
        
        # Ajouter le texte avec la numérotation
        num_label = f"{label}{idx}"  # Exemple: 'J1', 'R1', etc.
        
        # Calculer la taille du texte avec cv2.getTextSize
        font_scale = 1.0
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size, _ = cv2.getTextSize(num_label, font, font_scale, 1)
        text_width, text_height = text_size

        # Calculer la taille maximale de la police qui s'adapte dans la boîte
        max_font_scale = min((xmax - xmin) / text_width, (ymax - ymin) / text_height)

        # Ajuster la taille de la police pour qu'elle soit la plus grande possible
        font_scale = max_font_scale
        
        # Calculer les coordonnées pour centrer le texte
        text_width, text_height = cv2.getTextSize(num_label, font, font_scale, 1)[0]
        text_x = int(xmin + (xmax - xmin - text_width) // 2)
        text_y = int(ymin + (ymax - ymin + text_height) // 2)

        # Dessiner le texte avec la taille ajustée
        cv2.putText(image, num_label, (text_x, text_y), font, font_scale, (0, 0, 0), 1, cv2.LINE_AA)
    
    # Sauvegarder l'image modifiée
    cv2.imwrite(output_path, image)
    print(f"Image enregistrée sous {output_path}")

# Définir les chemins des fichiers
image_path = "input/top.png"
xml_path = "input/top.xml"
output_path = "output/top_annotated.png"

# Créer le dossier de sortie s'il n'existe pas
os.makedirs("output", exist_ok=True)

draw_boxes(image_path, xml_path, output_path)
