import functools

f =open("result.txt", "w")
name =input("ENTER YOUR NAME: ")
dis =input("ENTER YOUR FIELD (C for Computer Science B for Biology)     :")
main =["SUBJECT","Obt_9th", "Obt_10th", "PRACTICAL", "TOTAL", "PER"]
Comp_Header =["ENGLISH  ", "URDU     ", "MATH     ", "ISL      ", "P.STUDY  ", "COMPUTER ", "PHYSICS  ", "CHEMISTRY"]
Comp_total =["75", "75", "75", "50", "50", "75", "75", "75"]
Bio_Header =["ENGLISH  ", "URDU     ", "MATH     ", "ISL      ", "P.STUDY  ", "BIOLOGY  ", "PHYSICS  ", "CHEMISTRY"]

Bio_total =["75", "75", "75", "50", "50", "75", "75", "75"]
nin =[""]*8
ten =[""]*8
if dis=="C" or "c":
    f.write("   _______________________________________________________________________________________________" + "\n")
    f.write("NAME: "+ str(name))
    i =0
    f.write("\n")
    while i<6:
        f.write(str(main[i]) + "    ")
        i =i+1
    f.write("\n")
    i =0
    per_tot =0
    while i<8:
        j =0
        obt =0
        tot =0
        f.write(str(Comp_Header[i])+ "     ")
        ni =input(f"ENTER MARKS OF 9TH IN {Comp_Header[i]}:")
        f.write(str(ni) +"        ")
        te = input(f"ENTER MARKS OF 10TH IN {Comp_Header[i]}:")
        f.write(str(te)+ "           ")
        if Comp_Header[i]=="COMPUTER " or Comp_Header[i]=="PHYSICS  " or Comp_Header[i]=="CHEMISTRY":
            pra =input(f"ENTER MARKS FOR PRACTICAL {Comp_Header[i]}:")
            f.write(str(pra)+ "         ")
        else:
            pra ="0 "
            f.write(str(pra) +"         ")
        f.write(str(int(ni)+int(te)+int(pra)) + "     ")
        obt =int(ni) +int(te) +int(pra)
        tot =int(Comp_total[i])
        j =(obt/(tot*2))*100
        f.write(str(round(j, 2)))
        per_tot +=int(j)



        f.write("\n")
        i =i+1
    p =per_tot/8
    f.write("\n")
    f.write("   _______________________________________________________________________________________________" + "\n")
    f.write("                                                       "+ str(per_tot/8) + "\n")

    cal =(p/100)*1100
    f.write(str(f"TOTAL MARKS ARE {int(cal)} OUT OF 1100"))





else:
    f.write("   _______________________________________________________________________________________________" + "\n")
    f.write("NAME: " + str(name))
    i = 0
    f.write("\n")
    while i < 6:
        f.write(str(main[i]) + "    ")
        i = i + 1
    f.write("\n")
    i = 0
    per_tot = 0
    while i < 8:
        j = 0
        obt = 0
        tot = 0
        f.write(str(Bio_Header[i]) + "     ")
        ni = input(f"ENTER MARKS OF 9TH IN {Bio_Header[i]}:")
        f.write(str(ni) + "        ")
        te = input(f"ENTER MARKS OF 10TH IN {Bio_Header[i]}:")
        f.write(str(te) + "           ")
        if Bio_Header[i] == "BIOLOGY  " or Bio_Header[i] == "PHYSICS  " or Bio_Header[i] == "CHEMISTRY":
            pra = input(f"ENTER MARKS FOR PRACTICAL {Bio_Header[i]}:")
            f.write(str(pra) + "         ")
        else:
            pra = "0 "
            f.write(str(pra) + "         ")
        f.write(str(int(ni) + int(te) + int(pra)) + "     ")
        obt = int(ni) + int(te) + int(pra)
        tot = int(Bio_total[i])
        j = (obt / (tot * 2)) * 100
        f.write(str(round(j, 2)))
        per_tot += int(j)

        f.write("\n")
        i = i + 1
    p = per_tot / 8
    f.write("\n")
    f.write("   _______________________________________________________________________________________________" + "\n")
    f.write("                                                       " + str(per_tot / 8) + "\n")

    cal = (p / 100) * 1100
    f.write(str(f"TOTAL MARKS ARE {int(cal)} OUT OF 1100"))




