console.log("using % operator");

var sum = 0;

for (var i = 1; i < 1000; ++i){
  if (i % 3 == 0 || i % 5 == 0)
    sum += i;
}

console.log(sum);
console.log();


console.log("using summation");

var sum1 = 0;
for (var i = 0; i < 1000; i += 3){
  sum1 += i;
}

var sum2 = 0;
for (var i = 0; i < 1000; i += 5){
  sum2 += i;
}

var sum3 = 0;
for (var i = 0; i < 1000; i += 15){
  sum3 += i;
}

console.log(sum1 + sum2 - sum3);
