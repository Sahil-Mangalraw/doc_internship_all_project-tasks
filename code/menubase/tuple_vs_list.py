import sys
import time
import memory_profiler

def demonstrate_tuple_vs_list():
    """Demonstrate the differences between tuples and lists"""
    print("=" * 60)
    print("📚 TUPLE vs LIST COMPARISON")
    print("=" * 60)
    
    print("\n🔍 TECHNICAL DIFFERENCES:")
    print("=" * 40)
    
    # 1. Mutability
    print("\n1️⃣  MUTABILITY:")
    print("-" * 20)
    
    # List - Mutable
    my_list = [1, 2, 3, 4, 5]
    print(f"📝 List (mutable): {my_list}")
    my_list[0] = 10
    print(f"📝 After modification: {my_list}")
    
    # Tuple - Immutable
    my_tuple = (1, 2, 3, 4, 5)
    print(f"📋 Tuple (immutable): {my_tuple}")
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print(f"❌ Error modifying tuple: {e}")
    
    # 2. Syntax
    print("\n2️⃣  SYNTAX:")
    print("-" * 20)
    print("📝 List: [1, 2, 3] or list([1, 2, 3])")
    print("📋 Tuple: (1, 2, 3) or tuple([1, 2, 3])")
    
    # 3. Memory Usage
    print("\n3️⃣  MEMORY USAGE:")
    print("-" * 20)
    
    # Create large collections
    large_list = list(range(1000))
    large_tuple = tuple(range(1000))
    
    list_size = sys.getsizeof(large_list)
    tuple_size = sys.getsizeof(large_tuple)
    
    print(f"📝 List size: {list_size} bytes")
    print(f"📋 Tuple size: {tuple_size} bytes")
    print(f"💾 Difference: {list_size - tuple_size} bytes")
    
    # 4. Performance
    print("\n4️⃣  PERFORMANCE:")
    print("-" * 20)
    
    # Creation time
    start_time = time.time()
    for _ in range(10000):
        list(range(100))
    list_creation_time = time.time() - start_time
    
    start_time = time.time()
    for _ in range(10000):
        tuple(range(100))
    tuple_creation_time = time.time() - start_time
    
    print(f"📝 List creation time: {list_creation_time:.4f} seconds")
    print(f"📋 Tuple creation time: {tuple_creation_time:.4f} seconds")
    print(f"⚡ Tuple is {list_creation_time/tuple_creation_time:.2f}x faster")
    
    # 5. Methods and Operations
    print("\n5️⃣  METHODS AND OPERATIONS:")
    print("-" * 20)
    
    print("📝 List methods:")
    list_methods = [method for method in dir(list) if not method.startswith('_')]
    print(f"   Available methods: {len(list_methods)}")
    print(f"   Methods: {', '.join(list_methods[:10])}...")
    
    print("\n📋 Tuple methods:")
    tuple_methods = [method for method in dir(tuple) if not method.startswith('_')]
    print(f"   Available methods: {len(tuple_methods)}")
    print(f"   Methods: {', '.join(tuple_methods)}")
    
    # 6. Use Cases
    print("\n6️⃣  USE CASES:")
    print("-" * 20)
    
    print("📝 Lists are best for:")
    print("   - Collections that need to be modified")
    print("   - Dynamic data structures")
    print("   - When you need to add/remove elements")
    print("   - Building collections incrementally")
    
    print("\n📋 Tuples are best for:")
    print("   - Fixed collections of data")
    print("   - Data that shouldn't change")
    print("   - Dictionary keys (immutable requirement)")
    print("   - Function return values")
    print("   - Performance-critical code")
    
    # 7. Practical Examples
    print("\n7️⃣  PRACTICAL EXAMPLES:")
    print("-" * 20)
    
    # Coordinates
    print("📍 Coordinates (tuple):")
    point = (10, 20)
    x, y = point  # Unpacking
    print(f"   Point: {point}, x={x}, y={y}")
    
    # RGB Colors
    print("\n🎨 RGB Colors (tuple):")
    color = (255, 128, 0)
    r, g, b = color
    print(f"   Color: {color}, R={r}, G={g}, B={b}")
    
    # Shopping List
    print("\n🛒 Shopping List (list):")
    shopping = ["apples", "bananas", "milk"]
    print(f"   Initial: {shopping}")
    shopping.append("bread")
    print(f"   After adding: {shopping}")
    shopping.remove("bananas")
    print(f"   After removing: {shopping}")
    
    # 8. Advanced Differences
    print("\n8️⃣  ADVANCED DIFFERENCES:")
    print("-" * 20)
    
    # Nested structures
    print("📊 Nested Structures:")
    nested_list = [[1, 2], [3, 4]]
    nested_tuple = ((1, 2), (3, 4))
    
    print(f"   Nested list: {nested_list}")
    print(f"   Nested tuple: {nested_tuple}")
    
    # Dictionary keys
    print("\n🔑 Dictionary Keys:")
    try:
        list_dict = {[1, 2]: "value"}
    except TypeError as e:
        print(f"   ❌ List as key: {e}")
    
    tuple_dict = {(1, 2): "value"}
    print(f"   ✅ Tuple as key: {tuple_dict}")
    
    # 9. Memory Profiling
    print("\n9️⃣  MEMORY PROFILING:")
    print("-" * 20)
    
    def create_list():
        return [i for i in range(1000)]
    
    def create_tuple():
        return tuple(i for i in range(1000))
    
    print("📊 Memory usage comparison:")
    print("   (Note: Memory profiling requires memory_profiler package)")
    
    # 10. Best Practices
    print("\n🔟 BEST PRACTICES:")
    print("-" * 20)
    
    print("✅ When to use Lists:")
    print("   - When you need to modify the collection")
    print("   - For building collections dynamically")
    print("   - When you need list-specific methods")
    print("   - For mutable data structures")
    
    print("\n✅ When to use Tuples:")
    print("   - For fixed collections of data")
    print("   - When you need immutability")
    print("   - For better performance")
    print("   - As dictionary keys")
    print("   - For function return values")
    print("   - When data shouldn't change")
    
    # 11. Conversion
    print("\n🔄 CONVERSION:")
    print("-" * 20)
    
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (1, 2, 3, 4, 5)
    
    print(f"📝 List to tuple: {tuple(my_list)}")
    print(f"📋 Tuple to list: {list(my_tuple)}")
    
    # 12. Summary
    print("\n📋 SUMMARY:")
    print("=" * 40)
    
    print("🔍 Key Differences:")
    print("   • Lists are mutable, tuples are immutable")
    print("   • Lists use [], tuples use ()")
    print("   • Tuples are more memory efficient")
    print("   • Tuples are faster to create")
    print("   • Lists have more methods")
    print("   • Tuples can be dictionary keys")
    print("   • Lists are better for dynamic data")
    print("   • Tuples are better for fixed data")

