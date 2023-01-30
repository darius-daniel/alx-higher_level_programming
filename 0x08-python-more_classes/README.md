# 0x08. Python - More Classes and Objects

## Tasks:

### 0. Simple rectangle

* **Files:**

  `0-rectangle.py` - Contains an empty class that defines a rectangle

  `0-main.py` - Tests the code in `0-rectangle.py`

### 1. Real definition of a rectangle

* **Files:**

  `1-rectangle.py` - Contains an empty class that defines a rectangle (based on `0-rectangle.py`)

  `1-main.py` - Tests the code in `1-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`

### 2. Area and Perimeter

* **Files:**

  `2-rectangle.py` - Contains an empty class that defines a rectangle (based on `1-rectangle.py`)

  `2-main.py` - Tests the code in `2-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`

### 3. String representation

* **Files:**

  `3-rectangle.py` - Contains an empty class that defines a rectangle (based on `2-rectangle.py`)

  `3-main.py` - Tests the code in `3-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`
  * `print()` and `str()` should print the rectangle with the character #
    * if `width` or `height` is equal to `0`, return an empty string

### 4. Eval is magic

* **Files:**

  `4-rectangle.py` - Contains an empty class that defines a rectangle (based on `3-rectangle.py`)

  `4-main.py` - Tests the code in `4-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`
  * `print()` and `str()` prints the rectangle with the character `#`
    * if `width` or `height` is equal to `0`, return an empty string
  * `repr()` returns a string representation of the rectangle to be able to recreate a new instance by using `eval()`

### 5. Detect instance deletion

* **Files:**

  `5-rectangle.py` - Contains an empty class that defines a rectangle (based on `4-rectangle.py`)

  `5-main.py` - Tests the code in `5-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`
  * `print()` and `str()` prints the rectangle with the character `#`
    * if `width` or `height` is equal to `0`, return an empty string
  * `repr()` returns a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  * Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted

### 6. How many instances

* **Files:**

  `6-rectangle.py` - Contains an empty class that defines a rectangle (based on `5-rectangle.py`)

  `6-main.py` - Tests the code in `6-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Public class attribute `number_of_instances`:
    * initialized to `0`
    * Incremented with each new instance instatiation
    * Decremented with each instance deletion
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`
  * `print()` and `str()` prints the rectangle with the character `#`
    * if `width` or `height` is equal to `0`, return an empty string
  * `repr()` returns a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  * Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted

### 7. Change representation

* **Files:**

  `7-rectangle.py` - Contains an empty class that defines a rectangle (based on `6-rectangle.py`)

  `7-main.py` - Tests the code in `7-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Public class attribute `number_of_instances`:
    * initialized to `0`
    * Incremented with each new instance instatiation
    * Decremented with each instance deletion
  * Public class attribute `print_symbol`:
    * Initialized to `#`
    * Used as symbol for string representation
    * Can be any type
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`
  * `print()` and `str()` prints the rectangle with the character `#`
    * if `width` or `height` is equal to `0`, return an empty string
  * `repr()` returns a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  * Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted

### 8. Compare rectangles

* **Files:**

  `8-rectangle.py` - Contains an empty class that defines a rectangle (based on `7-rectangle.py`)

  `8-main.py` - Tests the code in `8-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Public class attribute `number_of_instances`:
    * initialized to `0`
    * Incremented with each new instance instatiation
    * Decremented with each instance deletion
  * Public class attribute `print_symbol`:
    * Initialized to `#`
    * Used as symbol for string representation
    * Can be any type
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`
  * `print()` and `str()` prints the rectangle with the character `#`
    * if `width` or `height` is equal to `0`, return an empty string
  * `repr()` returns a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  * Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted
  * Static method def `bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    * `rect_1` must be an instance of `Rectangle`, otherwise a `TypeError` exception is raised with the message `rect_1 must be an instance of Rectangle`
    * `rect_2` must be an instance of `Rectangle`, otherwise a `TypeError` exception is raised with the message `rect_2 must be an instance of Rectangle`
    * Returns `rect_1` if both have the same area value

### 9. A square is a rectangle

* **Files:**

  `8-rectangle.py` - Contains an empty class that defines a rectangle (based on `7-rectangle.py`)

  `8-main.py` - Tests the code in `8-rectangle.py`
* class `Rectangle` defines a rectangle by:

  * Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
      * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
      * if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
  * Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height (self, value):` to set it:
      * `height` must be an integer, otherwise a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is less than `0`, a `ValueError` exception is raised with the message `height must be >= 0`
  * Public class attribute `number_of_instances`:
    * initialized to `0`
    * Incremented with each new instance instatiation
    * Decremented with each instance deletion
  * Public class attribute `print_symbol`:
    * Initialized to `#`
    * Used as symbol for string representation
    * Can be any type
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
  * Public instance method: `def area(self):` that returns the rectangle area
  * Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or height is equal to `0`, perimeter is equal to `0`
  * `print()` and `str()` prints the rectangle with the character `#`
    * if `width` or `height` is equal to `0`, return an empty string
  * `repr()` returns a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  * Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted
  * Static method def `bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    * `rect_1` must be an instance of `Rectangle`, otherwise a `TypeError` exception is raised with the message `rect_1 must be an instance of Rectangle`
    * `rect_2` must be an instance of `Rectangle`, otherwise a `TypeError` exception is raised with the message `rect_2 must be an instance of Rectangle`
    * Returns `rect_1` if both have the same area value
  * Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
