#==============================================================================
# 2 -> IIIm
#==============================================================================

def chord_number_to_letter(chord_number = 0):
    chord_letter = 'None'
    
    if(chord_number == 1):
        chord_letter = 'I'
                
    if(chord_number == 2):
        chord_letter = 'IIIm'
                    
    if(chord_number == 3):
        chord_letter = 'V'
                
    if(chord_number == 4):
        chord_letter = 'VIIdim'
                          
    if(chord_number == 5):
        chord_letter = 'IIm'

    if(chord_number == 6):
        chord_letter = 'IV'

    if(chord_number == 7):
        chord_letter = 'VIm'
        
    return chord_letter

#==============================================================================
# Change [10] to [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
#==============================================================================

def one_hot_conversion(features):
    for feature in features:
        for i in range(0, 8):
            arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if(feature[0] > 0):
                arr[feature[0] - 1] = 1
            feature.extend(arr)
            del(feature[0])
            
    return features

#==============================================================================
# D -> 3
#==============================================================================

def pitch_letter_to_number(pitch_letter = "C"):
    pitch_number = 0
    
    if(pitch_letter == "C"):
        pitch_number = 1
                
    if(pitch_letter == "D"):
        pitch_number = 3
                    
    if(pitch_letter == "E"):
        pitch_number = 5
                
    if(pitch_letter == "F"):
        pitch_number = 6
                          
    if(pitch_letter == "G"):
        pitch_number = 8

    if(pitch_letter == "A"):
        pitch_number = 10

    if(pitch_letter == "B"):
        pitch_number = 12
        
    return pitch_number

#==============================================================================
# def sixteenth_duration_to_ly(note_duration = 1):
#     ly_duration = ''
#     if(note_duration == 1):
#         ly_duration = '16'
#     if(note_duration == 2):
#         ly_duration = '8'
#     if(note_duration == 3):
#         ly_duration = '8.'
#     if(note_duration == 4):
#         ly_duration = '4'
#     if(note_duration == 6):
#         ly_duration = '4.'
#     if(note_duration == 7):
#         ly_duration = '4..'
#     if(note_duration == 8):
#         ly_duration = '2'
#     if(note_duration == 12):
#         ly_duration = '2.'
#     if(note_duration == 14):
#         ly_duration = '2..'
#     if(note_duration == 15):
#         ly_duration = '2...'
#     if(note_duration == 16):
#         ly_duration = '1'
#         
#     return ly_duration
#==============================================================================
