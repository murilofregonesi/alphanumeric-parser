import cv2 as opencv
import pytesseract

example = 'example_b'


if __name__ == '__main__':
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    img = opencv.imread(example + '.png', opencv.IMREAD_GRAYSCALE)
    
    # opencv.imshow("Text Detection", img)
    # opencv.waitKey(0)
    # opencv.destroyAllWindows()

    # img = opencv.GaussianBlur(img, (5, 5), 0)
    # img = opencv.Canny(img, 50, 200, 255)
    # img = opencv.threshold(img, 180, 255, opencv.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(img)
    print(text)
