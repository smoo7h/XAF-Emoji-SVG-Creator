import os
import shutil

# Define the paths
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_dir, 'fluentui-emoji-main', 'assets')
project_root = os.path.dirname(os.path.dirname(assets_dir))
output_dir = os.path.join(project_root, 'Emojis')

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Walk through the assets directory
for root, dirs, files in os.walk(assets_dir):
    # Check if current directory is a 'Flat' variant directory
    if os.path.basename(root) == 'Flat':
        for file in files:
            if file.endswith('.svg'):
                # Create new filename by removing '_flat'
                original_name = os.path.splitext(file)[0]
                new_name = original_name.replace('_flat', '') + '.svg'
                new_name = new_name.replace('_', ' ')
                # Define paths
                src_path = os.path.join(root, file)
                dest_path = os.path.join(output_dir, new_name)
                
                # Copy and rename the file
                shutil.copy2(src_path, dest_path)
                print(f'Copied: {file} -> {new_name}')

print(f'\nAll Flat emojis copied to: {output_dir}')