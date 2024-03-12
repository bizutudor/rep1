# import sys
#
#
# nums = list(range(1, 111_111_111))
#
# squared_list = [x**2 for x in nums]
# squared_gen = (x**2 for x in nums)  # generator expression
#
# print(sys.getsizeof(squared_list), 'bytes')
# print(sys.getsizeof(squared_gen), 'bytes')
#
# # print(squared_list)
#
# # print(next(squared_gen))
# # print(next(squared_gen))
#
# # for num in squared_gen:
# #     print(num)
#
#
# def new_decorator(original_func):
#     def wrapper_func():
#         print("Niste cod inaintea apelului original_func")
#         original_func()
#         print("Niste cod dupa apelul original_func")
#
#     return wrapper_func
#
#
# @new_decorator
# def func_needs_decoration():
#     print("Vreau sa fiu decorata")
#
#
# @new_decorator
# def hello():
#     print("Hello Pythonistas!")
#
#
# @new_decorator
# def greet(name: str):
#     print(f"Greetings to you, {name}!")
#
#
# func_needs_decoration()
# hello()
# print("-"*40)
# greet("Felix")


