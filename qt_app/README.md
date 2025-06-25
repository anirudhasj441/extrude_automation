## Dependencies
- CMake 
- Make
- Python v3.12


## Steps to run
1. Create and activate virtual environment
    ```bash 
    python -m venv .venv
    ```
    ```bash
    .venv/Scripts/activate.bat
    ```
2. Install python packages
    ```bash
    pip install -r requirements.txt
    ```

1. Craete a build folder open cmd in build forlder to compile ui and rcc files run following commands
    ```bash
    cmake ..
    ```
    ```bash
    make 
    ```

1. Run the app
    ```bash
    python src/main.py
    ```