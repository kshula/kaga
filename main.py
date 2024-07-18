import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import geopandas as gpd
import pandas as pd
import gzip
from modules.utils import provinces, district_coords, kabwe_coords, broken_hill_coords, text

st.set_page_config(layout="wide")

# Load compressed GeoJSON data
@st.cache_data
def load_compressed_geojson(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        return json.load(f)

# Load CSV data
@st.cache_data
def load_csv(file_path):
    return pd.read_csv(file_path)

# Load GeoJSON data
@st.cache_data
def load_geojson(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to create a Folium map with a marker for lead poisoning
def create_lead_poisoning_map():
    m = folium.Map(location=kabwe_coords, zoom_start=13)

    # Add marker for Kabwe
    folium.Marker(
        location=kabwe_coords,
        popup="Kabwe Town",
        tooltip="Kabwe",
        icon=folium.Icon(color="lightgray", icon="info-sign")
    ).add_to(m)

    # Add marker for Broken Hill Mine
    folium.Marker(
        location=broken_hill_coords,
        popup="""
        <b>Broken Hill Mine</b><br>
        Historical lead mine<br>
        Known for lead contamination<br>
        """,
        tooltip="Broken Hill Mine",
        icon=folium.Icon(color="red", icon="exclamation-sign")
    ).add_to(m)

    # Add a circle to highlight the affected area
    folium.Circle(
        location=broken_hill_coords,
        radius=1500,  # radius in meters
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.4,
        tooltip="Affected Area"
    ).add_to(m)

    return m

# Function to create a Folium map
def create_hotspot_map(df, coords):
    m = folium.Map(location=[-13.1339, 27.8493], zoom_start=6)  # Coordinates for Zambia

    for _, row in df.iterrows():
        district = row["DISTRICT"]
        if district in coords:
            lat, lon = coords[district]
            popup_text = f"""
                <b>District:</b> {district}<br>
                <b>Type:</b> {row['TYPE']}<br>
                <b>Province:</b> {row['PROVINCE']}<br>
                <b>% of total cases:</b> {row['% of total cases']}<br>
                <b>Recurrence (No. of outbreaks):</b> {row['Recurrence (No. of outbreaks)']}<br>
                <b>Outbreak duration (median, in weeks):</b> {row['Outbreak duration (median, in weeks)']}<br>
                <b>Attack rate (median per 10,000 inhab.):</b> {row['Attack rate (median per 10,000 inhab.)']}<br>
                <b>Crossborder area:</b> {row['Crossborder area']}
            """
            folium.Marker(
                location=[lat, lon],
                popup=popup_text,
                tooltip=district
            ).add_to(m)

    return m


# Create a Folium map with health facilities for a specific province
def create_map(geojson_data, province):
    m = folium.Map(location=[-13.1339, 27.8493], zoom_start=6)  # Coordinates for Zambia

    for feature in geojson_data['features']:
        properties = feature['properties']
        geometry = feature['geometry']

        # Only process Point geometries and filter by province
        if geometry['type'] == 'Point' and properties.get('province') == province:
            coordinates = geometry['coordinates'][::-1]  # Reverse coordinates to (lat, lon)
            
            # Customize the icon as needed
            icon = folium.Icon(icon="medkit", prefix="fa", color="red")
            
            # Create a marker
            folium.Marker(
                location=coordinates,
                popup=f"Health Facility: {properties.get('name', 'N/A')}",
                icon=icon
            ).add_to(m)

    folium.LayerControl().add_to(m)
    return m

# Create a Folium map with regions
def create_regions_map(geojson_data):
    m = folium.Map(location=[-13.1339, 27.8493], zoom_start=6)  # Coordinates for Zambia

    folium.GeoJson(
        geojson_data,
        name='Regions',
        style_function=lambda feature: {
            'fillColor': 'blue',
            'color': 'blue',
            'weight': 2,
            'fillOpacity': 0.1,
        }
    ).add_to(m)

    folium.LayerControl().add_to(m)
    return m


# Streamlit app
def main():
    st.title("Kabwe 1 - Geospatial Analysis - KAGA")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page", ["Home","Health Facilities","Kabwe Lead Poisoning", "Province","Hotspot Map",  "Regions", "About"])

    if page == "Home":
            
            st.image("images\\zambia.png")
            st.markdown(
            """
            
            KAGA is a comprehensive web application designed to visualize and address 
            environmental and health challenges in Zambia. Explore interactive maps and 
            data visualizations on malaria hotspots, health facilities, cholera outbreaks, 
            and lead poisoning in Kabwe.
            """
        )

            st.write("---")
            st.header("Explore KAGA Features:")
            st.markdown(
                """
                - **Malaria Hotspots:** Identify areas prone to malaria outbreaks and implement targeted interventions.
                - **Health Facilities:** Access maps of health facilities across Zambia for better resource planning.
                - **Cholera Outbreaks:** Visualize cholera hotspots and understand outbreak patterns.
                - **Lead Poisoning in Kabwe:** Learn about areas affected by historical lead contamination.
                """
            )

            st.write("---")
            st.header("Get Started:")
            st.markdown(
                """
                Use the sidebar to navigate through different sections of the app:
                - **Malaria Hotspots**
                - **Health Facilities**
                - **Cholera Outbreaks**
                - **Lead Poisoning in Kabwe**
                
                Click on each section to explore detailed maps and data visualizations.
                """
            )

            st.write("---")
            st.markdown(
                """
                🌍 **Let's make a positive impact together! Explore KAGA and join us in addressing Zambia's 
                environmental and health challenges.**

                [Start Exploring](#) (Add link to app if available)

                ---
                """
            )


    elif page == "Health Facilities":
        st.header("Map of Health Facilities")

        geojson_file_path = "data\\health_site.geojson"  # Replace with the path to your GeoJSON file
        geojson_data = load_geojson(geojson_file_path)
        folium_map = create_map(geojson_data, None)

        st_folium(folium_map, width=1100, height=800)

    elif page == "Kabwe Lead Poisoning":
        st.header("Lead Poisoning spatial parameters in Kabwe")

        folium_map = create_lead_poisoning_map()
        st_folium(folium_map, width=1100, height=800)

        st.write(text)

    
    elif page == "Hotspot Map":
        st.header("Cholera Hotspot Map of Zambia")

        file_path = "data\\admin_hotspots.csv"
        df = load_csv(file_path)
        folium_map = create_hotspot_map(df, district_coords)
        st_folium(folium_map, width=700, height=500)

    elif page == "Regions":
        st.header("Map of Regions")

        geojson_file_path = "data\\regions.geojson"  # Replace with the path to your regions.geojson file
        geojson_data = load_geojson(geojson_file_path)
        folium_map = create_regions_map(geojson_data)

        st_folium(folium_map, width=1400, height=1000)

    elif page == "Province":
        st.header("Map by Province")

        selected_province = st.selectbox("Select Province", provinces)

        geojson_file_path = "data\\health_site.geojson"  # Replace with the path to your GeoJSON file
        geojson_data = load_geojson(geojson_file_path)
        folium_map = create_map(geojson_data, selected_province)

        st_folium(folium_map, width=700, height=500)


    elif page == "About":
        st.header("About")
        st.write("KAGA is a comprehensive web application built to visualize and analyse various environmental and health issues in Zambia. The app provides interactive maps and data visualizations to raise awareness and help in decision-making processes. The current features include maps and data on malaria hotspots, health facilities, cholera outbreaks and lead poisoning in Kabwe.")

if __name__ == "__main__":
    main()