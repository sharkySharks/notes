# JavaScript Fundamentals

- Execution Context
    + global, includes the window object if running JS in the browser
    + JS engine creates the global object for you in the global execution context
- Hoisting - how the JS engine stores variables and fn during the creation of execution contexts
    + You can reference a variable or execute a fn, lexically speaking, before you declare it because of the 2 phases of creation for the execution context
    + Execution Context is created in 2 phases
        +  Phase I - Creation Phase
            + Global Object, 'this', and outer lexical env reference are created
            + Sets up in memory space for variables and functions
                * this is hoisting, not actually moving anything anywhere
                * variable names are hoisted and are set to `undefined` initially
                * functions are put in memory in their entirety
        + Phase II - Code Execution
            * Runs your code line by line
- Single-Threaded - one command executed at a time
    + browser is not single-threaded, but JS engine is
- Synchronous - one at a time in order
    + JS is single-threaded, synchronous execution
- Execution Stack
    + Whichever is on the top is the one that is currently running
    + Whenever you run a function a new execution context is created and put on the stack
    + Once the function is done running it pops off the stack
    + When the execution stack is empty THEN JS engine processes the event queue (clicks, HTTP Requests)
        * [async] events are happening outside of the JS engine, those are put in an event queue and processed after the execution stack is cleared
- Coercion - converting a value from one type to another
    + `==` coerces types when checking equality
    + `===` does strict type checking for equality
- JSON - JavaScript Object Notation
    + inspired by object literal notation, JSON is more strict though
- Functions are Objects
    + `NAME` and `CODE` properties are two additions to the function object
        * can run the `code` property
        * `name` is optional, can be anonymous
    + object literal syntax - { }
- Expressions & Statements
    + expressions return values, statements just do work and do not return values
    + fn statements have to be invoked() in order to execute the code, otherwise it is just in memory, fn expressions are created on the fly
    + IIFE (Immediately Invoked Function Expression)
- by value (primitives) and by reference (Objects)
    + by value: different memory spaces
    + by reference: same memory space
- `this` is a keyword that references the execution context, either global or within a function
- `arguments` - keyword that contains all the parameters you pass to a function
- spread syntax `...<iterableObj>` - expands iterable objects for fn calls, array elements, or object key/val
- Closures - functions having access to the lexical environments in which the function was declared
    + references to variables in the outer lexical scope will be available to the function, even when the execution context has already run and been popped off the execution stack
        * fn have access to the memory space of its outer lexical environment and all variables stored there, goes up the scope chain when looking for variable references
    + Use cases:
        * gives data privacy through privileged methods
        * event handlers and callbacks
        * currying - fn that takes a fn with multiple params as input and returns a fn with exactly 1 param
- `call`, `apply`, `bind`
    * methods available to all fn to pass the ref for `this` around
    * `fn.bind(this, parameters, to, be, set, as, default, values)` - returns a new fn
    * `fn.call(this, params, to, pass, to, fn)` - executes the fn
    * `fn.apply(this, [Array of parameters])` - executes the fn
- currying - creating a copy of a fn but with some preset parameters
- prototypical inheritance
    + inheritance - one object gets access to/inherits the properties and methods of another object
    + each object has a object prototype in which it has access to its properties/methods
    + objects will go up the prototype chain until it finds the property/method it is looking for
- problems with classes - OpenCafe class examples
    + tight coupling - leads to below issues
    + fragile base class - everyone using the base class, hard to change
    + inflexible hierarchy
    + duplication by necessity
    + gorilla vs banana - just wanted the banana, not the gorilla and jungle
- reflection - an obj can look at itself and change its properties/methods
- Creating Objects
    + `new` keyword - creates an empty object with a fn constructor, setting `this` to the fn and adding properties/methods to it
        + `new String("John")` & `new Number(2)` are built in fn constructors
            * These can be extended by adding to the prototype: `String.prototype.sharkyProp = fn`
            * fn contructors DO NOT create primitives, they create objects
        + created to mimic other languages' classes
    ```
    // EX: `new` + fn constructor
    function Person(firstname, lastname) {
        this.firstname = firstname;
        this.lastname = lastname;
    }
    // best practice to add methods to the prototype and properties to the fn constructor
    Person.prototype.getFullName = function () {
        return this.firstname + ' ' + this.lastname;
    }

    var john = new Person('John', 'Doe');
    // every object created gets a reference to and share the prototype
    john.getFullName(); // `John Doe`
    ```
    + `Object.create()` - pure prototypal inheritance
        * create objects from objects, overriding the base object's properties/methods
    ```
    EX:
    var person = {
        firstname: 'Default',
        lastname: 'Default',
        greet: function() {
            return 'Hi ' + this.firstname;
        }
    };

    var john = Object.create(person);
    john.firstname = "john";
    john.lastname = "Doe";
    ```
    + `class` - defines an object with a `constructor()` fn
        * uses the `new` keyword
        * still using objects and prototypal inheritance, not classes as other languages implement classes
    ```
    EX: 
    class Person {
        constructor(firstname, lastname) {
            this.firstname = firstname;
            this.lastname = lastname;
        }

        greet() {
            return 'Hi ' + firstname;
        }
    }
    var john = new Person('John', 'Doe');
    
    // setting the prototype of a new class with extends
    class myNewClass extends Person {
        constructor(firstname, lastname) {
            super(first, lastname);
        }

        greet() {
            return 'Yo ' + firstname;
        }
    }
    ```

- `'use strict';` - strict mode doesn't allow access to the global object from the script, so it doesn't get polluted by accident - stricter rules
    + browsers implement this differently so this can't be entirely relied on
- `var`, `let`, `const`
    + `var` - defines a variable globally, or locally to an entire function regardless of block scope
    + `let` - block scope local variable, does not create properties on the global obj, can't redeclare in same block
        * use `let` in `for` loops - captures the value of the variable at the block scope level and solves issue with reference to variable value always being the last value in the for loop
    + `const` - block scoped, global or local, cannot be re-assigned or redeclared
- `Promise` is an object which represents an asynchronous task that will eventually finish
    + three states: pending, fulfilled, rejected
    + `Promise.all()` takes an array/iterable and returns a Promise that resolves when all the Promises in the iterable are resolved or when the first one rejects
    ```
    var promise1 = new Promise(function(resolve, reject) { 
        // do something asynchronously which eventually calls either:
        // resolve(someValue); // fulfilled
        // or
        // reject("failure reason"); // rejected
        fs.readFile('veryImportantFile.txt', (err, data) => {
            if (err) {
                reject(err)
            } else {
                resolve(data);
            }
        }); 
    });

    promise1.then(data => {
        // do something in here if it is resolved successfully
    }).catch(err => {
        // do something in here if it is rejected
    }).finally(() => {
        // do something every time no matter what happens
    });

    // can also return a Promise from a function 
    ```
- `async` - syntactic sugar for creating fn that return Promises
    + `await` - only used inside an `async` fn, it waits on a `Promise` to be resolved and returns the value from it, pauses the `async` fn
    + makes async code look synchronous and therefore easier to understand
    + can use `.then` & `.catch` on async fns
