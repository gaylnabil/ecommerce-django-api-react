
from PIL import Image, ImageOps
from enum import Enum


class Mode(Enum):
    RESIZE = 0
    THUMBNAIL = 1
    FIT = 2
    ZOOM = 3


def resize_image(image_name, size, mode):
    img = Image.open(image_name)

    # ImageOps compatible mode
    if img.mode not in ("L", "RGB"):
        img = img.convert("RGB")

    if mode == Mode.RESIZE:
        img.resize(size, Image.ANTIALIAS)
        # img = img.resize((200,200), Image.ANTIALIAS)
        # imageresize.save('resize_200_200_aa.jpg', 'JPEG', quality=75)

    elif mode == Mode.THUMBNAIL:

        img.thumbnail(size, Image.ANTIALIAS)
        # image.save('thumbnail_200_200_aa.jpg', 'JPEG', quality=75)
    elif mode == Mode.ZOOM:
        img.thumbnail(size, Image.ANTIALIAS)
        img.resize(size, Image.ANTIALIAS)
        # img = ImageOps.fit(img, size,Image.ANTIALIAS)
    else:
        img = ImageOps.fit(img, size, Image.ANTIALIAS)
        # imagefit.save('fit_200_200_aa.jpg', 'JPEG', quality=75)

    return img
