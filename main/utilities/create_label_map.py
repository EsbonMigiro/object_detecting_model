from .dir_creator import ProjectDirectoryManager

def create_label_map():
    labels = [{'name':'salmonella_typhi5', 'id':1}, {'name':'Vibrio_cholerae5', 'id':2}, {'name':'e.coli5', 'id':3}]
    
    try:
        # Write the label map to the file
        with open(ProjectDirectoryManager.files['LABELMAP'], 'w') as f:
            for label in labels:
                f.write('item { \n')
                f.write('\tname:\'{}\'\n'.format(label['name']))
                f.write('\tid:{}\n'.format(label['id']))
                f.write('}\n')
        
        # If no error occurred, print success
        print("success")
    except Exception as e:
        # Handle errors (e.g., file access issues)
        print(f"Error occurred: {e}")
