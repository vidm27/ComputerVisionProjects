import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="path to input image")

args = vars(ap.parse_args())

# load the image from disk
image = cv2.imread(args["image"])

(h, w, c) = image.shape[:3]


print(f"width: {w} pixels")
print(f"height: {h} pixels")
print(f"channels: {c}")

cv2.imshow("Image", image)
cv2.waitKey(0)

# write image to new format
cv2.imwrite("new_image.png", image)