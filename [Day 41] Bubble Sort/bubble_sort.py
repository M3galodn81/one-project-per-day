import random

def bubble_sort(arr):
    n = len(arr)
    
    unsorted = True
    while unsorted:
        swap_count = 0
        for i in range(n):
            if i+1 == n:
                break
            
            temp = 0
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap_count += 1
        
        if swap_count > 0:
            continue
        else:
            break

    return (arr)

def main():
    print(bubble_sort([5,6,2,3,4]))

    random_num_list = [random.randint(1,100) for _ in range(100)]
    print(f"Before sorting: {random_num_list}")

    print(f"After sorting: {bubble_sort(random_num_list)}")

if __name__ == "__main__":
    main()