import qrcode
import streamlit as st
from io import BytesIO
import base64
from datetime import datetime
import folium
from folium import plugins


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Data to be encoded in the QR code
st.title("QR-code Generation")
# def create_map():
#     # Create a map centered around a specific latitude and longitude (India)
#     m = folium.Map(location=[28.6139, 77.2090], zoom_start=10)  # New Delhi, India
    
#     # Add Google Maps tile layer
#     folium.TileLayer('cartodb positron').add_to(m)  # Example: CartoDB's Positron
#     folium.TileLayer(
#         'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 
#         attr='OpenStreetMap'
#     ).add_to(m)  # Example: OpenStreetMap

#     # Save map as an HTML file
#     map_html = 'india_map.html'
#     m.save(map_html)

#     return map_html

# map_html = create_map()
# with open(map_html, "r") as f:
#     st.components.v1.html(f.read(), height=600)





data = st.text_input("Input your google map location here")# data = "https://maps.app.goo.gl/1UAPouG4Ekm8GK4F8?g_st=com.google.maps.preview.copy"
def download_image():
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest, up to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    image_file = f"qrcode_{timestamp}.png"

    buffer = BytesIO()
    img.save(buffer, format="PNG")  # Save the image as PNG
    buffer.seek(0)  # Rewind buffer to the start
    st.download_button(
        label="Download the QR-code",
        data=buffer,
        file_name=image_file,
        mime="image/png"

    )

if st.button("Generate"):
    download_image()


    # Save the image or show it
    # img.save("qrcode_parish.png")
    # img.show()
