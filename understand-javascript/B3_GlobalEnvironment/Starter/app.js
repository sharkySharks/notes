
function a() {
    function b() {
        console.log('inside b:', myVar);
    }
    var myVar = 2;
    b();
    console.log('inside a:', myVar);
}

var myVar = 1;
console.log('global level:', myVar);
a();
console.log("last time:", myVar);

// javascript won't look at the event queue until the execution stack has completed
// the JS engine is synchronous
// stuff outside of the JS engine can happen asynchronously, but it processes them synchronously
