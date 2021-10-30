import cv2 as opencv
import numpy as np

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
        
        # image processing TODO
        # img = opencv.imdecode(img, opencv.IMREAD_GRAYSCALE)
        # img = opencv.GaussianBlur(img, (5, 5), 0)
        # img = opencv.Canny(img, 50, 200, 255)

        breakpoint()

        """
        'content_length' - 0
        'content_type' - 'image/png'
        'filename' - 'Screenshot from 2021-10-30 11-04-23.png'
        'mimetype' - 'image/png'
        'name' - 'image'
        'stream' - image.stream.read() - content (tempfile.SpooledTemporaryFile)
        """

        return redirect(url_for('alpha.index'))
