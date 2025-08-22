"""
Program Perulangan Dengan "While" undefined count with stop point
"""

# Dengan 'While'
print("With WHILE")
book_count = 10
print('Mom said, "Read the books"')

read_count = 0
understood_count = 0
print(f"Total books that have been read & undestood {understood_count} books")

while read_count < book_count * 2:
    read_count += 1
    if understood_count == 9:
        print(f"Book - {understood_count + 1} not understood")
    else:
        understood_count += 1
        print(f"Book - {understood_count} read & understood")

print(f"Total books that have been read & understood are {understood_count} books")

if understood_count == book_count:
    print('Kid says, "Mom, all the books have been read & understood"')
else:
    print(f'Kid says, "Mom, '
          f'i can only have {understood_count} books " ')
