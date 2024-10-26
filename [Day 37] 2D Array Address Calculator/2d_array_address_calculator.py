def row_major_system(bassAddress,weight,rows,target_X_index,target_Y_index):
    return bassAddress + weight * (rows* target_X_index + target_Y_index)

def column_major_system(bassAddress,weight,cols,target_X_index,target_Y_index):
    return bassAddress + weight * (cols* target_Y_index + target_X_index)

def main():
    print(row_major_system(10,1,4,3,2))
    print(column_major_system(10,1,4,3,2))


if __name__ == "__main__":
    main()