import numpy as np
import cv2 as opencv
import pytesseract

from flask import (Blueprint,
                   render_template,
                   request,
                   redirect,
                   url_for)


alpha = Blueprint('alpha', __name__)

ALLOWED_MIME = ['image/png', 'image/jpeg']


@alpha.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        # get image
        file = request.files.get('image')
        if file.filename == '' or file.mimetype not in ALLOWED_MIME:
            # TODO flash error
            return redirect(url_for('alpha.index'))

        img = np.fromstring(file.stream.read(), dtype='uint8')
        img = opencv.imdecode(img, opencv.IMREAD_GRAYSCALE)
        
        # image processing
        # img = opencv.GaussianBlur(img, (5, 5), 0)
        # img = opencv.Canny(img, 50, 200, 255)
        # img = opencv.threshold(img, 180, 255, opencv.THRESH_BINARY)[1]

        # text detection
        text = pytesseract.image_to_string(img)

        return render_template('index.html', detection=text)
