SELECT group_id, lesson, ROUND (AVG(rate), 2) as avg_rate
FROM students, marks, lessons
WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id
GROUP BY group_id, lesson
ORDER BY lesson ASC