import subprocess
import stat
import sys
import os

def create_venv(venv_name, python_version):
    """
    Create a virtual environment with the given name and Python version.
    """
    try:
        subprocess.check_call(["python" + python_version, "-m", "venv", venv_name])
        print(f"Virtual environment '{venv_name}' created successfully with Python {python_version}.")
    except subprocess.CalledProcessError:
        print("Error occurred while creating virtual environment.")
        sys.exit(1)

def install_packages(venv_name, packages):
    """
    Install specified packages in the virtual environment.
    """
    try:
        subprocess.check_call([os.path.join(venv_name, "bin", "pip"), "install"] + packages)
        print("Packages installed successfully.")
    except subprocess.CalledProcessError:
        print("Error occurred while installing packages.")
        sys.exit(1)

def activate_env(venv_name):
    """
    Activate the virtual environment.
    """
    activate_script = os.path.join(venv_name, "bin", "activate")

    try:
        #subprocess.check_call(["source", activate_script], shell=True)
        os.chmod(activate_script, os.stat(activate_script).st_mode | stat.S_IEXEC)
        subprocess.check_call([activate_script], shell=True)
        print(f"Virtual environment '{venv_name}' activated.")
    except subprocess.CalledProcessError:
        print("Error occurred while activating virtual environment.")
        sys.exit(1)

def main():
    # Define virtual environment name
    venv_name = "minimal_ds"

    # Define Python version (default to 3.9)
    python_version = "3.9"
    
    if not os.path.exists(f'./{venv_name}'):
        # Prompt user to choose CPU or GPU version
        torch_variant = input("Choose PyTorch variant (CPU/GPU): ").lower().strip()
        while torch_variant not in ["cpu", "gpu"]:
            print("Invalid input! Please choose either 'cpu' or 'gpu'.")
            torch_variant = input("Choose PyTorch variant (CPU/GPU): ").lower().strip()

        # Specify packages to install with recommended stable versions
        if torch_variant == "gpu":
            torch_package = "torch==1.10.0+cu113"
        else:
            torch_package = "torch==1.10.0"

        packages = [
            "numpy==1.21.5",
            "scipy==1.7.3",
            "matplotlib==3.4.3",
            "pandas==1.3.3",
            "seaborn==0.11.2",
            "scikit-learn==0.24.2",
            torch_package
        ]

        # Create virtual environment if it doesn't exist
        if not os.path.exists(venv_name):
            create_venv(venv_name, python_version)

        # Install packages
        install_packages(venv_name, packages)
        activate_env(venv_name)
        print("\nVirtual environment setup complete.")

    else:
        # Activate the virtual environment
        print("Virtual environment found, activate it")
        activate_env(venv_name)



if __name__ == "__main__":
    main()