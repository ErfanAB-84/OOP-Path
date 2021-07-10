# OOP-Path

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/Interstellar-destaque.jpg">
  <p>this path for basics learn object oriented programming</p>
<img src="https://img.shields.io/github/stars/mehranalam/oop-in-python?style=flat-square" alt="Repo stars"/>
  <a href="https://github.com/mehranalam/oop-in-python/blob/master/LICENSE" target="blank">
<img src="https://img.shields.io/github/license/mehranalam/oop-in-python?style=flat-square" alt="Repo license" />
</a>
  <img src="https://img.shields.io/github/languages/code-size/mehranalam/oop-in-python?style=flat-square">
  <img src="https://img.shields.io/github/forks/mehranalam/oop-in-python?style=flat-square">
  </div>

### Tic Tac Toe (xoxo) in Python

this small Program implements, in **Python 3**,the **minimax** algorithm and OOP(object-oriented programming) for Tic Tac Toe 

### References

* The Wikipedia page : [**MinMax**](https://en.wikipedia.org/wiki/Minimax)

* The Wikipedia page : [**Tic Tac Toe**](https://en.wikipedia.org/wiki/Tic-tac-toe)

## OOP structure

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/20210710_113856.jpg">
</div>

# More information
  
### Class

#### Py

**Classes** provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

```python

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world
```

#### java

In the real world, you'll often find many **individual objects** all of the same kind. There may be thousands of other bicycles in existence, all of the same make and model. Each bicycle was built from the same set of blueprints and therefore contains the same components. In object-oriented terms, we say that your bicycle is an instance of the class of objects known as bicycles. A class is the blueprint from which individual objects are created.

```java

class Bicycle {

    int cadence = 0;
    int speed = 0;
    int gear = 1;

    void changeCadence(int newValue) {
         cadence = newValue;
    }

    void changeGear(int newValue) {
         gear = newValue;
    }

    void speedUp(int increment) {
         speed = speed + increment;   
    }

    void applyBrakes(int decrement) {
         speed = speed - decrement;
    }

    void printStates() {
         System.out.println("cadence:" +
             cadence + " speed:" + 
             speed + " gear:" + gear);
    }
}

```
