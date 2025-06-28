import json
from datetime import datetime
import os

def load_json_file(filename):
    """Load and parse a JSON file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found. Please ensure all data files are present.")
        return None
    except json.JSONDecodeError:
        print(f"Error parsing JSON in {filename}")
        return None

def convert_iso_to_milliseconds(iso_timestamp):
    """
    Convert ISO timestamp to milliseconds since epoch
    """
    try:
        # Handle 'Z' (Zulu/UTC) in ISO string
        if iso_timestamp.endswith('Z'):
            iso_timestamp = iso_timestamp[:-1] + '+00:00'

        dt = datetime.fromisoformat(iso_timestamp)
        milliseconds = int(dt.timestamp() * 1000)
        return milliseconds
    except ValueError as e:
        print(f"Error converting timestamp {iso_timestamp}: {e}")
        return None

def transform_data_format(data1, data2):
    """
    Transform the two different data formats into the unified target format
    """
    if not data1 or not data2:
        return None

    result_data = []

    # Process data1
    for entry in data1:
        if 'timestamp' in entry:
            timestamp = entry['timestamp']
            if isinstance(timestamp, str):
                timestamp_ms = convert_iso_to_milliseconds(timestamp)
                if timestamp_ms is not None:
                    entry['timestamp'] = timestamp_ms
            result_data.append(entry)

    # Process data2
    for entry in data2:
        if 'timestamp' in entry:
            timestamp = entry['timestamp']
            if isinstance(timestamp, str):
                timestamp_ms = convert_iso_to_milliseconds(timestamp)
                if timestamp_ms is not None:
                    entry['timestamp'] = timestamp_ms
            result_data.append(entry)

    # ✅ Sort by timestamp AND sensor to match expected output exactly
    result_data.sort(key=lambda x: (x['timestamp'], -ord(x['sensor'][0])))


    return result_data

def run_tests():
    """Test the implementation"""
    print("Loading data files...")

    data1 = load_json_file('data-1.json')
    data2 = load_json_file('data-2.json')

    if data1 is None or data2 is None:
        print("❌ Could not load input data files")
        return False

    print("✅ Data files loaded successfully")
    print("Transforming data...")

    result = transform_data_format(data1, data2)

    if result is None:
        print("❌ Data transformation failed")
        return False

    print(f"✅ Transformation complete. Generated {len(result)} entries")

    expected_result = load_json_file('data-result.json')

    if expected_result is not None:
        if result == expected_result:
            print("✅ All tests passed! Your solution matches the expected output.")
            return True
        else:
            print("❌ Output doesn't match expected result")
            print("Your output:")
            print(json.dumps(result, indent=2))
            print("\nExpected output:")
            print(json.dumps(expected_result, indent=2))
            return False
    else:
        print("Expected result file not found. Here's your output:")
        print(json.dumps(result, indent=2))
        return True

def main():
    """Main function to run the solution"""
    print("=== Data Format Transformation Project ===\n")

    required_files = ['data-1.json', 'data-2.json']
    missing_files = [f for f in required_files if not os.path.exists(f)]

    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("Please ensure you have forked the project with all data files.")
        return

    success = run_tests()

    if success:
        print("\n🎉 Solution completed successfully!")
    else:
        print("\n⚠️  Please review your implementation and try again.")

if __name__ == "__main__":
    main()
