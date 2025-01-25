"""
This is a very long comment
that takes several lines

"""

users_input = input("File name?: ").strip().lower()


if users_input.count('.') == 1:

    filename, file_extension = users_input.split(".")

    if file_extension == "gif":
        print("image/gif")
    elif file_extension == "jpg":
        print("image/jpeg")
    elif file_extension == "jpeg":
        print("image/jpeg")
    elif file_extension == "png":
        print("image/png")
    elif file_extension == "pdf":
        print("application/pdf")
    elif file_extension == "txt":
        print("text/plain")
    elif file_extension == "zip":
        print("application/zip")
    elif file_extension == "bin":
        print("application/octet-stream")
    #elif  mid == "txt" and file_extension2 == "pdf":
    #       print("application/pdf")
    elif users_input.split(".") == 3:
        print("Three items")
elif users_input.count('.') == 2:
    filename1, middle, file_extension = users_input.split(".")
    if file_extension == "pdf":
        print("application/pdf")
else: print("application/octet-stream")