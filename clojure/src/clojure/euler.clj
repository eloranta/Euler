(def problem1
  (reduce + (filter (fn [n] (or (zero? (mod n 3)) (zero? (mod n 5)))) (range 1000))))

(assert (= problem1 233168))

(def fibonacci
  (map first (iterate (fn [[a b]] [b (+ a b)]) [0 1])))

(def problem2
  (reduce + (filter even? (take-while (fn [n] (< n 4000000)) fibonacci))))

(assert (= problem2 4613732))

(defn prime_internal? [n]
  (take-while (fn [i] (<= (* i i) n)) (interleave (map dec (range 6 100 6)) (map inc (range 6 100 6)))))

(defn prime? [n]
  (cond
    (< n 2) false
    (= n 2) true
    (= n 3) true
    (zero? (mod n 2)) false
    (zero? (mod n 3)) false
    (prime_internal? n) true
    :else false))

(assert (= (prime? -1) false))
(assert (= (prime? 0) false))
(assert (= (prime? 1) false))
(assert (= (prime? 2) true))
(assert (= (prime? 3) true))
(assert (= (prime? 4) false))
(assert (= (prime? 5) true))
(assert (= (prime? 6) false))
(assert (= (prime? 7) true))
;(assert (= (prime? 25) false))

 
(prime_internal? 100)