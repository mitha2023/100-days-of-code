#TIP CALCULATOR
print("WELCOME TO THE TIP CALCULATOR!!!!")
Total_bill=float(input("what was the total bill? $"))
Tip=int(input("how much percent would you like to give? 10,12,15"))
People=int(input("how many people are going to split the bill?"))
tip_in_totalbill=Tip/100*Total_bill
Total=tip_in_totalbill+Total_bill
per_person=Total/People
final="{:.2f}".format(per_person)
print(f"each person should pay: $ {final}")
