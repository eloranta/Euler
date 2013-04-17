var sum = 0;

for (var n = 2; n < 2000000; ++n)
	if (isPrime(n))
		sum += n;

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

console.log(sum); 