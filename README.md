# BoardMapper

🌍 [🇫🇷 Lire en français](README.fr.md)

## 🚀 Overview
![Main Preview](assets/img/main.png)

BoardMapper is an open-source tool designed to automatically generate PCB layout. It labels component references (e.g. U1, R1, C1) directly on the circuit image, facilitating component identification for reverse engineering purposes.

## 🎯 Purpose
- 🤖 **Automation**: Eliminates the need for manual placement annotation on PCB layouts.
- ⏱️ **Efficiency**: Saves time for engineers and makers working on PCB assembly and debugging.
- 🔍 **Clarity**: Provides a clear visual reference for debugging, testing, and manufacturing.
- 💻 **Cross-Platform**: Works on Windows, Linux, and macOS systems.

## 📝 Annotation

| Position | Original | Annotated |
|----------|----------|-----------|
| **Top**  | <img src="example/input/top.png" width="200"> | <img src="example/output/top_annotated.png" width="200"> |
| **Bottom** | <img src="example/input/bottom.png" width="200"> | <img src="example/output/bottom_annotated.png" width="200"> |

## 📋 Requirements
- **Python**: Version 3.6 or higher
- **Required Libraries**:
  - `opencv-python` (for image processing)
  - `lxml` (for XML parsing)

## 🚀 Installation Instructions

### 🛠️ Setup
1. **Clone the repository** or **Download the project** to your local machine.

2. **Labeling the PCB**:
   - **Step 1**: Take a photo of both the top and bottom layers of the chosen PCB.
   - **Step 2**: Place the `top.png` and `bottom.png` images into the `input` folder.
   - **Step 3**: Install the latest version of [LabelImg](https://github.com/HumanSignal/labelImg/releases).
   - **Step 4**: Open `top.png` in LabelImg and draw bounding boxes around each component. Label each component according to its type:
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
     
     **LabelImg Shortcuts**:
     - ✏️ **W**: Draw a new rectangular bounding box (RectBox)
     - ❌ **D**: Delete the last drawn bounding box
     - 💾 **Ctrl + S**: Save the annotation as an XML file
     - ⏪ **Ctrl + Z**: Undo the last action
     - 📋 **Ctrl + C**: Copy a bounding box
     - 📏 **Ctrl + V**: Paste a copied bounding box
     - 🔍 **Ctrl + A**: Select all bounding boxes
     - 🔄 **Ctrl + R**: Rotate the image (for better labeling)
     - 🚫 **Esc**: Cancel the current operation or close a dialog box

   - **Step 5**: After labeling the `top.png`, save the annotation as `top.xml`.
   - **Step 6**: Repeat the labeling process for the `bottom.png` and save it as `bottom.xml`.
   - **Step 7**: Place both `top.xml` and `bottom.xml` into the `input` folder.

3. **Running the Tool**:
   - **Windows**: Double-click on `setup_and_run.bat` to automatically run the script. The tool will read the XML annotations, draw bounding boxes on the images, and save the annotated images.
   - **Linux/macOS**: You can run the script from the terminal:
     ```
     chmod +x script.sh
     ./script.sh
     ```

5. **📂 Output**: 
   - After the script has executed, navigate to the `output` folder to find the resulting annotated images:
     - `top_annotated.png`
     - `bottom_annotated.png`

## 🤝 Contributions
If you'd like to contribute to the project, please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

We welcome any contributions to improve BoardMapper! 🎉

## 🌟 License
This project is open-source. Feel free to use, modify, and contribute! 🚀
