import random

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_element = arr[i]
        min_index = i
        for j in range(i+1,n):
            if min_element > arr[j]:
                min_element = arr[j]
                min_index = j

        arr[i],arr[min_index] = arr[min_index] ,arr[i]
        
    return (arr)

def main():
    print(selection_sort([5,6,2,3,4]))
    print(selection_sort([64, 25, 12, 22, 11]))

    random_num_list = [random.randint(1,100) for _ in range(10)]
    print(f"Before sorting: {random_num_list}")

    print(f"After sorting: {selection_sort(random_num_list)}")

if __name__ == "__main__":
    main()