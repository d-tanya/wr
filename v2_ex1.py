file = open("config_v2_ex1.txt","r")

age = file.readlines()
agenum = int(str(age[0]))
max_pulse = 220 - agenum
razminka1 = int(max_pulse * 0.5)
razminka2 = int(max_pulse * 0.6)
fitness1 = int(max_pulse * 0.6)
fitness2 = int(max_pulse * 0.7)
run1 = int(max_pulse * 0.7)
run2 = int(max_pulse * 0.8)
silovaya1 = int(max_pulse * 0.8)
silovaya2 = int(max_pulse * 0.9)
maxnagruzka1 = int(max_pulse * 0.9)
maxnagruzka2 = int(max_pulse)

print("Zona razminki: ",razminka1," - ", razminka2)

print("Zona fitness: ",fitness1," - ", fitness2)

print("Aerobic zone: ",run1," - ", run2)

print("Anaerobic zone: ",silovaya1," - ", silovaya2)

print("Max zone: ",maxnagruzka1," - ", maxnagruzka2)