var common = require("./common");

function add(a, b){
  return a + b;
}

console.log(common.primes(2000000).reduce(add));
