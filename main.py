from d0_yield import y
from d000_onehot import XOH
from conversion_tools import one_hot_conversion
from add_chord_notations import add_chord_notations
from xml_to_feature import xml_to_feature
import xml.etree.cElementTree as ET

from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier

def HANCOC(music_xml_string, name = 'new_music_with_chords'):
    XTrain, XTest, yTrain, yTest = train_test_split(XOH, y, test_size = 0.3731343)
    RFC = RandomForestClassifier(n_estimators = 50, criterion = "gini",	max_features = 10)
    RFC.fit(XTrain, yTrain)

    features = xml_to_feature(music_xml_string)
    features = one_hot_conversion(features)

    predictions = RFC.predict(features)

    tree = ET.fromstring(music_xml_string)
    tree = add_chord_notations(tree, predictions)

    xmlstr = ET.tostring(tree, encoding = "unicode")
    result_file = open(name + '.xml', 'w')
    result_file.write(xmlstr)
