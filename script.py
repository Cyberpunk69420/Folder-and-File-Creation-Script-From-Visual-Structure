import os
import re

def create_project_structure(structure_text: str):
    """
    Creates a directory and file structure from a multi-line text string.

    This function is designed to be flexible and can handle variations in the
    tree-like formatting (e.g., different box-drawing characters, spacing).

    Args:
        structure_text: A string representing the project hierarchy.
    """
    lines = structure_text.strip().split('\n')
    path_stack = []
    last_depth = -1

    # Find the name of the root directory from the first line
    root_dir_name = lines[0].strip().replace('/', '')
    if not root_dir_name:
        print("Error: Could not determine the root directory from the first line.")
        return

    print(f"Creating root directory: {root_dir_name}")
    os.makedirs(root_dir_name, exist_ok=True)
    path_stack.append(root_dir_name)

    # Process the rest of the structure
    for line in lines[1:]:
        if not line.strip():
            continue

        # Regex to separate the prefix (for depth calculation) from the name
        match = re.match(r'^([\s│├└─]*)(\S.*)', line)
        if not match:
            continue
            
        prefix, name = match.groups()
        name = name.strip().replace('/', '')

        # Calculate depth based on the length of the prefix string
        # This is a robust way to handle different spacing/characters
        current_depth = len(prefix)

        # Adjust the path stack based on the current depth
        if current_depth > last_depth:
            # Going deeper into the hierarchy
            pass
        else:
            # Going up or staying at the same level
            # Pop items from the stack until we are at the correct parent level
            # Heuristic: roughly 4 chars per level is common
            levels_to_pop = (last_depth - current_depth) // 4 + 1
            for _ in range(levels_to_pop):
                if len(path_stack) > 1: # Don't pop the root
                    path_stack.pop()
        
        # Determine if it's a file or a directory
        # Simple check: if it has a common file extension, it's a file.
        is_file = '.' in name and not name.endswith('.')

        # Construct the full path
        current_path = os.path.join(*path_stack)
        item_path = os.path.join(current_path, name)

        if is_file:
            print(f"  Creating file: {item_path}")
            # Create an empty file
            open(item_path, 'a').close()
        else:
            print(f"Creating directory: {item_path}")
            os.makedirs(item_path, exist_ok=True)
            path_stack.append(name)

        last_depth = current_depth
        
    print("\n✅ Project structure created successfully!")


# --- HOW TO USE ---
# 1. Copy your project structure text and paste it inside the triple quotes below.
# 2. Run the script: python create_structure.py

project_hierarchy = """
dnd-survivors-frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ClassSelection.js
│   │   ├── Enemy.js
│   │   └── Player.js
│   ├── hooks/
│   │   └── usePlayerInput.js
│   ├── App.js
│   ├── index.css
│   └── index.js
└── package.json
"""

if __name__ == "__main__":
    create_project_structure(project_hierarchy)
