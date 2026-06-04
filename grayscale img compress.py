from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
original_image = Image.open("dollar.tif")

if original_image.mode != 'L':
    grayscale_image = original_image.convert('L')
else:
    grayscale_image = original_image

img_array = np.array(grayscale_image)
bit_planes_data = []
for i in range(8):
    bit_mask = 2**i
    bit_plane = (img_array & bit_mask) > 0 
    bit_planes_data.append(bit_plane)
new_img=Image.fromarray((bit_planes_data[3]*8+bit_planes_data[4]*16+bit_planes_data[5]*32+64*bit_planes_data[6]+bit_planes_data[7]*128).astype(np.uint8))

fig, axes = plt.subplots(2, 1, figsize=(10, 10))
axes = axes.ravel()

axes[0].imshow(grayscale_image, cmap='gray')
axes[0].set_title("Original")
axes[0].axis('off')
print()
print()
axes[1].set_title("Compressed")
axes[1].imshow(new_img,cmap='gray')
new_img.save("compressed_output.png")
new_img.save("compressed_output.png")

original_bytes=os.path.getsize("dollar.tif")
compressed_bytes=os.path.getsize("compressed_output.png")
physical_savings=(1-(compressed_bytes / original_bytes))*100
print(f"Physical File Size Savings: {physical_savings:.2f}%")
plt.tight_layout()
plt.show()
