import os
import base64
import numpy as np
import cv2 as opencv
import pytesseract

from flask import (Blueprint,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   jsonify)


alpha = Blueprint('alpha', __name__)

ALLOWED_MIME = ['image/png', 'image/jpeg']


@alpha.route('/', methods=['GET', 'POST'])
def index():
    def detect_text(img) -> str:
        pytesseract.pytesseract.tesseract_cmd = os.environ.get('TESSERACT_CMD')
        text = pytesseract.image_to_string(img)
        text = text.strip()

        return text

    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        # image upload
        if request.files.get('image'):
            file = request.files.get('image')
            if file.filename == '' or file.mimetype not in ALLOWED_MIME:
                # TODO flash error
                return redirect(url_for('alpha.index'))

            img = np.fromstring(file.stream.read(), dtype='uint8')
            img = opencv.imdecode(img, opencv.IMREAD_GRAYSCALE)

            # text detection
            text = detect_text(img)
            return render_template('index.html', detection=text)

        # image paste
        elif request.json.get('image'):
            file = request.json.get('image')
            sufix, file = request.json.get('image').split(';')
            
            # TODO verify sufix
            # sufix[0][5:]
            
            file = file.replace('base64,', '')
            file = base64.b64decode(file)

            img = np.fromstring(file, dtype='uint8')
            img = opencv.imdecode(img, opencv.IMREAD_GRAYSCALE)

            # text detection
            text = detect_text(img)
            return jsonify({
                "text": text
            }), 200

        # no image
        else:
            # TODO flash error
            return redirect(url_for('alpha.index'))
        
        # TODO deal with dark images
        # image processing
        # img = opencv.GaussianBlur(img, (5, 5), 0)
        # img = opencv.Canny(img, 50, 200, 255)
        # img = opencv.threshold(img, 180, 255, opencv.THRESH_BINARY)[1]
