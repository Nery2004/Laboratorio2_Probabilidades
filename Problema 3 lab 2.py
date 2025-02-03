#Laboratorio 2
#Mario Rocha 23501
#Kevin Villagran 23584
#Jonathan Zacarias 231104
#Luis Pedro Lira 23669
#Carlos Alburez 231311
#Nery Molina 23218

Enfermedad=0.00001
Sano=0.99999
Tiene_enfermedad_pos=0.95
No_tiene_enfermedad_pos=0.001
ProbabilidadPos=(Tiene_enfermedad_pos*Enfermedad)+(Sano*No_tiene_enfermedad_pos)
N=(Tiene_enfermedad_pos*Enfermedad)/ProbabilidadPos

print("La probababilidad real de que el paciente tenga la enfermedad:",N)