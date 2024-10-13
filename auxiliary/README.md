# RENDER

Libraries inside the render module use PyQt5, which doesn't have Python 3.12 support. Therefore, it is recommended to have a Python 3.11 or 3.10 virtual environment (venv) to run the following `animate.py` function; otherwise, a `ModuleNotFoundError` will be raised.

## Setting up the virtual environment and installing requirements

To set up a virtual environment and install the required packages, follow these steps:

1. Create a virtual environment:
    ```sh
    python3.11 -m venv venv
    ```

2. Activate the virtual environment:
    - On Linux/Mac:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Handling .bds files

Most of the files in the SPICE kernel are in .bds format. While using the animate function, using .bds files directly may cause an error. It is recommended to use the SPICE toolkit named [`dskexp`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fastavak%2Fpython%2FAnimations%2Fauxiliary%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A189%7D%7D%5D%2C%2250652d94-2251-47ba-a20c-8a6beb58d21a%22%5D "Go to definition") to convert the file to .obj, save it locally, and then render it.

Example command:
```sh
dskexp -dsk didymos_g_04657mm_spc_0000n00000_v003.bds -text didymos_g_04657mm_spc_0000n00000_v003.obj -format obj -pec 10