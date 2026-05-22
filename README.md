# Image-compressor
This project compresses any image over 40% 


It demonstrates low-level binary data manipulation, image matrix decomposition, and structural information analysis at the bit level without relying on heavy external digital image processing frameworks. In an 8-bit grayscale image, each pixel intensity is represented by an integer ranging from 0 to 255 (2^0 to 2^7).

While all bits contribute to the final pixel value, they do not carry equal visual significance:
-Most Significant Bits (MSBs): Higher-order bits (planes 4 to 7) contain the core structural layouts, high-contrast edges, and geometric shapes of the image.
-Least Significant Bits (LSBs): Lower-order bits (planes 0 to 3) capture subtle gray-level variations, fine textures, and imperceptible high-frequency background noise.By decomposing an image into its eight constituent binary matrices, we can isolate and discard the lower-order bit-planes.
This significantly reduces data entropy while reconstructing a visually acceptable approximation of the original image from the remaining higher-order planes.

Technical Features and Methodology
1. Bit-Plane ExtractionThe decomposition algorithm applies a localized bitwise masking operation across the entire image matrix. For an 8-bit image array $I(x,y)$, each binary plane $P_i(x,y)$ is isolated using the bitwise AND operator matched with increasing powers of two.

2. Variable-Threshold Lossy Reconstruction - Reconstruction is achieved by scaling the active boolean matrices back to their respective base-2 weights and computing their summation. Discarding the $k$ lowest bit-planes yields a predictable, hardcoded mathematical data reduction before file-level encoding takes place.

<b>Performance and Compression Metrics</b> - The data reduction percentage can be calculated via theoretical bit allocation or by evaluating physical disk footprints. Dropping the three least significant bit-planes yields an immediate theoretical data reduction of 37.5%,as visible in my project's output.
