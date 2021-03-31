/* creating database - schema and tables */

DROP SCHEMA IF EXISTS skni_project CASCADE;
CREATE SCHEMA IF NOT EXISTS skni_project;

DROP TABLE IF EXISTS skni_project.company CASCADE;
CREATE TABLE IF NOT EXISTS skni_project.company(
	id_company serial PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	full_name varchar(50),
	industry varchar(100)
);

DROP TABLE IF EXISTS skni_project.measure CASCADE;
CREATE TABLE IF NOT EXISTS skni_project.measure (
	id_value serial PRIMARY KEY,
	value_name varchar(100) NOT NULL 
);

DROP TABLE IF EXISTS skni_project.financial_indicators CASCADE;
CREATE TABLE IF NOT EXISTS skni_project.financial_indicators(
	id_indicator serial PRIMARY KEY,
	indicator_name varchar(100),
	indicator_type varchar(100)
);

DROP TABLE IF EXISTS skni_project.financial_indicators_measure CASCADE;
CREATE TABLE IF NOT EXISTS skni_project.financial_indicators_measure(
	id serial PRIMARY KEY,
	id_company integer,
	id_indicator integer,
	indicator_value integer,
	date date,
	FOREIGN KEY (id_indicator) REFERENCES skni_project.financial_indicators (id_indicator),
	FOREIGN KEY (id_company) REFERENCES skni_project.company (id_company)
);

DROP TABLE IF EXISTS skni_project.company_measure CASCADE;
CREATE TABLE IF NOT EXISTS skni_project.company_measure(
	id serial PRIMARY KEY,
	id_company integer,
	id_value integer,
	end_date date,
	value integer,
	FOREIGN KEY (id_company) REFERENCES skni_project.company(id_company),
	FOREIGN KEY (id_value) REFERENCES skni_project.measure(id_value)
);