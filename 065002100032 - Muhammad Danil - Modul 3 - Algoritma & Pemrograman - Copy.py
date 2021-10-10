# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:18:29 2021
@judul : Laporan Praktikum 3
@author: Muhammad Danil Hidayat
@NIM : 065002100032
@hari/tanggal : 20211010
"""

import math
pilihan1 = int(input("masukkan angka yang pertama: "))
pilihan2 = int(input("masukkan angka yang kedua: "))
pilihan3 = int(input("masukkan angka yang ketiga: "))
                     
if pilihan1 == 0:
    print("bukan persamaan kuadrat")
   
else:
    rumus = (pilihan2**2) - (4*pilihan1*pilihan3)
 
    if rumus > 0 :
      x1 = (-pilihan2 + math.sqrt(rumus)) /(2*pilihan1)
      x2 = (-pilihan2 - math.sqrt(rumus)) /(2*pilihan1)
      print("jenis akar yang berbeda")
      print("jadi persamaan kuadrat nya adalah",x1,"dan",x2)
      print("dengan determinan",rumus,)

    elif rumus == 0 :
        x1 = (-pilihan2)/ (2*pilihan1)
        x2 = (-pilihan2)/ (2*pilihan1)
        print("jenis akar yang kembar")
        print("jadi persamaan kuadrat nya adalah",x1,"dan",x2)
        print("dengan determinan",rumus,)

    else:
        x1 = (-pilihan2 + math.sqrt(rumus)) / (2*pilihan1)
        x2 = (-pilihan2 - math.sqrt(rumus)) / (2*pilihan1)
     
        print("jenis akar imaginer")
        print("jadi persamaan kuadrat nya adalah",x1,"dan",x2)
        print("dengan determinan",rumus,)
 
