import os
import shutil

# Data output operations

def save_data(df, output_path, output_filename):
    # Data saving logic here
    file_path = os.path.join(output_path, output_filename)
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    
    df.write.csv(output_path, header=True)


    # Rename the part file
    for filename in os.listdir(output_path):
        if filename.startswith('part'):
            shutil.move(os.path.join(output_path, filename), os.path.join(output_path, output_filename))

