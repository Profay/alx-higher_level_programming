import hidden_4

if __name__ == "__main__":
    file = dir(hidden_4)
    a = len(file)
    for i in range(0, a):
        if file[i][0:2] == "__":
            continue
        else:
            print(file[i])
