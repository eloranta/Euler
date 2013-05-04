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

exports.primes = function(maxNumber){
  var n = prime = 2;
  var number = [];
  init();

  while (true)
    if (handleElement(n == prime) == -1)
      break;
  
  var result = [];
  for (var i = 0; i < maxNumber; ++i)
    if (number[i] != 0)
      result.push(i);
  
  return result;

  function init(){
    number.length = 0;
    number.push(0);
    number.push(0);
    for (var i = 2; i < maxNumber; ++i)
      number.push(-1);
  }

  function handleElement(primean){
    if (prime * prime >= maxNumber)
      return -1;
    if (primean)
      number[n] = 1;
    else
      number[n] = 0;

    n += prime;
    if (n >= number.length)
      n = prime = findNextPrime();
    
    return n;
  }
  
  function findNextPrime(){
    for (var i = 0; i < number.length; ++i)
      if (number[i] == -1)
        return i;
    return -1;
  }
}


