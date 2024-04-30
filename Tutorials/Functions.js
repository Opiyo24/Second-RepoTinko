// Function declaration
function sayHello(name) {
    // let name = "OPiyo";

    console.log('------------------------------');
    console.log("Hello" + " " + name);
    console.log('------------------------------');
}

sayHello("Opiyo");

function calculateTax(amount) {
    let result = amount * 0.0825;

    return result;
}

let Tax = calculateTax(100);
console.log(Tax);