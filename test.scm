
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

(define (length list)
    (if (cdr list)
        (+ 1 (length (cdr list)))
        1))

(define (sublist list start)
    (if (= start 0)
        list
        (sublist (cdr list) (- start 1)))
)

(define (truncate list end)
    (if  (= end 0)
        null
        (cons (car list) (truncate (cdr list) (- end 1)))
        ))

(define (merge a b)
    (if (and a (not b))
        a
    (if (and b (not a))
        b
    (if (< (car a) (car b))
        (cons (car a) (merge (cdr a) b))
        (cons (car b) (merge (cdr b) a))
    )
)))

(define (sort list)
    (if (< (length list) 2) list
        (merge (sort (sublist list (// (length list) 2))) (sort (truncate list (// (length list) 2)))))
)


(map (quote (1 2 3 4)) (lambda (x) (+ x 1)))
