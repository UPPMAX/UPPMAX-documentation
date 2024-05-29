# Compile Java programs using `javac`

[javac](javac.md) is a Java [compilers](compilers.md).

This page describes how to compile Java code using `javac`.

## Procedure

### 1. Load a GCC module

Before compiling a java program, the module java has to be loaded.
To load the java module, enter the command:

``` console
module load java
```

### 2. Create a Java source file

Create and write a Java source file called `hello_world.java`:

```bash
nano hello_world.java
```

In [nano](nano.md), write the Java program as such:

```java
class hello_world
{
  public static void main(String[] args)
  {
    System.out.println("hello, world");
  }
}
```

### 3. Compile the source file

To compile, enter the command:

```console
javac hello_world.java
```

### 4. Run

to run, enter:

``` console
java hello_world
```
