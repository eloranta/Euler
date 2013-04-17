var common = require("../common/common");

var sum = 0;

for (var n = 2; n < 2000000; ++n)
	if (common.isPrime(n))
		sum += n;

console.log(sum); 