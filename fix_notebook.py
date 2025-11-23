import json

nb_path = r"c:/Users/juang/Documents/tn/first_class.ipynb"

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Get the first cell
cells = nb.get('cells', [])
if cells:
    first_cell = cells[0]
    source = first_cell.get('source', [])
    
    new_source = []
    for line in source:
        if line.strip() == "%matplotlib widget":
            new_source.append("# %matplotlib widget\n")
            new_source.append("try:\n")
            new_source.append("    get_ipython().run_line_magic('matplotlib', 'widget')\n")
            new_source.append("except:\n")
            new_source.append("    pass\n")
        else:
            new_source.append(line)
            
    first_cell['source'] = new_source

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
