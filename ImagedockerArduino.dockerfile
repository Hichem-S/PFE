# Utiliser l'image officielle Arduino comme base
FROM arduino

# Copier le code Arduino dans le conteneur
COPY arduino_project.ino /usr/src/app/arduino_project.ino
WORKDIR /usr/src/app

# Compiler le code Arduino pour Arduino Uno R3
RUN arduino-cli core update-index
RUN arduino-cli core install arduino:avr

# Compiler le code Arduino pour Arduino Uno R3
RUN arduino-cli compile --fqbn arduino:avr:uno /usr/src/app/arduino_project.ino

# Flasher le code sur la carte Arduino Uno R3 (ajuster le port série en fonction de votre configuration)
CMD arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /usr/src/app/arduino_project.ino
