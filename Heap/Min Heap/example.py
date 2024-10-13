from min_heap import MinHeap

def main():
    # Create a MinHeap with initial data
    initial_data = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    min_heap = MinHeap(initial_data)
    
    print("Initial Min Heap:")
    print(min_heap.heap)

    # Insert a new element
    min_heap.insert(4)
    print("\nAfter inserting 4:")
    print(min_heap.heap)

    # Remove the minimum element (root) multiple times
    print("\nRemoving elements:")
    for _ in range(5):
        removed = min_heap.remove()
        print(f"Removed: {removed}")
        print(f"Heap after removal: {min_heap.heap}")

    # Insert more elements
    new_elements = [1, 7, 8]
    print("\nInserting new elements:", new_elements)
    for elem in new_elements:
        min_heap.insert(elem)
        print(f"After inserting {elem}: {min_heap.heap}")

if __name__ == "__main__":
    main()
