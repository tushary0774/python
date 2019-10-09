while (1):
    ans=input("Do you want to print a directory (Y/N)?")
    Y="Y"
    if ans==Y:
        name = input("Input the Filename: ")
        s   = name.split(".")
        print ("The extension of the file is :\t" ,(s[-1]))
    elif ans!=Y:
        raise SystemExit
