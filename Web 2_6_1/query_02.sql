SELECT lesson, student_name, max(rate) as max_rate
FROM students, marks, lessons
WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id
GROUP BY lesson
ORDER BY lesson ASC