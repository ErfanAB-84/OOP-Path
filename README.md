# OOP-Path

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/Interstellar-destaque.jpg">
  <p>this path for basics learn object oriented programming</p>
<a href="https://github.com/mehranalam/Fibonacci-SEN" target="blank">
    <img src="https://img.shields.io/github/stars/mehranalam/oop-path?style=flat-square" alt="Repo stars"/>
  </a>
  <a href="https://github.com/mehranalam/oop-path/blob/master/LICENSE" target="blank">
    <img src="https://img.shields.io/github/license/mehranalam/oop-path?style=flat-square" alt="Repo license" />
  </a>
  <img src="https://img.shields.io/github/languages/code-size/mehranalam/oop-path?style=flat-square">
  <img src="https://img.shields.io/github/forks/mehranalam/oop-path?style=flat-square">
  <p>
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Mehranalam/oop-path?style=flat-square">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Mehranalam/oop-path?style=flat-square">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Mehranalam/oop-path?style=flat-square">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/Mehranalam/oop-path?style=flat-square">
    <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/Mehranalam/oop-path?style=flat-square">
  </p>
  </div>
  
## Project this Repo

### Tic Tac Toe (xoxo) in Python

this small Program implements, in **Python 3**,the **minimax** algorithm and OOP(object-oriented programming) for Tic Tac Toe 

* The Wikipedia page : [**MinMax**](https://en.wikipedia.org/wiki/Minimax)

* The Wikipedia page : [**Tic Tac Toe**](https://en.wikipedia.org/wiki/Tic-tac-toe)

### Fibonacci 

Sequence of Fibonacci numbers and addition of even numbers

* The Wikipadia page : [**Fibonacci**](https://en.wikipedia.org/wiki/Fibonacci_number)

* The Wikipadia page : [**Even Number**](https://simple.wikipedia.org/wiki/Even_number)



## OOP structure

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/20210710_113856.jpg">
</div>

# More information

## Object

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/1_gjyhqdy5jXjd7L0ILzu5qA.jpeg.jpg">
  </div>

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

## Class

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/images.png">
  </div>

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


## Inheritance

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/typesofinheritance.jpg">
  </div>

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

## Polymorphism

<div align="center">
  <img src="https://cdn.askpython.com/wp-content/uploads/2019/12/Polymorphism-in-Python.png">
  </div>

#### Python

**Polymorphism** means multiple forms. In python we can find the same operator or function taking multiple forms. It also useful in creating different classes which will have class methods with same name. That helps in re using a lot of code and decreases code complexity. Polymorphism is also linked to inheritance as we will see in some examples below.

```python

class Rectangle:
   def __init__(self, length, breadth):
      self.l = length
      self.b = breadth
   def perimeter(self):
      return 2*(self.l + self.b)
   def area(self):
      return self.l * self.b

class Circle:
   def __init__(self, radius):
      self.r = radius
   def perimeter(self):
      return 2 * pi * self.r
   def area(self):
      return pi * self.r ** 2

```

#### java

**Polymorphism** is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

Any Java object that can pass more than one IS-A test is considered to be polymorphic. In Java, all Java objects are polymorphic since any object will pass the IS-A test for their own type and for the class Object.

```java

class Animal {
  public void animalSound() {
    System.out.println("The animal makes a sound");
  }
}

class Pig extends Animal {
  public void animalSound() {
    System.out.println("The pig says: wee wee");
  }
}
```

- this override from father class

```java
class Dog extends Animal {
  @override
  public void animalSound() {
    super.animalSound();
    System.out.println("The dog says: bow wow");
  }
}

```

## abstract

<div align="center">
  <img src="https://files.virgool.io/upload/users/44457/posts/fgmmonxbfdqs/tohavr0hq6oc.jpeg">
  </div>

#### Python

An **abstract** class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.


```python

from abc import ABC, abstractmethod
class Animal(ABC):
 
    def move(self):
        pass
 
class Human(Animal):
 
    def move(self):
        print("I can walk and run")
 
 
```

#### java

An abstract class is a class that is declared ``abstract``—it may or may not include abstract methods. Abstract classes cannot be instantiated, but they can be subclassed.

An abstract method is a method that is declared without an implementation

```java

abstract class GraphicObject {
    int x, y;
    ...
    void moveTo(int newX, int newY) {
        ...
    }
    abstract void draw();
    abstract void resize();
}

```
Fahter Class :)

```java

class Circle extends GraphicObject {
    void draw() {
        ...
    }
    void resize() {
        ...
    }
}
class Rectangle extends GraphicObject {
    void draw() {
        ...
    }
    void resize() {
        ...
    }
}
```

Child Class :)

## Encapsulation

#### Python
The process of wrapping up variables and methods into a single entity is known as **Encapsulation**. It is one of the underlying concepts in object-oriented programming (OOP). It acts as a protective shield that puts restrictions on accessing variables and methods directly, and can prevent accidental or unauthorized modification of data. Encapsulation also makes objects into more self-sufficient, independently functioning pieces.

```python

class Robot(object):
   def __init__(self):
      self.__version = 22

   def getVersion(self):
      print(self.__version)

   def setVersion(self, version):
      self.__version = version

obj = Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version)

```

- Getter Func
- Setter Func

#### java

**Encapsulation** is one of the key features of object-oriented programming. Encapsulation refers to the bundling of fields and methods inside a single class.

It prevents outer classes from accessing and changing fields and methods of a class. This also helps to achieve data hiding.


- Getter Func
- Setter Func

```java

class Person {

  // private field
  private int age;

  // getter method
  public int getAge() {
    return age;
  }

  // setter method
  public void setAge(int age) {
    this.age = age;
  }
}

class Main {
  public static void main(String[] args) {

    // create an object of Person
    Person p1 = new Person();

    // change age using setter
    p1.setAge(24);

    // access age using getter
    System.out.println("My age is " + p1.getAge());
  }
}

```

<div align="center">
  <img src="https://raw.githubusercontent.com/Mehranalam/Mehranalam/main/assets/interstellar-review.jpg">
  
<p>I hope this <b>Repository</b> will help you think of the concepts of object oriented programming And what should we use them at all ;),</p>
  <img src="https://img.shields.io/twitter/follow/mehranalambeigi?color=blue&style=for-the-badge">
  <img src="https://img.shields.io/github/followers/Mehranalam?color=black&style=for-the-badge">
  <img src="https://img.shields.io/github/languages/count/mehranalam/oop-path?color=orange&style=for-the-badge">
  </div>


## license

Permissions of this weak copyleft license are conditioned on making available source code of **licensed** files and modifications of those files under the same license (or in certain cases, one of the **GNU licenses**). Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. However, a larger work using the licensed work may be distributed under different terms and without source code for files added in the larger work.
