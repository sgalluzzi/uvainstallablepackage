import shared as sh
sh.afunction()

print(sh.space_compress('A dog   went   to the zoo'))
print(sh.space_compress('A dog \n went \n to the zoo'))
print(sh.space_compress(3))