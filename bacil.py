print('## Program Python Piramida ##')

print()
 
tinggi_piramida = int (input('berapa baris :'))
print()

for i in range(tinggi_piramida):
  for j in range(tinggi_piramida-i):
    print(' ',end='')
     
  for j in range(i+1):
    print('$ ',end='')
  print()