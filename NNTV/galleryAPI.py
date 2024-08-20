from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route to serve the gallery page
@app.route('/')
def gallery():
    image_folder = 'images'
    images = []
    
    # Loop through all files in the image folder
    for index, filename in enumerate(os.listdir(image_folder)):
        if filename.endswith('.jpg'):  # Add more extensions if needed
            if (index + 1) % 3 == 0:  # Check if the current image is the 3rd in sequence
                timestamp = filename.split('_')[-1].split('.')[0]
                images.append({'src': f'/images/{filename}', 'datetime': timestamp})
    
    # Render the HTML template with the images data
    return render_template('gallery.html', images=images)

# Route to serve images from the 'images' folder
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

if __name__ == "__main__":
    app.run(debug=True)