def interactive_comparison():
    """Interactive comparison tool"""
    print("\n" + "=" * 60)
    print("🎯 INTERACTIVE COMPARISON TOOL")
    print("=" * 60)
    
    while True:
        print("\nChoose an option:")
        print("1. Test mutability")
        print("2. Compare memory usage")
        print("3. Test performance")
        print("4. Show methods")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            test_mutability()
        elif choice == "2":
            compare_memory()
        elif choice == "3":
            test_performance()
        elif choice == "4":
            show_methods()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")

def test_mutability():
    """Test mutability differences"""
    print("\n🧪 MUTABILITY TEST:")
    print("-" * 30)
    
    # List test
    print("📝 Testing List (mutable):")
    my_list = [1, 2, 3]
    print(f"   Original: {my_list}")
    my_list.append(4)
    print(f"   After append: {my_list}")
    my_list[0] = 10
    print(f"   After modification: {my_list}")
    
    # Tuple test
    print("\n📋 Testing Tuple (immutable):")
    my_tuple = (1, 2, 3)
    print(f"   Original: {my_tuple}")
    try:
        my_tuple.append(4)
    except AttributeError as e:
        print(f"   ❌ Cannot append: {e}")
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print(f"   ❌ Cannot modify: {e}")

def compare_memory():
    """Compare memory usage"""
    print("\n💾 MEMORY COMPARISON:")
    print("-" * 30)
    
    sizes = [10, 100, 1000, 10000]
    
    for size in sizes:
        list_obj = list(range(size))
        tuple_obj = tuple(range(size))
        
        list_size = sys.getsizeof(list_obj)
        tuple_size = sys.getsizeof(tuple_obj)
        
        print(f"Size {size}:")
        print(f"   List: {list_size} bytes")
        print(f"   Tuple: {tuple_size} bytes")
        print(f"   Difference: {list_size - tuple_size} bytes")

def test_performance():
    """Test performance differences"""
    print("\n⚡ PERFORMANCE TEST:")
    print("-" * 30)
    
    iterations = 10000
    size = 100
    
    # List creation
    start_time = time.time()
    for _ in range(iterations):
        list(range(size))
    list_time = time.time() - start_time
    
    # Tuple creation
    start_time = time.time()
    for _ in range(iterations):
        tuple(range(size))
    tuple_time = time.time() - start_time
    
    print(f"📝 List creation: {list_time:.4f} seconds")
    print(f"📋 Tuple creation: {tuple_time:.4f} seconds")
    print(f"⚡ Tuple is {list_time/tuple_time:.2f}x faster")

def show_methods():
    """Show available methods"""
    print("\n🔧 AVAILABLE METHODS:")
    print("-" * 30)
    
    print("📝 List methods:")
    list_methods = [method for method in dir(list) if not method.startswith('_')]
    for method in list_methods:
        print(f"   • {method}")
    
    print("\n📋 Tuple methods:")
    tuple_methods = [method for method in dir(tuple) if not method.startswith('_')]
    for method in tuple_methods:
        print(f"   • {method}")

if __name__ == "__main__":
    demonstrate_tuple_vs_list()
    interactive_comparison() 