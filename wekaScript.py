import weka.core.jvm as jvm
jvm.start()

from weka.core.converters import Loader, Saver
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file("./Listas/train.arff")

print data


jvm.stop()