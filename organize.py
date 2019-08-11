import os
import shutil

dir_names = ["images", "videos", "audios", "compressed",
             "disc images", "executables", "text files"]
audio_ext = ["aif", "cda", "mid", "midi",
             "mp3", "mpa", "ogg", "wav", "wma", "wpl"]
image_ext = ["ai", "bmp", "gif", "ico", "jpeg",
             "jpg", "png", "ps", "psd", "svg", "tif", "tiff"]
comp_ext = ["7z", "arj", "deb", "pkg", "rar", "rpm", "tar.gz", "z", "zip"]
video_ext = ["3g2", "3gp", "avi", "flv", "h264", "m4v", "mkv",
             "mov", "mp4", "mpg", "mpeg", "rm", "swf", "vob", "wmv"]
disc_img_ext = ["dmg", "iso", "toast", "vcd"]
exe_ext = ["apk", "bat", "cgi", "pl", "com",
           "exe", "gadget", "jar", "py", "wsf"]
text_ext = ["doc", "docx", "odt", "pdf",
            "rtf", "tex", "txt", "wks", "wps", "wpd"]
path = input("Where would you like to scan?\nLocation: ")
files = os.scandir(path)
file_names = []


def ask_user():
    print("\n**** WARNING: THIS WILL MOVE YOUR FILES INTO SUBFOLDERS ****")
    decision = input("\nReorganize files? (y\\n): ")
    if decision.lower() == "y" or "yes":
        reorganize()
    elif decision.lower() == "n" or "no":
        print("\nGoodbye!")


def check_dir(name):
    if not os.path.exists(f"{path}/{name}"):
        os.mkdir(f"{path}/{name}")


def move_file(file_name, location):
    shutil.move(f"{path}/{file_name}", f"{path}/{location}/{file_name}")


def reorganize():
    print("\nMoving files...")
    for file in file_names:
        for ext in image_ext:
            if file.endswith(ext):
                check_dir(dir_names[0])
                move_file(file, dir_names[0])
                break
        for ext in video_ext:
            if file.endswith(ext):
                check_dir(dir_names[1])
                move_file(file, dir_names[1])
                break
        for ext in audio_ext:
            if file.endswith(ext):
                check_dir(dir_names[2])
                move_file(file, dir_names[2])
                break
        for ext in comp_ext:
            if file.endswith(ext):
                check_dir(dir_names[3])
                move_file(file, dir_names[3])
                break
        for ext in disc_img_ext:
            if file.endswith(ext):
                check_dir(dir_names[4])
                move_file(file, dir_names[4])
                break
        for ext in exe_ext:
            if file.endswith(ext):
                check_dir(dir_names[5])
                move_file(file, dir_names[5])
                break
        for ext in text_ext:
            if file.endswith(ext):
                check_dir(dir_names[6])
                move_file(file, dir_names[6])
                break
    print("\nSuccess! ")


def main():
    for file in files:
        if file.is_file():
            file_names.append(file.name)

    if len(file_names) > 0:
        print(f"\nFound {len(file_names)} file(s).")
        ask_user()
    else:
        print("\nOh no! There are no files in this directory!")


main()
