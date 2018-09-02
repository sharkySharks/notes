# Node.js

- microprocessor is a tiny machine in your computer
    + accepts instructions and carries them out
    + speaks machine code/language
        * all code compiles into machine code
        * EX: ARM, MIPS, x64, IA-32
- Node is written in C++ & V8 (JavaScript engine) is written in C++
- ECMAScript - the core scripting standard JS is based on
- JavaScript Engine - a program that converts JS code into comething the computer processor can understand, it should follow the ECMAScript standard
- V8 - C++ program, one of the JS engines
    + open source by Google (made for Chrome)
        * Chrome is also a C++ program
    + very performant and fast
    + converts JS code into machine code
    + you can extend JS through adding features by embedding the V8 engine in C++ code
- Client-Server Model of Computing
    + Clients asks for services and makes a request
    + Server performs the services and sends a response
    + Browsers and Web Servers request services over HTTP
    + Node server-side JS program that allows devs to use 1 programming language for the client and server
- Nodejs is a C++ program that accepts JS
- Modules, exports, require, import/export
    + module - a reusable block of code that does not accidentally impact other code
        * COMMONJS modules - an agreed upon standard for how to structure modules
    + `require` is a node fn that pulls in files/modules
        * it takes the module code as a parameter, which becomes the body of the fn, and then returns `module.exports` with the module code added to the exports object
    + `module.exports = whatever-you-want-to-expose` from your module
    + IIFEs are how devs have been faking modules over the years, since the code inside an IIFE is scoped to that fn and is therefore protected
    + module patterns:
    ```
    // overriding the default object with a fn
    module.exports = function() {
        console.log("Hello world");
    }
    
    // add a method to the exports object
    module.exports.greet = function() {
        console.log('Hello world');
    }
    
    // using a fn constructor
    function Greeter() {
        this.greeting = 'Hello world';
        this.greet = function() {
            console.log(this.greeting);
        }
    }
    // module.exports is cached, so this will point to the same object with every require
    module.exports = new Greeter();

    // will need to be required with the `new` keyword to create a new instance each time
    module.exports = Greeter; 
    
    // Revealing module pattern
    var greeting = 'Hello World';
    function greet() {
        console.log(greeting);
    }
    // only exposes what you want, everything else is private
    module.exports = {
        greet: greet
    }
    ```
    + `exports` & `module.exports` are the same object initially, but you can't reassign `exports` or it will break the short cut association of `exports` and `module.exports`, but you can extend it with more methods/properties
        * just use `modules.exports` to make life easier
    + `export function greet() { }` then... `import * as greeter from 'greet'` from greet.js file
- Node event emitter
    + A lot of functionality in node is built on top of the event emitter
    + Event emitter simple example, replicates the functionality of the node event emitter:
    ```
    // emitter.js
    function Emitter() {
        this.events = {};
    }

    Emitter.prototype.on = function(type, listener) {
        this.events[type] = this.events[type] || [];
        this.events[type].push(listener);
    }

    Emitter.prototype.emit = type => {
        if (this.events[type]) {
            this.events[type].forEach(listener => listener());
        }
    }

    module.exports = Emitter;

    // app.js
    var Emitter = require('./emitter');
    var emtr = new Emitter();

    emtr.on('greet', () => {
      console.log('Somewhere, someone said hello.')  
    });
    emtr.on('greet', () => {
      console.log('Heyo.')  
    });
    emtr.emit('greet');
    ```
    + internal node event emitter is called `events`, so the only difference above in the `app.js` file is the require statement:
        * `var Emitter = require('events');`
    + `util.inherits(constructor, superConstructor)` - native utility fn in node that creates a prototype chain between two separate constructors so that fn can be inherited between both
        * this connects the prototypes, but you need to connect the two fn constructors' properties with `super` and the `constructor` in ES6 `class`, or `superConstructor.call(this)` inside the `constructor` so that it pulls in the super's properties (methods are available on the prototype already)
        ```
        class Greeter extends EventEmitter {
            constructor() {
                super(); // looks at what is extended above
                this.greeting = 'Hi';
            }
        }
        ```
