# KAGA: Zambia Environmental and Health Issues Map
KAGA is a comprehensive web application built to visualize and analyse various environmental and health issues in Zambia. The app provides interactive maps and data visualizations to raise awareness and help in decision-making processes. The current features include maps and data on malaria hotspots, health facilities, cholera outbreaks and lead poisoning in Kabwe.

## Features
### 1. Malaria Hotspots
Objective: Identify and visualize areas prone to malaria outbreaks using geospatial analysis.
Approach: Use satellite data and GIS to map potential mosquito breeding sites and overlay malaria incidence data.
Interventions: Targeted larval source management (LSM), habitat modification and biological control.
### 2. Health Facilities
Objective: Display the location of health facilities across Zambia for better accessibility and resource planning.
Approach: Use GeoJSON data to mark health facility locations on the map with interactive icons.
Data: Health facility data including types and services offered.
### 3. Cholera Outbreaks
Objective: Visualize cholera hotspots and understand the recurrence, outbreak duration, and attack rates in different districts.
Approach: Use CSV data to plot cholera hotspots on the map with detailed outbreak statistics.
Data: District-level data on cholera cases, recurrence, outbreak duration and attack rates.
### 4. Lead Poisoning in Kabwe
Objective: Highlight the areas affected by lead poisoning from the historical Broken Hill Mine in Kabwe.
Approach: Use markers and circles to denote contaminated areas and provide detailed information on the health impacts.(Additional machine learning applications to come soon)
Data: Locations of high lead concentration and affected populations.
Installation
To run this app locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/kshula/kaga.git
cd kaga
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Usage
Navigation: Use the sidebar to navigate between different pages - Home, Malaria Hotspots, Health Facilities, Cholera Outbreaks, and Lead Poisoning in Kabwe.
Interactive Maps: Each page contains an interactive map with markers and other visual elements to display relevant data.
Data Details: Click on markers or map areas to view detailed information about each data point.
Data Sources
Malaria Hotspots: Satellite data and GIS analysis for water bodies and malaria incidence.
Health Facilities: GeoJSON data for health facility locations and details.
Cholera Outbreaks: CSV data with district-level cholera statistics.
Lead Poisoning in Kabwe: Historical data on lead contamination and health impacts from the Broken Hill Mine.
Future Enhancements
Additional Layers: Integrate more health and environmental data layers.
Real-time Data: Incorporate real-time data feeds for dynamic updates.
User Contributions: Enable user submissions of data for community-driven updates.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project's coding standards and include relevant tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or support, please contact:

Name: Kampamba Shula
Email: kampambashula@gmail.com
