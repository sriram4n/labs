from tensorflow.keras.models import Sequential
from tensorflow.keras.appliations VGG16
from tensorflow.keras.layers import Dropout, Dense, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_PATH = r'c:/Users'

print("Loading dataset")

# normalize
datagen = ImageDataGenerator(
    rescale = 1./255,
    validation_split = 0.2
)

# train test
train = datagen.flow_from_directory(
    DATASET_PATH,
    batch_size = 32,
    class_mode = 'binary',
    target_size = (224,224),
    subset = 'training'
)

test = datagen.flow_from_directory(
    DATASET_PATH,
    batch_size = 32,
    class_mode = 'binary',
    target_size = (224,224),
    subset = 'validation'
)

base_model = VGG16(
    dataset = 'imagenet',
    include_top = false,
    input_shape = (224,224,3)
)
base_model.trainable = false
model = Sequential([
    base_model,
    Flatten(),
    Dense(128, activation = 'relu'),
    Dropout(0.5),
    Dense(1, activation = 'sigmoid')
])
model.compile(
    optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy']
)
model.fit(train, validation = test, epochs = 1)

loss, acc = model.evaluate(test)

print("Acccc: ", acc*100)
