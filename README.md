# Xlyon IDE (GUI Version)

A simple IDE for the Xlyon language, supporting editing, running, and batch execution of `.xly` files in folders.

## Structure

```
xlyon_ide/
    __init__.py
    compiler.py
    gui.py
examples/
    hello.xly
main.py
README.md
requirements.txt
```

## Features

- Edit and run Xlyon code with a GUI.
- Save/load `.xly` files.
- Run all `.xly` files in a folder.
- View output/errors in an output pane.

## Usage

1. Install dependencies (see `requirements.txt`).
2. Run the IDE:

   ```
   python main.py
   ```

3. Use the menu to open, save, and run code. Use "Run All .xly Files in Folder..." to execute all Xlyon scripts in a directory.

## Notes

- The Xlyon language currently works as a Python superset. Compilation is a stub.
- Contributions for language parsing and more features are welcome!
