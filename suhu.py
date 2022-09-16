def suhu(x):
    reamur = x * 4/5
    fahrenheit = (x * 9/5)+32
    kelvin = x + 273
    print("suhu dalam reamur : ", reamur)
    print("suhu dalam fahrenheit : ", fahrenheit)
    print("suhu dalam kelvin : ", kelvin)

a = int(input("Masukan Suhu Dalam Celcius : "))
suhu(a)