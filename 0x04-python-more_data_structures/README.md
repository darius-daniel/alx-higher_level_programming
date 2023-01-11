# 0x04-python-more_data_structures

## Mandatory Tasks

### Tasks:

#### 0. Squared simple:

**File:** `0-square_matrix_simple.py` - contains a function that computes the square value of all integers of a matrix

**Prototype:** `def square_matrix_simple(matrix=[])`

* `matrix` is a 2-dimensional array
* Returns a new matrix:

  * Same size as `matrix`
  * Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You are allowed to use regular loops, `map`, etc.

#### 1. Search and replace:

* **File:** `1-search_replace.py` - contains a function that replaces all the occurences of an element by another in a new list.
* **Prototype:** `def search-replace(my_list, search, replace):`
* `my_list` is the intitial list
* `search` is the element to replace in the list
* `replace` is the new element
* You are not allowed to import any module

#### 2. Unique addition:

* **File:** `2-uniq_add.py` - contains a function that add all unique integers in a list (only once for each integer)
* **Prototype:** `def uniq_add(my_list=[]):`
* Not allowed to import new modules

#### 3. Present in both

* **File:** `3-common_elements.py` - contains a function that returns a set of common elements in two sets.
* **Prototype:** `def common_elements(set_1, set_2):`
* Not allowed to import new modules

#### 4. Only differents

* **File:** `4-only_diff_elements.py `- contains a function that returns a set of all elements present only in one set.
* **Prototype:** `def only_diff_elements(set_1, set_2):`
* Not allowed to import new modules

#### 5. Number of keys

* **File:** `5-number_keys.py `- contains a function that returns the number of keys in a dictionary.
* **Prototype:** `def number_keys(a_dictionary):`
* Not allowed to import new modules

#### 6. Print sorted dictionary

* **File:** `6-print_sorted_dictionary.py `- contains a function that prints a dictionary by ordered type.
* **Prototype:** `def print_sorted_dictionary(a_dictionary):`
* Keys should be sorted by alphabetical order
* Only keys of the first order should be sorted (don't sort keys of a dictionary inside the main directory)
* Not allowed to import new modules

#### 7. Update dictionary

* **File:** `7-update_dictionary.py `- contains a function that replaces or add key/value in a dictionary.
* **Prototype:** `def update_dictionary(a_dictionary, key, value):`
* `key` argument will always be a string
* `value` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn't exist in the dictionary, it will be created.
* Not allowed to import new modules

#### 8. Simple delete by key

* **File:** `8-simple_delete.py `- contains a function that deletes a key in a dictionary
* **Prototype:** `def simple_delete(a_dictionary, key=""):`
* `key` argument will always be a string
* If a key doesn't exist, the dictionary won't change
* Not allowed to import new modules

#### 9. Multiply by 2

* **File:** `9-multiply_by_2.py `- contains a function that returns a new dictionary with all values multiplied by 2
* **Prototype:** `def multiply_by_2(a_dictionary):`
* All values are assumed to be integers
* Returns a new dictionary
* Not allowed to import new modules

#### 10. Best score

* **File:** `10-best_score.py `- contains a function that returns a key with the biggest integer value.
* **Prototype:** `def best_score(a_dictionary):`
* All values are assumed to be integers
* If no score found, return `None`
* All students are assumed to have a different score (i.e. no two students have the same score)
* Not allowed to import new modules

#### 11. Multiply by using map

* **File:** `11-multiply_list_map.py `- contains a function that returns a list with all values multiplied by a number without using any loops.
* **Prototype:** `def multiply_list_map(my_list=[], number=0):`
* Returns a new list:
  * Same length as `my_list`
  * Each value should be multiplied by `number`
* Initial list should not be modified
* Not allowed to import new modules
