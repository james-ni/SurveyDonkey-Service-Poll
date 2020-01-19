CREATE TABLE if not exists question (
    id UUID not null constraint question_pkey primary key,
    title varchar not null,
    created_date timestamp,
    updated_date timestamp
);

insert into question
    ("id", "title","created_date","updated_date")
values
(
    uuid_in(md5(random()::text || now()::text)::cstring),
    'What is your favourite car brand?',
    now(),
    now()
);

CREATE TABLE if not exists option (
    id UUID not null constraint option_pkey primary key,
    description varchar not null,
    question_id uuid references question(id),
    created_date timestamp,
    updated_date timestamp

);

insert into option
    ("id", "description","question_id","created_date","updated_date")
select
    uuid_in(md5(random()::text || now()::text)::cstring),
    brand.*,
    question.id,
    now(),
    now()
from
    question, (values ('Benz'), ('Toyota'),('Honda'),('BMW')) as brand
where
    question.title = 'What is your favourite car brand?'
;
