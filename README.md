# Kanban (tkinter)

A simple Kanban Board made with Python and `tkinter`.

![img](doc/kanban_screenshot.png)
![img](doc/kanban_screenshot_dark.png)

## Feature list

+ Add tasks to any stage (To Do, In Progress, Done)
+ Delete selected tasks by pressing the delete key
+ Use arrow keys to move around
+ Use Command + arrow keys to move tasks around
+ Export the board to a CSV file with "Command-E"
+ Insert new tasks with "Command-I"


# Development

## Setup using conda

```bash
# List you python envs
$ conda env list

# Create new python envs
$ conda env create --prefix ./ops/pyenv/kanban_tkinter --file ./app/environment.yml

# Init you shell to use conda activate
$ conda init
$ conda init zsh

# Activate your new created python env
$ conda activate ./ops/pyenv/kanban_tkinter
```
