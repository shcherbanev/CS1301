def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Is it longer than 7 and more than 2?
def length7(plate):
     if len(plate) < 7 and len(plate) >= 2 and plate[0].isalpha() and plate[1].isalpha():
          return True
     else:
          return False

# Is it all chars/digits?
def all_chars_digits(plate_array):

    extra_symbols_present = False
    number_of_digits = int()
    for i in plate_array:
          if i.isalpha() or i.isdigit():
               extra_symbols_present = False
               continue
          else:
               extra_symbols_present = True
               break


    if extra_symbols_present:
          return False
    else:

          return True

# Zero in the middle?
def zero_middle(ww):
    half = int(len(ww)/2)
    middle_plus_one = int(half)
    middle_plus_one_char = ww[middle_plus_one]
    if middle_plus_one_char == "0":
         return False
    else:
         return True



def is_valid(s):

     plate_array = []
     if length7(s):
          element_counter = int()
          for i in s:
               element_counter += 1
               plate_array.append(i)
               continue
     else:
          return False

     if all_chars_digits(plate_array):
               if zero_middle(plate_array):
                    return True
     else:
          return False

main()