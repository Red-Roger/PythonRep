SELECT lesson, tutor_name, ROUND (AVG (rate), 2)
FROM marks, lessons, tutors
WHERE tutors.id = lessons.tutor_id AND lessons.id = marks.lesson_id
GROUP BY tutor_name, lesson_id
ORDER BY lesson