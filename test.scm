
(define (factorial n)
    (if (> n 0)
        (* n (factorial (- n 1)))
        1
))

(define x (factorial 6))
