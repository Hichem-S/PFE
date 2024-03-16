import os
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Chemin vers le dossier contenant les images (assurez-vous que le dossier s'appelle "dataset")
data_dir = "dataset"

# Créez un générateur d'images pour l'entraînement et la validation
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Créez un modèle CNN simple
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entraînez le modèle
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size
)

# Évaluez le modèle sur de nouvelles images
test_image_path = "path/to/your/test/image.jpg"  # Remplacez par le chemin réel de votre image de test
test_image = plt.imread(test_image_path)
test_image = np.expand_dims(test_image, axis=0)
prediction = model.predict(test_image)

if prediction[0][0] > 0.5:
    print("La plante est malade.")
else:
    print("La plante est saine.")
