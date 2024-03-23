# def tip(amt):
#     t=amt*0.15

# def float_input(amt):
def dollars_to_float(amt):
 a=amt.replace("$","")
 a=float(a)
 return a
def percent_to_float(tip):
 t=tip.replace("%","")
 t=float(t)
 return t
 
def main():
 rais=input("How was the bill amount ")
 perc=input("What percentage for tip ")
 f=dollars_to_float(rais)
 p=percent_to_float(perc)
 t=f*p/100
 print(f"The tip is ${t:.2f}") 
main()

