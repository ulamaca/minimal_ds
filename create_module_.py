import os

USER_MODE = False


# User input for custom names
# level1 = input("Enter name for level1: ")
# level2 = input("Enter name for level2: ")
# level3 = input("Enter name for level3: ")
# tools_filename = input("Enter filename for 'tools' (without .py): ")
# cools_filename = input("Enter filename for 'cools' (without .py): ")
# function1_name = input("Enter function name for 'xxx': ")
# function2_name = input("Enter function name for 'yyy': ")
level1 = 'digital_peptides'
level2 = 'repr'
level3 = 'str'
tools_filename = 'sequence'
cools_filename = 'smiles'
function1_name = 'convert_to_sequence'
function2_name = 'convert_to_smiles'

# Creating directories
os.makedirs(f"{level1}/{level2}/{level3}", exist_ok=True)

# Creating and writing to __init__.py files with guiding comments
init_paths = [
    f"{level1}/__init__.py",
    f"{level1}/{level2}/__init__.py",
    f"{level1}/{level2}/{level3}/__init__.py"
]

for path in init_paths:
    with open(path, 'w') as f:
        if level3 in path:
            f.write(f"# Expose functions from modules within {level3}.\n")
            f.write(f"from .{tools_filename} import {function1_name}\n")
            f.write(f"from .{cools_filename} import {function2_name}\n")
            f.write("\n# Add more imports here if you want to expose more functions from this level.")
        elif level2 in path:
            f.write(f"# Expose functions from {level3} at the {level2} package level.\n")
            f.write(f"from .{level3}.{tools_filename} import {function1_name}\n")
            f.write(f"from .{level3}.{cools_filename} import {function2_name}\n")
            f.write("\n# Add more imports here if you want to expose more functions from deeper levels.")
        else:
            f.write(f"# This is the top-level package file for {level1}.\n")
            f.write("# Import sub-packages or modules here if you want to expose them at the package level.")
            f.write("\n# For example, to expose a function from level2/level3/tools.py directly:")
            f.write("\n# from .level2.level3.tools import some_function")

# Creating tools.py and cools.py with function definitions
with open(f"{level1}/{level2}/{level3}/{tools_filename}.py", 'w') as f:
    f.write(f"def {function1_name}():\n")
    f.write(f"    print('Function {function1_name} from {tools_filename}.py')\n")

with open(f"{level1}/{level2}/{level3}/{cools_filename}.py", 'w') as f:
    f.write(f"def {function2_name}():\n")
    f.write(f"    print('Function {function2_name} from {cools_filename}.py')\n")

print("Folder structure and files have been created with guiding comments.")