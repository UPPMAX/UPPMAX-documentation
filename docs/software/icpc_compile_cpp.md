# Compile a C++ program using `icpc`

[icpc](icpc.md) is an Intel C++ [compiler](compilers.md).
This page describes how to compile C++ code using `icpc`.

## Procedure

### 1. Load the modules

Load a recent `intel` module:

```bash
module load intel/20.4
```

### 2. Write the C++ program

Create and write a C++ source file called `hello_world.cpp`:

```bash
nano hello_world.cpp
```

In [nano](nano.md), write the C++ program as such:

```c++
#include <iostream>

int main()
{
  std::cout << "hello, world\n";
}

```

### 3. Compile the C++ program

After saving and closing nano, compile as such:

```bash
icpc hello_world.cpp
```

### 4. Run the executable

Run the program:

```bash
./a.out
```

Output:

```console
hello, world
```
