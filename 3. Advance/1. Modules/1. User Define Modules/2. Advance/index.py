# ---------------------------
# Both will work just fine
import same_code_one
import same_code_two

same_code_one.intro()
print(same_code_one.add_to_numbers(2, 2))

same_code_two.intro()
print(same_code_two.add_to_numbers(2, 2))


# ---------------------------
# Only the last import will work because it's priority is high
# from same_code_one import intro, add_to_numbers
# from same_code_two import intro, add_to_numbers

# intro()
# print(add_to_numbers(10, 20))
