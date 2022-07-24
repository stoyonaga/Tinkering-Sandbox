from PIL import Image, ImageDraw, ImageChops
import random
import colorsys
import os

"""
Tutorial Video: https://www.youtube.com/watch?v=BMq2Jrvp9AA

This is an adapted version of the Python NFT Generator.
A large majority of the source code is from Pixelgami

Adaptations
    - Generates Randomized Gifs (Dynamic FPS value from io) <Mainly, used to generate a Discord profile picture!> .
    - Improving Readability, Refactored Source Program As Well
    - Install Script for Linux Packages 
    - Uninstall Script for Linux Packages
"""


def random_color() -> tuple:
    # We only want the hue of the colour to change!
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]
    return tuple(rgb)


def interpolate(start_color, end_color, factor: float):
    reciprocal = 1 - factor
    return (
        int(start_color[0] * reciprocal + end_color[0] * factor),
        int(start_color[1] * reciprocal + end_color[0] * factor),
        int(start_color[2] * reciprocal + end_color[0] * factor),
    )


def generate_art(image_name: str, sc: tuple, ec: tuple, segments: int) -> None:
    target_size_px = 256
    scale_factor = 2
    image_size_px = target_size_px * scale_factor
    padding_px = int(128 * 0.12) * scale_factor
    image_bg_color = (0, 0, 0)
    start_color = sc
    end_color = ec
    image = Image.new("RGB", size=(image_size_px, image_size_px), color=image_bg_color)

    points = []

    # Generate the points
    for _ in range(segments):
        random_point = (random.randint(padding_px, image_size_px - padding_px), random.randint(padding_px,
                        image_size_px - padding_px))
        points.append(random_point)

    # Draw Bounding Box
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    # Center the image
    delta_x = min_x - (image_size_px - max_x)
    delta_y = min_y - (image_size_px - max_y)
    for i, point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y // 2)

    thickness = 0
    n_points = len(points) - 1
    for i, point in enumerate(points):
        # Overlay Canvas
        overlay_image = Image.new("RGB", size=(image_size_px, image_size_px), color=image_bg_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        p1 = point
        if i == n_points:
            p2 = points[0]
        else:
            p2 = points[i + 1]

        line_xy = (p1, p2)
        color_factor = i / n_points
        line_color = interpolate(start_color, end_color, color_factor)
        thickness += scale_factor
        overlay_draw.line(line_xy, fill=line_color, width=thickness)
        image = ImageChops.add(image, overlay_image)
    image = image.resize((target_size_px, target_size_px), resample=Image.Resampling.BICUBIC)
    image.save(image_name)


"""
VSCode Blue: 
    - Start: (0, 125, 255)
    - End: (255, 232, 0)
Neon Purple:
    - Start: (225, 0, 255)
    - End: (216, 0, 255)
Neon Red:
    - Start: (255, 1, 0)
    - End: (248, 0, 255)
Neon Green:
    - Start: (0, 255, 43)
    - End: (255, 0, 203)
"""

if __name__ == "__main__":
    print("========== Neon Generator ==========")
    print("1) Generate RGB\n2) Generate Linear")
    generator = int(input(">"))
    print(" Enter FPS for the gif:")
    fps_cntr = int(input(">"))
    print("Generating gif...")
    start_gr = random_color()
    end_gr = random_color()
    if not os.path.isdir("output"):
        os.system("mkdir output")
    for i in range(fps_cntr):
        if generator == 1:
            generate_art("image-{}.png".format(i), random_color(), random_color(), random.randrange(5, 20))
        elif generator == 2:
            generate_art("image-{}.png".format(i), start_gr, end_gr, 10)
os.system("mv *.png output")
os.system("cd output && ffmpeg -f image2 -i image-%d.png out.gif")
os.system("cd output && rm *.png")
print("gif has successfully been generated!")
os.system("mv output/out.gif /mnt/c/Users/Shogo/Desktop")
quit(0)
