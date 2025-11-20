import cv2
import PIL

def show_image(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        print("Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku.")
        return None

    print(img)
    print(img.shape)
    print(type(img))
    show_image(img)
    return img

read_image_cv("lekcja35/doberman.jpg")

def read_image_PIL(path):
    im = PIL.Image.open(path)
    try:
        print(im)
    except:
        print(type(im))
    im.show()
    return im

read_image_PIL("lekcja35\doberman.jpg")