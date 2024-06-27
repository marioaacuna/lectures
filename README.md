# Lectures Repository

This repository contains materials for various lecture topics, including interactive scripts and demonstrations. It's designed to provide a consistent environment for running lecture-specific scripts across different topics.

## Repository Structure

```
Lectures/
│
├── environment.yml
├── setup_conda_env.py
│
├── BasicPhysiology/
│   ├── syn_transmission_GUI.py
│   └── other_basic_physiology_scripts.py
│
├── Blank_yet/
│   └── blank_yet_script.py
│
└── README.md
```

Each lecture topic has its own directory containing specific scripts and materials.

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system.

## Setup Instructions

1. Clone this repository to your local machine:
   ``` bash
   git clone https://github.com/marioaacuna/Lectures.git
   cd Lectures
   ```

2. Create and activate the Conda environment:
   ```bash
   python setup_conda_env.py
   conda activate lectures_env
   ```

   This will create a Conda environment named `lectures_env` with all necessary dependencies.

## Running Lecture Scripts

After setting up and activating the environment, you can run specific lecture scripts:

1. Navigate to the lecture folder:
   ```bash
   cd BasicsPhysiology
   ```

2. Run the desired script:
   ```bash
   python syn_transmission_GUI.py
   ```

## Updating the Environment

If there are updates to the `environment.yml` file, you can update your existing environment:

```bash
conda env update -f environment.yml --prune
```

## Adding New Dependencies

If you need to add new dependencies:

1. Add the package to the `environment.yml` file.
2. Run the update command mentioned above.

## Troubleshooting

If you encounter any issues:
- Ensure Conda is correctly installed and accessible from your command line.
- Make sure you're in the correct directory when running scripts.
- Check that you've activated the `lectures_env` environment.

## Contributing

If you're contributing to this repository, please ensure any new scripts are placed in the appropriate lecture folder and any new dependencies are added to the `environment.yml` file.

## Contact

For any questions or issues, please [open an issue](https://github.com/your-username/Lectures/issues) on this repository.