from score_data_tools import get_measure_duration
from score_data_tools import get_part_index
from chord_notation_generator import generate_chord_notation

def add_chord_notations(music_xml_tree, chord_progression = []):
    part_index = get_part_index(music_xml_tree)
    measures = music_xml_tree.findall('part/measure')
    measures_size = len(measures)
    measure_duration = get_measure_duration(music_xml_tree)
    fifths_transpose = int(measures[0].find('attributes/key/fifths').text)
    chord_index = 0
    
    for measure_index in range(0, measures_size):
        measure_children = measures[measure_index].getchildren()
        measure_children_size = len(measure_children)
        total_duration = 0
        
        first_chord_index = 0
        second_chord_index = 0
        
        for child_index in range(0, measure_children_size):
            if(measures[measure_index][child_index].tag == 'note'):
                if(total_duration == 0):
                    first_chord_index = child_index
                if(total_duration == measure_duration):
                    second_chord_index = child_index
                note_duration = int((measures[measure_index][child_index].find('duration')).text)
                total_duration += note_duration
        
        first_chord_notation = generate_chord_notation(chord_progression[chord_index], fifths_transpose)
        second_chord_notation = generate_chord_notation(chord_progression[chord_index + 1], fifths_transpose)
        chord_index += 2
        music_xml_tree[part_index][measure_index].insert(second_chord_index, second_chord_notation)
        music_xml_tree[part_index][measure_index].insert(first_chord_index, first_chord_notation)
                
    return music_xml_tree