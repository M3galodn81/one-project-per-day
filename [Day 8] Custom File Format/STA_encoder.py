import os
from collections.abc import Iterable

class STAKeyValue:

    key_name = ""
    values = []

    def __init__(self,input_key,input_value):

        if type(input_key) is str:
            self.key_name = input_key
        else:
            print("Invalid name. The name should be a string")

        if (isinstance,input_value):
            if all(not isinstance(elem,Iterable) or isinstance(elem, (str, bytes)) for elem in input_value):
                self.values = input_value
            else:
                print("Invalid values. The values should not have any list, tuples, sets or dictionaries")
        else:
            print("Invalid value. The value must be a 1D list")

filename = "test.sta"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

def Encode(filename: str, STAKeyValues):
    try:
        f = open(file_path, "x")
    except:
        print(f"{file_path} is already created")
        f = open(file_path, "w")


    f.write(f"[{filename}]\n")

    for x in STAKeyValues:
        f.write(f"+ {x.key_name}\n")

        for value in x.values:
            f.write(f"- {value}\n")
    
    f.write("= END\n") 
    f.close()

def Decode(filename):
    STAKeyValues = []
    
    try:
        with open(filename, "r") as f:
            current_key = None
            current_values = []

            for line in f:
                line = line.strip()  # Remove leading and trailing whitespace
                
                if line.startswith("[") and line.endswith("]"):
                    print(f"Decoding {filename}")  

                if line.startswith("+ "):
                    if current_key is not None: 
                        STAKeyValues.append({"key_name": current_key, "values": current_values})
                    current_key = line[2:]  
                    current_values = []  

                elif line.startswith("- ") and current_key is not None:
                    current_values.append(line[2:]) 

            if current_key is not None:
                STAKeyValues.append({"key_name": current_key, "values": current_values})

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    
    return STAKeyValues


test_KeyValue = STAKeyValue("Test",["Hello","hi"])

Encode("Test",[test_KeyValue])
print(Decode(file_path))