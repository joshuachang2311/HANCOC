import xml.etree.cElementTree as ET
#from score_data_tools import get_transpose

def engrave_chord_type(chord_number):
    chord_type = 'diminished'
    if(chord_number == 1):
        chord_type = 'major'
    if(chord_number == 2):
        chord_type = 'minor'
    if(chord_number == 3):
        chord_type = 'major'
    if(chord_number == 5):
        chord_type = 'minor'
    if(chord_number == 6):
        chord_type = 'major'
    if(chord_number == 7):
        chord_type = 'minor'
        
    return chord_type

def array_rotate(array, shift_right):
    array_size = len(array)
    new_array = []

    for i in range(0, array_size):
        new_array.append(0)
    
    for i in range(0, array_size):
        current_index = (i + shift_right) % array_size
        new_array[current_index] = array[i]
        
    return new_array

def generate_root_letter(fifths_transpose):
    root_letter = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    root_letter = array_rotate(root_letter, (fifths_transpose * -4) % 7)
    return root_letter

def generate_root_alter(fifths_transpose):
    root_alter = [0, 0, 0, 0, 0, 0, 0]
    if(fifths_transpose > 0):
        for sharp_number in range(0, fifths_transpose):
            sharp_index = (sharp_number * 4 + 3) % 7
            root_alter[sharp_index] = 1
    if(fifths_transpose < 0):
        for flat_number in range(0, fifths_transpose * -1):
            flat_index = (flat_number * 3 + 6) % 7
            root_alter[flat_index] = -1
    
    root_alter = array_rotate(root_alter, (fifths_transpose * -4) % 7)
    
    return root_alter


def get_root_index(chord_number):    
    root_index = (chord_number * 2 - 2) % 7
    return root_index
    
def generate_chord_notation(chord_number, fifths_transpose):
    root_letter = generate_root_letter(fifths_transpose)
    root_alter = generate_root_alter(fifths_transpose)
    root_index = get_root_index(chord_number)
    
    chord_notation = ET.Element('harmony')
    chord_root = ET.SubElement(chord_notation, 'root')
    chord_kind = ET.SubElement(chord_notation, 'kind')
    chord_kind.text = engrave_chord_type(chord_number)
    
    chord_root_step = ET.SubElement(chord_root, 'root-step')
    chord_root_step.text = root_letter[root_index]
    
    if not(root_alter[root_index] == 0):
        chord_root_alter = ET.SubElement(chord_root, 'root-alter')
        chord_root_alter.text = str(root_alter[root_index])
    
    return chord_notation