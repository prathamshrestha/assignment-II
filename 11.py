def exe(string):
    return string[-4:]

if __name__ == "__main__":
    string=input('enter a string ')
    print('the extension is ',exe(string))