SELECT tutor_name, lesson
FROM tutors, lessons
WHERE tutor_id = tutors.id
ORDER BY tutor_name