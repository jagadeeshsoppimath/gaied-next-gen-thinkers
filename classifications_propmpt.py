import json


def create_classification_hierarchy_from_json(json_data):
    if not isinstance(json_data, dict):
        print("Error: Input must be a dictionary.")
        return []

    classification = "Classification Hierarchy List: "

    for type_name, subtypes in json_data.items():
        if not isinstance(subtypes, list):
            print(f"Error: Subtypes for Type '{type_name}' must be a list.")
            return []
        classification += f"\n• Request Type: {type_name}"
        for subtype in subtypes:
            classification += f"\n\t- Request Sub Type: {subtype}"
            
    return classification

def classify_request_type():
    json_data = {
        "Adjustment": [],
        "AU Transfer": [],
        "Closing Notice": ["Reallocation Fees", "Amendment Fees", "Reallocation Principal"],
        "Commitment Change": ["Cashless Roll", "Decrease", "Increase"],
        "Fee Payment": ["Ongoing Fee", "Letter of Credit Fee"],
        "Money Movment-Inbound": ["Principal", "Interest", "Principal and Interest", "Principal and Interest and Fees"],
        "Money Movment-Outbound": ["Timebound", "Foriegn Currency"]
    }

    return create_classification_hierarchy_from_json(json_data)
    

    # Classification Hierarchy:
    #     - Type: Adjustment
    #     - Type: AU Transfer
    #     - Type: Closing Notice
    #         - Subtype: Reallocation Fees
    #         - Subtype: Amendment Fees
    #         - Subtype: Reallocation Principal
    #     - Type: Commitment Change
    #         - Subtype: Cashless Roll
    #         - Subtype: Decrease
    #         - Subtype: Increase
    #     - Type: Fee Payment
    #         - Subtype: Ongoing Fee
    #         - Subtype: Letter of Credit Fee
    #     - Type: Money Movment-Inbound
    #         - Subtype: Principal
    #         - Subtype: Interest
    #         - Subtype: Principal and Interest
    #         - Subtype: Principal and Interest and Fees
    #     - Type: Money Movment-Outbound
    #         - Subtype: Timebound
    #         - Subtype: Foriegn Currency
