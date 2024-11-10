import logging
import random
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

def selection_sort(arr):
    logging.debug(f"Starting sorting the array using selection sort")
    start = time.time()

    n = len(arr)

    for i in range(n):
        min_element = arr[i]
        min_index = i
        for j in range(i+1,n):
            if min_element > arr[j]:
                min_element = arr[j]
                min_index = j

        arr[i],arr[min_index] = arr[min_index] ,arr[i]
    
    end = time.time()
    elapsed_time = end-start
    logging.info(f"Finished sorting the array using selection sort in {elapsed_time:.6f} seconds ")
    return (arr)

def bubble_sort(arr):
    logging.debug(f"Starting sorting the array using bubble sort")
    start = time.time()


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

    end = time.time()
    elapsed_time = end-start
    logging.info(f"Finished sorting the array using bubble sort in {elapsed_time:.6f} seconds")
    return (arr)


def main():
    random_num_list = [random.randint(1,100000) for _ in range(100000)]
    selection_sort(random_num_list.copy()) 
    selection_sort(random_num_list.copy()) 


if __name__ == "__main__":
    main()
