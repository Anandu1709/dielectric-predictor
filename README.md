🧠 Project Title: Dielectric Property Prediction Web App

📘 Description

The Dielectric Property Prediction Web App is a Flask-based machine learning web application that predicts the dielectric properties of a 3D-printed material based on three key input parameters:

Infill Density (%)

Infill Pattern (1, 2, or 3)

Printing Speed (mm/sec)

The app allows users to interactively input values using dynamic sliders and dropdown menus, all on a single-page interface. It utilizes a pre-trained machine learning model (dielectric_model.pkl) to generate predictions for dielectric constant, dissipation factor, and resistivity.

The system is designed to help researchers, engineers, and material scientists quickly estimate dielectric behavior under different print settings — improving experimental efficiency and reducing material wastage.

⚙️ Tech Stack

Frontend: HTML, CSS (Dark Theme)

Backend: Python (Flask Framework)

Machine Learning: Scikit-learn

Model Storage: Pickle (.pkl file)

Deployment Platform: Render

💡 Key Features

🧩 User-friendly Interface: Sliders and dropdowns for smooth parameter selection

⚡ Real-time Updates: Textboxes update dynamically with slider movement

🎯 Instant Prediction: Single-click prediction for all three dielectric outputs

🧹 Reset Option: Quickly clear inputs and outputs to default values

🖤 Dark Themed UI: Sleek and modern layout for comfortable use

☁️ Cloud Deployment: Fully hosted and accessible online via Render

🚀 How It Works

User selects:

Infill Density (%): 50–100

Infill Pattern: 1 / 2 / 3

Printing Speed (mm/sec): 20–60

On clicking Predict, the app loads the trained model (dielectric_model.pkl) and predicts the three dielectric properties.

Results are displayed immediately below the input form in a neat results section.

🧪 Use Cases

Optimization of 3D printing parameters for electrical component fabrication

Rapid prediction of material properties without physical testing

Academic and industrial research on polymer-based dielectric materials

🏗️ Future Improvements

Integration of auto-updating models using online learning (e.g., River library)

Addition of data visualization charts for predicted vs. experimental results

Support for multiple material types and pattern-based visual previews
