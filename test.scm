
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

(define (append list n)
    (if (cdr list)
        (cons (car list) (append (cdr list) n))
        (cons (car list) n))
)

(define (range n)
    (if (= n 1)
        (cons 0 null)
        (append (range (- n 1)) ( - n 1))
))

(define (map list fn)
    (if (cdr list)
        (cons (fn (car list)) (map (cdr list) fn))
        (cons (fn (car list)) null)
))

(map (quote (1 2 3 4)) (lambda (x) (+ x 1)))
