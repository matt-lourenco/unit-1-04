# Created by: Matthew Lourenco
# Created on: 22 Sept 2016
# This program is a program that calculates circumference

import ui

PI = 3.14

def calculate_touch_up_inside(sender):
    #calculate circumference
    
    #input
    radius = view['radius_textfield'].text
    
    #process
    circumference = 2 * PI * int(radius)
    
    #output
    view['circumference_label'].text = 'Circumference: ' + str(circumference)

view = ui.load_view()
view.present('full_screen')
