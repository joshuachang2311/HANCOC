#==============================================================================
# Get the durations per measure
#==============================================================================

def get_measure_duration(music_xml_tree):
    measures = music_xml_tree.findall('part/measure')
    
    measure_duration = 0 #Duration per half bars
    first_measure = measures[0]
    first_measure_notes = first_measure.findall('note')
    for note in first_measure_notes:
        measure_duration += int(note.find('duration').text)
    measure_duration /= 2
        
    return measure_duration

#==============================================================================
# Get the number of half notes being transposed upwards
#==============================================================================

def get_transpose(music_xml_tree):
    measures = music_xml_tree.findall('part/measure')
    first_measure = measures[0]
    
    transpose = int(first_measure.find('attributes/key/fifths').text) #volume of transpose
    transpose *= -7
    transpose = transpose % 12
    
    return transpose

#==============================================================================
# Get the index of the part of the music XML that contains notes
#==============================================================================

def get_part_index(music_xml_tree):
    score_size = len(music_xml_tree.getchildren())
    part_index = 0
    
    for score_index in range(0, score_size):
        if(music_xml_tree[score_index].tag == 'part'):
            part_index = score_index
            break
            
    return part_index