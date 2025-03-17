print (''' 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Programma: "FIZIKA"
Mērķis: Programma ir veidota, lai ievadītu iegūtus datus fizikas ekspirementā "Brīvas krišanas paātrinājums" 10 reizes.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
import csv
import pytz
from datetime import datetime

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums1 = input()
    try:
        augstums1 = float(augstums1)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums1 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums1 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums2 = input()
    try:
        augstums2 = float(augstums2)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums2 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums2 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums3 = input()
    try:
        augstums3 = float(augstums3)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums3 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums3 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums4 = input()
    try:
        augstums4 = float(augstums4)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums4 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums4 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums5 = input()
    try:
        augstums5 = float(augstums5)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums5 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums5 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums6 = input()
    try:
        augstums6 = float(augstums6)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums6 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums6 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums7 = input()
    try:
        augstums7 = float(augstums7)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums7 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums7 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums8 = input()
    try:
        augstums8 = float(augstums8)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums8 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums8 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums9 = input()
    try:
        augstums9 = float(augstums9)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums9 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums9 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet augstumu metros. Ievadot decimdaļu, lietojiet punktu. :')
    augstums10 = input()
    try:
        augstums10 = float(augstums10)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if augstums10 >= 20:
        print('Kluda! Skaitlim jābūt mazāk par 20!')
        continue
    if augstums10 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks1 = input()
    try:
        laiks1 = float(laiks1)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks1 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks1 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks2 = input()
    try:
        laiks2 = float(laiks2)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks2 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks2 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks3 = input()
    try:
        laiks3 = float(laiks3)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks3 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks3 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks4 = input()
    try:
        laiks4 = float(laiks4)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks4 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks4 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks5 = input()
    try:
        laiks5 = float(laiks5)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks5 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks5 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks6 = input()
    try:
        laiks6 = float(laiks6)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks6 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks6 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks7 = input()
    try:
        laiks7 = float(laiks7)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks7 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks7 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks8 = input()
    try:
        laiks8 = float(laiks8)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks8 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks8 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks9 = input()
    try:
        laiks9 = float(laiks9)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks9 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks9 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

while True:
    print('Ievadiet laiku sekundēs. Ievadot decimdaļu, lietojiet punktu. :')
    laiks10 = input()
    try:
        laiks10 = float(laiks10)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if laiks10 >= 10:
        print('Kluda! Skaitlim jābūt mazāk par 10!')
        continue
    if laiks10 <= 0:
        print('Kluda! Skaitlim jābūt vairāk par 0!')
        continue
    break

tz = pytz.timezone('Europe/Riga')
Datums = riga_current_datetime = datetime.now(tz)
Ievad_laiks = Datums.strftime("%X %d/%m/%Y")
  
with open('Dati.csv','w', newline='') as csvfile: 
  fieldnames = ['h(m)','t(s)','datums']
  writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = ';')

  writer.writerow({'h(m)':'h (m)','t(s)':'t(s)','datums':'Ievadīšanas laiks'})
  writer.writerow({'h(m)': augstums1,'t(s)': laiks1,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums2,'t(s)': laiks2,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums3,'t(s)': laiks3,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums4,'t(s)': laiks4,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums5,'t(s)': laiks5,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums6,'t(s)': laiks6,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums7,'t(s)': laiks7,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums8,'t(s)': laiks8,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums9,'t(s)': laiks9,'datums': Ievad_laiks})
  writer.writerow({'h(m)': augstums10,'t(s)': laiks10,'datums': Ievad_laiks})