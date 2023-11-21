import re
import argparse

# Define a dictionary to store hierarchical structure
hierarchical_structure = {}

# Define a function to parse the netlist file and build hierarchical structure
def parse_netlist(file_path, target_hierarchy):
  with open(file_path, 'r') as file:
    content = file.read()

  instance_definitions = re.findall(r'\w+\s+(\w+)\s+\(.+?\);', content)
  hierarchy = [target_hierarchy]

  def process_instance(definition):
    module_name = definition
    current_hierarchy = hierarchical_structure
    for idx, h in enumerate(hierarchy):
      if h not in current_hierarchy:
        current_hierarchy[h] = {}
      current_hierarchy = current_hierarchy[h]
      module_name = h + "." + module_name
      if idx == len(hierarchy) - 1:
        current_hierarchy[module_name] = {}
      else:
        current_hierarchy[module_name] = {}
    hierarchy.append(definition)

  for definition in instance_definitions:
    process_instance(definition)

# Create an argument parser
parser = argparse.ArgumentParser(description="Build hierarchical structure of a netlist file.")

# Add the file path argument
parser.add_argument("file_path", help="Path to the netlist.txt file.")
parser.add_argument("target_hierarchy", help="Name of the hierarchy to build the structure.")

# Parse the command-line arguments
args = parser.parse_args()

# Call the parse_netlist function with the provided file path and target hierarchy
parse_netlist(args.file_path, args.target_hierarchy)

# Output the hierarchical structure in a more formatted way
import json
formatted_structure = json.dumps(hierarchical_structure, indent=4)
print(formatted_structure)
