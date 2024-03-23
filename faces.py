
def emoji(i,i2):
    conv_inp=i.replace(" :)","🙂")
    print()
    conv_inp2=i2.replace('):','🙁')
    return conv_inp,conv_inp2

inp=input("Enter a greeting with text emoji")
inp2=input()
con_emoji=emoji(inp,inp2)
for j in con_emoji:
  print(j)
