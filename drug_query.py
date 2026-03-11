# import necessary libraries and define constants for text formatting
import requests
BOLD = '\033[1m'
RESET = '\033[0m'
UNDERLINE = '\033[4m'

def search_drug(drug_name):
    """Function to request the drug's JSON file"""
    try:
        response = requests.get(f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}&limit=1")
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None
    

def extract_drug_info(drug_data):
    """Function to extract relevant information from the OpenFDA API response"""
    result = drug_data['results'][0]
    info = {
        'brand_name': result.get('openfda', {}).get('brand_name', ['N/A'])[0],
        'manufacturer_name': result.get('openfda', {}).get('manufacturer_name', ['N/A'])[0],
        'purpose': result.get('purpose', ['N/A'])[0],
        'indications_and_usage': result.get('indications_and_usage', ['N/A'])[0],
        'adverse_reactions': '\n'.join(result.get('adverse_reactions', ['N/A'])),
        'warnings': '\n'.join(result.get('warnings', ['N/A'])),
        'do_not_use': '\n'.join(result.get('do_not_use', ['N/A'])),
        'ask_doctor': '\n'.join(result.get('ask_doctor', ['N/A'])),
        'stop_use': '\n'.join(result.get('stop_use', ['N/A'])),
        'pregnancy': '\n'.join(result.get('pregnancy', ['N/A'])),
        'keep_out_of_reach_of_children': '\n'.join(result.get('keep_out_of_reach_of_children', ['N/A'])),
        'dosage_and_administration': result.get('dosage_and_administration', ['N/A'])[0],
        'storage_and_handling': result.get('storage_and_handling', ['N/A'])[0],
        'inactive_ingredient': '\n'.join(result.get('inactive_ingredient', ['N/A'])),
        'questions': result.get('questions', ['N/A'])[0],
        'generic_name': result.get('openfda', {}).get('generic_name', ['N/A'])[0],
        'route': result.get('openfda', {}).get('route', ['N/A'])[0]

    }
    return info

def display_info(info):
    """Function to display the drug's information"""
    print("\n-------------------- Drug Information --------------------")
    print("---------- Basic Information ----------")
    print(f"{BOLD}{UNDERLINE}Brand Name: {RESET}{info['brand_name']}")
    print(f"{BOLD}{UNDERLINE}Generic Name: {RESET}{info['generic_name']}")
    print(f"{BOLD}{UNDERLINE}Route: {RESET}{info['route']}")
    print(f"{BOLD}{UNDERLINE}Manufacturer Name: {RESET}{info['manufacturer_name']}")
    print(f"{BOLD}{UNDERLINE}Dosage and Administration: {RESET}{info['dosage_and_administration']}")
    print("------------- Usage -------------------")
    print(f"{BOLD}{UNDERLINE}Purpose: {RESET}{info['purpose']}")
    print(f"{BOLD}{UNDERLINE}Indications and Usage: {RESET}{info['indications_and_usage']}")
    print("--------- Safety Information ----------")
    print(f"{BOLD}{UNDERLINE}Warnings: {RESET}{info['warnings']}")
    print(f"{BOLD}{UNDERLINE}Do Not Use: {RESET}{info['do_not_use']}")
    print(f"{BOLD}{UNDERLINE}Stop Use: {RESET}{info['stop_use']}")
    print(f"{BOLD}{UNDERLINE}Pregnancy: {RESET}{info['pregnancy']}")
    print(f"{BOLD}{UNDERLINE}Keep Out of Reach of Children: {RESET}{info['keep_out_of_reach_of_children']}")
    print(f"{BOLD}{UNDERLINE}Adverse Reactions: {RESET}{info['adverse_reactions']}")
    print(f"{BOLD}{UNDERLINE}Ask Doctor: {RESET}{info['ask_doctor']}")
    print("-- Additional Information -------------")
    print(f"{BOLD}{UNDERLINE}Storage and Handling: {RESET}{info['storage_and_handling']}")
    print(f"{BOLD}{UNDERLINE}Inactive Ingredients: {RESET}{info['inactive_ingredient']}")
    print(f"{BOLD}{UNDERLINE}Questions: {RESET}{info['questions']}")
    print("----------------------------------------------------------")

def main():
    print("OpenFDA Drug Query")
    while True:
        drug_name = input("Enter drug name (or 'exit' to quit): ").strip()
        drug_name = drug_name.replace(" ", "+")
        if drug_name.lower() == 'exit':
            print("Thank you for using the OpenFDA Drug Query!")
            break
        try:
            drug_data = search_drug(drug_name)
            if drug_data is None:
                print("Drug not found or API error.")
                continue
            info = extract_drug_info(drug_data)
            display_info(info)
        except (KeyError, IndexError):
            print("Error occurred while parsing drug information.")
        

# Run the main function when the script is executed
main()