var common = require("../common/common");

var primes = [];

for (var n = 2; n < 200000; ++n)
	if (common.isPrime(n))
		primes.push(n);

console.log(primes[10000]);
