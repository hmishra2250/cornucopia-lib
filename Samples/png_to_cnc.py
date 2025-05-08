import json
from PIL import Image

def extract_points_from_png(image_path):
    img = Image.open(image_path).convert("L")  # Convert to grayscale
    width, height = img.size

    pixels = img.load()
    points = []

    for y in range(height):
        for x in range(width):
            if pixels[x, y] < 250:  # Consider anything not near-white as a line
                points.append((x, y))

    return points

def convert_to_cnc_format(points):
    cnc_data = [{
        "pts": [float(x) for pt in points for x in pt],
        "oversketch": -1
    }]
    return cnc_data

def write_cnc_file(output_path, cnc_data):
    with open(output_path, "w") as f:
        json.dump(cnc_data, f, indent=2)

def main():
    import sys
    if len(sys.argv) != 3:
        print("Usage: python png_to_cnc.py input.png output.cnc")
        return

    image_path = sys.argv[1]
    output_path = sys.argv[2]

    points = extract_points_from_png(image_path)
    if not points:
        print("No sketch data found in image.")
        return

    cnc_data = convert_to_cnc_format(points)
    write_cnc_file(output_path, cnc_data)
    print(f"Converted {len(points)} points to {output_path}")

if __name__ == "__main__":
    main()
