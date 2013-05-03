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

function primes(n){
  var prime = [];
  prime.push(0);
  prime.push(0);
  for (var i = 2; i < n; ++i){
    prime.push(-1);
  }
  
  var i = step = 2;
  
  while (true){
    if (i == step){
      prime[i] = 1;
    }
    else{
      prime[i] = 0;
    }
    i += step;
    if (i >= n){
      var p = -1;
      for (var j = 0; j < n; ++j){
        if (prime[j] == -1){
          p = j;
          break;
        }
      }
      console.log(p);
      if (p == -1){
        break;
      i = step = p;
      }
    }
  }
  return prime;
  
}

console.log(primes(10));