# BoardMapper

## Overview
BoardMapper is an open-source tool designed to automatically generate a component placement map for PCBs. It labels component references (U1, R1, C1, etc.) directly on the board image, simplifying assembly and troubleshooting.

## Purpose
- **Automation**: Eliminates the need for manual placement annotation on PCB layouts.
- **Efficiency**: Saves time for engineers and makers working on PCB assembly.
- **Clarity**: Provides a clear visual reference for debugging and manufacturing.

## Instructions

### Steps:
1) Take a photo of both the top and bottom layers of the chosen PCB.
2) Place `top.png` and `bottom.png` into the `input` folder.
3) Install the latest version of LabelImg from the following link: [LabelImg Releases](https://github.com/HumanSignal/labelImg/releases).
4) Open `top.png` in LabelImg, and draw bounding boxes around each component, labeling them according to their type:
    - **R**: Resistor
    - **C**: Capacitor
    - **L**: Inductor
    - **F**: Fuse
    - **POT**: Potentiometer
    - **D**: Diode
    - **LED**: LED
    - **Q**: Transistor (BJT, MOSFET)
    - **U**: Integrated Circuit (IC)
    - **J**: Connector
    - **K**: Relay
    - **SW**: Switch
    - **Y**: Quartz / Resonator
    - **SP**: Speaker
    - **ANT**: Antenna
    
    **Shortcuts for LabelImg:**
    - **W**: Draw a new rectangular bounding box (RectBox)
    - **D**: Delete the last drawn bounding box
    - **Ctrl + S**: Save the annotation (XML)
    - **Ctrl + Z**: Undo the last action
    - **Ctrl + C**: Copy a bounding box
    - **Ctrl + V**: Paste a copied bounding box
    - **Ctrl + A**: Select all bounding boxes
    - **Ctrl + R**: Rotate the image (for better labeling)
    - **Esc**: Cancel the current operation or close a dialog box
    
    After labeling, save the file as `top.xml`.
5) Repeat the same steps with `bottom.png` to create `bottom.xml`.
6) Place `top.xml` and `bottom.xml` into the `input` folder.
7) Double-click on `main.py` to run the tool.
8) Navigate to the `output` folder to retrieve the resulting annotated images: `top_annotated.png` and `bottom_annotated.png`.

## License
This project is open-source. Feel free to use, modify, and contribute!
