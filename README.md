# ISM Data Science 2026

Welcome to the 2026 ISM data science course! This is the repository via which all course notebooks will be shared. You can also use this repository for homeworks.

## Quick Start

### Option 1: Local Setup (Recommended)

This option requires the most work on your part, but it will teach you how to set up a development environment that you will be able to use in projects to come.

1. Download and install [VS Code](https://code.visualstudio.com/download).
2. Open VS Code and click Clone Git Repository. Enter the URL to this repository: `https://github.com/harismck/ism-data-science-2026`. You might also have to [install Git](https://git-scm.com/install/) in order to complete this step.
3. Install recommended extensions (see below).
4. Open terminal or powershell in VS Code.
    - Mac: Cmd + Shift + P -> Create new terminal.
    - Windows: Ctrl + Shift + P -> Create new terminal (use powershell).
5. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) by pasting the relevant command into the terminal. Make sure to follow the instructions for your platform (Mac vs Windows).
6. Run `uv sync` in the terminal to install dependencies (might take a while). If the command does not work try restarting VS Code or your laptop.
7. Open `notebooks/lectures/01_intro/getting_started.ipynb` and run it.

### Option 2: GitHub Codespaces - Browser (Easiest)

This is the easiest option, as all computations happen remotely, so you do not need to set up any Python packages locally.

1. Click the green **Code** button above.
2. Select **Codespaces** tab.
3. Click **Create codespace on main**.
4. Wait for setup to complete.
5. Install recommended extensions (see below).
6. Open `notebooks/lectures/01_intro/getting_started.ipynb` and run it.

### Option 3: GitHub Codespaces in VS Code

This allows you to run on Codespaces but use your local VS Code editor.

1. Download and install [VS Code](https://code.visualstudio.com/download).
2. Follow Option 2, steps 1-5.
3. On GitHub, click the **...** menu next to your Codespace → **Open in Visual Studio Code**.
4. VS Code will prompt to install the Codespaces extension - click Install.
5. Open `notebooks/lectures/01_intro/getting_started.ipynb` and run it.

## VS Code Extensions

When you open this project, VS Code will prompt you to install recommended extensions. Click **Install All**.

If you don't see the prompt, install manually:
1. Open Command Palette (Cmd+Shift+P on Mac, Ctrl+Shift+P on Windows/Linux).
2. Run: `Extensions: Show Recommended Extensions`.
3. Click the cloud icon to install all.

## Workflow

Before and after lectures I will share notebooks with you. You will need to pull these notebooks into your local repository:

1. Open the Source Control panel (click the branch icon in the left sidebar, or Cmd+Shift+G / Ctrl+Shift+G).
2. Click the **...** menu (three dots) at the top of the panel.
3. Click **Pull**.

## Selecting the Python Kernel

When you open a notebook for the first time, VS Code will ask you to select an environment. Choose the project environment (marked with a star in the dropdown) from the list. You'll need to do this once for each new notebook you open.

## Accessing Course Data

All course data is in a remote file storage. Sometimes I might ask you to download the most recent data, in which case you should go to `notebooks/lectures/01_intro/getting_started.ipynb` notebook and run its first cell.
