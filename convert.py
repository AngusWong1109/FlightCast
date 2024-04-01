import tensorflow as tf
import tensorflow_decision_forests as tfdf

def convert_to_tf_life(filePath, outputFilePath):
    """
    model = tf.keras.models.load_model(filePath)
    print('loaded model')
    converter = tf.lite.TFLiteConverter.from_saved_model(filePath)
    tflite_model = converter.convert()
    filename = '{}.tflite'.format(outputFilePath)
    with open(filename, 'wb') as f:
        f.write(tflite_model)
    """
    
    tfdf.keras.yggdrasil_model_to_keras_model(filePath, outputFilePath)

convert_to_tf_life('model/dep_weather_model/assets', 'model/new_dep_weather_model')
# convert_to_tf_life('model/arr_weather_model.keras', 'model/arr_weather_model')