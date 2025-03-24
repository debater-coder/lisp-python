
(define (factorial n)
    (if (> n 0)
        (* n (factorial (- n 1)))
        1)
)

(define (fib n)
    (if (<= n 2)
        1
        (+
            (fib (- n 1)) (fib (- n 2))
        )
    )
)

(define comment-ThisFunctionAppliesTheFunctionToTheFirstN 0)
(define (fnRange fn n)
    (print (fn n))
    (if (= n 1)
        0
        (fnRange fn (- n 1))
    )
)
