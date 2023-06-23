create table if not exists Employee (
	employee_id SERIAL primary key,
	name VARCHAR(120) not null,
	department VARCHAR(120),
	boss_id INTEGER references Employee(employee_id) on delete set NULL
);