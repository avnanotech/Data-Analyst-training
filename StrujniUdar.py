# ЛИСТЕ 

meseci=["Јануар","Фебруар","Март","Април","Мај","Јун","Јул","Август","Септембар","Октобар","Новембар","Децембар"]
potrosnja=[1149,1078,934,729,630,720,774,808,910,957,1033,1092]
kvartali=[0,0,0,0]

print("Потрошња електричне енергије по месецима\n")

# ПОЧЕТНЕ ВРЕДНОСТИ
maksimum=potrosnja[0]
minimum=potrosnja[0]
ukupno=0

#ФУНКЦИЈЕ

def zamena():
 gornjavrednost=0
 for x in range(0,11):
  for y in range(x+1,12):
   if potrosnja[x]>potrosnja[y]:  
    gornjavrednost=potrosnja[x]
    potrosnja[x]=potrosnja[y]
    potrosnja[y]=gornjavrednost

def sumakvartala(n):
 if(n>=0 and n<=2):
   kvartali[0]=kvartali[0]+potrosnja[n] 
 elif(n>=3 and n<=5):
   kvartali[1]=kvartali[1]+potrosnja[n]
 elif(n>=6 and n<=8):
   kvartali[2]=kvartali[2]+potrosnja[n]
 else:
   kvartali[3]=kvartali[3]+potrosnja[n]


for x in range(0,12):
 print(meseci[x]," - ",potrosnja[x])

# ОДРЕЂИВАЊЕ МИНИМАЛНЕ И МАКСИМАЛНЕ ПОТРОШЊЕ
 if(minimum>potrosnja[x]):
    minimum=potrosnja[x]	
 if(maksimum<potrosnja[x]):
    maksimum=potrosnja[x]	
 ukupno=ukupno+potrosnja[x]  


# ОДРЕЂИВАЊЕ КВАРТАЛНИХ ВРЕДНИОСТИ     
 sumakvartala(x)

sredina=int(ukupno/12)

print("\n1.квартал - Укупно ",kvartali[0],"Просек ",int(kvartali[0]/3))
print("\n2.квартал - Укупно ",kvartali[1],"Просек ",int(kvartali[1]/3))
print("\n3.квартал - Укупно ",kvartali[2],"Просек ",int(kvartali[2]/3))
print("\n4.квартал - Укупно ",kvartali[3],"Просек ",int(kvartali[3]/3))

print("\nНајвећа потрошња: ",maksimum)
print("Најмања потрошња: ",minimum)
print("Аритметичка средина: ",sredina)

# СОРТИРАЊЕ ВРЕДНОСТИ НИЗА
zamena()
print("Медијана: ",int((potrosnja[5]+potrosnja[6])/2))

