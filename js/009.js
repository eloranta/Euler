for (var a = 1; a < 1000; ++a)
	for (var b = 1; b < 1000; ++b){
		var c = 1000 - a - b;
		if (c <= 0)
			continue;
		if (a*a + b*b == c*c){
			console.log(a*b*c);
			process.exit();
		}
}