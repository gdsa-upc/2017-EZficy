# Reads an image from disk and scales and crops to match a target resolution and aspect ratio.
from scipy import misc
import matplotlib.pyplot as plt

curl = misc.imread('curl.jpg')
print(curl.shape)
plt.imshow(curl)
plt.show()

curl_resized = misc.imresize(curl, 3000.0 / len(curl), interp='nearest', mode=None)
dims = curl_resized.shape
print(dims)
plt.imshow(curl_resized)
plt.show()

curl_resized_cropped = curl_resized[0:3000,(dims[1]/2 - 2000):(dims[1]/2 + 2000)]
print(curl_resized_cropped.shape)

plt.imshow(curl_resized_cropped)
plt.show()