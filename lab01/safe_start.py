import os
import levenstein as lev

def get_key():
    output = os.popen("cat /var/lib/dbus/machine-id").read()[:-1]
    return output


def main():
    if get_key() == '8e3cfaa74f6a4b0eb36cf60b0b979874':
        lev.main()
    else:
        print("Доступ запрещен!")

if __name__ == "__main__":
    main()
