var counts = {2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0};

for (n = 2; n <= 20; ++n){
	var primes = {2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0};
	for (var i in primes){
		var n1 = n;
		while (n1 % i == 0){
			primes[i] += 1;
			n1 = n1 / i;
		}
	}
	for (var i in primes){
		if (primes[i] > counts[i])
			counts[i] = primes[i];
	}
}

var result = 1;
for (var i in counts){
	for (var j = 0; j < counts[i]; ++j)
		result *= i;
}

console.log(result);