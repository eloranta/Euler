var sum = 0;
var sum2 = 0;

for (var i = 1; i <= 100; ++i)
{
	sum += i;
	sum2 += i*i;
}

console.log(sum*sum-sum2);
