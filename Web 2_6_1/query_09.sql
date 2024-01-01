SELECT student_name, lesson
FROM students, lessons, marks \
WHERE students.id = marks.student_id AND lessons.id = marks.lesson_id \
AND  students.id = 46