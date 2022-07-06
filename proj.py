def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
    # Step1 : To read the file and store in the variable data_a
    # data_a = r.read()
    # data_a = a.read
    # data_a = a.read()
    # data_a = aread()

	with open(file2, 'r') as b:
    data_b = b.read()

    with open(file1, 'w') as a:
    # Step 2: To write to the file
    # a.write(data_b)
    # a.write[data_b]
    # a.write{data_b}
    # awrite(data_b)

    with open(file2, 'w') as b:
    b.write(data_a)

swapFileData()