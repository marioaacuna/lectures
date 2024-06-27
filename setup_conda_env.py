import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")
        sys.exit(1)

def create_conda_env(env_file):
    print(f"Creating Conda environment from {env_file}...")
    run_command(f"conda env create -f {env_file}")

def main():
    # Directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the environment.yml file
    env_file = os.path.join(script_dir, "environment.yaml")

    create_conda_env(env_file)

    print("\nEnvironment setup complete!")
    print("To activate the Conda environment:")
    print("    conda activate lectures_env")
    print("\nTo run a specific lecture script, navigate to its folder and run:")
    print("    python script_name.py")

if __name__ == "__main__":
    main()