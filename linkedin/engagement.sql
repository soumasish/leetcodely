create table posts
(
	id            SERIAL,
	date          date,
	author_id     int,
	has_text      boolean,
	has_image     boolean,
	hashtag       varchar ARRAY,

	primary key(id)
);

insert into departments
	(name)
values
	('2021-08-02', ),
	('Engineering'),
	('Marketing'),
	('Biz Dev'),
	('Silly Walks');

create table employees
(
	id            SERIAL,
	first_name    varchar(255),
	last_name     varchar(255),
	salary        int,
	department_id int references departments,

	primary key (id)
);

insert into employees
	(first_name, last_name, salary, department_id)
values
	('John',   'Smith',     20000, 1),
	('Ava',    'Muffinson', 10000, 5),
	('Cailin', 'Ninson',    30000, 2),
	('Mike',   'Peterson',  20000, 2),
	('Ian',    'Peterson',  80000, 2),
	('John',   'Mills',     50000, 3);

create table projects
(
	id            SERIAL,
	title         varchar(255),
	start_date    date,
	end_date      date,
	budget        int,

	primary key(id)
);

insert into projects
	(title, start_date, end_date, budget)
values
	('Build a cool site',        '2011-10-28', '2012-01-26', 1000000),
	('Update TPS Reports',       '2011-07-20', '2011-10-28',  100000),
	('Design 3 New Silly Walks', '2009-05-11', '2009-08-19',     100);


create table employees_projects
(
	project_id    int references projects,
	employee_id   int references employees
);

insert into employees_projects
	(project_id, employee_id)
values
	(2, 1),
	(3, 2),
	(1, 3),
	(1, 4),
	(1, 5);