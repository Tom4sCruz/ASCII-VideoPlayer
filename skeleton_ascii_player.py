import os

VIDEO = 1
IMG = 2

def ascii_video():
    # TODO
    return 0

def ascii_img():
    # TODO
    return 0

def ascii_player(option, path):
    if option == VIDEO:
        print("You've chosen VIDEO")
        ascii_video()
    else:
        print("You've chosen IMG")
        ascii_img()

if __name__ == "__main__":
    os.system("figlet ASCII Player")
    print("###########################################")
    print("# What do you want to convert into ASCII? #")
    print("#                                         #")
    print("# (1) - Video (.mp4)                      #")
    print("# (2) - Image (.png)                      #")
    print("###########################################")
    
    chosen = "0"
    while chosen not in "12":
        print("\n (choose one of the numbers in parentheses) (Default=1)", end=" ")
        chosen = input()
        chosen = '1' if chosen == "" else chosen
    print(" (path to your file)", end=" ")
    file_path = input()

    ascii_player(int(chosen), file_path)
