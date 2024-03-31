#!/bin/bash

# Function to create virtual environment
create_venv() {
    python_version=$1
    venv_name=$2
    python${python_version} -m venv ${venv_name}
    echo "Virtual environment '${venv_name}' created successfully with Python ${python_version}."
}

# Function to activate virtual environment
activate_env() {
    venv_name=$1
    source ./${venv_name}/bin/activate
    echo "Virtual environment '${venv_name}' activated."
}

# Function to install packages
install_packages() {
    venv_name=$1
    pip install numpy==1.21.5
    pip install scipy==1.7.3
    pip install matplotlib==3.4.3
    pip install pandas==1.3.3
    pip install seaborn==0.11.2
    pip install scikit-learn==0.24.2
    pip install yapf==0.40.2
}

# Function to install PyTorch (CPU or GPU version)
install_pytorch() {
    venv_name=$1
    use_gpu=$2
    if [ $use_gpu -eq 1 ]; then
        pip install torch==1.10.0+cu113
    else
        pip install torch==1.10.0
    fi
}

# Define virtual environment name and Python version
venv_name="minimal_ds"
python_version="3.9"

# Check if virtual environment exists
if [ -d "${venv_name}" ]; then
    echo "Virtual environment '${venv_name}' found."
    # Activate virtual environment
    activate_env $venv_name
else
    # Create virtual environment
    create_venv $python_version $venv_name
    # Activate virtual environment
    activate_env $venv_name

    # Prompt user to choose CPU or GPU version of PyTorch
    read -p "Do you want to install GPU version of PyTorch? (y/n): " gpu_choice
    if [ "$gpu_choice" == "y" ]; then
        use_gpu=1
    else
        use_gpu=0
    fi

    # Install packages
    install_packages $venv_name

    # Install PyTorch
    install_pytorch $venv_name $use_gpu
fi

echo -e "\nVirtual environment setup complete."