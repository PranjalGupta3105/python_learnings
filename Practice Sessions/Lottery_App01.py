def get_player_numbers():
    number_csv=input("Enter the 6 numbers Seperated by commas from 1 to 20:-")
    cnvtno=[int(number) for number in number_csv.split(",")]
    print(cnvtno)
    print(type(cnvtno))
    ipset=set(cnvtno)
    print(ipset)
    print(type(ipset))




get_player_numbers()


