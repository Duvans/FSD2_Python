# ############# FILE NEED TO GET EXECUTED TWICE
# print('file')
# try:
#     #    f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
#     with open("sample.txt", 'r', encoding='utf-8') as f:
#         print("opened!")
#         # # write
#         # f.write("File Contoh\n")
#         # f.write("Test lorem ipsum\n\n")
#         # f.write("ini file sample\n")
#         # # append
#         # f.write("\nappend masuk kesini\n")
#         #read
#         print(f.read(4)) #first 4 line charac
#         print(f.read(4)) #next 4 line charac
#         print(f.read())     # read in the rest till end of file
#         print(f.read(), "0")  # further reading returns empty string
#         print(f.tell())    # get the current file position
#         print(f.seek(3))   # bring file cursor to initial position
#         print(f.read(5)) #next 4 line charac
#         print(f.seek(0))   # bring file cursor to initial position
#         print(f.readline()) # read until nextline

#     # perform file operations
# finally:
#     f.close()
#     print("closed")


# #---------------------------------------------------------------------------------
# #exception

# # x = 10
# # if x > 5:
# #     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


# # x = 10
# # if x > 5:
# #     raise Exception('your custom exception')

# import sys

# #ERROR IMPLEMENTATION
# # assert ('macOS' in sys.platform), "This code runs on macos only"
# # assert ('linux' in sys.platform), "This code runs on Linux only."
# # assert ('win32' in sys.platform), "This code runs on Windows only."

# #BEST PRACTICE => The try and except Block: Handling Exceptions
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win32' in sys.platform), "This code runs on Windows only."
#     assert ('macOS' in sys.platform), "This code runs on macos only"
#     print('Doing something.')

# # try:
# #     os_interaction()
# # except AssertionError as error:
# #     print(error)
# #     print('The os_interaction() function was not executed')

# #------------------
# #another example 

# # try:
# #     with open('file.log') as file:
# #         read_data = file.read()
# # except:
# #     print('Could not open file.log')

# # try:
# #     with open('file.log') as file:
# #         read_data = file.read()
# # except FileNotFoundError as fnf_error:
# #     print(fnf_error)

# #first call the os_interaction() function and then try to open a file
# # try:
# #     os_interaction()
# #     with open('file.log') as file:
# #         read_data = file.read()
# # except FileNotFoundError as fnf_error:
# #     print(fnf_error)
# # except AssertionError as error:
# #     print(error)
# #     print('os_interaction() function was not executed')

# #else clause ->instruct a program to execute a certain block of code only in the absence of exceptions.
# # try:
# #     os_interaction()
# # except AssertionError as error:
# #     print(error)
# # else:
# #     print('Executing the else clause.')

# # try:
# #     os_interaction()
# # except AssertionError as error:
# #     print(error)
# # else:
# #     try:
# #         with open('file.log') as file:
# #             read_data = file.read()
# #     except FileNotFoundError as fnf_error:
# #         print(fnf_error)



# #Cleaning Up After Using finally -> finally akan berjalan terus ketika code dieksekusi

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('Cleaning up, irrespective of any exceptions.')