- Asynchronous Node - non-blocking 
    + Node runs asynchronously while V8 is synchronously running inside of it
    + System events handled by C++ core runs libuv, a library, which communicates with the OS
    + Inside Node: V8 (synchronous) & libuv (has an event loop queue)
        * libuv processes events in its queue and then sends a callback to V8 when an event has completed
        * V8 will only run the libuv callback from its event loop once it finishes the code it is running
        * All of this is happening asynchronously, even though V8 is running synchronously
    + Non-blocking - doing other things without stopping your program from running, made possible by Node running asynchronously
- Buffers & Streams
    + Buffer - temporary holding spot in memory for data being moved from one place to another (intentionally limited in size)
    + Stream - a sequence of data made available over time
        * pieces of data that eventually combine into a whole
    + Binary data - data stories in binary (1s and 0s), Base 2 representation of #
        * 0   1   0   1   (Base 2 #)
        * x   x   x   x   (multiply)
        * 2^3 2^2 2^1 2^0 (from right to left)
        * 0 + 4 + 0 + 1   (added together)
        * 5               (Base 10 #)
    + Character set - unicode & ASCII
        * number representation for characters
    + Character Encoding - UTF-8
        * how characters are stored in binary
        * how many bits are used to store the character
    + Byte = 8 bits
    + ES6 allows for dealing with binary data now, previously JS did not have a way to do this
    + Files and `fs` - `require('fs');`
        * allows access to the file system asynchronously
        * create readable and writable streams to consume data in particular kinds of chunks
            - don't want to necessarily read large chunks of data from files all at once bc it will be slow, more performant to use streams
    ```
    var fs = require('fs');

    var greet2 = fs.readfile(__dirname + '/greet.txt', 'utf8', (err, data) => {
        // error-first callback, `err` returns `null` if there is no error
        // asynchronous callback
    });

    ```
        
    + Pipe - connecting 2 streams by writing to one stream what is being read from another
        * In Node you pipe from a readable stream to a writable stream
        
    ```
    var fs = require('fs');
    var zlib = require('zlib');

    // only a readable stream, not writable
    var readable = fs.createReadStream(__dirname + '/greet.txt');

    // only a writable stream, not readable
    var writable = fs.createWriteStream(__dirname + '/greetCopy.txt');

    var compressed = fs.createWriteStream(__dirname + '/greetCopy.txt.gz'); // compressed file destination

    // new transform stream (readable and writable) that compresses the files
    var gzip = zlib.createGzip(); 

    // copies all the text from greet.txt to greetCopy.txt
    readable.pipe(writable);

    // data sent through the compressor and then to the compressed file
    readable.pipe(gzip).pipe(compressed); 
    ```

- TCP/IP
    + Protocol - a set of rules that two sides agree to communicate on
    + IP - Internet Protocol
    + TCP - Transmission Control Protocol, how information is sent over the internet
    + Port - once a computer receives a packet, how it knows what program to send it to, unique number part of the socket address
- HTTP - HyperText Transfer Protocol
    + set of rules for data being transferred on the web
    + defines data being transferred via TCP/IP
    + MIME type - Multipurpose Internet Mail Extensions
        * a standard for specifying the type of data being sent to the server
        * EXs: application/json, text/html, image/jpeg
    + routing - mapping HTTP requests to content, to actual files on the server or not
    + http web server:
    ```
    // serving a file and changing content
    var http = require('http');
    var fs = require('fs');

    http.createServer((req, res) => {

        res.writeHead(200, { 'Content-Type': 'text/html' });
        // use 'fs' module to serve a file
        var html = fs.readFileSync(__dirname + '/index.htm', 'utf8');
        var message = 'Hello world...';
        html = html.replace('{Message}', message);
        res.end(html);  

    }).listen(1337, '127.0.0.1');


    // now with streams:
    var http = require('http');
    var fs = require('fs');

    http.createServer((req, res) => {

        res.writeHead(200, { 'Content-Type': 'text/html' });
        // create a read stream that pipes to a writable stream
        fs.createReadStream(__dirname + '/index.htm').pipe(res);

    }).listen(1337, '127.0.0.1');


    // now with JSON:
    var http = require('http');
    var fs = require('fs');

    http.createServer((req, res) => {

        res.writeHead(200, { 'Content-Type': 'application/json' });
        var obj = {
            firstname: 'John',
            lastname: 'Doe' 
        };
        res.end(JSON.stringify(obj));

    }).listen(1337, '127.0.0.1');


    // now with routing:
    var http = require('http');
    var fs = require('fs');

    http.createServer((req, res) => {
        
        if (req.url === '/') {
            fs.createReadStream(__dirname + '/index.htm').pipe(res);
        } else if (req.url === '/api') {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            var obj = {
                firstname: 'John',
                lastname: 'Doe' 
            };
            res.end(JSON.stringify(obj));
        } else {
            res.writeHead('404')
            res.end();
        }

    }).listen(1337, '127.0.0.1');
    ```

- Express
    + Framework that wraps Node functionality
    + HTTP web server:
    ```
    var express = require('express');
    var bodyParser = require('body-parser');
    var app = express();
    
    // process is a core node module, env returns an obj with the user env
    var port = process.env.PORT || 3000;

    // use the url encoded parser
    var urlnecodedParser = bodyParser.urlencoded({ extended: false });
    
    var jsonParser = bodyParser.json();
    
    // serving static files
    app.use('/assets', express.static(__dirname + '/public'));

    // http requests GET
    app.get('/', (req, res) => {
        res.send('<html><head><link href=assets/style.css type=text/css rel=stylesheet /></head><body><h1>Hello World</h1</body></html>');

        // OR send a file:
        res.render('index');
    });
    
    // accessing url params
    app.get('/person/:id', (req, res) => {
        
        res.send('<html><head></head><body><h1>Hello' + req.params.id + '</h1</body></html>');

        // OR send a file back:
        res.render('person', { ID: req.params.id, Qstr: req.query.qstr });
    });

    // http POST req
    app.post('/person', urlencodedParser, (req, res) => {
        res.send('Thank you!');
        console.log(req.body.firstname);
        console.log(req.body.lastname);
    });

    app.post('/personjson', jsonParser, (req, res) => {
        res.send('Thank you for json data!');
        console.log(req.body.firstname);
        console.log(req.body.lastname);
    });

    app.get('/api', (req, res) => {
        // JSON functionality built in
        res.json({ firstname: 'John', lastname: 'Doe' });
    });

    // http.createServer() is being run under the hood here
    app.listen(port);

    ```
    + REST - Representational State Transfer
        * use HTTP verbs for the requests
        * urls are resources, no verbs
    + Structure
    ```
    // In app.js
    var express = require('express');
    var app = express();
    var apiController = require('./controllers/apiController');
    var htmlController = require('./controllers/htmlController');
    
    // process is a core node module, env returns an obj with the user env
    var port = process.env.PORT || 3000;
    
    // serving static files
    app.use('/assets', express.static(__dirname + '/public'));
    
    // pass the `app` function around
    htmlController(app);
    apiController(app);

    // http.createServer() is being run under the hood here
    app.listen(port);


    // In /controllers/apiController.js
    var bodyParser = require('body-parser');
    var urlnecodedParser = bodyParser.urlencoded({ extended: false });
    module.exports = (app) =>{
        
        app.get('/api', (req, res) => {
            // JSON functionality built in
            res.json({ firstname: 'John', lastname: 'Doe' });
        });

        app.post('/api/person', (req, res) => {
            res.send('Thank you!');
            console.log(req.body.firstname);
            console.log(req.body.lastname);
        });
    }

    // In /controllers/htmlController.js
    module.exports = app => {

        app.get('/', (req, res) => {
            res.render('index');
        });
        
        app.get('/person/:id', (req, res) => {
            res.render('person', { ID: req.params.id, Qstr: req.query.qstr });
        });
    }
    ```
- Databases
    + Relational Databases - tables and IDs
        * SQL - Structured Query Language
        * MySQL, Postgres
    + NOSQL Databases - variety of technologies that are alternatives to tables and SQL
        * Document database, more flexible to structure changes
            - contains the structure and the data in the document
        * MongoDB (Mongoose)
            - Schema - like a fn constructor, can be passed around
                + keys and expected data types as values
            - Make models based on the Schema, ie Person
            - Make individual documents based on the model, ie John
