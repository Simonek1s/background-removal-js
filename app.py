from flask import Flask, request, send_file
import io
from PIL import Image
from your_model_file import remove_background

app = Flask(__name__)

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    image = request.files['image']
    img = Image.open(image)
    
    # Process the image using your model
    result = remove_background(img)
    
    img_io = io.BytesIO()
    result.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
