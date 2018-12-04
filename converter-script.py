import coremltools

# This is a scipt to convert a caffe model in to a ML file for swift
# coremltools MUST be imported
# MUST be running in a python2.7 enviormnent!


#              file path goes below(you can put it all in the same folder to make is easier)
caffe_model = ()

# This is the variable for teh labes.txt file
labels = ''

# this is the script that converts the files into a coreML file
coreml_model = coremltools.converters.caffe.convert(
    caffe_model, # From above
    class_labels=labels, # Labels from above
    image_input_names='data' # This is what is used in the ml file
)

# This will save the file into a mlmodel(put a name before the .)
coreml_model.save('.mlmodel')
