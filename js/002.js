function fibonacci(n){
  result = [];
  a = 0;
  result.push(a);
  b = 1;
  result.push(b);
  while (true){
    sum = a + b;
    if (sum > n)
      return result;
    a = b;
    b = sum
    result.push(b);
  }
}

function even(n){
  if (n % 2 == 0)
    return true;
  return false;
}

function add(a, b){
  return a + b;
}

console.log(fibonacci(4000000).filter(even).reduce(add));

