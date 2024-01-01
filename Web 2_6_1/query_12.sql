SELECT students.group_id, lessons.lesson, students.student_name, rate, MAX (marks.date_of)
FROM marks, lessons, students
WHERE lessons.id = marks.lesson_id AND marks.student_id = students.id
AND students.group_id = 1 AND lessons.ID = 2
GROUP BY students.group_id, lessons.lesson, students.student_name, rate