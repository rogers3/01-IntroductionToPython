"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Christina Rogers.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg
window = rg.TurtleWindow()

j = 1
bert = rg.SimpleTurtle('turtle')
bert.pen = rg.Pen('red', 10)
bert.speed = 1000
ernie = rg.SimpleTurtle('turtle')
ernie.pen = rg.Pen('green', 10)

for j in range(6):
    for i in range(45):
        bert.forward(j)
        bert. left(5)
bert.forward(100)
for k in range(18):
    bert.left(10)
    bert.forward(10)
bert.forward(100)

ernie.pen_up()
ernie.right(90)
ernie.forward(150)
ernie.pen_down()
for l in range(10):
    ernie.forward(20)