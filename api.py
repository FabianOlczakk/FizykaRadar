# biblioteki
import serial
import json

# przypisuje zmiennej port seryjny
ser = serial.Serial('/dev/cu.usbmodem14102')
# ustawia wczytywanie tylko najnowszych danych z portu, tzn takich, których nigdy wcześniej nie załadowało
ser.flushInput()

# główna pętla
while True:
	# przypisuje zmiennej najnowsze dane z portu i rozszyfrowuje je z formatu binarnego
    raw_data = json.loads(ser.readline().decode('utf-8').rstrip().replace('\\', ''))
    print(raw_data)

    #zapisuje dane do pliku .json
    with open('data.json', 'w') as file:
    	json.dump(raw_data, file)
