from PIL import Image, ImageDraw, ImageFont

def combine_images(before_path, after_path, output_path):
    # Open the images
    before_image = Image.open(before_path)
    after_image = Image.open(after_path)

    # Ensure both images have the same height
    height = max(before_image.height, after_image.height)
    before_image = before_image.resize((before_image.width, height))
    after_image = after_image.resize((after_image.width, height))

    # Create a new image with double width for both images and an arrow in the middle
    combined_width = before_image.width + after_image.width + 50  # extra space for the arrow
    combined_image = Image.new("RGB", (combined_width, height), "white")

    # Paste the before and after images onto the combined image
    combined_image.paste(before_image, (0, 0))
    combined_image.paste(after_image, (before_image.width + 50, 0))

    # Draw an arrow in the middle
    draw = ImageDraw.Draw(combined_image)
    arrow_start = before_image.width
    arrow_end = arrow_start + 50
    draw.line([(arrow_start, height // 2), (arrow_end, height // 2)],
              fill="black", width=2)
    draw.polygon([(arrow_end, height // 2), (arrow_end - 5, height // 2 - 5), (arrow_end - 5, height // 2 + 5)],
                 fill="black")

    # Add text "Shift 40 degrees" above the arrow
    arial_font = ImageFont.truetype("Arial.ttf", size=12) 
    text = "Shift 3 offsets degrees"
    bbox = draw.textbbox(((arrow_start + arrow_end - 130) // 2, height // 2 - 20), text, font=arial_font)
    draw.text(bbox, text, font=arial_font, fill="black")

    # Save the combined image
    combined_image.save(output_path)


graph_path = "data_analysis/mean_bar_graphoffset2"
combine_images(graph_path + "_12.png", graph_path+"_22.png", "combined.png")
