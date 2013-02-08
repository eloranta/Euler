(def problem1
  (reduce + (filter (fn [n] (or (zero? (mod n 3)) (zero? (mod n 5)))) (range 1000))))

(assert (= problem1 233168))

(def fibonacci
  (map first (iterate (fn [[a b]] [b (+ a b)]) [0 1])))

(def problem2
  (reduce + (filter even? (take-while (fn [n] (< n 4000000)) fibonacci))))

(assert (= problem2 4613732))