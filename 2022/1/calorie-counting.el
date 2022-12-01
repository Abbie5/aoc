(setq input
      (with-temp-buffer
        (insert-file-contents "input.txt")
        (buffer-string)))

(defun sum (li)
  (apply '+ li))

(defun first (x li)
  (butlast li (- (length li) x)))

(setq elves
      (sort
       (mapcar #'sum
               (mapcar #'(lambda (elf)
                          (mapcar #'string-to-number
                                  (split-string elf "\n")))
                       (split-string input "\n\n")))
       '>))

(defun prinn (s)
  (prin1 s)
  (terpri))

(with-output-to-temp-buffer "*output*"
  (prinn (car elves))
  (prinn (sum (first 3 elves))))
