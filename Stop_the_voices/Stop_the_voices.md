# Stop the voices
### Description
Patrick’s been trying to remember the flag, but his vision seems a little blurry and the voices just don't stop...

## Solution
The challenge give us a folder with 400 images with a lot of noise.
These images are generated with `generator.py`.
My solution was to sum up the noise of all the images and divide them by len of the images, then output an `mean image`.

With these lines of code i improved the readability of the `mean image`
```python
mean_image_8bit = cv2.normalize(mean_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
mean_image_clahe = clahe.apply(mean_image_8bit)
output_path_clahe = os.path.join(output_folder_path, "mean_image_clahe.png")
cv2.imwrite(output_path_clahe, mean_image_clahe)
```

Result:
- inserire immagine flag