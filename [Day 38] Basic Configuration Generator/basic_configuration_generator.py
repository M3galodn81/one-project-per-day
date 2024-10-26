def base_config():
    output = []
    output.append("enable \nconfig t\n")
    output.append("hostname " + input("Enter the hostname: ") +"\n")

    output.append("line console 0 \npassword " + input("Enter the console password: ") + "login\nexit"+"\n")
    output.append("line vty 0 4 \npassword " + input("Enter the vty password: ") + "login\nexit"+"\n")
    output.append("end \nwrite memory"+"\n")
    return "".join(output)

def main():
    print(base_config())


if __name__ == "__main__":
    main()