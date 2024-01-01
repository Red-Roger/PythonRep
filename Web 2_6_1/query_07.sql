SELECT group_id, lesson, student_name, rate
FROM students, lessons, marks
WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id
AND group_id = 2 AND lessons.id = 3
ORDER BY group_id, lesson