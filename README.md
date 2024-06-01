**Project Name: Maze Generator using Depth First Search (Pygame)**

## Overview
This project is a Pygame application that generates random mazes using the depth-first search algorithm. The generated mazes can be displayed on the screen, and users have the option to change the seed for generating different mazes. Additionally, users can save the generated maze as a `.maze` file and load previously saved maze files. The `.maze` file format contains information about the seed used for maze generation and the maze structure.

## Features
- Random maze generation using depth-first search algorithm.
- Displaying generated mazes on the Pygame screen.
- Option to change the seed for generating different mazes.
- Saving generated maze as a `.maze` file.
- Loading saved maze files in `.maze` format.

## How to Use
1. **Installation**
   - Ensure you have Python installed on your system.
   - Install Pygame library using pip:
     ```
     pip install pygame
     ```

2. **Running the Application**
   - Run the `main.py` file to start the application:
     ```
     python main.py
     ```
   
3. **Generating and Displaying Mazes**
   - Upon running the application, a random maze will be generated and displayed on the Pygame window.

4. **Changing Seed**
   - Press the 'GENERATE' key to change the seed for generating a different maze.
   - Enter the new seed value.

5. **Saving and Loading Mazes**
   - Press the 'SAVE' button to save the current maze as a `.maze` file.
   - Press the 'LOAD' button to load a saved `.maze` file.
   - Specify the file path of the `.maze` file.

## File Format (.maze)
- The `.maze` file contains JSON data with the following structure:
  ```
  {
    "seed": seed_value,
    "maze": [
      {"i": row_index, "j": column_index, "walls": [top, right, bottom, left]},
      ...
    ]
  }
  ```

- `seed`: The seed value used for generating the maze.
- `maze`: An array of objects representing each cell in the maze.
  - `i`: Row index of the cell.
  - `j`: Column index of the cell.
  - `walls`: Array representing the walls of the cell in the order [top, right, bottom, left]. Each value is a boolean indicating whether the corresponding wall exists (True) or not (False).

## Dependencies
- Python 3.10
- Pygame

## Credits
This project was created by Hamza makedi and is licensed under the MIT license. 

For more information, visit the project repository https://github.com/hamza-makedi/Maze-Generator.

## Feedback and Contributions
Feedback and contributions are welcome! If you have any suggestions or would like to contribute to the project, feel free to open an issue or submit a pull request on the project repository.
