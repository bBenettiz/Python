#ANSI padrao
#escape sequence
#model:
#\033[(color code)m
#\033[style(0,1,4,7);text(30-37);back()m
#style             text             back
# 0 none           30 white         40 white
# 1 bold           31 red           41 red
# 4 underline      32 green         42 green
# 7 negative       33 yellow        43 yellow
#                  34 blue          44 blue
#                  35 purple        45 purple
#                  36 cyan          46 cyan
#                  37 gray          47 gray
#for more color options, utilize modules
#test:
x= 5
print('\033[1;32m this is a test {}'.format(x))
