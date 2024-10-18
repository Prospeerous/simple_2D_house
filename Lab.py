import cairo
import math

# Set the width and height of the canvas
WIDTH, HEIGHT = 800, 400

# Create the surface (canvas)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set background to white
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

#Draw the house body
context.set_source_rgb(0, 0, 0)  # Black color for outlines
context.set_line_width(3)
#context.rectangle(100, 150, 200, 150)  # Main house body
context.stroke()

# Draw the roof
context.move_to(200, 150)
context.line_to(280, 210)
context.line_to(280, 220)
context.line_to(200, 160)
context.line_to(120, 220)
context.line_to(120, 210)
context.line_to(200, 150)
context.stroke()

# Draw the roof house
context.move_to(130, 210)
context.line_to(130, 310)
context.stroke()

context.move_to(270, 210)
context.line_to(270, 310)
context.stroke()

# Draw bottom rectangle
context.rectangle(120, 310, 420, 8)
context.stroke()

context.move_to(530, 310)
context.line_to(530, 210)
context.stroke()

context.move_to(280, 210)
context.line_to(540, 210)
context.line_to(490, 155)
context.line_to(210, 155)
context.stroke()

# Draw bottom rectangle
context.rectangle(185, 190, 30, 30)
context.stroke()

context.rectangle(160, 240, 80, 40)
context.stroke()

context.rectangle(150, 280, 100, 8)
context.stroke()

context.rectangle(430, 240, 80, 40)
context.stroke()

context.rectangle(420, 280, 100, 8)
context.stroke()


# Crescent moon (two overlapping circles)
# Outer circle (big)
context.arc(600, 100, 50, 0, 2 * math.pi)  # center x, center y, radius
context.set_source_rgb(0.8, 0.8, 0.8)
context.fill_preserve()
context.set_line_width(1)
context.set_source_rgb(0, 0, 0)
context.stroke()

# Inner circle (cut-out)
context.arc(620, 90, 40, 0, 2 * math.pi)  # center x, center y, radius
context.set_source_rgb(1, 1, 1)  # white to create crescent
context.fill_preserve()
context.stroke()

# Save the image
surface.write_to_png("simple_house.png")
print("Image saved as 'simple_house.png'")