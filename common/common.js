exports.isPrime = function(n){
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
