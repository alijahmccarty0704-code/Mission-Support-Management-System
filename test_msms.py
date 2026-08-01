import unittest
import msms

class TestMsms(unittest.TestCase):

    def test_equipment_id_exists(self):
        fake_inventory = [{"id": "LT860404850", "name": "Laptop", "category": "Desktop Hardware", "status": "Assigned", "location": "Hangar 4"}, {"id": "8694958", "name": "DT95069840949", "category": "Desktop", "status": "Maintenance", "location": "Hangar A"}, {"id": "EQ-NEW-1", "name": "Tablet", "category": "IT", "status": "Available", "location": "Office B"}]

        id_exists = msms.equipment_id_exists(fake_inventory, "LT860404850")

        self.assertTrue(id_exists)


    def test_equipment_id_missing(self):
        fake_inventory = [{"id": "LT860404850", "name": "Laptop", "category": "Desktop Hardware", "status": "Assigned", "location": "Hangar 4"}, {"id": "8694958", "name": "DT95069840949", "category": "Desktop", "status": "Maintenance", "location": "Hangar A"}, {"id": "EQ-NEW-1", "name": "Tablet", "category": "IT", "status": "Available", "location": "Office B"}]

        id_missing = msms.equipment_id_exists(fake_inventory, "VM847AJDJ8GHGHJ")

        self.assertFalse(id_missing)


    def test_equipment_inventory_empty(self):
        fake_inventory = []

        empty_inventory = msms.equipment_id_exists(fake_inventory, "DTFHJ7875HFVBHVTV")

        self.assertFalse(empty_inventory)


    