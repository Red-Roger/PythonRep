SELECT tutor_name, student_name, lesson
FROM marks, lessons, tutors, students
WHERE tutors.id = lessons.tutor_id AND lessons.id = marks.lesson_id AND marks.student_id = students.id
AND tutor_id = 1 AND student_id = 37