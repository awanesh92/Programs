import re
import argparse

# Define a dictionary to store instance counts
instance_counts = {}

# Define a function to parse the netlist file and count instances
def parse_netlist(file_path, target_hierarchy):
  with open(file_path, 'r') as file:
    content = file.read()

  instance_definitions = re.findall(r'\w+\s+(\w+)\s+\(.+?\);', content)
  print(instance_definitions)
  hierarchy = [target_hierarchy]

  def process_instance(definition):
    module_name = definition
    for h in hierarchy:
      module_name = h + "." + module_name
      if module_name in instance_counts:
        instance_counts[module_name] += 1
      else:
        instance_counts[module_name] = 1

  for definition in instance_definitions:
    process_instance(definition)

# Create an argument parser
parser = argparse.ArgumentParser(description="Count instances in a netlist file.")

# Add the file path argument
parser.add_argument("file_path", help="Path to the netlist.txt file.")
parser.add_argument("target_hierarchy", help="Name of the hierarchy to count instances.")

# Parse the command-line arguments
args = parser.parse_args()

# Call the parse_netlist function with the provided file path and target hierarchy
parse_netlist(args.file_path, args.target_hierarchy)

# Output the instance counts
for module, count in instance_counts.items():
  print(f"{module} : {count} placements")
