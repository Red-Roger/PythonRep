SELECT student_name, ROUND (AVG(rate), 2) as avg_rate
FROM students, marks
WHERE marks.student_id = students.id
GROUP BY student_name
ORDER BY avg_rate DESC
LIMIT 5