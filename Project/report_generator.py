def generate_summary(analysis):

    print("\n===== MEDICAL REPORT SUMMARY =====\n")

    for item in analysis:

        print(f"Test Name     : {item['test_name']}")
        print(f"Result        : {item['value']}")
        print(f"Status        : {item['status']}")
        print(f"Normal Range  : {item['normal_range']}")
        print("-" * 40)