var primes = [];

for (var n = 2; n < 200000; ++n)
	if (isPrime(n))
		primes.push(n);

function isPrime(n){
	if (n < 2)
		return false;
	if (n == 2 || n == 3)
		return true;
	var i = 2;
	while(i*i <= n){
		if (n % i == 0)
			return false;
		i++;
	}
	return true;
}

console.log(primes[10000]);

// var util = require("util");

// for (var i = 0; i < 100; ++i)
	// console.log(util.format("%d: %d", i, isPrime(i)));
