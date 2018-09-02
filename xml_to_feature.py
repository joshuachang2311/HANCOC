import xml.etree.cElementTree as ET
from conversion_tools import pitch_letter_to_number
from score_data_tools import get_measure_duration
from score_data_tools import get_transpose

def xml_to_feature(data = ''):
    music_xml_tree = ET.fromstring(data)
    measures = music_xml_tree.findall('part/measure')
    measure_duration = get_measure_duration(music_xml_tree)
    transpose = get_transpose(music_xml_tree)
    
    loop_counter = 0 #8-bar loop counter, in the range between 1 ~ 16 after initialisation
    features = [] #Data Set
    
    for measure in measures:
        current_position = 0 #current_positionent place in a bar, in the range between 0 ~ (2 * measure_duration)
        measure_data = [] #Note data of the measure
        notes = measure.findall('note') #Array of notes
    
    
        for note in notes:
            if not(note.find('pitch/step') is None):
                pitch_letter = note.find('pitch/step').text #Text that describes the pitch
            else:
                pitch_letter = 'L'
            
            pitch_number = pitch_letter_to_number(pitch_letter) #Pitch data in integers, in the range between 0 ~ 12
        
            if not(note.find('pitch/alter') is None):
                pitch_number += int(note.find('pitch/alter').text) #Adding alters to the note
            
            if not(pitch_number == 0):
                pitch_number += transpose
                pitch_number = pitch_number % 12
        
            note_duration = int(note.find('duration').text) #Duration of the note, in the range between 0 ~ (2 * measure_duration)

            starting_point = int(round(current_position / measure_duration * 8)) #The 16th-note-wise starting point of the note, in the range between 0 ~ 15
            ending_point = int(round((current_position + note_duration) / measure_duration * 8)) #The 16th-note-wise ending point of the note, in the range between 0 ~ 15
        
            for i in range(starting_point, ending_point):
                measure_data.append(pitch_number) #Assigning the pitch to measure's note data

            current_position += note_duration #Moving current_positionent point by duration
        
            if(current_position >= 2 * measure_duration): #If current_positionent point reaches the end of the measure
                #Loop counting and mod by 16
                loop_counter += 1
    
                if loop_counter > 16:
                    loop_counter -= 16

                #Splitting into half-bar data
                feature = []

                #Assigning the first half of measure_data
                for i in range(0, 8):
                    feature.append(measure_data[i])
                feature.append(loop_counter) #Assigning 8-bar loop value

                features.append(feature)

                loop_counter += 1
    
                if loop_counter > 16:
                    loop_counter -= 16
                
                feature = []
            
                for i in range(8, 16):
                    feature.append(measure_data[i])
                feature.append(loop_counter)
                
                features.append(feature)
                break
    
    return features