### **NumPy: Array Attributes**

1. **`ndim`**:
   - Returns the number of dimensions (axes) of the array.
   - **Example**:
     ```python
     a = np.array([10, 20, 30, 40])
     a.ndim  # Output: 1
     ```

2. **`shape`**:
   - Returns the shape (dimensions) of the array as a tuple.
   - **Example**:
     ```python
     a.shape  # Output: (4,)
     ```

3. **`size`**:
   - Returns the total number of elements in the array.
   - **Example**:
     ```python
     a.size  # Output: 4
     ```

4. **`dtype`**:
   - Returns the data type of the array elements.
   - **Example**:
     ```python
     a.dtype  # Output: int32
     ```

5. **`itemsize`**:
   - Returns the size (in bytes) of each element in the array.
   - **Example**:
     ```python
     a.itemsize  # Output: 4 (bytes)
     ```

---

### **NumPy: Data Types**

NumPy provides additional data types beyond standard Python types. Each data type is identified by a single character or a longer name.

#### **Common NumPy Data Types**:
1. **`i`**: Integer types (`int8`, `int16`, `int32`, `int64`)
   - **Example**: `a = np.array([10, 20, 30], dtype='int8')`
   - **int8 Range**: -128 to 127
   - **int16 Range**: -32768 to 32767
   - **int32 Range**: -2147483648 to 2147483647
   - **int64 Range**: -9223372036854775808 to 9223372036854775807

2. **`b`**: Boolean (`True`/`False`)
   - **Example**: `a = np.array([True, False], dtype='b')`

3. **`u`**: Unsigned integer types (`uint8`, `uint16`, `uint32`, `uint64`)
   - **Example**: `a = np.array([10, 20, 30], dtype='uint8')`

4. **`f`**: Float types (`float16`, `float32`, `float64`)
   - **Example**: `a = np.array([10.5, 20.6], dtype='float32')`

5. **`c`**: Complex numbers (`complex64`, `complex128`)
   - **Example**: `a = np.array([1+2j, 3+4j], dtype='complex64')`

6. **`s`**: String types
   - **Example**: `a = np.array(['hello', 'world'], dtype='S')`

7. **`U`**: Unicode string
   - **Example**: `a = np.array(['hello', 'world'], dtype='U')`

8. **`M`**: DateTime
   - **Example**: `a = np.array(['2021-01-01'], dtype='M')`

---

### **Creating Arrays with Specific Data Types**

- You can specify the data type of an array during its creation using the `dtype` argument.
  - **Example**:
    ```python
    a = np.array([10, 20, 30, 40], dtype='i8')  # Creates an int64 array
    print(a.dtype)  # Output: int64
    ```

- Attempting to create an array with elements that cannot be converted to the specified type will result in an error.
  - **Example**:
    ```python
    a = np.array(['a', 20, 30, 40], dtype=int)  # Raises ValueError
    ```

---

### **Changing the Data Type of an Existing Array**

- You can change the data type of an array using the `astype()` method.
  - **Example**:
    ```python
    a = np.array([10, 20, 30, 40])
    b = a.astype('float64')
    print(b)        # Output: [10. 20. 30. 40.]
    print(b.dtype)  # Output: float64
    ```

- Alternatively, you can use the corresponding data type function.
  - **Example**:
    ```python
    a = np.array([10, 20, 30, 40])
    c = np.float64(a)
    print(c)        # Output: [10. 20. 30. 40.]
    print(c.dtype)  # Output: float64
    ```

- You can also convert arrays to other types like boolean:
  - **Example**:
    ```python
    a = np.array([10, 20, 0, 40])
    x = np.bool_(a)
    print(x)        # Output: [ True  True False  True]
    ```

---

### **Memory Consideration: Size of Different Data Types**

The memory size of an array can vary based on the data type. For example, an `int8` array will consume less memory than an `int32` array.

- **Example**:
  ```python
  a = np.array([10, 20, 30, 40])
  print(sys.getsizeof(a))          # Output: 128 (bytes)
  
  a = np.array([10, 20, 30, 40], dtype='int8')
  print(sys.getsizeof(a))          # Output: 116 (bytes)
  ```

---

### **Summary of Key Functions and Concepts**:

- **Array Attributes**: `ndim`, `shape`, `size`, `dtype`, `itemsize`.
- **Data Type Creation**: `dtype` argument to create arrays of specific types.
- **Data Type Conversion**: `astype()` to change the data type of existing arrays.
- **Memory Efficiency**: Choose appropriate data types (`int8` vs `int32`) to save memory.

---

 