import tensorflow as tf

def convert_to_tf_life(filePath, outputFilePath):
    model = tf.saved_model.load(filePath)
    # converter = tf.compat.v1.lite.TFLiteConverter.from_saved_model(filePath)
    # tflite_model = converter.convert()
    # filename = '{}.tflite'.format(outputFilePath)
    # with open(filename, 'wb') as f:
    #     f.write(tflite_model)
   

convert_to_tf_life('model/pass_dep_model/model-877815998755897344/tf-saved-model/2024-04-05T01:42:31.205485Z/predict/001', 'model/pass_dep_tflite_model')
# convert_to_tf_life('model/arr_weather_model.keras', 'model/arr_weather_model')