import json

def show_menu():
    print("Mission Support Management System:\n")
    print("1. Add equipment")
    print("2. List Equipment")
    print("3. Find Equipment by ID")
    print("4. Export Inventory Report")
    print("5. Exit")


def menu_input(user_input):

    if user_input.isdigit():
        user_input = int(user_input)
        return user_input


def get_valid_status():

    status_invalid = True
    while status_invalid:
        print("Available, Assigned, Maintenance, Retired")
        status_input = input("Please enter a valid status: ")
        if status_input.lower() == "available":
            return "Available"
        elif status_input.lower() == "assigned":
            return "Assigned"
        elif status_input.lower() == "maintenance":
            return "Maintenance"
        elif status_input.lower() == "retired":
            return "Retired"
        else:
            print("Invalid Status")
            continue


def equipment_id_exists(equipment_list, equipment_id):
    for item in equipment_list:
        if item["id"] == equipment_id:
            return True
    return False


def add_equipment(equipment_list):

    equipment_id = input("Enter in the equipment ID: ")
    if equipment_id_exists(equipment_list, equipment_id):
        print("Duplicate ID")
        return
    equipment_name = input("Enter in the equipment name: ")
    equipment_category = input("Enter in the equipment category: ")
    equipment_status = get_valid_status()
    equipment_location = input("Enter in the equipment location: ")

    equipment_record = {
        "id": equipment_id,
        "name": equipment_name,
        "category": equipment_category,
        "status": equipment_status,
        "location": equipment_location
    }

    equipment_list.append(equipment_record)
    print("Equipment Added")
    save_inventory(equipment_list)


def save_inventory(equipment_list):
    with open("equipment_inventory.json", "w") as file:
        json.dump(equipment_list, file)


def load_inventory():
    with open("equipment_inventory.json", "r") as file:
        contents = json.load(file)
        return contents


def display_equipment(item):
    print("ID:", item["id"])
    print("Name:", item["name"])
    print("Category:", item["category"])
    print("Status:", item["status"])
    print("Location:", item["location"])


def list_equipment(all_inventory):
    if all_inventory == []:
        print("No equipment listed")
        return
    else:
        for item in all_inventory:
            display_equipment(item)
        print("Inventory Count:", len(all_inventory))


def find_equipment_by_id(equipment_list):
    id_input = input("Equipment ID:")
    found = False

    for item in equipment_list:
        if item["id"] == id_input:
            display_equipment(item)
            found = True
    if found == False:
        print("Equipment ID not found")


def inventory_export_report(equipment_list):

    if equipment_list == []:
        print("No inventory to export.")
    else:
        with open("inventory_report.txt", "w") as file:
            file.write("Mission Support Management System\n")
            for item in equipment_list:
                file.write("ID: " + item["id"] + "\n")
                file.write("Name: " + item["name"] + "\n")
                file.write("Category: " + item["category"] + "\n")
                file.write("Status: " + item["status"] + "\n")
                file.write("Location: " + item["location"] + "\n")
                file.write("\n")
            file.write("Inventory count: " + str(len(equipment_list)) + "\n")
            print("Inventory report exported.")


def main():
    main_menu = True

    equipment_inventory = load_inventory()

    while main_menu:
        show_menu()

        menu_selection = input()

        menu_selection_input = menu_input(menu_selection)

        if menu_selection_input == 1:
            print("Add Equipment: \n")
            add_equipment(equipment_inventory)
        elif menu_selection_input == 2:
            list_equipment(equipment_inventory)
        elif menu_selection_input == 3:
            find_equipment_by_id(equipment_inventory)
        elif menu_selection_input == 4:
            print("Exporting inventory report...")
            inventory_export_report(equipment_inventory)
        elif menu_selection_input == 5:
            print("Goodbye!")
            return
        else:
            print("Please select a valid option....")


if __name__ == "__main__":
    main()
