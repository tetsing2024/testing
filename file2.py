#!/usr/bin/env python3

from complex_buggy_code_clean import DataProcessor, validate_user_data, calculate_statistics, process_file_content

def test_data_processor():
    print("=== Testing DataProcessor ===")
    
    # Test 1: Division by zero
    processor = DataProcessor('nonexistent_file.json')
    try:
        avg = processor.calculate_average([])
        print(f"Average of empty list: {avg}")
    except ZeroDivisionError as e:
        print(f"✓ Caught ZeroDivisionError: {e}")
    
    # Test 2: KeyError in process_items
    test_items = [
        {'id': 1, 'name': 'Item 1', 'value': 10},
        {'id': 2, 'name': 'Item 2', 'value': 20},
        {'id': 3, 'value': 30},  # Missing 'name'
        {'id': 4, 'name': 'Item 4', 'value': 'invalid'}  # Non-numeric value
    ]
    
    try:
        processed = processor.process_items(test_items)
        print(f"Processed items: {len(processed)}")
    except KeyError as e:
        print(f"✓ Caught KeyError: {e}")
    except TypeError as e:
        print(f"✓ Caught TypeError: {e}")
    
    # Test 3: Cache bug
    processor.update_cache('test_key', {'data': 'test_value'})
    cached_item = processor.get_cached_item('test_key')
    print(f"Cached item: {cached_item}")  # Should return {'key': 'test_key'} instead of actual data

def test_validation():
    print("\n=== Testing Validation ===")
    
    # Test 1: Valid user
    valid_user = {'name': 'John', 'age': 25, 'email': 'john@example.com'}
    result = validate_user_data(valid_user)
    print(f"Valid user result: {result}")
    
    # Test 2: Invalid user (negative age)
    invalid_user = {'name': 'John', 'age': -5, 'email': 'john@example.com'}
    result = validate_user_data(invalid_user)
    print(f"Invalid user (negative age) result: {result}")
    
    # Test 3: Invalid email
    invalid_email_user = {'name': 'John', 'age': 25, 'email': 'invalid-email'}
    result = validate_user_data(invalid_email_user)
    print(f"Invalid email user result: {result}")

def test_statistics():
    print("\n=== Testing Statistics ===")
    
    # Test with even-length list
    numbers = [1, 2, 3, 4, 5, 6]
    stats = calculate_statistics(numbers)
    print(f"Statistics for {numbers}:")
    print(f"  Count: {stats['count']}")
    print(f"  Sum: {stats['sum']}")
    print(f"  Mean: {stats['mean']}")
    print(f"  Median: {stats['median']} (should be 3.5)")
    print(f"  Variance: {stats['variance']}")
    print(f"  Std Dev: {stats['std_dev']} (should be sqrt of variance)")
    print(f"  Min: {stats['min']}")
    print(f"  Max: {stats['max']}")
    
    # Test with odd-length list
    numbers_odd = [1, 2, 3, 4, 5]
    stats_odd = calculate_statistics(numbers_odd)
    print(f"\nStatistics for {numbers_odd}:")
    print(f"  Median: {stats_odd['median']} (should be 3)")

def test_empty_statistics():
    print("\n=== Testing Empty Statistics ===")
    
    # Test with empty list
    stats = calculate_statistics([])
    print(f"Empty list statistics: {stats}")  # Should return consistent structure

if __name__ == "__main__":
    test_data_processor()
    test_validation()
    test_statistics()
    test_empty_statistics() 
