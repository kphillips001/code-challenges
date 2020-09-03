# Print out all of the numbers in the following array that are divisible by 3:
my_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
#   27
#   81
#   9
#   27
#   99
#   63
#   42
# Verbalize your thought process as much as possible before writing any code. Run through #  the UPER problem solving framework while going through your thought process.
for x in my_list:
  if x % 3 == 0:
    print(x)

