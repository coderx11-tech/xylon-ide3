import os

def compile_xlyon_code(code):
    # Stub: In future, parse/transpile Xlyon to Python here
    print("Compiling Xlyon code...")
    print(code)
    return code

def run_xlyon_code(code, output_callback=print):
    py_code = compile_xlyon_code(code)
    try:
        exec(py_code, {"print": output_callback})
    except Exception as e:
        output_callback(f"Error running code: {e}")

def find_xlyon_files(root_dir):
    xly_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.xly'):
                xly_files.append(os.path.join(dirpath, filename))
    return xly_files

def run_folder(root_dir, output_callback=print):
    files = find_xlyon_files(root_dir)
    if not files:
        output_callback(f"No .xly files found in {root_dir}")
        return
    for file_path in files:
        output_callback(f"Running Xlyon file: {file_path}")
        with open(file_path) as f:
            code = f.read()
        run_xlyon_code(code, output_callback)
