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

### Object

#### Python

The **object** is essential to work with the class attributes. Instantiate is a term used when we create the object of any class, and the instance is also referred to as an object. The object is created using the class name. The syntax is given below.

Template :

```rust
<object-name> = <class-name>(<arguments>)
```
Example :

```python

class Person:         
    name = "John"      
    age = 24  
    def display (self):      
        print("Age: %d \nName: %s"%(self.age,self.name))      
# Creating a emp instance of Employee class    
per = Person()      
per.display()

```

#### java

A Java **object** is a combination of data and procedures working on the available data. An object has a state and behavior.

The state of an object is stored in fields (variables), while methods (functions) display the object's behavior. Objects are created from templates known as classes.

```java

public class Main {
  int x = 5;

  public static void main(String[] args) {
    Main myObj = new Main();
    System.out.println(myObj.x);
  }
}

```

### Class

#### Python

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


### Inheritance

#### Python

**Inheritance** is an important aspect of the object-oriented paradigm. Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch.

In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class. A child class can also provide its specific implementation to the functions of the parent class. In this section of the tutorial, we will discuss inheritance in detail.

```python

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()

```

#### java

**Inheritance** can be defined as the process where one class acquires the properties (methods and fields) of another. With the use of inheritance the information is made manageable in a hierarchical order.

The class which inherits the properties of other is known as subclass (derived class, child class) and the class whose properties are inherited is known as superclass (base class, parent class).

```java

class Super_class {
   int num = 20;

   // display method of superclass
   public void display() {
      System.out.println("This is the display method of superclass");
   }
}

public class Sub_class extends Super_class {
   int num = 10;

   // display method of sub class
   public void display() {
      System.out.println("This is the display method of subclass");
   }

   public void my_method() {
      // Instantiating subclass
      Sub_class sub = new Sub_class();

      // Invoking the display() method of sub class
      sub.display();

      // Invoking the display() method of superclass
      super.display();

      // printing the value of variable num of subclass
      System.out.println("value of the variable named num in sub class:"+ sub.num);

      // printing the value of variable num of superclass
      System.out.println("value of the variable named num in super class:"+ super.num);
   }

   public static void main(String args[]) {
      Sub_class obj = new Sub_class();
      obj.my_method();
   }
}

```
