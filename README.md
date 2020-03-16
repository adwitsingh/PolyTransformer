# PolyTransformer
An interactive python program to apply transformations (both linear and non - linear) to an object and plot it using matplotlib.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project needs python3 installed on the local machine along with *matplotlib*, which can be installed using:

```bash
$ python3 -m pip install matplotlib
```



## Running

main.py defines all the functions and can be run using:

```bash
$ python3 main.py
```

### Input

The first line contains the word **disc** or **polygon** denoting the figure you want to plot and transform

- If the word is **disc**, the next line contains three space-separated integers as:

  ```bash
  disc
  center_X center_Y radius
  ```

  

- If the word is **polygon**, the next two lines contain space separated lists **X[]** and **Y[]** of equal length, denoting the x-y co-ordinates of the vertices of the polygon. 

  ```
  polygon
  x1 x2 x3 ... xN
  y1 y2 y3 ... yN
  ```


The next few lines should contain a single query each, denoting the transformation you have to perform. Each query will be of the form:

- **S x y** : scale the object by a factor of x along the x-axis, and y along the y-axis.

- **R theta** : rotate the object by angle theta(in degrees, 0 <= theta <= 360) in the counter-clockwise direction about the origin.

- **T dx dy** : translate the object by dx units along the x-axis, and by dy units along the y-axis. 

Each transformation will be performed on the shape obtained as a result of all the previous transformations, ie the effect of the transformations will be cumulative. 

To exit the program, type ***quit*** and enter.

### Output

Each transformation will be reflected on an X-Y plot and the new coordinates after each transformation will be printed as output.



## Example

### Input

```
polygon
1 -1 -1 1
1 1 -1 -1
S 2 1
R 90
T 0 -2
quit
```

### Output

```
2 -2 -2 2
1 1 -1 -1

-1 -1 1 1
2 -2 -2 2

-1 -1 1 1
0 -4 -4 0
```



## Authors

* **Adwit Singh Kochar** - *Initial work* - [adwitsingh](https://github.com/adwitsingh)
