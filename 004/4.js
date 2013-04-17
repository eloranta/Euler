var palindromes = [];

for (var i = 999; i > 99; --i)
	for (var j = 999; j > 99; --j){
		var s1 = (i*j).toString();
		var s2 = s1.split("").reverse().join("");
		if (s1 == s2)
			palindromes.push(s1);
	}

console.log(Math.max.apply(null, palindromes));