--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.6
-- Dumped by pg_dump version 10.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


--
-- Name: citext; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;


--
-- Name: EXTENSION citext; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


SET search_path = public, pg_catalog;

--
-- Name: gender_type; Type: TYPE; Schema: public; Owner: nyimbi
--

CREATE TYPE gender_type AS ENUM (
    'Male',
    'Female',
    'Other'
);


ALTER TYPE gender_type OWNER TO nyimbi;

--
-- Name: marital_status_type; Type: TYPE; Schema: public; Owner: nyimbi
--

CREATE TYPE marital_status_type AS ENUM (
    'Single',
    'Married',
    'Divorced',
    'Widowed',
    'Other'
);


ALTER TYPE marital_status_type OWNER TO nyimbi;

--
-- Name: document_search_vector_update(); Type: FUNCTION; Schema: public; Owner: nyimbi
--

CREATE FUNCTION document_search_vector_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
            BEGIN
                NEW.search_vector = to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_text, ''), '[-@.]', ' ', 'g')) || to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_title, ''), '[-@.]', ' ', 'g'));
                RETURN NEW;
            END
            $$;


ALTER FUNCTION public.document_search_vector_update() OWNER TO nyimbi;

--
-- Name: document_version_search_vector_update(); Type: FUNCTION; Schema: public; Owner: nyimbi
--

CREATE FUNCTION document_version_search_vector_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
            BEGIN
                NEW.search_vector = to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_text, ''), '[-@.]', ' ', 'g')) || to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_title, ''), '[-@.]', ' ', 'g'));
                RETURN NEW;
            END
            $$;


ALTER FUNCTION public.document_version_search_vector_update() OWNER TO nyimbi;

--
-- Name: exhibit_search_vector_update(); Type: FUNCTION; Schema: public; Owner: nyimbi
--

CREATE FUNCTION exhibit_search_vector_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
            BEGIN
                NEW.search_vector = to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_text, ''), '[-@.]', ' ', 'g')) || to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_title, ''), '[-@.]', ' ', 'g'));
                RETURN NEW;
            END
            $$;


ALTER FUNCTION public.exhibit_search_vector_update() OWNER TO nyimbi;

--
-- Name: exhibit_version_search_vector_update(); Type: FUNCTION; Schema: public; Owner: nyimbi
--

CREATE FUNCTION exhibit_version_search_vector_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
            BEGIN
                NEW.search_vector = to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_text, ''), '[-@.]', ' ', 'g')) || to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_title, ''), '[-@.]', ' ', 'g'));
                RETURN NEW;
            END
            $$;


ALTER FUNCTION public.exhibit_version_search_vector_update() OWNER TO nyimbi;

--
-- Name: transcript_search_vector_update(); Type: FUNCTION; Schema: public; Owner: nyimbi
--

CREATE FUNCTION transcript_search_vector_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
            BEGIN
                NEW.search_vector = to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_text, ''), '[-@.]', ' ', 'g')) || to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_title, ''), '[-@.]', ' ', 'g'));
                RETURN NEW;
            END
            $$;


ALTER FUNCTION public.transcript_search_vector_update() OWNER TO nyimbi;

--
-- Name: transcript_version_search_vector_update(); Type: FUNCTION; Schema: public; Owner: nyimbi
--

CREATE FUNCTION transcript_version_search_vector_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
            BEGIN
                NEW.search_vector = to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_text, ''), '[-@.]', ' ', 'g')) || to_tsvector('pg_catalog.english', regexp_replace(coalesce(NEW.doc_title, ''), '[-@.]', ' ', 'g'));
                RETURN NEW;
            END
            $$;


ALTER FUNCTION public.transcript_version_search_vector_update() OWNER TO nyimbi;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: ab_permission; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_permission (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE ab_permission OWNER TO nyimbi;

--
-- Name: ab_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_permission_id_seq OWNER TO nyimbi;

--
-- Name: ab_permission_view; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_permission_view (
    id integer NOT NULL,
    permission_id integer,
    view_menu_id integer
);


ALTER TABLE ab_permission_view OWNER TO nyimbi;

--
-- Name: ab_permission_view_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_permission_view_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_permission_view_id_seq OWNER TO nyimbi;

--
-- Name: ab_permission_view_role; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_permission_view_role (
    id integer NOT NULL,
    permission_view_id integer,
    role_id integer
);


ALTER TABLE ab_permission_view_role OWNER TO nyimbi;

--
-- Name: ab_permission_view_role_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_permission_view_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_permission_view_role_id_seq OWNER TO nyimbi;

--
-- Name: ab_register_user; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_register_user (
    id integer NOT NULL,
    first_name character varying(64) NOT NULL,
    last_name character varying(64) NOT NULL,
    username character varying(64) NOT NULL,
    password character varying(256),
    email character varying(64) NOT NULL,
    registration_date timestamp without time zone,
    registration_hash character varying(256)
);


ALTER TABLE ab_register_user OWNER TO nyimbi;

--
-- Name: ab_register_user_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_register_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_register_user_id_seq OWNER TO nyimbi;

--
-- Name: ab_role; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_role (
    id integer NOT NULL,
    name character varying(64) NOT NULL
);


ALTER TABLE ab_role OWNER TO nyimbi;

--
-- Name: ab_role_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_role_id_seq OWNER TO nyimbi;

--
-- Name: ab_user; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_user (
    id integer NOT NULL,
    first_name character varying(64) NOT NULL,
    last_name character varying(64) NOT NULL,
    username character varying(64) NOT NULL,
    password character varying(256),
    active boolean,
    email character varying(64) NOT NULL,
    last_login timestamp without time zone,
    login_count integer,
    fail_login_count integer,
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    created_by_fk integer,
    changed_by_fk integer
);


ALTER TABLE ab_user OWNER TO nyimbi;

--
-- Name: ab_user_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_user_id_seq OWNER TO nyimbi;

--
-- Name: ab_user_role; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_user_role (
    id integer NOT NULL,
    user_id integer,
    role_id integer
);


ALTER TABLE ab_user_role OWNER TO nyimbi;

--
-- Name: ab_user_role_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_user_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_user_role_id_seq OWNER TO nyimbi;

--
-- Name: ab_view_menu; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ab_view_menu (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE ab_view_menu OWNER TO nyimbi;

--
-- Name: ab_view_menu_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ab_view_menu_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ab_view_menu_id_seq OWNER TO nyimbi;

--
-- Name: accounttype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE accounttype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE accounttype OWNER TO nyimbi;

--
-- Name: accounttype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE accounttype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE accounttype_id_seq OWNER TO nyimbi;

--
-- Name: accounttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE accounttype_id_seq OWNED BY accounttype.id;


--
-- Name: accounttype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE accounttype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE accounttype_version OWNER TO nyimbi;

--
-- Name: bill; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE bill (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    assessing_registrar integer,
    receiving_registrar integer,
    lawyer_paying integer,
    party_paying integer,
    documents integer,
    date_of_payment timestamp without time zone,
    paid boolean,
    pay_code character varying(20),
    bill_total numeric(12,2),
    court integer,
    court_account_courts integer,
    court_account_account__types integer,
    validated boolean,
    validation_date timestamp without time zone,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE bill OWNER TO nyimbi;

--
-- Name: bill_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE bill_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bill_id_seq OWNER TO nyimbi;

--
-- Name: bill_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE bill_id_seq OWNED BY bill.id;


--
-- Name: bill_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE bill_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    assessing_registrar integer,
    receiving_registrar integer,
    lawyer_paying integer,
    party_paying integer,
    documents integer,
    date_of_payment timestamp without time zone,
    paid boolean,
    pay_code character varying(20),
    bill_total numeric(12,2),
    court integer,
    court_account_courts integer,
    court_account_account__types integer,
    validated boolean,
    validation_date timestamp without time zone,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE bill_version OWNER TO nyimbi;

--
-- Name: billdetail; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE billdetail (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    receipt_id integer,
    feetype integer,
    purpose text,
    unit text,
    qty integer,
    unit_cost numeric(12,2),
    amount numeric(12,2),
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE billdetail OWNER TO nyimbi;

--
-- Name: billdetail_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE billdetail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE billdetail_id_seq OWNER TO nyimbi;

--
-- Name: billdetail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE billdetail_id_seq OWNED BY billdetail.id;


--
-- Name: billdetail_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE billdetail_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    receipt_id integer,
    feetype integer,
    purpose text,
    unit text,
    qty integer,
    unit_cost numeric(12,2),
    amount numeric(12,2),
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE billdetail_version OWNER TO nyimbi;

--
-- Name: biodata; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE biodata (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    allergies text,
    chronic_conditions text,
    chronic_medications text,
    hbp boolean,
    diabetes boolean,
    hiv boolean,
    current_health_status text,
    bc_id character varying(20),
    bc_number character varying(20),
    bc_serial character varying(20),
    bc_place character varying(20),
    bc_scan text,
    citizenship character varying(20),
    nat_id_num character varying(15),
    nat_id_serial character varying(30),
    nat_id_scan text,
    pp_no character varying(20),
    pp_issue_date date,
    pp_issue_place character varying(40),
    pp_scan text,
    pp_expiry_date date,
    kin1_name character varying(100),
    kin1_phone character varying(50),
    kin1_email character varying(125),
    kin1_addr text,
    kin2_name character varying(100),
    kin1_relation character varying(100),
    kin2_phone character varying(50),
    kin2_email character varying(125),
    kin2_addr text,
    blood_group character varying(3),
    striking_features text,
    height_m double precision,
    weight_kg double precision,
    eye_colour character varying(20),
    hair_colour character varying(20),
    complexion character varying(50),
    ethnicity character varying(40),
    fp_lthumb text,
    fp_left2 text,
    fp_left3 text,
    fp_left4 text,
    fp_left5 text,
    fp_rthumb text,
    fp_right2 text,
    fp_right3 text,
    fp_right4 text,
    fp_right5 text,
    palm_left text,
    palm_right text,
    eye_left text,
    eye_right text,
    m_prn character varying(6),
    m_firstname character varying(40),
    m_surname character varying(40),
    m_othernames character varying(100),
    m_nat_id_num character varying(15),
    m_education character varying(40),
    m_occupation character varying(40),
    m_income character varying(50),
    f_prn character varying(6),
    f_firstname character varying(40),
    f_surname character varying(40),
    f_othernames character varying(100),
    f_nat_id_num character varying(15),
    f_education character varying(40),
    f_occupation character varying(40),
    f_income character varying(50),
    id integer NOT NULL,
    party integer,
    economic_class integer,
    religion integer,
    health_status text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE biodata OWNER TO nyimbi;

--
-- Name: biodata_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE biodata_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE biodata_id_seq OWNER TO nyimbi;

--
-- Name: biodata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE biodata_id_seq OWNED BY biodata.id;


--
-- Name: biodata_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE biodata_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    allergies text,
    chronic_conditions text,
    chronic_medications text,
    hbp boolean,
    diabetes boolean,
    hiv boolean,
    current_health_status text,
    bc_id character varying(20),
    bc_number character varying(20),
    bc_serial character varying(20),
    bc_place character varying(20),
    bc_scan text,
    citizenship character varying(20),
    nat_id_num character varying(15),
    nat_id_serial character varying(30),
    nat_id_scan text,
    pp_no character varying(20),
    pp_issue_date date,
    pp_issue_place character varying(40),
    pp_scan text,
    pp_expiry_date date,
    kin1_name character varying(100),
    kin1_phone character varying(50),
    kin1_email character varying(125),
    kin1_addr text,
    kin2_name character varying(100),
    kin1_relation character varying(100),
    kin2_phone character varying(50),
    kin2_email character varying(125),
    kin2_addr text,
    blood_group character varying(3),
    striking_features text,
    height_m double precision,
    weight_kg double precision,
    eye_colour character varying(20),
    hair_colour character varying(20),
    complexion character varying(50),
    ethnicity character varying(40),
    fp_lthumb text,
    fp_left2 text,
    fp_left3 text,
    fp_left4 text,
    fp_left5 text,
    fp_rthumb text,
    fp_right2 text,
    fp_right3 text,
    fp_right4 text,
    fp_right5 text,
    palm_left text,
    palm_right text,
    eye_left text,
    eye_right text,
    m_prn character varying(6),
    m_firstname character varying(40),
    m_surname character varying(40),
    m_othernames character varying(100),
    m_nat_id_num character varying(15),
    m_education character varying(40),
    m_occupation character varying(40),
    m_income character varying(50),
    f_prn character varying(6),
    f_firstname character varying(40),
    f_surname character varying(40),
    f_othernames character varying(100),
    f_nat_id_num character varying(15),
    f_education character varying(40),
    f_occupation character varying(40),
    f_income character varying(50),
    id integer NOT NULL,
    party integer,
    economic_class integer,
    religion integer,
    health_status text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE biodata_version OWNER TO nyimbi;

--
-- Name: casecategory; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casecategory (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    subcategory integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE casecategory OWNER TO nyimbi;

--
-- Name: casecategory_courtcase; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casecategory_courtcase (
    casecategory integer NOT NULL,
    courtcase integer NOT NULL
);


ALTER TABLE casecategory_courtcase OWNER TO nyimbi;

--
-- Name: casecategory_courtcase_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casecategory_courtcase_version (
    casecategory integer NOT NULL,
    courtcase integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE casecategory_courtcase_version OWNER TO nyimbi;

--
-- Name: casecategory_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE casecategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE casecategory_id_seq OWNER TO nyimbi;

--
-- Name: casecategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE casecategory_id_seq OWNED BY casecategory.id;


--
-- Name: casecategory_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casecategory_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    subcategory integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE casecategory_version OWNER TO nyimbi;

--
-- Name: casecategorychecklist; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casecategorychecklist (
    case_checklists integer NOT NULL,
    case_categories integer NOT NULL
);


ALTER TABLE casecategorychecklist OWNER TO nyimbi;

--
-- Name: casecategorychecklist_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casecategorychecklist_version (
    case_checklists integer NOT NULL,
    case_categories integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE casecategorychecklist_version OWNER TO nyimbi;

--
-- Name: casechecklist; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casechecklist (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    code character varying(20),
    id integer NOT NULL,
    name character varying(100),
    description character varying(100),
    notes text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE casechecklist OWNER TO nyimbi;

--
-- Name: casechecklist_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE casechecklist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE casechecklist_id_seq OWNER TO nyimbi;

--
-- Name: casechecklist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE casechecklist_id_seq OWNED BY casechecklist.id;


--
-- Name: casechecklist_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE casechecklist_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    code character varying(20),
    id integer NOT NULL,
    name character varying(100),
    description character varying(100),
    notes text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE casechecklist_version OWNER TO nyimbi;

--
-- Name: caselinktype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE caselinktype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE caselinktype OWNER TO nyimbi;

--
-- Name: caselinktype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE caselinktype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE caselinktype_id_seq OWNER TO nyimbi;

--
-- Name: caselinktype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE caselinktype_id_seq OWNED BY caselinktype.id;


--
-- Name: caselinktype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE caselinktype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE caselinktype_version OWNER TO nyimbi;

--
-- Name: celltype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE celltype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE celltype OWNER TO nyimbi;

--
-- Name: celltype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE celltype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE celltype_id_seq OWNER TO nyimbi;

--
-- Name: celltype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE celltype_id_seq OWNED BY celltype.id;


--
-- Name: celltype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE celltype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE celltype_version OWNER TO nyimbi;

--
-- Name: commital; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE commital (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    priority integer,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    prisons integer,
    police_station integer,
    parties integer,
    casecomplete boolean,
    commit_date date,
    purpose text,
    warrant_type integer,
    warrant_docx text,
    warrant_issue_date date,
    warrant_issued_by text,
    warrant_date_attached timestamp without time zone,
    duration interval,
    commital integer,
    commital_type integer,
    court_case integer,
    concurrent boolean,
    life_imprisonment boolean,
    arrival_date timestamp without time zone,
    sentence_start_date timestamp without time zone,
    arrest_date timestamp without time zone,
    remaining_years integer,
    remaining_months integer,
    remaining_days integer,
    cell_number text,
    cell_type integer,
    release_date timestamp without time zone,
    exit_date timestamp without time zone,
    reason_for_release text,
    with_children boolean,
    release_type integer,
    receiving_officer integer,
    releasing_officer integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE commital OWNER TO nyimbi;

--
-- Name: commital_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE commital_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE commital_id_seq OWNER TO nyimbi;

--
-- Name: commital_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE commital_id_seq OWNED BY commital.id;


--
-- Name: commital_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE commital_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    priority integer,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    prisons integer,
    police_station integer,
    parties integer,
    casecomplete boolean,
    commit_date date,
    purpose text,
    warrant_type integer,
    warrant_docx text,
    warrant_issue_date date,
    warrant_issued_by text,
    warrant_date_attached timestamp without time zone,
    duration interval,
    commital integer,
    commital_type integer,
    court_case integer,
    concurrent boolean,
    life_imprisonment boolean,
    arrival_date timestamp without time zone,
    sentence_start_date timestamp without time zone,
    arrest_date timestamp without time zone,
    remaining_years integer,
    remaining_months integer,
    remaining_days integer,
    cell_number text,
    cell_type integer,
    release_date timestamp without time zone,
    exit_date timestamp without time zone,
    reason_for_release text,
    with_children boolean,
    release_type integer,
    receiving_officer integer,
    releasing_officer integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE commital_version OWNER TO nyimbi;

--
-- Name: commitaltype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE commitaltype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    maxduration interval,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE commitaltype OWNER TO nyimbi;

--
-- Name: commitaltype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE commitaltype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE commitaltype_id_seq OWNER TO nyimbi;

--
-- Name: commitaltype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE commitaltype_id_seq OWNED BY commitaltype.id;


--
-- Name: commitaltype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE commitaltype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    maxduration interval,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE commitaltype_version OWNER TO nyimbi;

--
-- Name: complaint; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaint (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    active boolean,
    ob_number character varying(20),
    police_station integer,
    daterecvd timestamp without time zone,
    datefiled timestamp without time zone,
    datecaseopened timestamp without time zone,
    casesummary character varying(2000),
    complaintstatement text,
    circumstances text,
    reportingofficer integer,
    casefileinformation text,
    p_request_help boolean,
    p_instruction text,
    p_submitted boolean,
    p_submission_date timestamp without time zone,
    p_submission_notes text,
    p_closed text,
    p_evaluation text,
    p_recommend_charge boolean,
    charge_sheet text,
    charge_sheet_docx text,
    evaluating_prosecutor_team integer,
    magistrate_report_date timestamp without time zone,
    reported_to_judicial_officer integer,
    closed boolean,
    close_date timestamp without time zone,
    close_reason text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE complaint OWNER TO nyimbi;

--
-- Name: complaint_complaintcategory; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaint_complaintcategory (
    complaint integer NOT NULL,
    complaintcategory integer NOT NULL
);


ALTER TABLE complaint_complaintcategory OWNER TO nyimbi;

--
-- Name: complaint_complaintcategory_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaint_complaintcategory_version (
    complaint integer NOT NULL,
    complaintcategory integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE complaint_complaintcategory_version OWNER TO nyimbi;

--
-- Name: complaint_courtcase; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaint_courtcase (
    complaint integer NOT NULL,
    courtcase integer NOT NULL
);


ALTER TABLE complaint_courtcase OWNER TO nyimbi;

--
-- Name: complaint_courtcase_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaint_courtcase_version (
    complaint integer NOT NULL,
    courtcase integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE complaint_courtcase_version OWNER TO nyimbi;

--
-- Name: complaint_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE complaint_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE complaint_id_seq OWNER TO nyimbi;

--
-- Name: complaint_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE complaint_id_seq OWNED BY complaint.id;


--
-- Name: complaint_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaint_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    active boolean,
    ob_number character varying(20),
    police_station integer,
    daterecvd timestamp without time zone,
    datefiled timestamp without time zone,
    datecaseopened timestamp without time zone,
    casesummary character varying(2000),
    complaintstatement text,
    circumstances text,
    reportingofficer integer,
    casefileinformation text,
    p_request_help boolean,
    p_instruction text,
    p_submitted boolean,
    p_submission_date timestamp without time zone,
    p_submission_notes text,
    p_closed text,
    p_evaluation text,
    p_recommend_charge boolean,
    charge_sheet text,
    charge_sheet_docx text,
    evaluating_prosecutor_team integer,
    magistrate_report_date timestamp without time zone,
    reported_to_judicial_officer integer,
    closed boolean,
    close_date timestamp without time zone,
    close_reason text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE complaint_version OWNER TO nyimbi;

--
-- Name: complaintcategory; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaintcategory (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    complaint_category_parent integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE complaintcategory OWNER TO nyimbi;

--
-- Name: complaintcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE complaintcategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE complaintcategory_id_seq OWNER TO nyimbi;

--
-- Name: complaintcategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE complaintcategory_id_seq OWNED BY complaintcategory.id;


--
-- Name: complaintcategory_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaintcategory_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    complaint_category_parent integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE complaintcategory_version OWNER TO nyimbi;

--
-- Name: complaintrole; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaintrole (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE complaintrole OWNER TO nyimbi;

--
-- Name: complaintrole_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE complaintrole_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE complaintrole_id_seq OWNER TO nyimbi;

--
-- Name: complaintrole_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE complaintrole_id_seq OWNED BY complaintrole.id;


--
-- Name: complaintrole_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE complaintrole_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE complaintrole_version OWNER TO nyimbi;

--
-- Name: country; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE country (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    name text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE country OWNER TO nyimbi;

--
-- Name: country_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE country_id_seq OWNER TO nyimbi;

--
-- Name: country_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE country_id_seq OWNED BY country.id;


--
-- Name: country_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE country_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    name text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE country_version OWNER TO nyimbi;

--
-- Name: county; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE county (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    country integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE county OWNER TO nyimbi;

--
-- Name: county_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE county_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE county_id_seq OWNER TO nyimbi;

--
-- Name: county_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE county_id_seq OWNED BY county.id;


--
-- Name: county_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE county_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    country integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE county_version OWNER TO nyimbi;

--
-- Name: court; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE court (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    place_name character varying(40),
    lat numeric(12,7),
    lng numeric(12,7),
    alt numeric(12,7),
    map text,
    info text,
    pin boolean,
    pin_color character varying(20),
    pin_icon character varying(50),
    centered boolean,
    nearest_feature character varying(100),
    id integer NOT NULL,
    court_rank integer,
    court_station integer,
    town integer,
    till_number text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE court OWNER TO nyimbi;

--
-- Name: court_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE court_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE court_id_seq OWNER TO nyimbi;

--
-- Name: court_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE court_id_seq OWNED BY court.id;


--
-- Name: court_judicialofficer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE court_judicialofficer (
    court integer NOT NULL,
    judicialofficer integer NOT NULL
);


ALTER TABLE court_judicialofficer OWNER TO nyimbi;

--
-- Name: court_judicialofficer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE court_judicialofficer_version (
    court integer NOT NULL,
    judicialofficer integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE court_judicialofficer_version OWNER TO nyimbi;

--
-- Name: court_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE court_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    place_name character varying(40),
    lat numeric(12,7),
    lng numeric(12,7),
    alt numeric(12,7),
    map text,
    info text,
    pin boolean,
    pin_color character varying(20),
    pin_icon character varying(50),
    centered boolean,
    nearest_feature character varying(100),
    id integer NOT NULL,
    court_rank integer,
    court_station integer,
    town integer,
    till_number text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE court_version OWNER TO nyimbi;

--
-- Name: courtaccount; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtaccount (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    courts integer NOT NULL,
    account__types integer NOT NULL,
    account_number text,
    account_name text,
    short_code text,
    bank_name text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE courtaccount OWNER TO nyimbi;

--
-- Name: courtaccount_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtaccount_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    courts integer NOT NULL,
    account__types integer NOT NULL,
    account_number text,
    account_name text,
    short_code text,
    bank_name text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE courtaccount_version OWNER TO nyimbi;

--
-- Name: courtcase; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtcase (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    docket_number text,
    case_number text,
    adr boolean,
    mediation_proposal text,
    case_received_date date,
    case_filed_date date,
    case_summary text,
    filing_prosecutor integer,
    fast_track boolean,
    priority integer,
    object_of_litigation text,
    grounds text,
    prosecution_prayer text,
    pretrial_date date,
    pretrial_notes text,
    pretrial_registrar integer,
    case_admissible boolean,
    indictment_date text,
    judgement text,
    judgement_docx text,
    case_link_type integer,
    linked_cases integer,
    appealed boolean,
    appeal_number text,
    inventory_of_docket text,
    next_hearing_date date,
    interlocutory_judgement text,
    reopen boolean,
    reopen_reason text,
    combined_case boolean,
    value_in_dispute numeric(12,2),
    award numeric(12,2),
    govt_liability text,
    active boolean,
    active_date timestamp without time zone,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE courtcase OWNER TO nyimbi;

--
-- Name: courtcase_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE courtcase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courtcase_id_seq OWNER TO nyimbi;

--
-- Name: courtcase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE courtcase_id_seq OWNED BY courtcase.id;


--
-- Name: courtcase_judicialofficer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtcase_judicialofficer (
    courtcase integer NOT NULL,
    judicialofficer integer NOT NULL
);


ALTER TABLE courtcase_judicialofficer OWNER TO nyimbi;

--
-- Name: courtcase_judicialofficer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtcase_judicialofficer_version (
    courtcase integer NOT NULL,
    judicialofficer integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE courtcase_judicialofficer_version OWNER TO nyimbi;

--
-- Name: courtcase_lawfirm; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtcase_lawfirm (
    courtcase integer NOT NULL,
    lawfirm integer NOT NULL
);


ALTER TABLE courtcase_lawfirm OWNER TO nyimbi;

--
-- Name: courtcase_lawfirm_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtcase_lawfirm_version (
    courtcase integer NOT NULL,
    lawfirm integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE courtcase_lawfirm_version OWNER TO nyimbi;

--
-- Name: courtcase_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtcase_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    docket_number text,
    case_number text,
    adr boolean,
    mediation_proposal text,
    case_received_date date,
    case_filed_date date,
    case_summary text,
    filing_prosecutor integer,
    fast_track boolean,
    priority integer,
    object_of_litigation text,
    grounds text,
    prosecution_prayer text,
    pretrial_date date,
    pretrial_notes text,
    pretrial_registrar integer,
    case_admissible boolean,
    indictment_date text,
    judgement text,
    judgement_docx text,
    case_link_type integer,
    linked_cases integer,
    appealed boolean,
    appeal_number text,
    inventory_of_docket text,
    next_hearing_date date,
    interlocutory_judgement text,
    reopen boolean,
    reopen_reason text,
    combined_case boolean,
    value_in_dispute numeric(12,2),
    award numeric(12,2),
    govt_liability text,
    active boolean,
    active_date timestamp without time zone,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE courtcase_version OWNER TO nyimbi;

--
-- Name: courtrank; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtrank (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE courtrank OWNER TO nyimbi;

--
-- Name: courtrank_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE courtrank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courtrank_id_seq OWNER TO nyimbi;

--
-- Name: courtrank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE courtrank_id_seq OWNED BY courtrank.id;


--
-- Name: courtrank_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtrank_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE courtrank_version OWNER TO nyimbi;

--
-- Name: courtstation; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtstation (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    till_number text,
    pay_bill text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE courtstation OWNER TO nyimbi;

--
-- Name: courtstation_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE courtstation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE courtstation_id_seq OWNER TO nyimbi;

--
-- Name: courtstation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE courtstation_id_seq OWNED BY courtstation.id;


--
-- Name: courtstation_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE courtstation_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    till_number text,
    pay_bill text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE courtstation_version OWNER TO nyimbi;

--
-- Name: crime; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE crime (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    law text,
    description text,
    ref text,
    ref_law integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE crime OWNER TO nyimbi;

--
-- Name: crime_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE crime_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE crime_id_seq OWNER TO nyimbi;

--
-- Name: crime_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE crime_id_seq OWNED BY crime.id;


--
-- Name: crime_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE crime_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    law text,
    description text,
    ref text,
    ref_law integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE crime_version OWNER TO nyimbi;

--
-- Name: csi_equipment; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE csi_equipment (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE csi_equipment OWNER TO nyimbi;

--
-- Name: csi_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE csi_equipment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE csi_equipment_id_seq OWNER TO nyimbi;

--
-- Name: csi_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE csi_equipment_id_seq OWNED BY csi_equipment.id;


--
-- Name: csi_equipment_investigationdiary; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE csi_equipment_investigationdiary (
    csi_equipment integer NOT NULL,
    investigationdiary integer NOT NULL
);


ALTER TABLE csi_equipment_investigationdiary OWNER TO nyimbi;

--
-- Name: csi_equipment_investigationdiary_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE csi_equipment_investigationdiary_version (
    csi_equipment integer NOT NULL,
    investigationdiary integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE csi_equipment_investigationdiary_version OWNER TO nyimbi;

--
-- Name: csi_equipment_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE csi_equipment_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE csi_equipment_version OWNER TO nyimbi;

--
-- Name: diagram; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE diagram (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    investigation_diary integer,
    image text,
    description text,
    docx text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE diagram OWNER TO nyimbi;

--
-- Name: diagram_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE diagram_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE diagram_id_seq OWNER TO nyimbi;

--
-- Name: diagram_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE diagram_id_seq OWNED BY diagram.id;


--
-- Name: diagram_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE diagram_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    investigation_diary integer,
    image text,
    description text,
    docx text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE diagram_version OWNER TO nyimbi;

--
-- Name: discipline; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE discipline (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    party integer,
    prison_officer integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE discipline OWNER TO nyimbi;

--
-- Name: discipline_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE discipline_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE discipline_id_seq OWNER TO nyimbi;

--
-- Name: discipline_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE discipline_id_seq OWNED BY discipline.id;


--
-- Name: discipline_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE discipline_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    party integer,
    prison_officer integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE discipline_version OWNER TO nyimbi;

--
-- Name: doctemplate; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE doctemplate (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    template text,
    docx text,
    name text,
    title text,
    summary text,
    template_type integer,
    icon text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE doctemplate OWNER TO nyimbi;

--
-- Name: doctemplate_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE doctemplate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE doctemplate_id_seq OWNER TO nyimbi;

--
-- Name: doctemplate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE doctemplate_id_seq OWNED BY doctemplate.id;


--
-- Name: doctemplate_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE doctemplate_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    template text,
    docx text,
    name text,
    title text,
    summary text,
    template_type integer,
    icon text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE doctemplate_version OWNER TO nyimbi;

--
-- Name: document; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE document (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    mime_type character varying(60),
    doc text,
    doc_text text,
    doc_binary text,
    doc_title character varying(200),
    subject character varying(100),
    author character varying(100),
    keywords character varying(200),
    comments text,
    doc_type character varying(5),
    char_count integer,
    word_count integer,
    lines integer,
    paragraphs integer,
    file_size_bytes integer,
    producer_prog character varying(40),
    immutable boolean,
    page_size character varying(40),
    hashx character varying(40),
    audio_duration_secs integer,
    audio_frame_rate integer,
    audio_channels integer,
    search_vector tsvector,
    id integer NOT NULL,
    name text,
    court_case integer,
    issue integer,
    document_admissibility text,
    admitted boolean,
    judicial_officer integer,
    filing_date timestamp without time zone,
    admisibility_notes text,
    docx text,
    document_text text,
    published boolean,
    publish_newspaper text,
    publish_date date,
    validated boolean,
    paid boolean,
    page_count integer,
    file_byte_count numeric(12,2),
    file_hash text,
    file_timestamp text,
    file_create_date timestamp without time zone,
    file_update_date timestamp without time zone,
    file_text text,
    file_ext text,
    file_load_path text,
    file_upload_date timestamp without time zone,
    file_parse_status text,
    doc_template integer,
    visible boolean,
    is_scan boolean,
    doc_shelf text,
    doc_row text,
    doc_room text,
    doc_placed_by text,
    citation text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE document OWNER TO nyimbi;

--
-- Name: document_documenttype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE document_documenttype (
    document integer NOT NULL,
    documenttype integer NOT NULL
);


ALTER TABLE document_documenttype OWNER TO nyimbi;

--
-- Name: document_documenttype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE document_documenttype_version (
    document integer NOT NULL,
    documenttype integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE document_documenttype_version OWNER TO nyimbi;

--
-- Name: document_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE document_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE document_id_seq OWNER TO nyimbi;

--
-- Name: document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE document_id_seq OWNED BY document.id;


--
-- Name: document_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE document_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    mime_type character varying(60),
    doc text,
    doc_text text,
    doc_binary text,
    doc_title character varying(200),
    subject character varying(100),
    author character varying(100),
    keywords character varying(200),
    comments text,
    doc_type character varying(5),
    char_count integer,
    word_count integer,
    lines integer,
    paragraphs integer,
    file_size_bytes integer,
    producer_prog character varying(40),
    immutable boolean,
    page_size character varying(40),
    hashx character varying(40),
    audio_duration_secs integer,
    audio_frame_rate integer,
    audio_channels integer,
    search_vector tsvector,
    id integer NOT NULL,
    name text,
    court_case integer,
    issue integer,
    document_admissibility text,
    admitted boolean,
    judicial_officer integer,
    filing_date timestamp without time zone,
    admisibility_notes text,
    docx text,
    document_text text,
    published boolean,
    publish_newspaper text,
    publish_date date,
    validated boolean,
    paid boolean,
    page_count integer,
    file_byte_count numeric(12,2),
    file_hash text,
    file_timestamp text,
    file_create_date timestamp without time zone,
    file_update_date timestamp without time zone,
    file_text text,
    file_ext text,
    file_load_path text,
    file_upload_date timestamp without time zone,
    file_parse_status text,
    doc_template integer,
    visible boolean,
    is_scan boolean,
    doc_shelf text,
    doc_row text,
    doc_room text,
    doc_placed_by text,
    citation text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE document_version OWNER TO nyimbi;

--
-- Name: documenttype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE documenttype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE documenttype OWNER TO nyimbi;

--
-- Name: documenttype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE documenttype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE documenttype_id_seq OWNER TO nyimbi;

--
-- Name: documenttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE documenttype_id_seq OWNED BY documenttype.id;


--
-- Name: documenttype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE documenttype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE documenttype_version OWNER TO nyimbi;

--
-- Name: economicclass; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE economicclass (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    code character varying(20),
    notes text,
    id integer NOT NULL,
    name character varying(50),
    description character varying(100),
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE economicclass OWNER TO nyimbi;

--
-- Name: economicclass_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE economicclass_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE economicclass_id_seq OWNER TO nyimbi;

--
-- Name: economicclass_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE economicclass_id_seq OWNED BY economicclass.id;


--
-- Name: economicclass_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE economicclass_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    code character varying(20),
    notes text,
    id integer NOT NULL,
    name character varying(50),
    description character varying(100),
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE economicclass_version OWNER TO nyimbi;

--
-- Name: exhibit; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE exhibit (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    mime_type character varying(60),
    doc text,
    doc_text text,
    doc_binary text,
    doc_title character varying(200),
    subject character varying(100),
    author character varying(100),
    keywords character varying(200),
    comments text,
    doc_type character varying(5),
    char_count integer,
    word_count integer,
    lines integer,
    paragraphs integer,
    file_size_bytes integer,
    producer_prog character varying(40),
    immutable boolean,
    page_size character varying(40),
    page_count integer,
    hashx character varying(40),
    audio_duration_secs integer,
    audio_frame_rate integer,
    audio_channels integer,
    search_vector tsvector,
    id integer NOT NULL,
    investigation_entry integer,
    exhibit_no text,
    docx text,
    seizure integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE exhibit OWNER TO nyimbi;

--
-- Name: exhibit_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE exhibit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE exhibit_id_seq OWNER TO nyimbi;

--
-- Name: exhibit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE exhibit_id_seq OWNED BY exhibit.id;


--
-- Name: exhibit_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE exhibit_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    mime_type character varying(60),
    doc text,
    doc_text text,
    doc_binary text,
    doc_title character varying(200),
    subject character varying(100),
    author character varying(100),
    keywords character varying(200),
    comments text,
    doc_type character varying(5),
    char_count integer,
    word_count integer,
    lines integer,
    paragraphs integer,
    file_size_bytes integer,
    producer_prog character varying(40),
    immutable boolean,
    page_size character varying(40),
    page_count integer,
    hashx character varying(40),
    audio_duration_secs integer,
    audio_frame_rate integer,
    audio_channels integer,
    search_vector tsvector,
    id integer NOT NULL,
    investigation_entry integer,
    exhibit_no text,
    docx text,
    seizure integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE exhibit_version OWNER TO nyimbi;

--
-- Name: expert; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE expert (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    institution text,
    jobtitle text,
    credentials text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE expert OWNER TO nyimbi;

--
-- Name: expert_experttype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE expert_experttype (
    expert integer NOT NULL,
    experttype integer NOT NULL
);


ALTER TABLE expert_experttype OWNER TO nyimbi;

--
-- Name: expert_experttype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE expert_experttype_version (
    expert integer NOT NULL,
    experttype integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE expert_experttype_version OWNER TO nyimbi;

--
-- Name: expert_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE expert_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE expert_id_seq OWNER TO nyimbi;

--
-- Name: expert_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE expert_id_seq OWNED BY expert.id;


--
-- Name: expert_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE expert_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    institution text,
    jobtitle text,
    credentials text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE expert_version OWNER TO nyimbi;

--
-- Name: experttestimony; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE experttestimony (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    investigation_entries integer NOT NULL,
    experts integer NOT NULL,
    task_given text,
    summary_of_facts text,
    statement text,
    task_request_date date,
    testimony_date timestamp without time zone,
    validated boolean,
    requesting_police_officer integer,
    court_case integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE experttestimony OWNER TO nyimbi;

--
-- Name: experttestimony_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE experttestimony_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    investigation_entries integer NOT NULL,
    experts integer NOT NULL,
    task_given text,
    summary_of_facts text,
    statement text,
    task_request_date date,
    testimony_date timestamp without time zone,
    validated boolean,
    requesting_police_officer integer,
    court_case integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE experttestimony_version OWNER TO nyimbi;

--
-- Name: experttype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE experttype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    expert_type integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE experttype OWNER TO nyimbi;

--
-- Name: experttype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE experttype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE experttype_id_seq OWNER TO nyimbi;

--
-- Name: experttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE experttype_id_seq OWNED BY experttype.id;


--
-- Name: experttype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE experttype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    expert_type integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE experttype_version OWNER TO nyimbi;

--
-- Name: feeclass; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE feeclass (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    fee_type integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE feeclass OWNER TO nyimbi;

--
-- Name: feeclass_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE feeclass_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE feeclass_id_seq OWNER TO nyimbi;

--
-- Name: feeclass_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE feeclass_id_seq OWNED BY feeclass.id;


--
-- Name: feeclass_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE feeclass_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    fee_type integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE feeclass_version OWNER TO nyimbi;

--
-- Name: feetype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE feetype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    notes text,
    id integer NOT NULL,
    filing_fee_type integer,
    amount numeric(12,2),
    unit text,
    min_fee numeric(12,2),
    max_fee numeric(12,2),
    description text,
    guide_sec text,
    guide_clause text,
    account_type integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE feetype OWNER TO nyimbi;

--
-- Name: feetype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE feetype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE feetype_id_seq OWNER TO nyimbi;

--
-- Name: feetype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE feetype_id_seq OWNED BY feetype.id;


--
-- Name: feetype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE feetype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    notes text,
    id integer NOT NULL,
    filing_fee_type integer,
    amount numeric(12,2),
    unit text,
    min_fee numeric(12,2),
    max_fee numeric(12,2),
    description text,
    guide_sec text,
    guide_clause text,
    account_type integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE feetype_version OWNER TO nyimbi;

--
-- Name: healthevent; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE healthevent (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    priority integer,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    party integer,
    reporting_prison_officer integer,
    health_event_type integer,
    startdate timestamp without time zone,
    enddate timestamp without time zone,
    notes text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE healthevent OWNER TO nyimbi;

--
-- Name: healthevent_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE healthevent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE healthevent_id_seq OWNER TO nyimbi;

--
-- Name: healthevent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE healthevent_id_seq OWNED BY healthevent.id;


--
-- Name: healthevent_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE healthevent_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    priority integer,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    party integer,
    reporting_prison_officer integer,
    health_event_type integer,
    startdate timestamp without time zone,
    enddate timestamp without time zone,
    notes text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE healthevent_version OWNER TO nyimbi;

--
-- Name: healtheventtype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE healtheventtype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE healtheventtype OWNER TO nyimbi;

--
-- Name: healtheventtype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE healtheventtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE healtheventtype_id_seq OWNER TO nyimbi;

--
-- Name: healtheventtype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE healtheventtype_id_seq OWNED BY healtheventtype.id;


--
-- Name: healtheventtype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE healtheventtype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE healtheventtype_version OWNER TO nyimbi;

--
-- Name: hearing; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    priority integer,
    segment integer,
    task_group integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    court_cases integer,
    hearing_type integer,
    schedule_status integer,
    hearing_date date,
    reason text,
    sequence bigint,
    yearday bigint,
    starttime time without time zone,
    endtime time without time zone,
    notes text,
    completed boolean,
    adjourned_to date,
    adjournment_reason text,
    transcript text,
    atendance text,
    next_hearing_date date,
    postponement_reason text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE hearing OWNER TO nyimbi;

--
-- Name: hearing_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE hearing_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE hearing_id_seq OWNER TO nyimbi;

--
-- Name: hearing_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE hearing_id_seq OWNED BY hearing.id;


--
-- Name: hearing_issue; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_issue (
    hearing integer NOT NULL,
    issue integer NOT NULL
);


ALTER TABLE hearing_issue OWNER TO nyimbi;

--
-- Name: hearing_issue_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_issue_version (
    hearing integer NOT NULL,
    issue integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE hearing_issue_version OWNER TO nyimbi;

--
-- Name: hearing_judicialofficer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_judicialofficer (
    hearing integer NOT NULL,
    judicialofficer integer NOT NULL
);


ALTER TABLE hearing_judicialofficer OWNER TO nyimbi;

--
-- Name: hearing_judicialofficer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_judicialofficer_version (
    hearing integer NOT NULL,
    judicialofficer integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE hearing_judicialofficer_version OWNER TO nyimbi;

--
-- Name: hearing_lawfirm; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_lawfirm (
    hearing integer NOT NULL,
    lawfirm integer NOT NULL
);


ALTER TABLE hearing_lawfirm OWNER TO nyimbi;

--
-- Name: hearing_lawfirm_2; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_lawfirm_2 (
    hearing integer NOT NULL,
    lawfirm integer NOT NULL
);


ALTER TABLE hearing_lawfirm_2 OWNER TO nyimbi;

--
-- Name: hearing_lawfirm_2_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_lawfirm_2_version (
    hearing integer NOT NULL,
    lawfirm integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE hearing_lawfirm_2_version OWNER TO nyimbi;

--
-- Name: hearing_lawfirm_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_lawfirm_version (
    hearing integer NOT NULL,
    lawfirm integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE hearing_lawfirm_version OWNER TO nyimbi;

--
-- Name: hearing_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearing_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    priority integer,
    segment integer,
    task_group integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    court_cases integer,
    hearing_type integer,
    schedule_status integer,
    hearing_date date,
    reason text,
    sequence bigint,
    yearday bigint,
    starttime time without time zone,
    endtime time without time zone,
    notes text,
    completed boolean,
    adjourned_to date,
    adjournment_reason text,
    transcript text,
    atendance text,
    next_hearing_date date,
    postponement_reason text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE hearing_version OWNER TO nyimbi;

--
-- Name: hearingtype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearingtype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    hearing_type integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE hearingtype OWNER TO nyimbi;

--
-- Name: hearingtype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE hearingtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE hearingtype_id_seq OWNER TO nyimbi;

--
-- Name: hearingtype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE hearingtype_id_seq OWNED BY hearingtype.id;


--
-- Name: hearingtype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE hearingtype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    hearing_type integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE hearingtype_version OWNER TO nyimbi;

--
-- Name: instancecrime; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE instancecrime (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    parties integer,
    crimes integer,
    crime_detail text,
    tffender_type text,
    crime_date timestamp without time zone,
    date_note text,
    place_of_crime text,
    place_note text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE instancecrime OWNER TO nyimbi;

--
-- Name: instancecrime_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE instancecrime_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instancecrime_id_seq OWNER TO nyimbi;

--
-- Name: instancecrime_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE instancecrime_id_seq OWNED BY instancecrime.id;


--
-- Name: instancecrime_issue; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE instancecrime_issue (
    instancecrime integer NOT NULL,
    issue integer NOT NULL
);


ALTER TABLE instancecrime_issue OWNER TO nyimbi;

--
-- Name: instancecrime_issue_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE instancecrime_issue_version (
    instancecrime integer NOT NULL,
    issue integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE instancecrime_issue_version OWNER TO nyimbi;

--
-- Name: instancecrime_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE instancecrime_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    parties integer,
    crimes integer,
    crime_detail text,
    tffender_type text,
    crime_date timestamp without time zone,
    date_note text,
    place_of_crime text,
    place_note text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE instancecrime_version OWNER TO nyimbi;

--
-- Name: interview; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE interview (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    investigation_entry integer,
    question text,
    answer text,
    validated boolean,
    language text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE interview OWNER TO nyimbi;

--
-- Name: interview_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE interview_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE interview_id_seq OWNER TO nyimbi;

--
-- Name: interview_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE interview_id_seq OWNED BY interview.id;


--
-- Name: interview_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE interview_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    investigation_entry integer,
    question text,
    answer text,
    validated boolean,
    language text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE interview_version OWNER TO nyimbi;

--
-- Name: investigationdiary; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    priority integer,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    activity text,
    complaint integer,
    location text,
    outcome text,
    equipmentresults text,
    startdate timestamp without time zone,
    enddate timestamp without time zone,
    advocate_present text,
    summons_statement text,
    arrest_statement text,
    arrest_warrant text,
    search_seizure_statement text,
    docx text,
    detained text,
    detained_at text,
    provisional_release_statement text,
    warrant_type integer,
    warrant_issued_by text,
    warrant_issue_date date,
    warrant_delivered_by text,
    warrant_received_by text,
    warrant_serve_date text,
    warrant_docx text,
    warrant_upload_date text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE investigationdiary OWNER TO nyimbi;

--
-- Name: investigationdiary_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE investigationdiary_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE investigationdiary_id_seq OWNER TO nyimbi;

--
-- Name: investigationdiary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE investigationdiary_id_seq OWNED BY investigationdiary.id;


--
-- Name: investigationdiary_party; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary_party (
    investigationdiary integer NOT NULL,
    party integer NOT NULL
);


ALTER TABLE investigationdiary_party OWNER TO nyimbi;

--
-- Name: investigationdiary_party_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary_party_version (
    investigationdiary integer NOT NULL,
    party integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE investigationdiary_party_version OWNER TO nyimbi;

--
-- Name: investigationdiary_policeofficer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary_policeofficer (
    investigationdiary integer NOT NULL,
    policeofficer integer NOT NULL
);


ALTER TABLE investigationdiary_policeofficer OWNER TO nyimbi;

--
-- Name: investigationdiary_policeofficer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary_policeofficer_version (
    investigationdiary integer NOT NULL,
    policeofficer integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE investigationdiary_policeofficer_version OWNER TO nyimbi;

--
-- Name: investigationdiary_vehicle; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary_vehicle (
    investigationdiary integer NOT NULL,
    vehicle integer NOT NULL
);


ALTER TABLE investigationdiary_vehicle OWNER TO nyimbi;

--
-- Name: investigationdiary_vehicle_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary_vehicle_version (
    investigationdiary integer NOT NULL,
    vehicle integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE investigationdiary_vehicle_version OWNER TO nyimbi;

--
-- Name: investigationdiary_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE investigationdiary_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    priority integer,
    segment integer,
    task_group integer,
    sequence integer,
    action character varying(40),
    activity_description text,
    goal text,
    status character varying(40),
    planned_start date,
    actual_start date,
    start_delay interval,
    start_notes character varying(100),
    active boolean,
    planned_end date,
    actual_end timestamp without time zone,
    end_delay interval,
    end_notes character varying(100),
    deadline date,
    not_started boolean,
    early_start boolean,
    late_start boolean,
    completed boolean,
    early_end boolean,
    late_end boolean,
    deviation_expected boolean,
    contingency_plan text,
    budget numeric(10,2),
    spend_td numeric(10,2),
    balance_avail numeric(10,2),
    over_budget boolean,
    under_budget boolean,
    id integer NOT NULL,
    activity text,
    complaint integer,
    location text,
    outcome text,
    equipmentresults text,
    startdate timestamp without time zone,
    enddate timestamp without time zone,
    advocate_present text,
    summons_statement text,
    arrest_statement text,
    arrest_warrant text,
    search_seizure_statement text,
    docx text,
    detained text,
    detained_at text,
    provisional_release_statement text,
    warrant_type integer,
    warrant_issued_by text,
    warrant_issue_date date,
    warrant_delivered_by text,
    warrant_received_by text,
    warrant_serve_date text,
    warrant_docx text,
    warrant_upload_date text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE investigationdiary_version OWNER TO nyimbi;

--
-- Name: issue; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    issue text,
    facts text,
    counter_claim boolean,
    argument text,
    argument_date date,
    argument_docx text,
    rebuttal text,
    rebuttal_date date,
    rebuttal_docx text,
    hearing_date date,
    determination text,
    dtermination_date date,
    determination_docx text,
    resolved boolean,
    defense_lawyer integer,
    prosecutor integer,
    judicial_officer integer,
    court_case integer,
    tasks text,
    is_criminal boolean,
    moral_element text,
    material_element text,
    legal_element text,
    debt_amount numeric(12,2),
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE issue OWNER TO nyimbi;

--
-- Name: issue_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE issue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE issue_id_seq OWNER TO nyimbi;

--
-- Name: issue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE issue_id_seq OWNED BY issue.id;


--
-- Name: issue_lawyer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_lawyer (
    issue integer NOT NULL,
    lawyer integer NOT NULL
);


ALTER TABLE issue_lawyer OWNER TO nyimbi;

--
-- Name: issue_lawyer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_lawyer_version (
    issue integer NOT NULL,
    lawyer integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE issue_lawyer_version OWNER TO nyimbi;

--
-- Name: issue_legalreference; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_legalreference (
    issue integer NOT NULL,
    legalreference integer NOT NULL
);


ALTER TABLE issue_legalreference OWNER TO nyimbi;

--
-- Name: issue_legalreference_2; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_legalreference_2 (
    issue integer NOT NULL,
    legalreference integer NOT NULL
);


ALTER TABLE issue_legalreference_2 OWNER TO nyimbi;

--
-- Name: issue_legalreference_2_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_legalreference_2_version (
    issue integer NOT NULL,
    legalreference integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE issue_legalreference_2_version OWNER TO nyimbi;

--
-- Name: issue_legalreference_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_legalreference_version (
    issue integer NOT NULL,
    legalreference integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE issue_legalreference_version OWNER TO nyimbi;

--
-- Name: issue_party; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_party (
    issue integer NOT NULL,
    party integer NOT NULL
);


ALTER TABLE issue_party OWNER TO nyimbi;

--
-- Name: issue_party_2; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_party_2 (
    issue integer NOT NULL,
    party integer NOT NULL
);


ALTER TABLE issue_party_2 OWNER TO nyimbi;

--
-- Name: issue_party_2_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_party_2_version (
    issue integer NOT NULL,
    party integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE issue_party_2_version OWNER TO nyimbi;

--
-- Name: issue_party_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_party_version (
    issue integer NOT NULL,
    party integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE issue_party_version OWNER TO nyimbi;

--
-- Name: issue_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE issue_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    issue text,
    facts text,
    counter_claim boolean,
    argument text,
    argument_date date,
    argument_docx text,
    rebuttal text,
    rebuttal_date date,
    rebuttal_docx text,
    hearing_date date,
    determination text,
    dtermination_date date,
    determination_docx text,
    resolved boolean,
    defense_lawyer integer,
    prosecutor integer,
    judicial_officer integer,
    court_case integer,
    tasks text,
    is_criminal boolean,
    moral_element text,
    material_element text,
    legal_element text,
    debt_amount numeric(12,2),
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE issue_version OWNER TO nyimbi;

--
-- Name: judicialofficer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE judicialofficer (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    firstname character varying(40) NOT NULL,
    surname character varying(40) NOT NULL,
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    id integer NOT NULL,
    rank integer,
    judicial_role integer,
    court_station integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE judicialofficer OWNER TO nyimbi;

--
-- Name: judicialofficer_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE judicialofficer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE judicialofficer_id_seq OWNER TO nyimbi;

--
-- Name: judicialofficer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE judicialofficer_id_seq OWNED BY judicialofficer.id;


--
-- Name: judicialofficer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE judicialofficer_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    firstname character varying(40),
    surname character varying(40),
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    id integer NOT NULL,
    rank integer,
    judicial_role integer,
    court_station integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE judicialofficer_version OWNER TO nyimbi;

--
-- Name: judicialrank; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE judicialrank (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE judicialrank OWNER TO nyimbi;

--
-- Name: judicialrank_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE judicialrank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE judicialrank_id_seq OWNER TO nyimbi;

--
-- Name: judicialrank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE judicialrank_id_seq OWNED BY judicialrank.id;


--
-- Name: judicialrank_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE judicialrank_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE judicialrank_version OWNER TO nyimbi;

--
-- Name: judicialrole; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE judicialrole (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE judicialrole OWNER TO nyimbi;

--
-- Name: judicialrole_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE judicialrole_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE judicialrole_id_seq OWNER TO nyimbi;

--
-- Name: judicialrole_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE judicialrole_id_seq OWNED BY judicialrole.id;


--
-- Name: judicialrole_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE judicialrole_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE judicialrole_version OWNER TO nyimbi;

--
-- Name: law; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE law (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    name text,
    description text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE law OWNER TO nyimbi;

--
-- Name: law_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE law_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE law_id_seq OWNER TO nyimbi;

--
-- Name: law_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE law_id_seq OWNED BY law.id;


--
-- Name: law_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE law_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    name text,
    description text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE law_version OWNER TO nyimbi;

--
-- Name: lawfirm; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE lawfirm (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    place_name character varying(40),
    lat numeric(12,7),
    lng numeric(12,7),
    alt numeric(12,7),
    map text,
    info text,
    pin boolean,
    pin_color character varying(20),
    pin_icon character varying(50),
    centered boolean,
    nearest_feature character varying(100),
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE lawfirm OWNER TO nyimbi;

--
-- Name: lawfirm_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE lawfirm_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE lawfirm_id_seq OWNER TO nyimbi;

--
-- Name: lawfirm_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE lawfirm_id_seq OWNED BY lawfirm.id;


--
-- Name: lawfirm_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE lawfirm_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    place_name character varying(40),
    lat numeric(12,7),
    lng numeric(12,7),
    alt numeric(12,7),
    map text,
    info text,
    pin boolean,
    pin_color character varying(20),
    pin_icon character varying(50),
    centered boolean,
    nearest_feature character varying(100),
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE lawfirm_version OWNER TO nyimbi;

--
-- Name: lawyer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE lawyer (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    firstname character varying(40) NOT NULL,
    surname character varying(40) NOT NULL,
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    law_firm integer,
    bar_no text,
    bar_date date,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE lawyer OWNER TO nyimbi;

--
-- Name: lawyer_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE lawyer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE lawyer_id_seq OWNER TO nyimbi;

--
-- Name: lawyer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE lawyer_id_seq OWNED BY lawyer.id;


--
-- Name: lawyer_party; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE lawyer_party (
    lawyer integer NOT NULL,
    party integer NOT NULL
);


ALTER TABLE lawyer_party OWNER TO nyimbi;

--
-- Name: lawyer_party_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE lawyer_party_version (
    lawyer integer NOT NULL,
    party integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE lawyer_party_version OWNER TO nyimbi;

--
-- Name: lawyer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE lawyer_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    firstname character varying(40),
    surname character varying(40),
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    law_firm integer,
    bar_no text,
    bar_date date,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE lawyer_version OWNER TO nyimbi;

--
-- Name: legalreference; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE legalreference (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    ref text,
    verbatim text,
    public boolean,
    commentary text,
    validated boolean,
    citation text,
    quote text,
    interpretation text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE legalreference OWNER TO nyimbi;

--
-- Name: legalreference_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE legalreference_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE legalreference_id_seq OWNER TO nyimbi;

--
-- Name: legalreference_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE legalreference_id_seq OWNED BY legalreference.id;


--
-- Name: legalreference_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE legalreference_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    ref text,
    verbatim text,
    public boolean,
    commentary text,
    validated boolean,
    citation text,
    quote text,
    interpretation text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE legalreference_version OWNER TO nyimbi;

--
-- Name: nextofkin; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE nextofkin (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    bc_id character varying(20),
    bc_number character varying(20),
    bc_serial character varying(20),
    bc_place character varying(20),
    bc_scan text,
    citizenship character varying(20),
    nat_id_num character varying(15),
    nat_id_serial character varying(30),
    nat_id_scan text,
    pp_no character varying(20),
    pp_issue_date date,
    pp_issue_place character varying(40),
    pp_scan text,
    pp_expiry_date date,
    kin1_name character varying(100),
    kin1_phone character varying(50),
    kin1_email character varying(125),
    kin1_addr text,
    kin2_name character varying(100),
    kin1_relation character varying(100),
    kin2_phone character varying(50),
    kin2_email character varying(125),
    kin2_addr text,
    firstname character varying(40) NOT NULL,
    surname character varying(40) NOT NULL,
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    biodata integer,
    childunder4 boolean,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE nextofkin OWNER TO nyimbi;

--
-- Name: nextofkin_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE nextofkin_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE nextofkin_id_seq OWNER TO nyimbi;

--
-- Name: nextofkin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE nextofkin_id_seq OWNED BY nextofkin.id;


--
-- Name: nextofkin_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE nextofkin_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    bc_id character varying(20),
    bc_number character varying(20),
    bc_serial character varying(20),
    bc_place character varying(20),
    bc_scan text,
    citizenship character varying(20),
    nat_id_num character varying(15),
    nat_id_serial character varying(30),
    nat_id_scan text,
    pp_no character varying(20),
    pp_issue_date date,
    pp_issue_place character varying(40),
    pp_scan text,
    pp_expiry_date date,
    kin1_name character varying(100),
    kin1_phone character varying(50),
    kin1_email character varying(125),
    kin1_addr text,
    kin2_name character varying(100),
    kin1_relation character varying(100),
    kin2_phone character varying(50),
    kin2_email character varying(125),
    kin2_addr text,
    firstname character varying(40),
    surname character varying(40),
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    biodata integer,
    childunder4 boolean,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE nextofkin_version OWNER TO nyimbi;

--
-- Name: notification; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notification (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    contact text,
    message text,
    confirmation text,
    notification_register integer,
    add_date timestamp without time zone,
    send_date timestamp without time zone,
    sent boolean,
    delivered boolean,
    retries integer,
    abandon boolean,
    retry_count integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE notification OWNER TO nyimbi;

--
-- Name: notification_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE notification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE notification_id_seq OWNER TO nyimbi;

--
-- Name: notification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE notification_id_seq OWNED BY notification.id;


--
-- Name: notification_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notification_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    contact text,
    message text,
    confirmation text,
    notification_register integer,
    add_date timestamp without time zone,
    send_date timestamp without time zone,
    sent boolean,
    delivered boolean,
    retries integer,
    abandon boolean,
    retry_count integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE notification_version OWNER TO nyimbi;

--
-- Name: notificationregister; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notificationregister (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    notification_type integer,
    contact text,
    notify_event integer,
    retry_count bigint,
    active boolean,
    hearing integer,
    document integer,
    court_case integer,
    complaint integer,
    complaint_category integer,
    health_event integer,
    party integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE notificationregister OWNER TO nyimbi;

--
-- Name: notificationregister_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE notificationregister_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE notificationregister_id_seq OWNER TO nyimbi;

--
-- Name: notificationregister_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE notificationregister_id_seq OWNED BY notificationregister.id;


--
-- Name: notificationregister_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notificationregister_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    notification_type integer,
    contact text,
    notify_event integer,
    retry_count bigint,
    active boolean,
    hearing integer,
    document integer,
    court_case integer,
    complaint integer,
    complaint_category integer,
    health_event integer,
    party integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE notificationregister_version OWNER TO nyimbi;

--
-- Name: notificationtype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notificationtype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    code character varying(20),
    notes text,
    id integer NOT NULL,
    name text,
    description text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE notificationtype OWNER TO nyimbi;

--
-- Name: notificationtype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE notificationtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE notificationtype_id_seq OWNER TO nyimbi;

--
-- Name: notificationtype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE notificationtype_id_seq OWNED BY notificationtype.id;


--
-- Name: notificationtype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notificationtype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    code character varying(20),
    notes text,
    id integer NOT NULL,
    name text,
    description text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE notificationtype_version OWNER TO nyimbi;

--
-- Name: notifyevent; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notifyevent (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE notifyevent OWNER TO nyimbi;

--
-- Name: notifyevent_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE notifyevent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE notifyevent_id_seq OWNER TO nyimbi;

--
-- Name: notifyevent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE notifyevent_id_seq OWNED BY notifyevent.id;


--
-- Name: notifyevent_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE notifyevent_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE notifyevent_version OWNER TO nyimbi;

--
-- Name: page; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE page (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    document integer,
    page_image bytea,
    page_no bigint,
    page_text text,
    image_ext text,
    image_width text,
    image_height text,
    create_date timestamp without time zone,
    update_date timestamp without time zone,
    upload_dt timestamp without time zone,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE page OWNER TO nyimbi;

--
-- Name: page_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE page_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE page_id_seq OWNER TO nyimbi;

--
-- Name: page_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE page_id_seq OWNED BY page.id;


--
-- Name: page_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE page_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    document integer,
    page_image bytea,
    page_no bigint,
    page_text text,
    image_ext text,
    image_width text,
    image_height text,
    create_date timestamp without time zone,
    update_date timestamp without time zone,
    upload_dt timestamp without time zone,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE page_version OWNER TO nyimbi;

--
-- Name: party; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE party (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    firstname character varying(40) NOT NULL,
    surname character varying(40) NOT NULL,
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    complaints integer,
    statement character varying(1000),
    statementdate timestamp without time zone,
    complaint_role integer,
    notes text,
    dateofrepresentation timestamp without time zone,
    party_type integer,
    relative integer,
    relationship_type text,
    is_infant boolean,
    is_minor boolean,
    miranda_read boolean,
    miranda_date timestamp without time zone,
    miranda_witness text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE party OWNER TO nyimbi;

--
-- Name: party_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE party_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE party_id_seq OWNER TO nyimbi;

--
-- Name: party_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE party_id_seq OWNED BY party.id;


--
-- Name: party_settlement; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE party_settlement (
    party integer NOT NULL,
    settlement integer NOT NULL
);


ALTER TABLE party_settlement OWNER TO nyimbi;

--
-- Name: party_settlement_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE party_settlement_version (
    party integer NOT NULL,
    settlement integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE party_settlement_version OWNER TO nyimbi;

--
-- Name: party_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE party_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    firstname character varying(40),
    surname character varying(40),
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    complaints integer,
    statement character varying(1000),
    statementdate timestamp without time zone,
    complaint_role integer,
    notes text,
    dateofrepresentation timestamp without time zone,
    party_type integer,
    relative integer,
    relationship_type text,
    is_infant boolean,
    is_minor boolean,
    miranda_read boolean,
    miranda_date timestamp without time zone,
    miranda_witness text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE party_version OWNER TO nyimbi;

--
-- Name: partytype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE partytype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE partytype OWNER TO nyimbi;

--
-- Name: partytype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE partytype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE partytype_id_seq OWNER TO nyimbi;

--
-- Name: partytype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE partytype_id_seq OWNED BY partytype.id;


--
-- Name: partytype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE partytype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE partytype_version OWNER TO nyimbi;

--
-- Name: payment; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE payment (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    bill integer,
    amount numeric(12,2),
    payment_ref text,
    date_paid timestamp without time zone,
    phone_number character varying(20),
    validated boolean,
    payment_description text,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE payment OWNER TO nyimbi;

--
-- Name: payment_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE payment_id_seq OWNER TO nyimbi;

--
-- Name: payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE payment_id_seq OWNED BY payment.id;


--
-- Name: payment_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE payment_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    bill integer,
    amount numeric(12,2),
    payment_ref text,
    date_paid timestamp without time zone,
    phone_number character varying(20),
    validated boolean,
    payment_description text,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE payment_version OWNER TO nyimbi;

--
-- Name: personaleffect; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE personaleffect (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    party integer,
    personal_effects_category integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE personaleffect OWNER TO nyimbi;

--
-- Name: personaleffect_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE personaleffect_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE personaleffect_id_seq OWNER TO nyimbi;

--
-- Name: personaleffect_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE personaleffect_id_seq OWNED BY personaleffect.id;


--
-- Name: personaleffect_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE personaleffect_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    party integer,
    personal_effects_category integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE personaleffect_version OWNER TO nyimbi;

--
-- Name: personaleffectscategory; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE personaleffectscategory (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE personaleffectscategory OWNER TO nyimbi;

--
-- Name: personaleffectscategory_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE personaleffectscategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE personaleffectscategory_id_seq OWNER TO nyimbi;

--
-- Name: personaleffectscategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE personaleffectscategory_id_seq OWNED BY personaleffectscategory.id;


--
-- Name: personaleffectscategory_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE personaleffectscategory_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE personaleffectscategory_version OWNER TO nyimbi;

--
-- Name: policeofficer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policeofficer (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    firstname character varying(40) NOT NULL,
    surname character varying(40) NOT NULL,
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    id integer NOT NULL,
    police_rank integer,
    servicenumber character varying(100),
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE policeofficer OWNER TO nyimbi;

--
-- Name: policeofficer_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE policeofficer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE policeofficer_id_seq OWNER TO nyimbi;

--
-- Name: policeofficer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE policeofficer_id_seq OWNED BY policeofficer.id;


--
-- Name: policeofficer_policestation; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policeofficer_policestation (
    policeofficer integer NOT NULL,
    policestation integer NOT NULL
);


ALTER TABLE policeofficer_policestation OWNER TO nyimbi;

--
-- Name: policeofficer_policestation_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policeofficer_policestation_version (
    policeofficer integer NOT NULL,
    policestation integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE policeofficer_policestation_version OWNER TO nyimbi;

--
-- Name: policeofficer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policeofficer_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    firstname character varying(40),
    surname character varying(40),
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    id integer NOT NULL,
    police_rank integer,
    servicenumber character varying(100),
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE policeofficer_version OWNER TO nyimbi;

--
-- Name: policeofficerrank; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policeofficerrank (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    code character varying(20),
    notes text,
    id integer NOT NULL,
    name text,
    description text,
    sequence integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE policeofficerrank OWNER TO nyimbi;

--
-- Name: policeofficerrank_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE policeofficerrank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE policeofficerrank_id_seq OWNER TO nyimbi;

--
-- Name: policeofficerrank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE policeofficerrank_id_seq OWNED BY policeofficerrank.id;


--
-- Name: policeofficerrank_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policeofficerrank_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    code character varying(20),
    notes text,
    id integer NOT NULL,
    name text,
    description text,
    sequence integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE policeofficerrank_version OWNER TO nyimbi;

--
-- Name: policestation; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policestation (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    town integer,
    officer_commanding integer,
    police_station_rank integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE policestation OWNER TO nyimbi;

--
-- Name: policestation_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE policestation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE policestation_id_seq OWNER TO nyimbi;

--
-- Name: policestation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE policestation_id_seq OWNED BY policestation.id;


--
-- Name: policestation_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policestation_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    town integer,
    officer_commanding integer,
    police_station_rank integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE policestation_version OWNER TO nyimbi;

--
-- Name: policestationrank; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policestationrank (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE policestationrank OWNER TO nyimbi;

--
-- Name: policestationrank_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE policestationrank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE policestationrank_id_seq OWNER TO nyimbi;

--
-- Name: policestationrank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE policestationrank_id_seq OWNED BY policestationrank.id;


--
-- Name: policestationrank_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE policestationrank_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE policestationrank_version OWNER TO nyimbi;

--
-- Name: prison; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prison (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    place_name character varying(40),
    lat numeric(12,7),
    lng numeric(12,7),
    alt numeric(12,7),
    map text,
    info text,
    pin boolean,
    pin_color character varying(20),
    pin_icon character varying(50),
    centered boolean,
    nearest_feature character varying(100),
    id integer NOT NULL,
    town integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE prison OWNER TO nyimbi;

--
-- Name: prison_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE prison_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE prison_id_seq OWNER TO nyimbi;

--
-- Name: prison_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE prison_id_seq OWNED BY prison.id;


--
-- Name: prison_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prison_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    place_name character varying(40),
    lat numeric(12,7),
    lng numeric(12,7),
    alt numeric(12,7),
    map text,
    info text,
    pin boolean,
    pin_color character varying(20),
    pin_icon character varying(50),
    centered boolean,
    nearest_feature character varying(100),
    id integer NOT NULL,
    town integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE prison_version OWNER TO nyimbi;

--
-- Name: prisonofficer; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prisonofficer (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    firstname character varying(40) NOT NULL,
    surname character varying(40) NOT NULL,
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    id integer NOT NULL,
    prison integer,
    prison_officer_rank integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE prisonofficer OWNER TO nyimbi;

--
-- Name: prisonofficer_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE prisonofficer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE prisonofficer_id_seq OWNER TO nyimbi;

--
-- Name: prisonofficer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE prisonofficer_id_seq OWNED BY prisonofficer.id;


--
-- Name: prisonofficer_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prisonofficer_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    firstname character varying(40),
    surname character varying(40),
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    id integer NOT NULL,
    prison integer,
    prison_officer_rank integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE prisonofficer_version OWNER TO nyimbi;

--
-- Name: prisonofficerrank; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prisonofficerrank (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE prisonofficerrank OWNER TO nyimbi;

--
-- Name: prisonofficerrank_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE prisonofficerrank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE prisonofficerrank_id_seq OWNER TO nyimbi;

--
-- Name: prisonofficerrank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE prisonofficerrank_id_seq OWNED BY prisonofficerrank.id;


--
-- Name: prisonofficerrank_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prisonofficerrank_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE prisonofficerrank_version OWNER TO nyimbi;

--
-- Name: prosecutor; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prosecutor (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    firstname character varying(40) NOT NULL,
    surname character varying(40) NOT NULL,
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    prosecutor_team integer,
    lawyer integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE prosecutor OWNER TO nyimbi;

--
-- Name: prosecutor_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE prosecutor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE prosecutor_id_seq OWNER TO nyimbi;

--
-- Name: prosecutor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE prosecutor_id_seq OWNED BY prosecutor.id;


--
-- Name: prosecutor_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prosecutor_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    firstname character varying(40),
    surname character varying(40),
    othernames character varying(40),
    dob date,
    gender gender_type,
    marital_status marital_status_type,
    mobile character varying(30),
    other_mobile character varying(30),
    fixed_line character varying(30),
    other_fixed_line character varying(20),
    email character varying(60),
    other_email character varying(60),
    address_line_1 character varying(200),
    address_line_2 character varying(200),
    zipcode character varying(30),
    town character varying(40),
    country character varying(50),
    facebook character varying(40),
    twitter character varying(40),
    instagram character varying(40),
    whatsapp boolean,
    other_whatsapp boolean,
    fax character varying(30),
    gcode character varying(40),
    okhi character varying(40),
    id integer NOT NULL,
    prosecutor_team integer,
    lawyer integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE prosecutor_version OWNER TO nyimbi;

--
-- Name: prosecutorteam; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prosecutorteam (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE prosecutorteam OWNER TO nyimbi;

--
-- Name: prosecutorteam_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE prosecutorteam_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE prosecutorteam_id_seq OWNER TO nyimbi;

--
-- Name: prosecutorteam_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE prosecutorteam_id_seq OWNED BY prosecutorteam.id;


--
-- Name: prosecutorteam_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE prosecutorteam_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE prosecutorteam_version OWNER TO nyimbi;

--
-- Name: releasetype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE releasetype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE releasetype OWNER TO nyimbi;

--
-- Name: releasetype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE releasetype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE releasetype_id_seq OWNER TO nyimbi;

--
-- Name: releasetype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE releasetype_id_seq OWNED BY releasetype.id;


--
-- Name: releasetype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE releasetype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE releasetype_version OWNER TO nyimbi;

--
-- Name: religion; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE religion (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE religion OWNER TO nyimbi;

--
-- Name: religion_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE religion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE religion_id_seq OWNER TO nyimbi;

--
-- Name: religion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE religion_id_seq OWNED BY religion.id;


--
-- Name: religion_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE religion_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE religion_version OWNER TO nyimbi;

--
-- Name: schedulestatustype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE schedulestatustype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE schedulestatustype OWNER TO nyimbi;

--
-- Name: schedulestatustype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE schedulestatustype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE schedulestatustype_id_seq OWNER TO nyimbi;

--
-- Name: schedulestatustype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE schedulestatustype_id_seq OWNED BY schedulestatustype.id;


--
-- Name: schedulestatustype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE schedulestatustype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE schedulestatustype_version OWNER TO nyimbi;

--
-- Name: seizure; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE seizure (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    investigation_diary integer,
    owner text,
    item text,
    item_packaging text,
    item_pic text,
    premises text,
    reg_no text,
    witness text,
    notes text,
    docx text,
    item_description text,
    returned boolean,
    return_date timestamp without time zone,
    return_notes text,
    return_signed_receipt text,
    destroyed boolean,
    destruction_date date,
    destruction_witnesses text,
    destruction_notes text,
    disposed boolean,
    sold_to text,
    disposal_date date,
    disposal_price numeric(12,2),
    disposal_receipt text,
    recovery_town integer,
    destruction_pic text,
    is_evidence boolean,
    immovable boolean,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE seizure OWNER TO nyimbi;

--
-- Name: seizure_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE seizure_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE seizure_id_seq OWNER TO nyimbi;

--
-- Name: seizure_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE seizure_id_seq OWNED BY seizure.id;


--
-- Name: seizure_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE seizure_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    investigation_diary integer,
    owner text,
    item text,
    item_packaging text,
    item_pic text,
    premises text,
    reg_no text,
    witness text,
    notes text,
    docx text,
    item_description text,
    returned boolean,
    return_date timestamp without time zone,
    return_notes text,
    return_signed_receipt text,
    destroyed boolean,
    destruction_date date,
    destruction_witnesses text,
    destruction_notes text,
    disposed boolean,
    sold_to text,
    disposal_date date,
    disposal_price numeric(12,2),
    disposal_receipt text,
    recovery_town integer,
    destruction_pic text,
    is_evidence boolean,
    immovable boolean,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE seizure_version OWNER TO nyimbi;

--
-- Name: settlement; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE settlement (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    complaint integer,
    terms text,
    amount numeric(12,2),
    paid boolean,
    docx text,
    settlor integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE settlement OWNER TO nyimbi;

--
-- Name: settlement_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE settlement_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE settlement_id_seq OWNER TO nyimbi;

--
-- Name: settlement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE settlement_id_seq OWNED BY settlement.id;


--
-- Name: settlement_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE settlement_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    complaint integer,
    terms text,
    amount numeric(12,2),
    paid boolean,
    docx text,
    settlor integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE settlement_version OWNER TO nyimbi;

--
-- Name: subcounty; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE subcounty (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    county integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE subcounty OWNER TO nyimbi;

--
-- Name: subcounty_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE subcounty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE subcounty_id_seq OWNER TO nyimbi;

--
-- Name: subcounty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE subcounty_id_seq OWNED BY subcounty.id;


--
-- Name: subcounty_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE subcounty_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    county integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE subcounty_version OWNER TO nyimbi;

--
-- Name: templatetype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE templatetype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    template_type integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE templatetype OWNER TO nyimbi;

--
-- Name: templatetype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE templatetype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE templatetype_id_seq OWNER TO nyimbi;

--
-- Name: templatetype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE templatetype_id_seq OWNED BY templatetype.id;


--
-- Name: templatetype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE templatetype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    template_type integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE templatetype_version OWNER TO nyimbi;

--
-- Name: town; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE town (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE town OWNER TO nyimbi;

--
-- Name: town_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE town_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE town_id_seq OWNER TO nyimbi;

--
-- Name: town_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE town_id_seq OWNED BY town.id;


--
-- Name: town_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE town_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE town_version OWNER TO nyimbi;

--
-- Name: town_ward; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE town_ward (
    town integer NOT NULL,
    ward integer NOT NULL
);


ALTER TABLE town_ward OWNER TO nyimbi;

--
-- Name: town_ward_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE town_ward_version (
    town integer NOT NULL,
    ward integer NOT NULL,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE town_ward_version OWNER TO nyimbi;

--
-- Name: transaction; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE transaction (
    issued_at timestamp without time zone,
    id bigint NOT NULL,
    remote_addr character varying(50),
    user_id integer
);


ALTER TABLE transaction OWNER TO nyimbi;

--
-- Name: transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE transaction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE transaction_id_seq OWNER TO nyimbi;

--
-- Name: transcript; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE transcript (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    mime_type character varying(60),
    doc text,
    doc_text text,
    doc_binary text,
    doc_title character varying(200),
    subject character varying(100),
    author character varying(100),
    keywords character varying(200),
    comments text,
    doc_type character varying(5),
    char_count integer,
    word_count integer,
    lines integer,
    paragraphs integer,
    file_size_bytes integer,
    producer_prog character varying(40),
    immutable boolean,
    page_size character varying(40),
    page_count integer,
    hashx character varying(40),
    audio_duration_secs integer,
    audio_frame_rate integer,
    audio_channels integer,
    search_vector tsvector,
    id integer NOT NULL,
    video text,
    audio text,
    add_date timestamp without time zone,
    asr_transcript text,
    asr_date timestamp without time zone,
    edited_transcript text,
    edit_date timestamp without time zone,
    certified_transcript text,
    certfiy_date timestamp without time zone,
    locked boolean,
    hearing integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE transcript OWNER TO nyimbi;

--
-- Name: transcript_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE transcript_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE transcript_id_seq OWNER TO nyimbi;

--
-- Name: transcript_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE transcript_id_seq OWNED BY transcript.id;


--
-- Name: transcript_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE transcript_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    mime_type character varying(60),
    doc text,
    doc_text text,
    doc_binary text,
    doc_title character varying(200),
    subject character varying(100),
    author character varying(100),
    keywords character varying(200),
    comments text,
    doc_type character varying(5),
    char_count integer,
    word_count integer,
    lines integer,
    paragraphs integer,
    file_size_bytes integer,
    producer_prog character varying(40),
    immutable boolean,
    page_size character varying(40),
    page_count integer,
    hashx character varying(40),
    audio_duration_secs integer,
    audio_frame_rate integer,
    audio_channels integer,
    search_vector tsvector,
    id integer NOT NULL,
    video text,
    audio text,
    add_date timestamp without time zone,
    asr_transcript text,
    asr_date timestamp without time zone,
    edited_transcript text,
    edit_date timestamp without time zone,
    certified_transcript text,
    certfiy_date timestamp without time zone,
    locked boolean,
    hearing integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE transcript_version OWNER TO nyimbi;

--
-- Name: vehicle; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE vehicle (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    police_station integer,
    make character varying(100),
    model character varying(100),
    regno character varying(100),
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE vehicle OWNER TO nyimbi;

--
-- Name: vehicle_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE vehicle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE vehicle_id_seq OWNER TO nyimbi;

--
-- Name: vehicle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE vehicle_id_seq OWNED BY vehicle.id;


--
-- Name: vehicle_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE vehicle_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    police_station integer,
    make character varying(100),
    model character varying(100),
    regno character varying(100),
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE vehicle_version OWNER TO nyimbi;

--
-- Name: ward; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ward (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    id integer NOT NULL,
    subcounty integer,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE ward OWNER TO nyimbi;

--
-- Name: ward_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE ward_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ward_id_seq OWNER TO nyimbi;

--
-- Name: ward_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE ward_id_seq OWNED BY ward.id;


--
-- Name: ward_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE ward_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    id integer NOT NULL,
    subcounty integer,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE ward_version OWNER TO nyimbi;

--
-- Name: warranttype; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE warranttype (
    created_on timestamp without time zone NOT NULL,
    changed_on timestamp without time zone NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer NOT NULL,
    changed_by_fk integer NOT NULL
);


ALTER TABLE warranttype OWNER TO nyimbi;

--
-- Name: warranttype_id_seq; Type: SEQUENCE; Schema: public; Owner: nyimbi
--

CREATE SEQUENCE warranttype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE warranttype_id_seq OWNER TO nyimbi;

--
-- Name: warranttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nyimbi
--

ALTER SEQUENCE warranttype_id_seq OWNED BY warranttype.id;


--
-- Name: warranttype_version; Type: TABLE; Schema: public; Owner: nyimbi
--

CREATE TABLE warranttype_version (
    created_on timestamp without time zone,
    changed_on timestamp without time zone,
    name character varying(100),
    code character varying(20),
    description character varying(100),
    notes text,
    id integer NOT NULL,
    photo text,
    file text,
    created_by_fk integer,
    changed_by_fk integer,
    transaction_id bigint NOT NULL,
    end_transaction_id bigint,
    operation_type smallint NOT NULL
);


ALTER TABLE warranttype_version OWNER TO nyimbi;

--
-- Name: accounttype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY accounttype ALTER COLUMN id SET DEFAULT nextval('accounttype_id_seq'::regclass);


--
-- Name: bill id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill ALTER COLUMN id SET DEFAULT nextval('bill_id_seq'::regclass);


--
-- Name: billdetail id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY billdetail ALTER COLUMN id SET DEFAULT nextval('billdetail_id_seq'::regclass);


--
-- Name: biodata id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata ALTER COLUMN id SET DEFAULT nextval('biodata_id_seq'::regclass);


--
-- Name: casecategory id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory ALTER COLUMN id SET DEFAULT nextval('casecategory_id_seq'::regclass);


--
-- Name: casechecklist id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casechecklist ALTER COLUMN id SET DEFAULT nextval('casechecklist_id_seq'::regclass);


--
-- Name: caselinktype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY caselinktype ALTER COLUMN id SET DEFAULT nextval('caselinktype_id_seq'::regclass);


--
-- Name: celltype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY celltype ALTER COLUMN id SET DEFAULT nextval('celltype_id_seq'::regclass);


--
-- Name: commital id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital ALTER COLUMN id SET DEFAULT nextval('commital_id_seq'::regclass);


--
-- Name: commitaltype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commitaltype ALTER COLUMN id SET DEFAULT nextval('commitaltype_id_seq'::regclass);


--
-- Name: complaint id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint ALTER COLUMN id SET DEFAULT nextval('complaint_id_seq'::regclass);


--
-- Name: complaintcategory id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintcategory ALTER COLUMN id SET DEFAULT nextval('complaintcategory_id_seq'::regclass);


--
-- Name: complaintrole id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintrole ALTER COLUMN id SET DEFAULT nextval('complaintrole_id_seq'::regclass);


--
-- Name: country id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY country ALTER COLUMN id SET DEFAULT nextval('country_id_seq'::regclass);


--
-- Name: county id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY county ALTER COLUMN id SET DEFAULT nextval('county_id_seq'::regclass);


--
-- Name: court id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court ALTER COLUMN id SET DEFAULT nextval('court_id_seq'::regclass);


--
-- Name: courtcase id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase ALTER COLUMN id SET DEFAULT nextval('courtcase_id_seq'::regclass);


--
-- Name: courtrank id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtrank ALTER COLUMN id SET DEFAULT nextval('courtrank_id_seq'::regclass);


--
-- Name: courtstation id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtstation ALTER COLUMN id SET DEFAULT nextval('courtstation_id_seq'::regclass);


--
-- Name: crime id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY crime ALTER COLUMN id SET DEFAULT nextval('crime_id_seq'::regclass);


--
-- Name: csi_equipment id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment ALTER COLUMN id SET DEFAULT nextval('csi_equipment_id_seq'::regclass);


--
-- Name: diagram id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY diagram ALTER COLUMN id SET DEFAULT nextval('diagram_id_seq'::regclass);


--
-- Name: discipline id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY discipline ALTER COLUMN id SET DEFAULT nextval('discipline_id_seq'::regclass);


--
-- Name: doctemplate id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY doctemplate ALTER COLUMN id SET DEFAULT nextval('doctemplate_id_seq'::regclass);


--
-- Name: document id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document ALTER COLUMN id SET DEFAULT nextval('document_id_seq'::regclass);


--
-- Name: documenttype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY documenttype ALTER COLUMN id SET DEFAULT nextval('documenttype_id_seq'::regclass);


--
-- Name: economicclass id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY economicclass ALTER COLUMN id SET DEFAULT nextval('economicclass_id_seq'::regclass);


--
-- Name: exhibit id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY exhibit ALTER COLUMN id SET DEFAULT nextval('exhibit_id_seq'::regclass);


--
-- Name: expert id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert ALTER COLUMN id SET DEFAULT nextval('expert_id_seq'::regclass);


--
-- Name: experttype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttype ALTER COLUMN id SET DEFAULT nextval('experttype_id_seq'::regclass);


--
-- Name: feeclass id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feeclass ALTER COLUMN id SET DEFAULT nextval('feeclass_id_seq'::regclass);


--
-- Name: feetype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feetype ALTER COLUMN id SET DEFAULT nextval('feetype_id_seq'::regclass);


--
-- Name: healthevent id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent ALTER COLUMN id SET DEFAULT nextval('healthevent_id_seq'::regclass);


--
-- Name: healtheventtype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healtheventtype ALTER COLUMN id SET DEFAULT nextval('healtheventtype_id_seq'::regclass);


--
-- Name: hearing id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing ALTER COLUMN id SET DEFAULT nextval('hearing_id_seq'::regclass);


--
-- Name: hearingtype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearingtype ALTER COLUMN id SET DEFAULT nextval('hearingtype_id_seq'::regclass);


--
-- Name: instancecrime id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime ALTER COLUMN id SET DEFAULT nextval('instancecrime_id_seq'::regclass);


--
-- Name: interview id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY interview ALTER COLUMN id SET DEFAULT nextval('interview_id_seq'::regclass);


--
-- Name: investigationdiary id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary ALTER COLUMN id SET DEFAULT nextval('investigationdiary_id_seq'::regclass);


--
-- Name: issue id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue ALTER COLUMN id SET DEFAULT nextval('issue_id_seq'::regclass);


--
-- Name: judicialofficer id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer ALTER COLUMN id SET DEFAULT nextval('judicialofficer_id_seq'::regclass);


--
-- Name: judicialrank id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrank ALTER COLUMN id SET DEFAULT nextval('judicialrank_id_seq'::regclass);


--
-- Name: judicialrole id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrole ALTER COLUMN id SET DEFAULT nextval('judicialrole_id_seq'::regclass);


--
-- Name: law id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY law ALTER COLUMN id SET DEFAULT nextval('law_id_seq'::regclass);


--
-- Name: lawfirm id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawfirm ALTER COLUMN id SET DEFAULT nextval('lawfirm_id_seq'::regclass);


--
-- Name: lawyer id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer ALTER COLUMN id SET DEFAULT nextval('lawyer_id_seq'::regclass);


--
-- Name: legalreference id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY legalreference ALTER COLUMN id SET DEFAULT nextval('legalreference_id_seq'::regclass);


--
-- Name: nextofkin id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY nextofkin ALTER COLUMN id SET DEFAULT nextval('nextofkin_id_seq'::regclass);


--
-- Name: notification id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notification ALTER COLUMN id SET DEFAULT nextval('notification_id_seq'::regclass);


--
-- Name: notificationregister id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister ALTER COLUMN id SET DEFAULT nextval('notificationregister_id_seq'::regclass);


--
-- Name: notificationtype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationtype ALTER COLUMN id SET DEFAULT nextval('notificationtype_id_seq'::regclass);


--
-- Name: notifyevent id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notifyevent ALTER COLUMN id SET DEFAULT nextval('notifyevent_id_seq'::regclass);


--
-- Name: page id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY page ALTER COLUMN id SET DEFAULT nextval('page_id_seq'::regclass);


--
-- Name: party id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party ALTER COLUMN id SET DEFAULT nextval('party_id_seq'::regclass);


--
-- Name: partytype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY partytype ALTER COLUMN id SET DEFAULT nextval('partytype_id_seq'::regclass);


--
-- Name: payment id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY payment ALTER COLUMN id SET DEFAULT nextval('payment_id_seq'::regclass);


--
-- Name: personaleffect id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffect ALTER COLUMN id SET DEFAULT nextval('personaleffect_id_seq'::regclass);


--
-- Name: personaleffectscategory id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffectscategory ALTER COLUMN id SET DEFAULT nextval('personaleffectscategory_id_seq'::regclass);


--
-- Name: policeofficer id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer ALTER COLUMN id SET DEFAULT nextval('policeofficer_id_seq'::regclass);


--
-- Name: policeofficerrank id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficerrank ALTER COLUMN id SET DEFAULT nextval('policeofficerrank_id_seq'::regclass);


--
-- Name: policestation id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation ALTER COLUMN id SET DEFAULT nextval('policestation_id_seq'::regclass);


--
-- Name: policestationrank id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestationrank ALTER COLUMN id SET DEFAULT nextval('policestationrank_id_seq'::regclass);


--
-- Name: prison id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prison ALTER COLUMN id SET DEFAULT nextval('prison_id_seq'::regclass);


--
-- Name: prisonofficer id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficer ALTER COLUMN id SET DEFAULT nextval('prisonofficer_id_seq'::regclass);


--
-- Name: prisonofficerrank id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficerrank ALTER COLUMN id SET DEFAULT nextval('prisonofficerrank_id_seq'::regclass);


--
-- Name: prosecutor id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutor ALTER COLUMN id SET DEFAULT nextval('prosecutor_id_seq'::regclass);


--
-- Name: prosecutorteam id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutorteam ALTER COLUMN id SET DEFAULT nextval('prosecutorteam_id_seq'::regclass);


--
-- Name: releasetype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY releasetype ALTER COLUMN id SET DEFAULT nextval('releasetype_id_seq'::regclass);


--
-- Name: religion id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY religion ALTER COLUMN id SET DEFAULT nextval('religion_id_seq'::regclass);


--
-- Name: schedulestatustype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY schedulestatustype ALTER COLUMN id SET DEFAULT nextval('schedulestatustype_id_seq'::regclass);


--
-- Name: seizure id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY seizure ALTER COLUMN id SET DEFAULT nextval('seizure_id_seq'::regclass);


--
-- Name: settlement id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY settlement ALTER COLUMN id SET DEFAULT nextval('settlement_id_seq'::regclass);


--
-- Name: subcounty id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY subcounty ALTER COLUMN id SET DEFAULT nextval('subcounty_id_seq'::regclass);


--
-- Name: templatetype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY templatetype ALTER COLUMN id SET DEFAULT nextval('templatetype_id_seq'::regclass);


--
-- Name: town id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town ALTER COLUMN id SET DEFAULT nextval('town_id_seq'::regclass);


--
-- Name: transcript id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transcript ALTER COLUMN id SET DEFAULT nextval('transcript_id_seq'::regclass);


--
-- Name: vehicle id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY vehicle ALTER COLUMN id SET DEFAULT nextval('vehicle_id_seq'::regclass);


--
-- Name: ward id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ward ALTER COLUMN id SET DEFAULT nextval('ward_id_seq'::regclass);


--
-- Name: warranttype id; Type: DEFAULT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY warranttype ALTER COLUMN id SET DEFAULT nextval('warranttype_id_seq'::regclass);


--
-- Data for Name: ab_permission; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_permission (id, name) FROM stdin;
1	can_this_form_post
2	can_this_form_get
3	can_userinfo
4	can_show
5	can_edit
6	can_list
7	can_download
8	can_delete
9	can_add
10	resetmypassword
11	resetpasswords
12	userinfoedit
13	menu_access
14	Copy Role
15	can_chart
16	muldelete
\.


--
-- Data for Name: ab_permission_view; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_permission_view (id, permission_id, view_menu_id) FROM stdin;
1	1	5
2	2	5
3	1	6
4	2	6
5	1	7
6	2	7
7	3	9
8	4	9
9	5	9
10	6	9
11	7	9
12	8	9
13	9	9
14	10	9
15	11	9
16	12	9
17	13	10
18	13	11
19	4	12
20	5	12
21	6	12
22	7	12
23	8	12
24	9	12
25	14	12
26	13	13
27	15	14
28	13	15
29	6	16
30	4	16
31	8	16
32	6	17
33	13	18
34	6	19
35	13	20
36	6	21
37	13	22
38	9	23
39	7	23
40	4	23
41	8	23
42	6	23
43	5	23
44	16	23
45	13	24
46	13	25
47	9	26
48	7	26
49	4	26
50	8	26
51	6	26
52	5	26
53	16	26
54	13	27
55	13	28
56	9	29
57	7	29
58	4	29
59	8	29
60	6	29
61	5	29
62	16	29
63	13	30
64	9	31
65	7	31
66	4	31
67	8	31
68	6	31
69	5	31
70	16	31
71	13	32
72	9	33
73	7	33
74	4	33
75	8	33
76	6	33
77	5	33
78	16	33
79	13	34
80	9	35
81	7	35
82	4	35
83	8	35
84	6	35
85	5	35
86	16	35
87	13	36
88	9	37
89	7	37
90	4	37
91	8	37
92	6	37
93	5	37
94	16	37
95	13	38
96	9	39
97	7	39
98	4	39
99	8	39
100	6	39
101	5	39
102	16	39
103	13	40
104	9	41
105	7	41
106	4	41
107	8	41
108	6	41
109	5	41
110	16	41
111	13	42
112	9	43
113	7	43
114	4	43
115	8	43
116	6	43
117	5	43
118	16	43
119	13	44
120	9	45
121	7	45
122	4	45
123	8	45
124	6	45
125	5	45
126	16	45
127	13	46
128	9	47
129	7	47
130	4	47
131	8	47
132	6	47
133	5	47
134	16	47
135	13	48
136	9	49
137	7	49
138	4	49
139	8	49
140	6	49
141	5	49
142	16	49
143	13	50
144	9	51
145	7	51
146	4	51
147	8	51
148	6	51
149	5	51
150	16	51
151	13	52
152	9	53
153	7	53
154	4	53
155	8	53
156	6	53
157	5	53
158	16	53
159	13	54
160	9	55
161	7	55
162	4	55
163	8	55
164	6	55
165	5	55
166	16	55
167	13	56
168	9	57
169	7	57
170	4	57
171	8	57
172	6	57
173	5	57
174	16	57
175	13	58
176	9	59
177	7	59
178	4	59
179	8	59
180	6	59
181	5	59
182	16	59
183	13	60
184	9	61
185	7	61
186	4	61
187	8	61
188	6	61
189	5	61
190	16	61
191	13	62
192	9	63
193	7	63
194	4	63
195	8	63
196	6	63
197	5	63
198	16	63
199	13	64
200	9	65
201	7	65
202	4	65
203	8	65
204	6	65
205	5	65
206	16	65
207	13	66
208	9	67
209	7	67
210	4	67
211	8	67
212	6	67
213	5	67
214	16	67
215	13	68
216	9	69
217	7	69
218	4	69
219	8	69
220	6	69
221	5	69
222	16	69
223	13	70
224	9	71
225	7	71
226	4	71
227	8	71
228	6	71
229	5	71
230	16	71
231	13	72
232	9	73
233	7	73
234	4	73
235	8	73
236	6	73
237	5	73
238	16	73
239	13	74
240	9	75
241	7	75
242	4	75
243	8	75
244	6	75
245	5	75
246	16	75
247	13	76
248	9	77
249	7	77
250	4	77
251	8	77
252	6	77
253	5	77
254	16	77
255	13	78
256	9	79
257	7	79
258	4	79
259	8	79
260	6	79
261	5	79
262	16	79
263	13	80
264	9	81
265	7	81
266	4	81
267	8	81
268	6	81
269	5	81
270	16	81
271	13	82
272	9	83
273	7	83
274	4	83
275	8	83
276	6	83
277	5	83
278	16	83
279	13	84
280	9	85
281	7	85
282	4	85
283	8	85
284	6	85
285	5	85
286	16	85
287	13	86
288	9	87
289	7	87
290	4	87
291	8	87
292	6	87
293	5	87
294	16	87
295	13	88
296	9	89
297	7	89
298	4	89
299	8	89
300	6	89
301	5	89
302	16	89
303	13	90
304	9	91
305	7	91
306	4	91
307	8	91
308	6	91
309	5	91
310	16	91
311	13	92
312	9	93
313	7	93
314	4	93
315	8	93
316	6	93
317	5	93
318	16	93
319	13	94
320	9	95
321	7	95
322	4	95
323	8	95
324	6	95
325	5	95
326	16	95
327	13	96
328	9	97
329	7	97
330	4	97
331	8	97
332	6	97
333	5	97
334	16	97
335	13	98
336	9	99
337	7	99
338	4	99
339	8	99
340	6	99
341	5	99
342	16	99
343	13	100
344	9	101
345	7	101
346	4	101
347	8	101
348	6	101
349	5	101
350	16	101
351	13	102
352	9	103
353	7	103
354	4	103
355	8	103
356	6	103
357	5	103
358	16	103
359	13	104
360	9	105
361	7	105
362	4	105
363	8	105
364	6	105
365	5	105
366	16	105
367	13	106
368	9	107
369	7	107
370	4	107
371	8	107
372	6	107
373	5	107
374	16	107
375	13	108
376	9	109
377	7	109
378	4	109
379	8	109
380	6	109
381	5	109
382	16	109
383	13	110
384	9	111
385	7	111
386	4	111
387	8	111
388	6	111
389	5	111
390	16	111
391	13	112
392	9	113
393	7	113
394	4	113
395	8	113
396	6	113
397	5	113
398	16	113
399	13	114
400	9	115
401	7	115
402	4	115
403	8	115
404	6	115
405	5	115
406	16	115
407	13	116
408	9	117
409	7	117
410	4	117
411	8	117
412	6	117
413	5	117
414	16	117
415	13	118
416	9	119
417	7	119
418	4	119
419	8	119
420	6	119
421	5	119
422	16	119
423	13	120
424	9	121
425	7	121
426	4	121
427	8	121
428	6	121
429	5	121
430	16	121
431	13	122
432	9	123
433	7	123
434	4	123
435	8	123
436	6	123
437	5	123
438	16	123
439	13	124
440	9	125
441	7	125
442	4	125
443	8	125
444	6	125
445	5	125
446	16	125
447	13	126
448	9	127
449	7	127
450	4	127
451	8	127
452	6	127
453	5	127
454	16	127
455	13	128
456	9	129
457	7	129
458	4	129
459	8	129
460	6	129
461	5	129
462	16	129
463	13	130
464	9	131
465	7	131
466	4	131
467	8	131
468	6	131
469	5	131
470	16	131
471	13	132
472	9	133
473	7	133
474	4	133
475	8	133
476	6	133
477	5	133
478	16	133
479	13	134
480	9	135
481	7	135
482	4	135
483	8	135
484	6	135
485	5	135
486	16	135
487	13	136
488	9	137
489	7	137
490	4	137
491	8	137
492	6	137
493	5	137
494	16	137
495	13	138
496	9	139
497	7	139
498	4	139
499	8	139
500	6	139
501	5	139
502	16	139
503	13	140
504	9	141
505	7	141
506	4	141
507	8	141
508	6	141
509	5	141
510	16	141
511	13	142
512	9	143
513	7	143
514	4	143
515	8	143
516	6	143
517	5	143
518	16	143
519	13	144
520	9	145
521	7	145
522	4	145
523	8	145
524	6	145
525	5	145
526	16	145
527	13	146
528	9	147
529	7	147
530	4	147
531	8	147
532	6	147
533	5	147
534	16	147
535	13	148
536	9	149
537	7	149
538	4	149
539	8	149
540	6	149
541	5	149
542	16	149
543	13	150
544	9	151
545	7	151
546	4	151
547	8	151
548	6	151
549	5	151
550	16	151
551	13	152
552	9	153
553	7	153
554	4	153
555	8	153
556	6	153
557	5	153
558	16	153
559	13	154
560	9	155
561	7	155
562	4	155
563	8	155
564	6	155
565	5	155
566	16	155
567	13	156
568	9	157
569	7	157
570	4	157
571	8	157
572	6	157
573	5	157
574	16	157
575	13	158
576	9	159
577	7	159
578	4	159
579	8	159
580	6	159
581	5	159
582	16	159
583	13	160
584	9	161
585	7	161
586	4	161
587	8	161
588	6	161
589	5	161
590	16	161
591	13	162
592	9	163
593	7	163
594	4	163
595	8	163
596	6	163
597	5	163
598	16	163
599	13	164
600	9	165
601	7	165
602	4	165
603	8	165
604	6	165
605	5	165
606	16	165
607	13	166
608	9	167
609	7	167
610	4	167
611	8	167
612	6	167
613	5	167
614	16	167
615	13	168
616	9	169
617	7	169
618	4	169
619	8	169
620	6	169
621	5	169
622	16	169
623	13	170
624	9	171
625	7	171
626	4	171
627	8	171
628	6	171
629	5	171
630	16	171
631	13	172
632	9	173
633	7	173
634	4	173
635	8	173
636	6	173
637	5	173
638	16	173
639	13	174
640	9	175
641	7	175
642	4	175
643	8	175
644	6	175
645	5	175
646	16	175
647	13	176
648	9	177
649	7	177
650	4	177
651	8	177
652	6	177
653	5	177
654	16	177
655	13	178
656	9	179
657	7	179
658	4	179
659	8	179
660	6	179
661	5	179
662	16	179
663	13	180
664	9	181
665	7	181
666	4	181
667	8	181
668	6	181
669	5	181
670	16	181
671	13	182
672	9	183
673	7	183
674	4	183
675	8	183
676	6	183
677	5	183
678	16	183
679	13	184
680	9	185
681	7	185
682	4	185
683	8	185
684	6	185
685	5	185
686	16	185
687	13	186
688	6	187
689	13	188
690	13	189
691	6	190
692	13	191
693	6	192
694	13	193
695	6	194
696	13	195
697	6	196
698	13	197
699	6	198
700	13	199
701	6	200
702	13	201
703	6	202
704	13	203
705	6	204
706	13	205
707	6	206
708	13	207
709	6	208
710	13	209
711	6	210
712	13	211
713	6	212
714	13	213
715	6	214
716	13	215
717	6	216
718	13	217
719	6	218
720	13	219
721	6	220
722	13	221
723	6	222
724	13	223
725	6	224
726	13	225
727	6	226
728	13	227
729	6	228
730	13	229
731	6	230
732	13	231
733	6	232
734	13	233
735	6	234
736	13	235
737	6	236
738	13	237
739	6	238
740	13	239
741	6	240
742	13	241
743	15	242
744	13	243
745	13	244
746	15	245
747	13	246
748	15	247
749	13	248
750	15	249
751	13	250
752	15	251
753	13	252
754	15	253
755	13	254
756	15	255
757	13	256
758	15	257
759	13	258
760	15	259
761	13	260
762	15	261
763	13	262
764	15	263
765	13	264
766	15	265
767	13	266
768	15	267
769	13	268
770	15	269
771	13	270
772	15	271
773	13	272
774	15	273
775	13	274
776	15	275
777	13	276
778	15	277
779	13	278
780	15	279
781	13	280
782	15	281
783	13	282
784	15	283
785	13	284
786	15	285
787	13	286
788	15	287
789	13	288
790	15	289
791	13	290
792	15	291
793	13	292
794	15	293
795	13	294
796	15	295
797	13	296
798	15	297
799	13	298
800	15	299
801	13	300
802	15	301
803	13	302
804	15	303
805	13	304
806	15	305
807	13	306
808	15	307
809	13	308
810	15	309
811	13	310
812	15	311
813	13	312
814	15	313
815	13	314
816	15	315
817	13	316
818	15	317
819	13	318
820	15	319
821	13	320
822	15	321
823	13	322
824	15	323
825	13	324
826	15	325
827	13	326
828	15	327
829	13	328
830	15	329
831	13	330
832	15	331
833	13	332
834	15	333
835	13	334
836	15	335
837	13	336
838	15	337
839	13	338
840	15	339
841	13	340
842	15	341
843	13	342
844	15	343
845	13	344
846	15	345
847	13	346
848	15	347
849	13	348
850	15	349
851	13	350
852	15	351
853	13	352
854	15	353
855	13	354
856	15	355
857	13	356
858	15	357
859	13	358
860	15	359
861	13	360
862	15	361
863	13	362
864	15	363
865	13	364
866	15	365
867	13	366
868	15	367
869	13	368
870	15	369
871	13	370
872	15	371
873	13	372
874	15	373
875	13	374
876	15	375
877	13	376
878	15	377
879	13	378
880	15	379
881	13	380
882	15	381
883	13	382
884	15	383
885	13	384
886	15	385
887	13	386
888	15	387
889	13	388
890	15	389
891	13	390
892	15	391
893	13	392
894	15	393
895	13	394
896	15	395
897	13	396
898	15	397
899	13	398
900	15	399
901	13	400
902	15	401
903	13	402
904	15	403
905	13	404
\.


--
-- Data for Name: ab_permission_view_role; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_permission_view_role (id, permission_view_id, role_id) FROM stdin;
1	1	1
2	2	1
3	3	1
4	4	1
5	5	1
6	6	1
7	7	1
8	8	1
9	9	1
10	10	1
11	11	1
12	12	1
13	13	1
14	14	1
15	15	1
16	16	1
17	17	1
18	18	1
19	19	1
20	20	1
21	21	1
22	22	1
23	23	1
24	24	1
25	25	1
26	26	1
27	27	1
28	28	1
29	29	1
30	30	1
31	31	1
32	32	1
33	33	1
34	34	1
35	35	1
36	36	1
37	37	1
38	38	1
39	39	1
40	40	1
41	41	1
42	42	1
43	43	1
44	44	1
45	45	1
46	46	1
47	47	1
48	48	1
49	49	1
50	50	1
51	51	1
52	52	1
53	53	1
54	54	1
55	55	1
56	56	1
57	57	1
58	58	1
59	59	1
60	60	1
61	61	1
62	62	1
63	63	1
64	64	1
65	65	1
66	66	1
67	67	1
68	68	1
69	69	1
70	70	1
71	71	1
72	72	1
73	73	1
74	74	1
75	75	1
76	76	1
77	77	1
78	78	1
79	79	1
80	80	1
81	81	1
82	82	1
83	83	1
84	84	1
85	85	1
86	86	1
87	87	1
88	88	1
89	89	1
90	90	1
91	91	1
92	92	1
93	93	1
94	94	1
95	95	1
96	96	1
97	97	1
98	98	1
99	99	1
100	100	1
101	101	1
102	102	1
103	103	1
104	104	1
105	105	1
106	106	1
107	107	1
108	108	1
109	109	1
110	110	1
111	111	1
112	112	1
113	113	1
114	114	1
115	115	1
116	116	1
117	117	1
118	118	1
119	119	1
120	120	1
121	121	1
122	122	1
123	123	1
124	124	1
125	125	1
126	126	1
127	127	1
128	128	1
129	129	1
130	130	1
131	131	1
132	132	1
133	133	1
134	134	1
135	135	1
136	136	1
137	137	1
138	138	1
139	139	1
140	140	1
141	141	1
142	142	1
143	143	1
144	144	1
145	145	1
146	146	1
147	147	1
148	148	1
149	149	1
150	150	1
151	151	1
152	152	1
153	153	1
154	154	1
155	155	1
156	156	1
157	157	1
158	158	1
159	159	1
160	160	1
161	161	1
162	162	1
163	163	1
164	164	1
165	165	1
166	166	1
167	167	1
168	168	1
169	169	1
170	170	1
171	171	1
172	172	1
173	173	1
174	174	1
175	175	1
176	176	1
177	177	1
178	178	1
179	179	1
180	180	1
181	181	1
182	182	1
183	183	1
184	184	1
185	185	1
186	186	1
187	187	1
188	188	1
189	189	1
190	190	1
191	191	1
192	192	1
193	193	1
194	194	1
195	195	1
196	196	1
197	197	1
198	198	1
199	199	1
200	200	1
201	201	1
202	202	1
203	203	1
204	204	1
205	205	1
206	206	1
207	207	1
208	208	1
209	209	1
210	210	1
211	211	1
212	212	1
213	213	1
214	214	1
215	215	1
216	216	1
217	217	1
218	218	1
219	219	1
220	220	1
221	221	1
222	222	1
223	223	1
224	224	1
225	225	1
226	226	1
227	227	1
228	228	1
229	229	1
230	230	1
231	231	1
232	232	1
233	233	1
234	234	1
235	235	1
236	236	1
237	237	1
238	238	1
239	239	1
240	240	1
241	241	1
242	242	1
243	243	1
244	244	1
245	245	1
246	246	1
247	247	1
248	248	1
249	249	1
250	250	1
251	251	1
252	252	1
253	253	1
254	254	1
255	255	1
256	256	1
257	257	1
258	258	1
259	259	1
260	260	1
261	261	1
262	262	1
263	263	1
264	264	1
265	265	1
266	266	1
267	267	1
268	268	1
269	269	1
270	270	1
271	271	1
272	272	1
273	273	1
274	274	1
275	275	1
276	276	1
277	277	1
278	278	1
279	279	1
280	280	1
281	281	1
282	282	1
283	283	1
284	284	1
285	285	1
286	286	1
287	287	1
288	288	1
289	289	1
290	290	1
291	291	1
292	292	1
293	293	1
294	294	1
295	295	1
296	296	1
297	297	1
298	298	1
299	299	1
300	300	1
301	301	1
302	302	1
303	303	1
304	304	1
305	305	1
306	306	1
307	307	1
308	308	1
309	309	1
310	310	1
311	311	1
312	312	1
313	313	1
314	314	1
315	315	1
316	316	1
317	317	1
318	318	1
319	319	1
320	320	1
321	321	1
322	322	1
323	323	1
324	324	1
325	325	1
326	326	1
327	327	1
328	328	1
329	329	1
330	330	1
331	331	1
332	332	1
333	333	1
334	334	1
335	335	1
336	336	1
337	337	1
338	338	1
339	339	1
340	340	1
341	341	1
342	342	1
343	343	1
344	344	1
345	345	1
346	346	1
347	347	1
348	348	1
349	349	1
350	350	1
351	351	1
352	352	1
353	353	1
354	354	1
355	355	1
356	356	1
357	357	1
358	358	1
359	359	1
360	360	1
361	361	1
362	362	1
363	363	1
364	364	1
365	365	1
366	366	1
367	367	1
368	368	1
369	369	1
370	370	1
371	371	1
372	372	1
373	373	1
374	374	1
375	375	1
376	376	1
377	377	1
378	378	1
379	379	1
380	380	1
381	381	1
382	382	1
383	383	1
384	384	1
385	385	1
386	386	1
387	387	1
388	388	1
389	389	1
390	390	1
391	391	1
392	392	1
393	393	1
394	394	1
395	395	1
396	396	1
397	397	1
398	398	1
399	399	1
400	400	1
401	401	1
402	402	1
403	403	1
404	404	1
405	405	1
406	406	1
407	407	1
408	408	1
409	409	1
410	410	1
411	411	1
412	412	1
413	413	1
414	414	1
415	415	1
416	416	1
417	417	1
418	418	1
419	419	1
420	420	1
421	421	1
422	422	1
423	423	1
424	424	1
425	425	1
426	426	1
427	427	1
428	428	1
429	429	1
430	430	1
431	431	1
432	432	1
433	433	1
434	434	1
435	435	1
436	436	1
437	437	1
438	438	1
439	439	1
440	440	1
441	441	1
442	442	1
443	443	1
444	444	1
445	445	1
446	446	1
447	447	1
448	448	1
449	449	1
450	450	1
451	451	1
452	452	1
453	453	1
454	454	1
455	455	1
456	456	1
457	457	1
458	458	1
459	459	1
460	460	1
461	461	1
462	462	1
463	463	1
464	464	1
465	465	1
466	466	1
467	467	1
468	468	1
469	469	1
470	470	1
471	471	1
472	472	1
473	473	1
474	474	1
475	475	1
476	476	1
477	477	1
478	478	1
479	479	1
480	480	1
481	481	1
482	482	1
483	483	1
484	484	1
485	485	1
486	486	1
487	487	1
488	488	1
489	489	1
490	490	1
491	491	1
492	492	1
493	493	1
494	494	1
495	495	1
496	496	1
497	497	1
498	498	1
499	499	1
500	500	1
501	501	1
502	502	1
503	503	1
504	504	1
505	505	1
506	506	1
507	507	1
508	508	1
509	509	1
510	510	1
511	511	1
512	512	1
513	513	1
514	514	1
515	515	1
516	516	1
517	517	1
518	518	1
519	519	1
520	520	1
521	521	1
522	522	1
523	523	1
524	524	1
525	525	1
526	526	1
527	527	1
528	528	1
529	529	1
530	530	1
531	531	1
532	532	1
533	533	1
534	534	1
535	535	1
536	536	1
537	537	1
538	538	1
539	539	1
540	540	1
541	541	1
542	542	1
543	543	1
544	544	1
545	545	1
546	546	1
547	547	1
548	548	1
549	549	1
550	550	1
551	551	1
552	552	1
553	553	1
554	554	1
555	555	1
556	556	1
557	557	1
558	558	1
559	559	1
560	560	1
561	561	1
562	562	1
563	563	1
564	564	1
565	565	1
566	566	1
567	567	1
568	568	1
569	569	1
570	570	1
571	571	1
572	572	1
573	573	1
574	574	1
575	575	1
576	576	1
577	577	1
578	578	1
579	579	1
580	580	1
581	581	1
582	582	1
583	583	1
584	584	1
585	585	1
586	586	1
587	587	1
588	588	1
589	589	1
590	590	1
591	591	1
592	592	1
593	593	1
594	594	1
595	595	1
596	596	1
597	597	1
598	598	1
599	599	1
600	600	1
601	601	1
602	602	1
603	603	1
604	604	1
605	605	1
606	606	1
607	607	1
608	608	1
609	609	1
610	610	1
611	611	1
612	612	1
613	613	1
614	614	1
615	615	1
616	616	1
617	617	1
618	618	1
619	619	1
620	620	1
621	621	1
622	622	1
623	623	1
624	624	1
625	625	1
626	626	1
627	627	1
628	628	1
629	629	1
630	630	1
631	631	1
632	632	1
633	633	1
634	634	1
635	635	1
636	636	1
637	637	1
638	638	1
639	639	1
640	640	1
641	641	1
642	642	1
643	643	1
644	644	1
645	645	1
646	646	1
647	647	1
648	648	1
649	649	1
650	650	1
651	651	1
652	652	1
653	653	1
654	654	1
655	655	1
656	656	1
657	657	1
658	658	1
659	659	1
660	660	1
661	661	1
662	662	1
663	663	1
664	664	1
665	665	1
666	666	1
667	667	1
668	668	1
669	669	1
670	670	1
671	671	1
672	672	1
673	673	1
674	674	1
675	675	1
676	676	1
677	677	1
678	678	1
679	679	1
680	680	1
681	681	1
682	682	1
683	683	1
684	684	1
685	685	1
686	686	1
687	687	1
688	688	1
689	689	1
690	690	1
691	691	1
692	692	1
693	693	1
694	694	1
695	695	1
696	696	1
697	697	1
698	698	1
699	699	1
700	700	1
701	701	1
702	702	1
703	703	1
704	704	1
705	705	1
706	706	1
707	707	1
708	708	1
709	709	1
710	710	1
711	711	1
712	712	1
713	713	1
714	714	1
715	715	1
716	716	1
717	717	1
718	718	1
719	719	1
720	720	1
721	721	1
722	722	1
723	723	1
724	724	1
725	725	1
726	726	1
727	727	1
728	728	1
729	729	1
730	730	1
731	731	1
732	732	1
733	733	1
734	734	1
735	735	1
736	736	1
737	737	1
738	738	1
739	739	1
740	740	1
741	741	1
742	742	1
743	743	1
744	744	1
745	745	1
746	746	1
747	747	1
748	748	1
749	749	1
750	750	1
751	751	1
752	752	1
753	753	1
754	754	1
755	755	1
756	756	1
757	757	1
758	758	1
759	759	1
760	760	1
761	761	1
762	762	1
763	763	1
764	764	1
765	765	1
766	766	1
767	767	1
768	768	1
769	769	1
770	770	1
771	771	1
772	772	1
773	773	1
774	774	1
775	775	1
776	776	1
777	777	1
778	778	1
779	779	1
780	780	1
781	781	1
782	782	1
783	783	1
784	784	1
785	785	1
786	786	1
787	787	1
788	788	1
789	789	1
790	790	1
791	791	1
792	792	1
793	793	1
794	794	1
795	795	1
796	796	1
797	797	1
798	798	1
799	799	1
800	800	1
801	801	1
802	802	1
803	803	1
804	804	1
805	805	1
806	806	1
807	807	1
808	808	1
809	809	1
810	810	1
811	811	1
812	812	1
813	813	1
814	814	1
815	815	1
816	816	1
817	817	1
818	818	1
819	819	1
820	820	1
821	821	1
822	822	1
823	823	1
824	824	1
825	825	1
826	826	1
827	827	1
828	828	1
829	829	1
830	830	1
831	831	1
832	832	1
833	833	1
834	834	1
835	835	1
836	836	1
837	837	1
838	838	1
839	839	1
840	840	1
841	841	1
842	842	1
843	843	1
844	844	1
845	845	1
846	846	1
847	847	1
848	848	1
849	849	1
850	850	1
851	851	1
852	852	1
853	853	1
854	854	1
855	855	1
856	856	1
857	857	1
858	858	1
859	859	1
860	860	1
861	861	1
862	862	1
863	863	1
864	864	1
865	865	1
866	866	1
867	867	1
868	868	1
869	869	1
870	870	1
871	871	1
872	872	1
873	873	1
874	874	1
875	875	1
876	876	1
877	877	1
878	878	1
879	879	1
880	880	1
881	881	1
882	882	1
883	883	1
884	884	1
885	885	1
886	886	1
887	887	1
888	888	1
889	889	1
890	890	1
891	891	1
892	892	1
893	893	1
894	894	1
895	895	1
896	896	1
897	897	1
898	898	1
899	899	1
900	900	1
901	901	1
902	902	1
903	903	1
904	904	1
905	905	1
\.


--
-- Data for Name: ab_register_user; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_register_user (id, first_name, last_name, username, password, email, registration_date, registration_hash) FROM stdin;
\.


--
-- Data for Name: ab_role; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_role (id, name) FROM stdin;
1	Admin
2	Public
\.


--
-- Data for Name: ab_user; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_user (id, first_name, last_name, username, password, active, email, last_login, login_count, fail_login_count, created_on, changed_on, created_by_fk, changed_by_fk) FROM stdin;
1	admin	user	admin	pbkdf2:sha256:50000$XltIvqcC$07ffeb8f651551e24083de80d6897fdc59566930c19991a50d44e43ea475933c	t	admin@fab.org	2018-02-07 10:24:05.000028	1	0	2018-02-07 10:23:09.194204	2018-02-07 10:23:09.194213	\N	\N
\.


--
-- Data for Name: ab_user_role; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_user_role (id, user_id, role_id) FROM stdin;
1	1	1
\.


--
-- Data for Name: ab_view_menu; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ab_view_menu (id, name) FROM stdin;
1	IndexView
2	UtilView
3	LocaleView
4	RegisterUserDBView
5	ResetPasswordView
6	ResetMyPasswordView
7	UserInfoEditView
8	AuthDBView
9	UserDBModelView
10	List Users
11	Security
12	RoleModelView
13	List Roles
14	UserStatsChartView
15	User's Statistics
16	RegisterUserModelView
17	PermissionModelView
18	Base Permissions
19	ViewMenuModelView
20	Views/Menus
21	PermissionViewModelView
22	Permission on Views/Menus
23	AccounttypeView
24	Accounttype
25	Admin
26	BillView
27	Bill
28	Setup
29	BilldetailView
30	Billdetail
31	BiodataView
32	Biodata
33	CasecategoryView
34	Casecategory
35	CasechecklistView
36	Casechecklist
37	CaselinktypeView
38	Caselinktype
39	CelltypeView
40	Celltype
41	CommitalView
42	Commital
43	CommitaltypeView
44	Commitaltype
45	ComplaintView
46	Complaint
47	ComplaintcategoryView
48	Complaintcategory
49	ComplaintroleView
50	Complaintrole
51	CountryView
52	Country
53	CountyView
54	County
55	CourtView
56	Court
57	CourtaccountView
58	Courtaccount
59	CourtcaseView
60	Courtcase
61	CourtrankView
62	Courtrank
63	CourtstationView
64	Courtstation
65	CrimeView
66	Crime
67	CsiEquipmentView
68	CsiEquipment
69	DiagramView
70	Diagram
71	DisciplineView
72	Discipline
73	DoctemplateView
74	Doctemplate
75	DocumentView
76	Document
77	DocumenttypeView
78	Documenttype
79	EconomicclassView
80	Economicclass
81	ExhibitView
82	Exhibit
83	ExpertView
84	Expert
85	ExperttestimonyView
86	Experttestimony
87	ExperttypeView
88	Experttype
89	FeeclassView
90	Feeclass
91	FeetypeView
92	Feetype
93	HealtheventView
94	Healthevent
95	HealtheventtypeView
96	Healtheventtype
97	HearingView
98	Hearing
99	HearingtypeView
100	Hearingtype
101	InstancecrimeView
102	Instancecrime
103	InterviewView
104	Interview
105	InvestigationdiaryView
106	Investigationdiary
107	IssueView
108	Issue
109	JudicialofficerView
110	Judicialofficer
111	JudicialrankView
112	Judicialrank
113	JudicialroleView
114	Judicialrole
115	LawView
116	Law
117	LawfirmView
118	Lawfirm
119	LawyerView
120	Lawyer
121	LegalreferenceView
122	Legalreference
123	NextofkinView
124	Nextofkin
125	NotificationView
126	Notification
127	NotificationregisterView
128	Notificationregister
129	NotificationtypeView
130	Notificationtype
131	NotifyeventView
132	Notifyevent
133	PageView
134	Page
135	PartyView
136	Party
137	PartytypeView
138	Partytype
139	PaymentView
140	Payment
141	PersonaleffectView
142	Personaleffect
143	PersonaleffectscategoryView
144	Personaleffectscategory
145	PoliceofficerView
146	Policeofficer
147	PoliceofficerrankView
148	Policeofficerrank
149	PolicestationView
150	Policestation
151	PolicestationrankView
152	Policestationrank
153	PrisonView
154	Prison
155	PrisonofficerView
156	Prisonofficer
157	PrisonofficerrankView
158	Prisonofficerrank
159	ProsecutorView
160	Prosecutor
161	ProsecutorteamView
162	Prosecutorteam
163	ReleasetypeView
164	Releasetype
165	ReligionView
166	Religion
167	SchedulestatustypeView
168	Schedulestatustype
169	SeizureView
170	Seizure
171	SettlementView
172	Settlement
173	SubcountyView
174	Subcounty
175	TemplatetypeView
176	Templatetype
177	TownView
178	Town
179	TranscriptView
180	Transcript
181	VehicleView
182	Vehicle
183	WardView
184	Ward
185	WarranttypeView
186	Warranttype
187	T_Casecategory_CourtcaseMultiView
188	['Casecategory', 'Courtcase'] Multi View
189	MultiViews
190	T_CasecategorychecklistMultiView
191	['Casecategorychecklist'] Multi View
192	T_Complaint_ComplaintcategoryMultiView
193	['Complaint', 'Complaintcategory'] Multi View
194	T_Complaint_CourtcaseMultiView
195	['Complaint', 'Courtcase'] Multi View
196	T_Court_JudicialofficerMultiView
197	['Court', 'Judicialofficer'] Multi View
198	T_Courtcase_JudicialofficerMultiView
199	['Courtcase', 'Judicialofficer'] Multi View
200	T_Courtcase_LawfirmMultiView
201	['Courtcase', 'Lawfirm'] Multi View
202	T_Csi_Equipment_InvestigationdiaryMultiView
203	['Csi', 'Equipment', 'Investigationdiary'] Multi View
204	T_Document_DocumenttypeMultiView
205	['Document', 'Documenttype'] Multi View
206	T_Expert_ExperttypeMultiView
207	['Expert', 'Experttype'] Multi View
208	T_Hearing_IssueMultiView
209	['Hearing', 'Issue'] Multi View
210	T_Hearing_JudicialofficerMultiView
211	['Hearing', 'Judicialofficer'] Multi View
212	T_Hearing_LawfirmMultiView
213	['Hearing', 'Lawfirm'] Multi View
214	T_Hearing_Lawfirm_MultiView
215	['Hearing', 'Lawfirm', ''] Multi View
216	T_Instancecrime_IssueMultiView
217	['Instancecrime', 'Issue'] Multi View
218	T_Investigationdiary_PartyMultiView
219	['Investigationdiary', 'Party'] Multi View
220	T_Investigationdiary_PoliceofficerMultiView
221	['Investigationdiary', 'Policeofficer'] Multi View
222	T_Investigationdiary_VehicleMultiView
223	['Investigationdiary', 'Vehicle'] Multi View
224	T_Issue_LawyerMultiView
225	['Issue', 'Lawyer'] Multi View
226	T_Issue_LegalreferenceMultiView
227	['Issue', 'Legalreference'] Multi View
228	T_Issue_Legalreference_MultiView
229	['Issue', 'Legalreference', ''] Multi View
230	T_Issue_PartyMultiView
231	['Issue', 'Party'] Multi View
232	T_Issue_Party_MultiView
233	['Issue', 'Party', ''] Multi View
234	T_Lawyer_PartyMultiView
235	['Lawyer', 'Party'] Multi View
236	T_Party_SettlementMultiView
237	['Party', 'Settlement'] Multi View
238	T_Policeofficer_PolicestationMultiView
239	['Policeofficer', 'Policestation'] Multi View
240	T_Town_WardMultiView
241	['Town', 'Ward'] Multi View
242	AccounttypeChartView
243	Accounttype Age Chart
244	Charts
245	BillChartView
246	Bill Age Chart
247	BilldetailChartView
248	Billdetail Age Chart
249	BiodataChartView
250	Biodata Age Chart
251	CasecategoryChartView
252	Casecategory Age Chart
253	CasechecklistChartView
254	Casechecklist Age Chart
255	CaselinktypeChartView
256	Caselinktype Age Chart
257	CelltypeChartView
258	Celltype Age Chart
259	CommitalChartView
260	Commital Age Chart
261	CommitaltypeChartView
262	Commitaltype Age Chart
263	ComplaintChartView
264	Complaint Age Chart
265	ComplaintcategoryChartView
266	Complaintcategory Age Chart
267	ComplaintroleChartView
268	Complaintrole Age Chart
269	CountryChartView
270	Country Age Chart
271	CountyChartView
272	County Age Chart
273	CourtChartView
274	Court Age Chart
275	CourtaccountChartView
276	Courtaccount Age Chart
277	CourtcaseChartView
278	Courtcase Age Chart
279	CourtrankChartView
280	Courtrank Age Chart
281	CourtstationChartView
282	Courtstation Age Chart
283	CrimeChartView
284	Crime Age Chart
285	CsiEquipmentChartView
286	CsiEquipment Age Chart
287	DiagramChartView
288	Diagram Age Chart
289	DisciplineChartView
290	Discipline Age Chart
291	DoctemplateChartView
292	Doctemplate Age Chart
293	DocumentChartView
294	Document Age Chart
295	DocumenttypeChartView
296	Documenttype Age Chart
297	EconomicclassChartView
298	Economicclass Age Chart
299	ExhibitChartView
300	Exhibit Age Chart
301	ExpertChartView
302	Expert Age Chart
303	ExperttestimonyChartView
304	Experttestimony Age Chart
305	ExperttypeChartView
306	Experttype Age Chart
307	FeeclassChartView
308	Feeclass Age Chart
309	FeetypeChartView
310	Feetype Age Chart
311	HealtheventChartView
312	Healthevent Age Chart
313	HealtheventtypeChartView
314	Healtheventtype Age Chart
315	HearingChartView
316	Hearing Age Chart
317	HearingtypeChartView
318	Hearingtype Age Chart
319	InstancecrimeChartView
320	Instancecrime Age Chart
321	InterviewChartView
322	Interview Age Chart
323	InvestigationdiaryChartView
324	Investigationdiary Age Chart
325	IssueChartView
326	Issue Age Chart
327	JudicialofficerChartView
328	Judicialofficer Age Chart
329	JudicialrankChartView
330	Judicialrank Age Chart
331	JudicialroleChartView
332	Judicialrole Age Chart
333	LawChartView
334	Law Age Chart
335	LawfirmChartView
336	Lawfirm Age Chart
337	LawyerChartView
338	Lawyer Age Chart
339	LegalreferenceChartView
340	Legalreference Age Chart
341	NextofkinChartView
342	Nextofkin Age Chart
343	NotificationChartView
344	Notification Age Chart
345	NotificationregisterChartView
346	Notificationregister Age Chart
347	NotificationtypeChartView
348	Notificationtype Age Chart
349	NotifyeventChartView
350	Notifyevent Age Chart
351	PageChartView
352	Page Age Chart
353	PartyChartView
354	Party Age Chart
355	PartytypeChartView
356	Partytype Age Chart
357	PaymentChartView
358	Payment Age Chart
359	PersonaleffectChartView
360	Personaleffect Age Chart
361	PersonaleffectscategoryChartView
362	Personaleffectscategory Age Chart
363	PoliceofficerChartView
364	Policeofficer Age Chart
365	PoliceofficerrankChartView
366	Policeofficerrank Age Chart
367	PolicestationChartView
368	Policestation Age Chart
369	PolicestationrankChartView
370	Policestationrank Age Chart
371	PrisonChartView
372	Prison Age Chart
373	PrisonofficerChartView
374	Prisonofficer Age Chart
375	PrisonofficerrankChartView
376	Prisonofficerrank Age Chart
377	ProsecutorChartView
378	Prosecutor Age Chart
379	ProsecutorteamChartView
380	Prosecutorteam Age Chart
381	ReleasetypeChartView
382	Releasetype Age Chart
383	ReligionChartView
384	Religion Age Chart
385	SchedulestatustypeChartView
386	Schedulestatustype Age Chart
387	SeizureChartView
388	Seizure Age Chart
389	SettlementChartView
390	Settlement Age Chart
391	SubcountyChartView
392	Subcounty Age Chart
393	TemplatetypeChartView
394	Templatetype Age Chart
395	TownChartView
396	Town Age Chart
397	TranscriptChartView
398	Transcript Age Chart
399	VehicleChartView
400	Vehicle Age Chart
401	WardChartView
402	Ward Age Chart
403	WarranttypeChartView
404	Warranttype Age Chart
\.


--
-- Data for Name: accounttype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY accounttype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: accounttype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY accounttype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: bill; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY bill (created_on, changed_on, id, assessing_registrar, receiving_registrar, lawyer_paying, party_paying, documents, date_of_payment, paid, pay_code, bill_total, court, court_account_courts, court_account_account__types, validated, validation_date, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: bill_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY bill_version (created_on, changed_on, id, assessing_registrar, receiving_registrar, lawyer_paying, party_paying, documents, date_of_payment, paid, pay_code, bill_total, court, court_account_courts, court_account_account__types, validated, validation_date, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: billdetail; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY billdetail (created_on, changed_on, id, receipt_id, feetype, purpose, unit, qty, unit_cost, amount, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: billdetail_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY billdetail_version (created_on, changed_on, id, receipt_id, feetype, purpose, unit, qty, unit_cost, amount, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: biodata; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY biodata (created_on, changed_on, allergies, chronic_conditions, chronic_medications, hbp, diabetes, hiv, current_health_status, bc_id, bc_number, bc_serial, bc_place, bc_scan, citizenship, nat_id_num, nat_id_serial, nat_id_scan, pp_no, pp_issue_date, pp_issue_place, pp_scan, pp_expiry_date, kin1_name, kin1_phone, kin1_email, kin1_addr, kin2_name, kin1_relation, kin2_phone, kin2_email, kin2_addr, blood_group, striking_features, height_m, weight_kg, eye_colour, hair_colour, complexion, ethnicity, fp_lthumb, fp_left2, fp_left3, fp_left4, fp_left5, fp_rthumb, fp_right2, fp_right3, fp_right4, fp_right5, palm_left, palm_right, eye_left, eye_right, m_prn, m_firstname, m_surname, m_othernames, m_nat_id_num, m_education, m_occupation, m_income, f_prn, f_firstname, f_surname, f_othernames, f_nat_id_num, f_education, f_occupation, f_income, id, party, economic_class, religion, health_status, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: biodata_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY biodata_version (created_on, changed_on, allergies, chronic_conditions, chronic_medications, hbp, diabetes, hiv, current_health_status, bc_id, bc_number, bc_serial, bc_place, bc_scan, citizenship, nat_id_num, nat_id_serial, nat_id_scan, pp_no, pp_issue_date, pp_issue_place, pp_scan, pp_expiry_date, kin1_name, kin1_phone, kin1_email, kin1_addr, kin2_name, kin1_relation, kin2_phone, kin2_email, kin2_addr, blood_group, striking_features, height_m, weight_kg, eye_colour, hair_colour, complexion, ethnicity, fp_lthumb, fp_left2, fp_left3, fp_left4, fp_left5, fp_rthumb, fp_right2, fp_right3, fp_right4, fp_right5, palm_left, palm_right, eye_left, eye_right, m_prn, m_firstname, m_surname, m_othernames, m_nat_id_num, m_education, m_occupation, m_income, f_prn, f_firstname, f_surname, f_othernames, f_nat_id_num, f_education, f_occupation, f_income, id, party, economic_class, religion, health_status, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: casecategory; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casecategory (created_on, changed_on, name, code, description, notes, id, subcategory, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: casecategory_courtcase; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casecategory_courtcase (casecategory, courtcase) FROM stdin;
\.


--
-- Data for Name: casecategory_courtcase_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casecategory_courtcase_version (casecategory, courtcase, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: casecategory_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casecategory_version (created_on, changed_on, name, code, description, notes, id, subcategory, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: casecategorychecklist; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casecategorychecklist (case_checklists, case_categories) FROM stdin;
\.


--
-- Data for Name: casecategorychecklist_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casecategorychecklist_version (case_checklists, case_categories, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: casechecklist; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casechecklist (created_on, changed_on, code, id, name, description, notes, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: casechecklist_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY casechecklist_version (created_on, changed_on, code, id, name, description, notes, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: caselinktype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY caselinktype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: caselinktype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY caselinktype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: celltype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY celltype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: celltype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY celltype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: commital; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY commital (created_on, changed_on, priority, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, prisons, police_station, parties, casecomplete, commit_date, purpose, warrant_type, warrant_docx, warrant_issue_date, warrant_issued_by, warrant_date_attached, duration, commital, commital_type, court_case, concurrent, life_imprisonment, arrival_date, sentence_start_date, arrest_date, remaining_years, remaining_months, remaining_days, cell_number, cell_type, release_date, exit_date, reason_for_release, with_children, release_type, receiving_officer, releasing_officer, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: commital_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY commital_version (created_on, changed_on, priority, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, prisons, police_station, parties, casecomplete, commit_date, purpose, warrant_type, warrant_docx, warrant_issue_date, warrant_issued_by, warrant_date_attached, duration, commital, commital_type, court_case, concurrent, life_imprisonment, arrival_date, sentence_start_date, arrest_date, remaining_years, remaining_months, remaining_days, cell_number, cell_type, release_date, exit_date, reason_for_release, with_children, release_type, receiving_officer, releasing_officer, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: commitaltype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY commitaltype (created_on, changed_on, name, code, description, notes, id, maxduration, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: commitaltype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY commitaltype_version (created_on, changed_on, name, code, description, notes, id, maxduration, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: complaint; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaint (created_on, changed_on, id, active, ob_number, police_station, daterecvd, datefiled, datecaseopened, casesummary, complaintstatement, circumstances, reportingofficer, casefileinformation, p_request_help, p_instruction, p_submitted, p_submission_date, p_submission_notes, p_closed, p_evaluation, p_recommend_charge, charge_sheet, charge_sheet_docx, evaluating_prosecutor_team, magistrate_report_date, reported_to_judicial_officer, closed, close_date, close_reason, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: complaint_complaintcategory; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaint_complaintcategory (complaint, complaintcategory) FROM stdin;
\.


--
-- Data for Name: complaint_complaintcategory_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaint_complaintcategory_version (complaint, complaintcategory, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: complaint_courtcase; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaint_courtcase (complaint, courtcase) FROM stdin;
\.


--
-- Data for Name: complaint_courtcase_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaint_courtcase_version (complaint, courtcase, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: complaint_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaint_version (created_on, changed_on, id, active, ob_number, police_station, daterecvd, datefiled, datecaseopened, casesummary, complaintstatement, circumstances, reportingofficer, casefileinformation, p_request_help, p_instruction, p_submitted, p_submission_date, p_submission_notes, p_closed, p_evaluation, p_recommend_charge, charge_sheet, charge_sheet_docx, evaluating_prosecutor_team, magistrate_report_date, reported_to_judicial_officer, closed, close_date, close_reason, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: complaintcategory; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaintcategory (created_on, changed_on, name, code, description, notes, id, complaint_category_parent, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: complaintcategory_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaintcategory_version (created_on, changed_on, name, code, description, notes, id, complaint_category_parent, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: complaintrole; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaintrole (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: complaintrole_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY complaintrole_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY country (created_on, changed_on, id, name, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: country_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY country_version (created_on, changed_on, id, name, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: county; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY county (created_on, changed_on, id, country, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: county_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY county_version (created_on, changed_on, id, country, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: court; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY court (created_on, changed_on, place_name, lat, lng, alt, map, info, pin, pin_color, pin_icon, centered, nearest_feature, id, court_rank, court_station, town, till_number, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: court_judicialofficer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY court_judicialofficer (court, judicialofficer) FROM stdin;
\.


--
-- Data for Name: court_judicialofficer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY court_judicialofficer_version (court, judicialofficer, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: court_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY court_version (created_on, changed_on, place_name, lat, lng, alt, map, info, pin, pin_color, pin_icon, centered, nearest_feature, id, court_rank, court_station, town, till_number, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: courtaccount; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtaccount (created_on, changed_on, courts, account__types, account_number, account_name, short_code, bank_name, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: courtaccount_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtaccount_version (created_on, changed_on, courts, account__types, account_number, account_name, short_code, bank_name, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: courtcase; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtcase (created_on, changed_on, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, docket_number, case_number, adr, mediation_proposal, case_received_date, case_filed_date, case_summary, filing_prosecutor, fast_track, priority, object_of_litigation, grounds, prosecution_prayer, pretrial_date, pretrial_notes, pretrial_registrar, case_admissible, indictment_date, judgement, judgement_docx, case_link_type, linked_cases, appealed, appeal_number, inventory_of_docket, next_hearing_date, interlocutory_judgement, reopen, reopen_reason, combined_case, value_in_dispute, award, govt_liability, active, active_date, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: courtcase_judicialofficer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtcase_judicialofficer (courtcase, judicialofficer) FROM stdin;
\.


--
-- Data for Name: courtcase_judicialofficer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtcase_judicialofficer_version (courtcase, judicialofficer, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: courtcase_lawfirm; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtcase_lawfirm (courtcase, lawfirm) FROM stdin;
\.


--
-- Data for Name: courtcase_lawfirm_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtcase_lawfirm_version (courtcase, lawfirm, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: courtcase_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtcase_version (created_on, changed_on, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, docket_number, case_number, adr, mediation_proposal, case_received_date, case_filed_date, case_summary, filing_prosecutor, fast_track, priority, object_of_litigation, grounds, prosecution_prayer, pretrial_date, pretrial_notes, pretrial_registrar, case_admissible, indictment_date, judgement, judgement_docx, case_link_type, linked_cases, appealed, appeal_number, inventory_of_docket, next_hearing_date, interlocutory_judgement, reopen, reopen_reason, combined_case, value_in_dispute, award, govt_liability, active, active_date, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: courtrank; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtrank (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: courtrank_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtrank_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: courtstation; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtstation (created_on, changed_on, name, code, description, notes, id, till_number, pay_bill, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: courtstation_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY courtstation_version (created_on, changed_on, name, code, description, notes, id, till_number, pay_bill, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: crime; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY crime (created_on, changed_on, id, law, description, ref, ref_law, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: crime_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY crime_version (created_on, changed_on, id, law, description, ref, ref_law, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: csi_equipment; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY csi_equipment (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: csi_equipment_investigationdiary; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY csi_equipment_investigationdiary (csi_equipment, investigationdiary) FROM stdin;
\.


--
-- Data for Name: csi_equipment_investigationdiary_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY csi_equipment_investigationdiary_version (csi_equipment, investigationdiary, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: csi_equipment_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY csi_equipment_version (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: diagram; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY diagram (created_on, changed_on, id, investigation_diary, image, description, docx, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: diagram_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY diagram_version (created_on, changed_on, id, investigation_diary, image, description, docx, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: discipline; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY discipline (created_on, changed_on, name, code, description, notes, id, party, prison_officer, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: discipline_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY discipline_version (created_on, changed_on, name, code, description, notes, id, party, prison_officer, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: doctemplate; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY doctemplate (created_on, changed_on, id, template, docx, name, title, summary, template_type, icon, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: doctemplate_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY doctemplate_version (created_on, changed_on, id, template, docx, name, title, summary, template_type, icon, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: document; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY document (created_on, changed_on, mime_type, doc, doc_text, doc_binary, doc_title, subject, author, keywords, comments, doc_type, char_count, word_count, lines, paragraphs, file_size_bytes, producer_prog, immutable, page_size, hashx, audio_duration_secs, audio_frame_rate, audio_channels, search_vector, id, name, court_case, issue, document_admissibility, admitted, judicial_officer, filing_date, admisibility_notes, docx, document_text, published, publish_newspaper, publish_date, validated, paid, page_count, file_byte_count, file_hash, file_timestamp, file_create_date, file_update_date, file_text, file_ext, file_load_path, file_upload_date, file_parse_status, doc_template, visible, is_scan, doc_shelf, doc_row, doc_room, doc_placed_by, citation, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: document_documenttype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY document_documenttype (document, documenttype) FROM stdin;
\.


--
-- Data for Name: document_documenttype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY document_documenttype_version (document, documenttype, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: document_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY document_version (created_on, changed_on, mime_type, doc, doc_text, doc_binary, doc_title, subject, author, keywords, comments, doc_type, char_count, word_count, lines, paragraphs, file_size_bytes, producer_prog, immutable, page_size, hashx, audio_duration_secs, audio_frame_rate, audio_channels, search_vector, id, name, court_case, issue, document_admissibility, admitted, judicial_officer, filing_date, admisibility_notes, docx, document_text, published, publish_newspaper, publish_date, validated, paid, page_count, file_byte_count, file_hash, file_timestamp, file_create_date, file_update_date, file_text, file_ext, file_load_path, file_upload_date, file_parse_status, doc_template, visible, is_scan, doc_shelf, doc_row, doc_room, doc_placed_by, citation, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: documenttype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY documenttype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: documenttype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY documenttype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: economicclass; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY economicclass (created_on, changed_on, code, notes, id, name, description, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: economicclass_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY economicclass_version (created_on, changed_on, code, notes, id, name, description, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: exhibit; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY exhibit (created_on, changed_on, mime_type, doc, doc_text, doc_binary, doc_title, subject, author, keywords, comments, doc_type, char_count, word_count, lines, paragraphs, file_size_bytes, producer_prog, immutable, page_size, page_count, hashx, audio_duration_secs, audio_frame_rate, audio_channels, search_vector, id, investigation_entry, exhibit_no, docx, seizure, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: exhibit_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY exhibit_version (created_on, changed_on, mime_type, doc, doc_text, doc_binary, doc_title, subject, author, keywords, comments, doc_type, char_count, word_count, lines, paragraphs, file_size_bytes, producer_prog, immutable, page_size, page_count, hashx, audio_duration_secs, audio_frame_rate, audio_channels, search_vector, id, investigation_entry, exhibit_no, docx, seizure, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: expert; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY expert (created_on, changed_on, id, institution, jobtitle, credentials, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: expert_experttype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY expert_experttype (expert, experttype) FROM stdin;
\.


--
-- Data for Name: expert_experttype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY expert_experttype_version (expert, experttype, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: expert_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY expert_version (created_on, changed_on, id, institution, jobtitle, credentials, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: experttestimony; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY experttestimony (created_on, changed_on, investigation_entries, experts, task_given, summary_of_facts, statement, task_request_date, testimony_date, validated, requesting_police_officer, court_case, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: experttestimony_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY experttestimony_version (created_on, changed_on, investigation_entries, experts, task_given, summary_of_facts, statement, task_request_date, testimony_date, validated, requesting_police_officer, court_case, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: experttype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY experttype (created_on, changed_on, name, code, description, notes, id, expert_type, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: experttype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY experttype_version (created_on, changed_on, name, code, description, notes, id, expert_type, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: feeclass; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY feeclass (created_on, changed_on, name, code, description, notes, id, fee_type, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: feeclass_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY feeclass_version (created_on, changed_on, name, code, description, notes, id, fee_type, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: feetype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY feetype (created_on, changed_on, name, code, notes, id, filing_fee_type, amount, unit, min_fee, max_fee, description, guide_sec, guide_clause, account_type, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: feetype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY feetype_version (created_on, changed_on, name, code, notes, id, filing_fee_type, amount, unit, min_fee, max_fee, description, guide_sec, guide_clause, account_type, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: healthevent; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY healthevent (created_on, changed_on, priority, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, party, reporting_prison_officer, health_event_type, startdate, enddate, notes, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: healthevent_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY healthevent_version (created_on, changed_on, priority, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, party, reporting_prison_officer, health_event_type, startdate, enddate, notes, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: healtheventtype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY healtheventtype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: healtheventtype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY healtheventtype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: hearing; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing (created_on, changed_on, priority, segment, task_group, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, court_cases, hearing_type, schedule_status, hearing_date, reason, sequence, yearday, starttime, endtime, notes, completed, adjourned_to, adjournment_reason, transcript, atendance, next_hearing_date, postponement_reason, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: hearing_issue; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_issue (hearing, issue) FROM stdin;
\.


--
-- Data for Name: hearing_issue_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_issue_version (hearing, issue, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: hearing_judicialofficer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_judicialofficer (hearing, judicialofficer) FROM stdin;
\.


--
-- Data for Name: hearing_judicialofficer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_judicialofficer_version (hearing, judicialofficer, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: hearing_lawfirm; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_lawfirm (hearing, lawfirm) FROM stdin;
\.


--
-- Data for Name: hearing_lawfirm_2; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_lawfirm_2 (hearing, lawfirm) FROM stdin;
\.


--
-- Data for Name: hearing_lawfirm_2_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_lawfirm_2_version (hearing, lawfirm, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: hearing_lawfirm_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_lawfirm_version (hearing, lawfirm, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: hearing_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearing_version (created_on, changed_on, priority, segment, task_group, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, court_cases, hearing_type, schedule_status, hearing_date, reason, sequence, yearday, starttime, endtime, notes, completed, adjourned_to, adjournment_reason, transcript, atendance, next_hearing_date, postponement_reason, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: hearingtype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearingtype (created_on, changed_on, name, code, description, notes, id, hearing_type, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: hearingtype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY hearingtype_version (created_on, changed_on, name, code, description, notes, id, hearing_type, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: instancecrime; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY instancecrime (created_on, changed_on, id, parties, crimes, crime_detail, tffender_type, crime_date, date_note, place_of_crime, place_note, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: instancecrime_issue; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY instancecrime_issue (instancecrime, issue) FROM stdin;
\.


--
-- Data for Name: instancecrime_issue_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY instancecrime_issue_version (instancecrime, issue, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: instancecrime_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY instancecrime_version (created_on, changed_on, id, parties, crimes, crime_detail, tffender_type, crime_date, date_note, place_of_crime, place_note, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: interview; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY interview (created_on, changed_on, id, investigation_entry, question, answer, validated, language, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: interview_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY interview_version (created_on, changed_on, id, investigation_entry, question, answer, validated, language, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: investigationdiary; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary (created_on, changed_on, priority, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, activity, complaint, location, outcome, equipmentresults, startdate, enddate, advocate_present, summons_statement, arrest_statement, arrest_warrant, search_seizure_statement, docx, detained, detained_at, provisional_release_statement, warrant_type, warrant_issued_by, warrant_issue_date, warrant_delivered_by, warrant_received_by, warrant_serve_date, warrant_docx, warrant_upload_date, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: investigationdiary_party; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary_party (investigationdiary, party) FROM stdin;
\.


--
-- Data for Name: investigationdiary_party_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary_party_version (investigationdiary, party, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: investigationdiary_policeofficer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary_policeofficer (investigationdiary, policeofficer) FROM stdin;
\.


--
-- Data for Name: investigationdiary_policeofficer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary_policeofficer_version (investigationdiary, policeofficer, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: investigationdiary_vehicle; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary_vehicle (investigationdiary, vehicle) FROM stdin;
\.


--
-- Data for Name: investigationdiary_vehicle_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary_vehicle_version (investigationdiary, vehicle, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: investigationdiary_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY investigationdiary_version (created_on, changed_on, priority, segment, task_group, sequence, action, activity_description, goal, status, planned_start, actual_start, start_delay, start_notes, active, planned_end, actual_end, end_delay, end_notes, deadline, not_started, early_start, late_start, completed, early_end, late_end, deviation_expected, contingency_plan, budget, spend_td, balance_avail, over_budget, under_budget, id, activity, complaint, location, outcome, equipmentresults, startdate, enddate, advocate_present, summons_statement, arrest_statement, arrest_warrant, search_seizure_statement, docx, detained, detained_at, provisional_release_statement, warrant_type, warrant_issued_by, warrant_issue_date, warrant_delivered_by, warrant_received_by, warrant_serve_date, warrant_docx, warrant_upload_date, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: issue; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue (created_on, changed_on, id, issue, facts, counter_claim, argument, argument_date, argument_docx, rebuttal, rebuttal_date, rebuttal_docx, hearing_date, determination, dtermination_date, determination_docx, resolved, defense_lawyer, prosecutor, judicial_officer, court_case, tasks, is_criminal, moral_element, material_element, legal_element, debt_amount, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: issue_lawyer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_lawyer (issue, lawyer) FROM stdin;
\.


--
-- Data for Name: issue_lawyer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_lawyer_version (issue, lawyer, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: issue_legalreference; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_legalreference (issue, legalreference) FROM stdin;
\.


--
-- Data for Name: issue_legalreference_2; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_legalreference_2 (issue, legalreference) FROM stdin;
\.


--
-- Data for Name: issue_legalreference_2_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_legalreference_2_version (issue, legalreference, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: issue_legalreference_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_legalreference_version (issue, legalreference, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: issue_party; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_party (issue, party) FROM stdin;
\.


--
-- Data for Name: issue_party_2; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_party_2 (issue, party) FROM stdin;
\.


--
-- Data for Name: issue_party_2_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_party_2_version (issue, party, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: issue_party_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_party_version (issue, party, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: issue_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY issue_version (created_on, changed_on, id, issue, facts, counter_claim, argument, argument_date, argument_docx, rebuttal, rebuttal_date, rebuttal_docx, hearing_date, determination, dtermination_date, determination_docx, resolved, defense_lawyer, prosecutor, judicial_officer, court_case, tasks, is_criminal, moral_element, material_element, legal_element, debt_amount, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: judicialofficer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY judicialofficer (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, id, rank, judicial_role, court_station, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: judicialofficer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY judicialofficer_version (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, id, rank, judicial_role, court_station, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: judicialrank; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY judicialrank (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: judicialrank_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY judicialrank_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: judicialrole; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY judicialrole (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: judicialrole_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY judicialrole_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: law; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY law (created_on, changed_on, id, name, description, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: law_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY law_version (created_on, changed_on, id, name, description, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: lawfirm; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY lawfirm (created_on, changed_on, name, code, description, notes, place_name, lat, lng, alt, map, info, pin, pin_color, pin_icon, centered, nearest_feature, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: lawfirm_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY lawfirm_version (created_on, changed_on, name, code, description, notes, place_name, lat, lng, alt, map, info, pin, pin_color, pin_icon, centered, nearest_feature, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: lawyer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY lawyer (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, law_firm, bar_no, bar_date, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: lawyer_party; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY lawyer_party (lawyer, party) FROM stdin;
\.


--
-- Data for Name: lawyer_party_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY lawyer_party_version (lawyer, party, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: lawyer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY lawyer_version (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, law_firm, bar_no, bar_date, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: legalreference; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY legalreference (created_on, changed_on, id, ref, verbatim, public, commentary, validated, citation, quote, interpretation, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: legalreference_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY legalreference_version (created_on, changed_on, id, ref, verbatim, public, commentary, validated, citation, quote, interpretation, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: nextofkin; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY nextofkin (created_on, changed_on, bc_id, bc_number, bc_serial, bc_place, bc_scan, citizenship, nat_id_num, nat_id_serial, nat_id_scan, pp_no, pp_issue_date, pp_issue_place, pp_scan, pp_expiry_date, kin1_name, kin1_phone, kin1_email, kin1_addr, kin2_name, kin1_relation, kin2_phone, kin2_email, kin2_addr, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, biodata, childunder4, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: nextofkin_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY nextofkin_version (created_on, changed_on, bc_id, bc_number, bc_serial, bc_place, bc_scan, citizenship, nat_id_num, nat_id_serial, nat_id_scan, pp_no, pp_issue_date, pp_issue_place, pp_scan, pp_expiry_date, kin1_name, kin1_phone, kin1_email, kin1_addr, kin2_name, kin1_relation, kin2_phone, kin2_email, kin2_addr, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, biodata, childunder4, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: notification; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notification (created_on, changed_on, id, contact, message, confirmation, notification_register, add_date, send_date, sent, delivered, retries, abandon, retry_count, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: notification_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notification_version (created_on, changed_on, id, contact, message, confirmation, notification_register, add_date, send_date, sent, delivered, retries, abandon, retry_count, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: notificationregister; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notificationregister (created_on, changed_on, id, notification_type, contact, notify_event, retry_count, active, hearing, document, court_case, complaint, complaint_category, health_event, party, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: notificationregister_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notificationregister_version (created_on, changed_on, id, notification_type, contact, notify_event, retry_count, active, hearing, document, court_case, complaint, complaint_category, health_event, party, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: notificationtype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notificationtype (created_on, changed_on, code, notes, id, name, description, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: notificationtype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notificationtype_version (created_on, changed_on, code, notes, id, name, description, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: notifyevent; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notifyevent (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: notifyevent_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY notifyevent_version (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: page; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY page (created_on, changed_on, id, document, page_image, page_no, page_text, image_ext, image_width, image_height, create_date, update_date, upload_dt, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: page_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY page_version (created_on, changed_on, id, document, page_image, page_no, page_text, image_ext, image_width, image_height, create_date, update_date, upload_dt, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: party; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY party (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, complaints, statement, statementdate, complaint_role, notes, dateofrepresentation, party_type, relative, relationship_type, is_infant, is_minor, miranda_read, miranda_date, miranda_witness, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: party_settlement; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY party_settlement (party, settlement) FROM stdin;
\.


--
-- Data for Name: party_settlement_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY party_settlement_version (party, settlement, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: party_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY party_version (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, complaints, statement, statementdate, complaint_role, notes, dateofrepresentation, party_type, relative, relationship_type, is_infant, is_minor, miranda_read, miranda_date, miranda_witness, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: partytype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY partytype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: partytype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY partytype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY payment (created_on, changed_on, id, bill, amount, payment_ref, date_paid, phone_number, validated, payment_description, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: payment_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY payment_version (created_on, changed_on, id, bill, amount, payment_ref, date_paid, phone_number, validated, payment_description, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: personaleffect; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY personaleffect (created_on, changed_on, id, party, personal_effects_category, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: personaleffect_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY personaleffect_version (created_on, changed_on, id, party, personal_effects_category, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: personaleffectscategory; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY personaleffectscategory (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: personaleffectscategory_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY personaleffectscategory_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: policeofficer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policeofficer (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, id, police_rank, servicenumber, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: policeofficer_policestation; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policeofficer_policestation (policeofficer, policestation) FROM stdin;
\.


--
-- Data for Name: policeofficer_policestation_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policeofficer_policestation_version (policeofficer, policestation, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: policeofficer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policeofficer_version (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, id, police_rank, servicenumber, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: policeofficerrank; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policeofficerrank (created_on, changed_on, code, notes, id, name, description, sequence, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: policeofficerrank_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policeofficerrank_version (created_on, changed_on, code, notes, id, name, description, sequence, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: policestation; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policestation (created_on, changed_on, name, code, description, notes, id, town, officer_commanding, police_station_rank, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: policestation_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policestation_version (created_on, changed_on, name, code, description, notes, id, town, officer_commanding, police_station_rank, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: policestationrank; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policestationrank (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: policestationrank_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY policestationrank_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: prison; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prison (created_on, changed_on, place_name, lat, lng, alt, map, info, pin, pin_color, pin_icon, centered, nearest_feature, id, town, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: prison_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prison_version (created_on, changed_on, place_name, lat, lng, alt, map, info, pin, pin_color, pin_icon, centered, nearest_feature, id, town, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: prisonofficer; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prisonofficer (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, id, prison, prison_officer_rank, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: prisonofficer_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prisonofficer_version (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, id, prison, prison_officer_rank, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: prisonofficerrank; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prisonofficerrank (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: prisonofficerrank_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prisonofficerrank_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: prosecutor; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prosecutor (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, prosecutor_team, lawyer, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: prosecutor_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prosecutor_version (created_on, changed_on, firstname, surname, othernames, dob, gender, marital_status, mobile, other_mobile, fixed_line, other_fixed_line, email, other_email, address_line_1, address_line_2, zipcode, town, country, facebook, twitter, instagram, whatsapp, other_whatsapp, fax, gcode, okhi, id, prosecutor_team, lawyer, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: prosecutorteam; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prosecutorteam (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: prosecutorteam_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY prosecutorteam_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: releasetype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY releasetype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: releasetype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY releasetype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: religion; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY religion (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: religion_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY religion_version (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: schedulestatustype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY schedulestatustype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: schedulestatustype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY schedulestatustype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: seizure; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY seizure (created_on, changed_on, id, investigation_diary, owner, item, item_packaging, item_pic, premises, reg_no, witness, notes, docx, item_description, returned, return_date, return_notes, return_signed_receipt, destroyed, destruction_date, destruction_witnesses, destruction_notes, disposed, sold_to, disposal_date, disposal_price, disposal_receipt, recovery_town, destruction_pic, is_evidence, immovable, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: seizure_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY seizure_version (created_on, changed_on, id, investigation_diary, owner, item, item_packaging, item_pic, premises, reg_no, witness, notes, docx, item_description, returned, return_date, return_notes, return_signed_receipt, destroyed, destruction_date, destruction_witnesses, destruction_notes, disposed, sold_to, disposal_date, disposal_price, disposal_receipt, recovery_town, destruction_pic, is_evidence, immovable, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: settlement; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY settlement (created_on, changed_on, id, complaint, terms, amount, paid, docx, settlor, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: settlement_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY settlement_version (created_on, changed_on, id, complaint, terms, amount, paid, docx, settlor, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: subcounty; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY subcounty (created_on, changed_on, id, county, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: subcounty_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY subcounty_version (created_on, changed_on, id, county, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: templatetype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY templatetype (created_on, changed_on, name, code, description, notes, id, template_type, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: templatetype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY templatetype_version (created_on, changed_on, name, code, description, notes, id, template_type, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: town; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY town (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: town_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY town_version (created_on, changed_on, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: town_ward; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY town_ward (town, ward) FROM stdin;
\.


--
-- Data for Name: town_ward_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY town_ward_version (town, ward, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: transaction; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY transaction (issued_at, id, remote_addr, user_id) FROM stdin;
\.


--
-- Data for Name: transcript; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY transcript (created_on, changed_on, mime_type, doc, doc_text, doc_binary, doc_title, subject, author, keywords, comments, doc_type, char_count, word_count, lines, paragraphs, file_size_bytes, producer_prog, immutable, page_size, page_count, hashx, audio_duration_secs, audio_frame_rate, audio_channels, search_vector, id, video, audio, add_date, asr_transcript, asr_date, edited_transcript, edit_date, certified_transcript, certfiy_date, locked, hearing, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: transcript_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY transcript_version (created_on, changed_on, mime_type, doc, doc_text, doc_binary, doc_title, subject, author, keywords, comments, doc_type, char_count, word_count, lines, paragraphs, file_size_bytes, producer_prog, immutable, page_size, page_count, hashx, audio_duration_secs, audio_frame_rate, audio_channels, search_vector, id, video, audio, add_date, asr_transcript, asr_date, edited_transcript, edit_date, certified_transcript, certfiy_date, locked, hearing, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: vehicle; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY vehicle (created_on, changed_on, id, police_station, make, model, regno, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: vehicle_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY vehicle_version (created_on, changed_on, id, police_station, make, model, regno, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: ward; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ward (created_on, changed_on, id, subcounty, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: ward_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY ward_version (created_on, changed_on, id, subcounty, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Data for Name: warranttype; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY warranttype (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk) FROM stdin;
\.


--
-- Data for Name: warranttype_version; Type: TABLE DATA; Schema: public; Owner: nyimbi
--

COPY warranttype_version (created_on, changed_on, name, code, description, notes, id, photo, file, created_by_fk, changed_by_fk, transaction_id, end_transaction_id, operation_type) FROM stdin;
\.


--
-- Name: ab_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_permission_id_seq', 16, true);


--
-- Name: ab_permission_view_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_permission_view_id_seq', 905, true);


--
-- Name: ab_permission_view_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_permission_view_role_id_seq', 905, true);


--
-- Name: ab_register_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_register_user_id_seq', 1, false);


--
-- Name: ab_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_role_id_seq', 2, true);


--
-- Name: ab_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_user_id_seq', 1, true);


--
-- Name: ab_user_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_user_role_id_seq', 1, true);


--
-- Name: ab_view_menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ab_view_menu_id_seq', 404, true);


--
-- Name: accounttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('accounttype_id_seq', 1, false);


--
-- Name: bill_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('bill_id_seq', 1, false);


--
-- Name: billdetail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('billdetail_id_seq', 1, false);


--
-- Name: biodata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('biodata_id_seq', 1, false);


--
-- Name: casecategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('casecategory_id_seq', 1, false);


--
-- Name: casechecklist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('casechecklist_id_seq', 1, false);


--
-- Name: caselinktype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('caselinktype_id_seq', 1, false);


--
-- Name: celltype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('celltype_id_seq', 1, false);


--
-- Name: commital_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('commital_id_seq', 1, false);


--
-- Name: commitaltype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('commitaltype_id_seq', 1, false);


--
-- Name: complaint_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('complaint_id_seq', 1, false);


--
-- Name: complaintcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('complaintcategory_id_seq', 1, false);


--
-- Name: complaintrole_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('complaintrole_id_seq', 1, false);


--
-- Name: country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('country_id_seq', 1, false);


--
-- Name: county_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('county_id_seq', 1, false);


--
-- Name: court_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('court_id_seq', 1, false);


--
-- Name: courtcase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('courtcase_id_seq', 1, false);


--
-- Name: courtrank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('courtrank_id_seq', 1, false);


--
-- Name: courtstation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('courtstation_id_seq', 1, false);


--
-- Name: crime_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('crime_id_seq', 1, false);


--
-- Name: csi_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('csi_equipment_id_seq', 1, false);


--
-- Name: diagram_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('diagram_id_seq', 1, false);


--
-- Name: discipline_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('discipline_id_seq', 1, false);


--
-- Name: doctemplate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('doctemplate_id_seq', 1, false);


--
-- Name: document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('document_id_seq', 1, false);


--
-- Name: documenttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('documenttype_id_seq', 1, false);


--
-- Name: economicclass_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('economicclass_id_seq', 1, false);


--
-- Name: exhibit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('exhibit_id_seq', 1, false);


--
-- Name: expert_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('expert_id_seq', 1, false);


--
-- Name: experttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('experttype_id_seq', 1, false);


--
-- Name: feeclass_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('feeclass_id_seq', 1, false);


--
-- Name: feetype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('feetype_id_seq', 1, false);


--
-- Name: healthevent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('healthevent_id_seq', 1, false);


--
-- Name: healtheventtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('healtheventtype_id_seq', 1, false);


--
-- Name: hearing_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('hearing_id_seq', 1, false);


--
-- Name: hearingtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('hearingtype_id_seq', 1, false);


--
-- Name: instancecrime_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('instancecrime_id_seq', 1, false);


--
-- Name: interview_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('interview_id_seq', 1, false);


--
-- Name: investigationdiary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('investigationdiary_id_seq', 1, false);


--
-- Name: issue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('issue_id_seq', 1, false);


--
-- Name: judicialofficer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('judicialofficer_id_seq', 1, false);


--
-- Name: judicialrank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('judicialrank_id_seq', 1, false);


--
-- Name: judicialrole_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('judicialrole_id_seq', 1, false);


--
-- Name: law_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('law_id_seq', 1, false);


--
-- Name: lawfirm_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('lawfirm_id_seq', 1, false);


--
-- Name: lawyer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('lawyer_id_seq', 1, false);


--
-- Name: legalreference_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('legalreference_id_seq', 1, false);


--
-- Name: nextofkin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('nextofkin_id_seq', 1, false);


--
-- Name: notification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('notification_id_seq', 1, false);


--
-- Name: notificationregister_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('notificationregister_id_seq', 1, false);


--
-- Name: notificationtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('notificationtype_id_seq', 1, false);


--
-- Name: notifyevent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('notifyevent_id_seq', 1, false);


--
-- Name: page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('page_id_seq', 1, false);


--
-- Name: party_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('party_id_seq', 1, false);


--
-- Name: partytype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('partytype_id_seq', 1, false);


--
-- Name: payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('payment_id_seq', 1, false);


--
-- Name: personaleffect_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('personaleffect_id_seq', 1, false);


--
-- Name: personaleffectscategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('personaleffectscategory_id_seq', 1, false);


--
-- Name: policeofficer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('policeofficer_id_seq', 1, false);


--
-- Name: policeofficerrank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('policeofficerrank_id_seq', 1, false);


--
-- Name: policestation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('policestation_id_seq', 1, false);


--
-- Name: policestationrank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('policestationrank_id_seq', 1, false);


--
-- Name: prison_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('prison_id_seq', 1, false);


--
-- Name: prisonofficer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('prisonofficer_id_seq', 1, false);


--
-- Name: prisonofficerrank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('prisonofficerrank_id_seq', 1, false);


--
-- Name: prosecutor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('prosecutor_id_seq', 1, false);


--
-- Name: prosecutorteam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('prosecutorteam_id_seq', 1, false);


--
-- Name: releasetype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('releasetype_id_seq', 1, false);


--
-- Name: religion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('religion_id_seq', 1, false);


--
-- Name: schedulestatustype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('schedulestatustype_id_seq', 1, false);


--
-- Name: seizure_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('seizure_id_seq', 1, false);


--
-- Name: settlement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('settlement_id_seq', 1, false);


--
-- Name: subcounty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('subcounty_id_seq', 1, false);


--
-- Name: templatetype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('templatetype_id_seq', 1, false);


--
-- Name: town_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('town_id_seq', 1, false);


--
-- Name: transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('transaction_id_seq', 1, false);


--
-- Name: transcript_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('transcript_id_seq', 1, false);


--
-- Name: vehicle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('vehicle_id_seq', 1, false);


--
-- Name: ward_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('ward_id_seq', 1, false);


--
-- Name: warranttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nyimbi
--

SELECT pg_catalog.setval('warranttype_id_seq', 1, false);


--
-- Name: ab_permission ab_permission_name_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission
    ADD CONSTRAINT ab_permission_name_key UNIQUE (name);


--
-- Name: ab_permission ab_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission
    ADD CONSTRAINT ab_permission_pkey PRIMARY KEY (id);


--
-- Name: ab_permission_view ab_permission_view_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission_view
    ADD CONSTRAINT ab_permission_view_pkey PRIMARY KEY (id);


--
-- Name: ab_permission_view_role ab_permission_view_role_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission_view_role
    ADD CONSTRAINT ab_permission_view_role_pkey PRIMARY KEY (id);


--
-- Name: ab_register_user ab_register_user_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_register_user
    ADD CONSTRAINT ab_register_user_pkey PRIMARY KEY (id);


--
-- Name: ab_register_user ab_register_user_username_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_register_user
    ADD CONSTRAINT ab_register_user_username_key UNIQUE (username);


--
-- Name: ab_role ab_role_name_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_role
    ADD CONSTRAINT ab_role_name_key UNIQUE (name);


--
-- Name: ab_role ab_role_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_role
    ADD CONSTRAINT ab_role_pkey PRIMARY KEY (id);


--
-- Name: ab_user ab_user_email_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user
    ADD CONSTRAINT ab_user_email_key UNIQUE (email);


--
-- Name: ab_user ab_user_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user
    ADD CONSTRAINT ab_user_pkey PRIMARY KEY (id);


--
-- Name: ab_user_role ab_user_role_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user_role
    ADD CONSTRAINT ab_user_role_pkey PRIMARY KEY (id);


--
-- Name: ab_user ab_user_username_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user
    ADD CONSTRAINT ab_user_username_key UNIQUE (username);


--
-- Name: ab_view_menu ab_view_menu_name_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_view_menu
    ADD CONSTRAINT ab_view_menu_name_key UNIQUE (name);


--
-- Name: ab_view_menu ab_view_menu_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_view_menu
    ADD CONSTRAINT ab_view_menu_pkey PRIMARY KEY (id);


--
-- Name: accounttype accounttype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY accounttype
    ADD CONSTRAINT accounttype_pkey PRIMARY KEY (id);


--
-- Name: accounttype_version accounttype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY accounttype_version
    ADD CONSTRAINT accounttype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: bill bill_pay_code_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_pay_code_key UNIQUE (pay_code);


--
-- Name: bill bill_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_pkey PRIMARY KEY (id);


--
-- Name: bill_version bill_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill_version
    ADD CONSTRAINT bill_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: billdetail billdetail_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY billdetail
    ADD CONSTRAINT billdetail_pkey PRIMARY KEY (id);


--
-- Name: billdetail_version billdetail_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY billdetail_version
    ADD CONSTRAINT billdetail_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: biodata biodata_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata
    ADD CONSTRAINT biodata_pkey PRIMARY KEY (id);


--
-- Name: biodata_version biodata_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata_version
    ADD CONSTRAINT biodata_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: casecategory_courtcase casecategory_courtcase_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory_courtcase
    ADD CONSTRAINT casecategory_courtcase_pkey PRIMARY KEY (casecategory, courtcase);


--
-- Name: casecategory_courtcase_version casecategory_courtcase_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory_courtcase_version
    ADD CONSTRAINT casecategory_courtcase_version_pkey PRIMARY KEY (casecategory, courtcase, transaction_id);


--
-- Name: casecategory casecategory_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory
    ADD CONSTRAINT casecategory_pkey PRIMARY KEY (id);


--
-- Name: casecategory_version casecategory_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory_version
    ADD CONSTRAINT casecategory_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: casecategorychecklist casecategorychecklist_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategorychecklist
    ADD CONSTRAINT casecategorychecklist_pkey PRIMARY KEY (case_checklists, case_categories);


--
-- Name: casecategorychecklist_version casecategorychecklist_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategorychecklist_version
    ADD CONSTRAINT casecategorychecklist_version_pkey PRIMARY KEY (case_checklists, case_categories, transaction_id);


--
-- Name: casechecklist casechecklist_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casechecklist
    ADD CONSTRAINT casechecklist_pkey PRIMARY KEY (id);


--
-- Name: casechecklist_version casechecklist_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casechecklist_version
    ADD CONSTRAINT casechecklist_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: caselinktype caselinktype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY caselinktype
    ADD CONSTRAINT caselinktype_pkey PRIMARY KEY (id);


--
-- Name: caselinktype_version caselinktype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY caselinktype_version
    ADD CONSTRAINT caselinktype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: celltype celltype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY celltype
    ADD CONSTRAINT celltype_pkey PRIMARY KEY (id);


--
-- Name: celltype_version celltype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY celltype_version
    ADD CONSTRAINT celltype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: commital commital_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_pkey PRIMARY KEY (id);


--
-- Name: commital_version commital_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital_version
    ADD CONSTRAINT commital_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: commitaltype commitaltype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commitaltype
    ADD CONSTRAINT commitaltype_pkey PRIMARY KEY (id);


--
-- Name: commitaltype_version commitaltype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commitaltype_version
    ADD CONSTRAINT commitaltype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: complaint_complaintcategory complaint_complaintcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_complaintcategory
    ADD CONSTRAINT complaint_complaintcategory_pkey PRIMARY KEY (complaint, complaintcategory);


--
-- Name: complaint_complaintcategory_version complaint_complaintcategory_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_complaintcategory_version
    ADD CONSTRAINT complaint_complaintcategory_version_pkey PRIMARY KEY (complaint, complaintcategory, transaction_id);


--
-- Name: complaint_courtcase complaint_courtcase_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_courtcase
    ADD CONSTRAINT complaint_courtcase_pkey PRIMARY KEY (complaint, courtcase);


--
-- Name: complaint_courtcase_version complaint_courtcase_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_courtcase_version
    ADD CONSTRAINT complaint_courtcase_version_pkey PRIMARY KEY (complaint, courtcase, transaction_id);


--
-- Name: complaint complaint_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint
    ADD CONSTRAINT complaint_pkey PRIMARY KEY (id);


--
-- Name: complaint_version complaint_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_version
    ADD CONSTRAINT complaint_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: complaintcategory complaintcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintcategory
    ADD CONSTRAINT complaintcategory_pkey PRIMARY KEY (id);


--
-- Name: complaintcategory_version complaintcategory_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintcategory_version
    ADD CONSTRAINT complaintcategory_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: complaintrole complaintrole_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintrole
    ADD CONSTRAINT complaintrole_pkey PRIMARY KEY (id);


--
-- Name: complaintrole_version complaintrole_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintrole_version
    ADD CONSTRAINT complaintrole_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: country country_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_pkey PRIMARY KEY (id);


--
-- Name: country_version country_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY country_version
    ADD CONSTRAINT country_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: county county_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY county
    ADD CONSTRAINT county_pkey PRIMARY KEY (id);


--
-- Name: county_version county_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY county_version
    ADD CONSTRAINT county_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: court_judicialofficer court_judicialofficer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court_judicialofficer
    ADD CONSTRAINT court_judicialofficer_pkey PRIMARY KEY (court, judicialofficer);


--
-- Name: court_judicialofficer_version court_judicialofficer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court_judicialofficer_version
    ADD CONSTRAINT court_judicialofficer_version_pkey PRIMARY KEY (court, judicialofficer, transaction_id);


--
-- Name: court court_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court
    ADD CONSTRAINT court_pkey PRIMARY KEY (id);


--
-- Name: court_version court_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court_version
    ADD CONSTRAINT court_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: courtaccount courtaccount_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtaccount
    ADD CONSTRAINT courtaccount_pkey PRIMARY KEY (courts, account__types);


--
-- Name: courtaccount_version courtaccount_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtaccount_version
    ADD CONSTRAINT courtaccount_version_pkey PRIMARY KEY (courts, account__types, transaction_id);


--
-- Name: courtcase_judicialofficer courtcase_judicialofficer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_judicialofficer
    ADD CONSTRAINT courtcase_judicialofficer_pkey PRIMARY KEY (courtcase, judicialofficer);


--
-- Name: courtcase_judicialofficer_version courtcase_judicialofficer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_judicialofficer_version
    ADD CONSTRAINT courtcase_judicialofficer_version_pkey PRIMARY KEY (courtcase, judicialofficer, transaction_id);


--
-- Name: courtcase_lawfirm courtcase_lawfirm_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_lawfirm
    ADD CONSTRAINT courtcase_lawfirm_pkey PRIMARY KEY (courtcase, lawfirm);


--
-- Name: courtcase_lawfirm_version courtcase_lawfirm_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_lawfirm_version
    ADD CONSTRAINT courtcase_lawfirm_version_pkey PRIMARY KEY (courtcase, lawfirm, transaction_id);


--
-- Name: courtcase courtcase_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase
    ADD CONSTRAINT courtcase_pkey PRIMARY KEY (id);


--
-- Name: courtcase_version courtcase_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_version
    ADD CONSTRAINT courtcase_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: courtrank courtrank_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtrank
    ADD CONSTRAINT courtrank_pkey PRIMARY KEY (id);


--
-- Name: courtrank_version courtrank_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtrank_version
    ADD CONSTRAINT courtrank_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: courtstation courtstation_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtstation
    ADD CONSTRAINT courtstation_pkey PRIMARY KEY (id);


--
-- Name: courtstation_version courtstation_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtstation_version
    ADD CONSTRAINT courtstation_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: crime crime_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY crime
    ADD CONSTRAINT crime_pkey PRIMARY KEY (id);


--
-- Name: crime_version crime_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY crime_version
    ADD CONSTRAINT crime_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: csi_equipment_investigationdiary csi_equipment_investigationdiary_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment_investigationdiary
    ADD CONSTRAINT csi_equipment_investigationdiary_pkey PRIMARY KEY (csi_equipment, investigationdiary);


--
-- Name: csi_equipment_investigationdiary_version csi_equipment_investigationdiary_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment_investigationdiary_version
    ADD CONSTRAINT csi_equipment_investigationdiary_version_pkey PRIMARY KEY (csi_equipment, investigationdiary, transaction_id);


--
-- Name: csi_equipment csi_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment
    ADD CONSTRAINT csi_equipment_pkey PRIMARY KEY (id);


--
-- Name: csi_equipment_version csi_equipment_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment_version
    ADD CONSTRAINT csi_equipment_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: diagram diagram_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY diagram
    ADD CONSTRAINT diagram_pkey PRIMARY KEY (id);


--
-- Name: diagram_version diagram_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY diagram_version
    ADD CONSTRAINT diagram_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: discipline discipline_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY discipline
    ADD CONSTRAINT discipline_pkey PRIMARY KEY (id);


--
-- Name: discipline_version discipline_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY discipline_version
    ADD CONSTRAINT discipline_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: doctemplate doctemplate_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY doctemplate
    ADD CONSTRAINT doctemplate_pkey PRIMARY KEY (id);


--
-- Name: doctemplate_version doctemplate_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY doctemplate_version
    ADD CONSTRAINT doctemplate_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: document_documenttype document_documenttype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document_documenttype
    ADD CONSTRAINT document_documenttype_pkey PRIMARY KEY (document, documenttype);


--
-- Name: document_documenttype_version document_documenttype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document_documenttype_version
    ADD CONSTRAINT document_documenttype_version_pkey PRIMARY KEY (document, documenttype, transaction_id);


--
-- Name: document document_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document
    ADD CONSTRAINT document_pkey PRIMARY KEY (id);


--
-- Name: document_version document_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document_version
    ADD CONSTRAINT document_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: documenttype documenttype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY documenttype
    ADD CONSTRAINT documenttype_pkey PRIMARY KEY (id);


--
-- Name: documenttype_version documenttype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY documenttype_version
    ADD CONSTRAINT documenttype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: economicclass economicclass_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY economicclass
    ADD CONSTRAINT economicclass_pkey PRIMARY KEY (id);


--
-- Name: economicclass_version economicclass_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY economicclass_version
    ADD CONSTRAINT economicclass_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: exhibit exhibit_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY exhibit
    ADD CONSTRAINT exhibit_pkey PRIMARY KEY (id);


--
-- Name: exhibit_version exhibit_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY exhibit_version
    ADD CONSTRAINT exhibit_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: expert_experttype expert_experttype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert_experttype
    ADD CONSTRAINT expert_experttype_pkey PRIMARY KEY (expert, experttype);


--
-- Name: expert_experttype_version expert_experttype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert_experttype_version
    ADD CONSTRAINT expert_experttype_version_pkey PRIMARY KEY (expert, experttype, transaction_id);


--
-- Name: expert expert_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert
    ADD CONSTRAINT expert_pkey PRIMARY KEY (id);


--
-- Name: expert_version expert_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert_version
    ADD CONSTRAINT expert_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: experttestimony experttestimony_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony
    ADD CONSTRAINT experttestimony_pkey PRIMARY KEY (investigation_entries, experts);


--
-- Name: experttestimony_version experttestimony_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony_version
    ADD CONSTRAINT experttestimony_version_pkey PRIMARY KEY (investigation_entries, experts, transaction_id);


--
-- Name: experttype experttype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttype
    ADD CONSTRAINT experttype_pkey PRIMARY KEY (id);


--
-- Name: experttype_version experttype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttype_version
    ADD CONSTRAINT experttype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: feeclass feeclass_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feeclass
    ADD CONSTRAINT feeclass_pkey PRIMARY KEY (id);


--
-- Name: feeclass_version feeclass_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feeclass_version
    ADD CONSTRAINT feeclass_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: feetype feetype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feetype
    ADD CONSTRAINT feetype_pkey PRIMARY KEY (id);


--
-- Name: feetype_version feetype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feetype_version
    ADD CONSTRAINT feetype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: healthevent healthevent_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent
    ADD CONSTRAINT healthevent_pkey PRIMARY KEY (id);


--
-- Name: healthevent_version healthevent_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent_version
    ADD CONSTRAINT healthevent_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: healtheventtype healtheventtype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healtheventtype
    ADD CONSTRAINT healtheventtype_pkey PRIMARY KEY (id);


--
-- Name: healtheventtype_version healtheventtype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healtheventtype_version
    ADD CONSTRAINT healtheventtype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: hearing_issue hearing_issue_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_issue
    ADD CONSTRAINT hearing_issue_pkey PRIMARY KEY (hearing, issue);


--
-- Name: hearing_issue_version hearing_issue_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_issue_version
    ADD CONSTRAINT hearing_issue_version_pkey PRIMARY KEY (hearing, issue, transaction_id);


--
-- Name: hearing_judicialofficer hearing_judicialofficer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_judicialofficer
    ADD CONSTRAINT hearing_judicialofficer_pkey PRIMARY KEY (hearing, judicialofficer);


--
-- Name: hearing_judicialofficer_version hearing_judicialofficer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_judicialofficer_version
    ADD CONSTRAINT hearing_judicialofficer_version_pkey PRIMARY KEY (hearing, judicialofficer, transaction_id);


--
-- Name: hearing_lawfirm_2 hearing_lawfirm_2_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm_2
    ADD CONSTRAINT hearing_lawfirm_2_pkey PRIMARY KEY (hearing, lawfirm);


--
-- Name: hearing_lawfirm_2_version hearing_lawfirm_2_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm_2_version
    ADD CONSTRAINT hearing_lawfirm_2_version_pkey PRIMARY KEY (hearing, lawfirm, transaction_id);


--
-- Name: hearing_lawfirm hearing_lawfirm_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm
    ADD CONSTRAINT hearing_lawfirm_pkey PRIMARY KEY (hearing, lawfirm);


--
-- Name: hearing_lawfirm_version hearing_lawfirm_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm_version
    ADD CONSTRAINT hearing_lawfirm_version_pkey PRIMARY KEY (hearing, lawfirm, transaction_id);


--
-- Name: hearing hearing_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing
    ADD CONSTRAINT hearing_pkey PRIMARY KEY (id);


--
-- Name: hearing_version hearing_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_version
    ADD CONSTRAINT hearing_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: hearingtype hearingtype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearingtype
    ADD CONSTRAINT hearingtype_pkey PRIMARY KEY (id);


--
-- Name: hearingtype_version hearingtype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearingtype_version
    ADD CONSTRAINT hearingtype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: instancecrime_issue instancecrime_issue_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime_issue
    ADD CONSTRAINT instancecrime_issue_pkey PRIMARY KEY (instancecrime, issue);


--
-- Name: instancecrime_issue_version instancecrime_issue_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime_issue_version
    ADD CONSTRAINT instancecrime_issue_version_pkey PRIMARY KEY (instancecrime, issue, transaction_id);


--
-- Name: instancecrime instancecrime_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime
    ADD CONSTRAINT instancecrime_pkey PRIMARY KEY (id);


--
-- Name: instancecrime_version instancecrime_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime_version
    ADD CONSTRAINT instancecrime_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: interview interview_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY interview
    ADD CONSTRAINT interview_pkey PRIMARY KEY (id);


--
-- Name: interview_version interview_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY interview_version
    ADD CONSTRAINT interview_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: investigationdiary_party investigationdiary_party_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_party
    ADD CONSTRAINT investigationdiary_party_pkey PRIMARY KEY (investigationdiary, party);


--
-- Name: investigationdiary_party_version investigationdiary_party_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_party_version
    ADD CONSTRAINT investigationdiary_party_version_pkey PRIMARY KEY (investigationdiary, party, transaction_id);


--
-- Name: investigationdiary investigationdiary_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary
    ADD CONSTRAINT investigationdiary_pkey PRIMARY KEY (id);


--
-- Name: investigationdiary_policeofficer investigationdiary_policeofficer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_policeofficer
    ADD CONSTRAINT investigationdiary_policeofficer_pkey PRIMARY KEY (investigationdiary, policeofficer);


--
-- Name: investigationdiary_policeofficer_version investigationdiary_policeofficer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_policeofficer_version
    ADD CONSTRAINT investigationdiary_policeofficer_version_pkey PRIMARY KEY (investigationdiary, policeofficer, transaction_id);


--
-- Name: investigationdiary_vehicle investigationdiary_vehicle_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_vehicle
    ADD CONSTRAINT investigationdiary_vehicle_pkey PRIMARY KEY (investigationdiary, vehicle);


--
-- Name: investigationdiary_vehicle_version investigationdiary_vehicle_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_vehicle_version
    ADD CONSTRAINT investigationdiary_vehicle_version_pkey PRIMARY KEY (investigationdiary, vehicle, transaction_id);


--
-- Name: investigationdiary_version investigationdiary_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_version
    ADD CONSTRAINT investigationdiary_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: issue_lawyer issue_lawyer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_lawyer
    ADD CONSTRAINT issue_lawyer_pkey PRIMARY KEY (issue, lawyer);


--
-- Name: issue_lawyer_version issue_lawyer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_lawyer_version
    ADD CONSTRAINT issue_lawyer_version_pkey PRIMARY KEY (issue, lawyer, transaction_id);


--
-- Name: issue_legalreference_2 issue_legalreference_2_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference_2
    ADD CONSTRAINT issue_legalreference_2_pkey PRIMARY KEY (issue, legalreference);


--
-- Name: issue_legalreference_2_version issue_legalreference_2_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference_2_version
    ADD CONSTRAINT issue_legalreference_2_version_pkey PRIMARY KEY (issue, legalreference, transaction_id);


--
-- Name: issue_legalreference issue_legalreference_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference
    ADD CONSTRAINT issue_legalreference_pkey PRIMARY KEY (issue, legalreference);


--
-- Name: issue_legalreference_version issue_legalreference_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference_version
    ADD CONSTRAINT issue_legalreference_version_pkey PRIMARY KEY (issue, legalreference, transaction_id);


--
-- Name: issue_party_2 issue_party_2_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party_2
    ADD CONSTRAINT issue_party_2_pkey PRIMARY KEY (issue, party);


--
-- Name: issue_party_2_version issue_party_2_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party_2_version
    ADD CONSTRAINT issue_party_2_version_pkey PRIMARY KEY (issue, party, transaction_id);


--
-- Name: issue_party issue_party_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party
    ADD CONSTRAINT issue_party_pkey PRIMARY KEY (issue, party);


--
-- Name: issue_party_version issue_party_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party_version
    ADD CONSTRAINT issue_party_version_pkey PRIMARY KEY (issue, party, transaction_id);


--
-- Name: issue issue_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue
    ADD CONSTRAINT issue_pkey PRIMARY KEY (id);


--
-- Name: issue_version issue_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_version
    ADD CONSTRAINT issue_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: judicialofficer judicialofficer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer
    ADD CONSTRAINT judicialofficer_pkey PRIMARY KEY (id);


--
-- Name: judicialofficer_version judicialofficer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer_version
    ADD CONSTRAINT judicialofficer_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: judicialrank judicialrank_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrank
    ADD CONSTRAINT judicialrank_pkey PRIMARY KEY (id);


--
-- Name: judicialrank_version judicialrank_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrank_version
    ADD CONSTRAINT judicialrank_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: judicialrole judicialrole_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrole
    ADD CONSTRAINT judicialrole_pkey PRIMARY KEY (id);


--
-- Name: judicialrole_version judicialrole_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrole_version
    ADD CONSTRAINT judicialrole_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: law law_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY law
    ADD CONSTRAINT law_pkey PRIMARY KEY (id);


--
-- Name: law_version law_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY law_version
    ADD CONSTRAINT law_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: lawfirm lawfirm_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawfirm
    ADD CONSTRAINT lawfirm_pkey PRIMARY KEY (id);


--
-- Name: lawfirm_version lawfirm_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawfirm_version
    ADD CONSTRAINT lawfirm_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: lawyer_party lawyer_party_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer_party
    ADD CONSTRAINT lawyer_party_pkey PRIMARY KEY (lawyer, party);


--
-- Name: lawyer_party_version lawyer_party_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer_party_version
    ADD CONSTRAINT lawyer_party_version_pkey PRIMARY KEY (lawyer, party, transaction_id);


--
-- Name: lawyer lawyer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer
    ADD CONSTRAINT lawyer_pkey PRIMARY KEY (id);


--
-- Name: lawyer_version lawyer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer_version
    ADD CONSTRAINT lawyer_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: legalreference legalreference_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY legalreference
    ADD CONSTRAINT legalreference_pkey PRIMARY KEY (id);


--
-- Name: legalreference_version legalreference_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY legalreference_version
    ADD CONSTRAINT legalreference_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: nextofkin nextofkin_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY nextofkin
    ADD CONSTRAINT nextofkin_pkey PRIMARY KEY (id);


--
-- Name: nextofkin_version nextofkin_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY nextofkin_version
    ADD CONSTRAINT nextofkin_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: notification notification_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notification
    ADD CONSTRAINT notification_pkey PRIMARY KEY (id);


--
-- Name: notification_version notification_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notification_version
    ADD CONSTRAINT notification_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: notificationregister notificationregister_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_pkey PRIMARY KEY (id);


--
-- Name: notificationregister_version notificationregister_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister_version
    ADD CONSTRAINT notificationregister_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: notificationtype notificationtype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationtype
    ADD CONSTRAINT notificationtype_pkey PRIMARY KEY (id);


--
-- Name: notificationtype_version notificationtype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationtype_version
    ADD CONSTRAINT notificationtype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: notifyevent notifyevent_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notifyevent
    ADD CONSTRAINT notifyevent_pkey PRIMARY KEY (id);


--
-- Name: notifyevent_version notifyevent_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notifyevent_version
    ADD CONSTRAINT notifyevent_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: page page_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY page
    ADD CONSTRAINT page_pkey PRIMARY KEY (id);


--
-- Name: page_version page_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY page_version
    ADD CONSTRAINT page_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: party party_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party
    ADD CONSTRAINT party_pkey PRIMARY KEY (id);


--
-- Name: party_settlement party_settlement_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party_settlement
    ADD CONSTRAINT party_settlement_pkey PRIMARY KEY (party, settlement);


--
-- Name: party_settlement_version party_settlement_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party_settlement_version
    ADD CONSTRAINT party_settlement_version_pkey PRIMARY KEY (party, settlement, transaction_id);


--
-- Name: party_version party_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party_version
    ADD CONSTRAINT party_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: partytype partytype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY partytype
    ADD CONSTRAINT partytype_pkey PRIMARY KEY (id);


--
-- Name: partytype_version partytype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY partytype_version
    ADD CONSTRAINT partytype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: payment payment_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (id);


--
-- Name: payment_version payment_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY payment_version
    ADD CONSTRAINT payment_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: personaleffect personaleffect_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffect
    ADD CONSTRAINT personaleffect_pkey PRIMARY KEY (id);


--
-- Name: personaleffect_version personaleffect_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffect_version
    ADD CONSTRAINT personaleffect_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: personaleffectscategory personaleffectscategory_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffectscategory
    ADD CONSTRAINT personaleffectscategory_pkey PRIMARY KEY (id);


--
-- Name: personaleffectscategory_version personaleffectscategory_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffectscategory_version
    ADD CONSTRAINT personaleffectscategory_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: policeofficer policeofficer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer
    ADD CONSTRAINT policeofficer_pkey PRIMARY KEY (id);


--
-- Name: policeofficer_policestation policeofficer_policestation_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer_policestation
    ADD CONSTRAINT policeofficer_policestation_pkey PRIMARY KEY (policeofficer, policestation);


--
-- Name: policeofficer_policestation_version policeofficer_policestation_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer_policestation_version
    ADD CONSTRAINT policeofficer_policestation_version_pkey PRIMARY KEY (policeofficer, policestation, transaction_id);


--
-- Name: policeofficer policeofficer_servicenumber_key; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer
    ADD CONSTRAINT policeofficer_servicenumber_key UNIQUE (servicenumber);


--
-- Name: policeofficer_version policeofficer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer_version
    ADD CONSTRAINT policeofficer_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: policeofficerrank policeofficerrank_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficerrank
    ADD CONSTRAINT policeofficerrank_pkey PRIMARY KEY (id);


--
-- Name: policeofficerrank_version policeofficerrank_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficerrank_version
    ADD CONSTRAINT policeofficerrank_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: policestation policestation_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation
    ADD CONSTRAINT policestation_pkey PRIMARY KEY (id);


--
-- Name: policestation_version policestation_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation_version
    ADD CONSTRAINT policestation_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: policestationrank policestationrank_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestationrank
    ADD CONSTRAINT policestationrank_pkey PRIMARY KEY (id);


--
-- Name: policestationrank_version policestationrank_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestationrank_version
    ADD CONSTRAINT policestationrank_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: prison prison_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prison
    ADD CONSTRAINT prison_pkey PRIMARY KEY (id);


--
-- Name: prison_version prison_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prison_version
    ADD CONSTRAINT prison_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: prisonofficer prisonofficer_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficer
    ADD CONSTRAINT prisonofficer_pkey PRIMARY KEY (id);


--
-- Name: prisonofficer_version prisonofficer_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficer_version
    ADD CONSTRAINT prisonofficer_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: prisonofficerrank prisonofficerrank_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficerrank
    ADD CONSTRAINT prisonofficerrank_pkey PRIMARY KEY (id);


--
-- Name: prisonofficerrank_version prisonofficerrank_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficerrank_version
    ADD CONSTRAINT prisonofficerrank_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: prosecutor prosecutor_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutor
    ADD CONSTRAINT prosecutor_pkey PRIMARY KEY (id);


--
-- Name: prosecutor_version prosecutor_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutor_version
    ADD CONSTRAINT prosecutor_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: prosecutorteam prosecutorteam_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutorteam
    ADD CONSTRAINT prosecutorteam_pkey PRIMARY KEY (id);


--
-- Name: prosecutorteam_version prosecutorteam_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutorteam_version
    ADD CONSTRAINT prosecutorteam_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: releasetype releasetype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY releasetype
    ADD CONSTRAINT releasetype_pkey PRIMARY KEY (id);


--
-- Name: releasetype_version releasetype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY releasetype_version
    ADD CONSTRAINT releasetype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: religion religion_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY religion
    ADD CONSTRAINT religion_pkey PRIMARY KEY (id);


--
-- Name: religion_version religion_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY religion_version
    ADD CONSTRAINT religion_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: schedulestatustype schedulestatustype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY schedulestatustype
    ADD CONSTRAINT schedulestatustype_pkey PRIMARY KEY (id);


--
-- Name: schedulestatustype_version schedulestatustype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY schedulestatustype_version
    ADD CONSTRAINT schedulestatustype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: seizure seizure_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY seizure
    ADD CONSTRAINT seizure_pkey PRIMARY KEY (id);


--
-- Name: seizure_version seizure_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY seizure_version
    ADD CONSTRAINT seizure_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: settlement settlement_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY settlement
    ADD CONSTRAINT settlement_pkey PRIMARY KEY (id);


--
-- Name: settlement_version settlement_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY settlement_version
    ADD CONSTRAINT settlement_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: subcounty subcounty_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY subcounty
    ADD CONSTRAINT subcounty_pkey PRIMARY KEY (id);


--
-- Name: subcounty_version subcounty_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY subcounty_version
    ADD CONSTRAINT subcounty_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: templatetype templatetype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY templatetype
    ADD CONSTRAINT templatetype_pkey PRIMARY KEY (id);


--
-- Name: templatetype_version templatetype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY templatetype_version
    ADD CONSTRAINT templatetype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: town town_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town
    ADD CONSTRAINT town_pkey PRIMARY KEY (id);


--
-- Name: town_version town_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town_version
    ADD CONSTRAINT town_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: town_ward town_ward_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town_ward
    ADD CONSTRAINT town_ward_pkey PRIMARY KEY (town, ward);


--
-- Name: town_ward_version town_ward_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town_ward_version
    ADD CONSTRAINT town_ward_version_pkey PRIMARY KEY (town, ward, transaction_id);


--
-- Name: transaction transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transaction
    ADD CONSTRAINT transaction_pkey PRIMARY KEY (id);


--
-- Name: transcript transcript_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transcript
    ADD CONSTRAINT transcript_pkey PRIMARY KEY (id);


--
-- Name: transcript_version transcript_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transcript_version
    ADD CONSTRAINT transcript_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: vehicle vehicle_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY vehicle
    ADD CONSTRAINT vehicle_pkey PRIMARY KEY (id);


--
-- Name: vehicle_version vehicle_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY vehicle_version
    ADD CONSTRAINT vehicle_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: ward ward_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ward
    ADD CONSTRAINT ward_pkey PRIMARY KEY (id);


--
-- Name: ward_version ward_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ward_version
    ADD CONSTRAINT ward_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: warranttype warranttype_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY warranttype
    ADD CONSTRAINT warranttype_pkey PRIMARY KEY (id);


--
-- Name: warranttype_version warranttype_version_pkey; Type: CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY warranttype_version
    ADD CONSTRAINT warranttype_version_pkey PRIMARY KEY (id, transaction_id);


--
-- Name: idx_bill__court_account_courts_court_account_account__types; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX idx_bill__court_account_courts_court_account_account__types ON bill USING btree (court_account_courts, court_account_account__types);


--
-- Name: ix_accounttype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_accounttype_name ON accounttype USING btree (name);


--
-- Name: ix_accounttype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_accounttype_version_end_transaction_id ON accounttype_version USING btree (end_transaction_id);


--
-- Name: ix_accounttype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_accounttype_version_name ON accounttype_version USING btree (name);


--
-- Name: ix_accounttype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_accounttype_version_operation_type ON accounttype_version USING btree (operation_type);


--
-- Name: ix_accounttype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_accounttype_version_transaction_id ON accounttype_version USING btree (transaction_id);


--
-- Name: ix_bill_assessing_registrar; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_assessing_registrar ON bill USING btree (assessing_registrar);


--
-- Name: ix_bill_court; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_court ON bill USING btree (court);


--
-- Name: ix_bill_documents; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_documents ON bill USING btree (documents);


--
-- Name: ix_bill_lawyer_paying; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_lawyer_paying ON bill USING btree (lawyer_paying);


--
-- Name: ix_bill_party_paying; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_party_paying ON bill USING btree (party_paying);


--
-- Name: ix_bill_receiving_registrar; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_receiving_registrar ON bill USING btree (receiving_registrar);


--
-- Name: ix_bill_version_assessing_registrar; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_assessing_registrar ON bill_version USING btree (assessing_registrar);


--
-- Name: ix_bill_version_court; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_court ON bill_version USING btree (court);


--
-- Name: ix_bill_version_documents; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_documents ON bill_version USING btree (documents);


--
-- Name: ix_bill_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_end_transaction_id ON bill_version USING btree (end_transaction_id);


--
-- Name: ix_bill_version_lawyer_paying; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_lawyer_paying ON bill_version USING btree (lawyer_paying);


--
-- Name: ix_bill_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_operation_type ON bill_version USING btree (operation_type);


--
-- Name: ix_bill_version_party_paying; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_party_paying ON bill_version USING btree (party_paying);


--
-- Name: ix_bill_version_receiving_registrar; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_receiving_registrar ON bill_version USING btree (receiving_registrar);


--
-- Name: ix_bill_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_bill_version_transaction_id ON bill_version USING btree (transaction_id);


--
-- Name: ix_billdetail_feetype; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_billdetail_feetype ON billdetail USING btree (feetype);


--
-- Name: ix_billdetail_receipt_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_billdetail_receipt_id ON billdetail USING btree (receipt_id);


--
-- Name: ix_billdetail_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_billdetail_version_end_transaction_id ON billdetail_version USING btree (end_transaction_id);


--
-- Name: ix_billdetail_version_feetype; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_billdetail_version_feetype ON billdetail_version USING btree (feetype);


--
-- Name: ix_billdetail_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_billdetail_version_operation_type ON billdetail_version USING btree (operation_type);


--
-- Name: ix_billdetail_version_receipt_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_billdetail_version_receipt_id ON billdetail_version USING btree (receipt_id);


--
-- Name: ix_billdetail_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_billdetail_version_transaction_id ON billdetail_version USING btree (transaction_id);


--
-- Name: ix_biodata_bc_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_bc_id ON biodata USING btree (bc_id);


--
-- Name: ix_biodata_bc_number; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_bc_number ON biodata USING btree (bc_number);


--
-- Name: ix_biodata_bc_place; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_bc_place ON biodata USING btree (bc_place);


--
-- Name: ix_biodata_bc_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_bc_serial ON biodata USING btree (bc_serial);


--
-- Name: ix_biodata_economic_class; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_economic_class ON biodata USING btree (economic_class);


--
-- Name: ix_biodata_f_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_f_nat_id_num ON biodata USING btree (f_nat_id_num);


--
-- Name: ix_biodata_f_prn; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_f_prn ON biodata USING btree (f_prn);


--
-- Name: ix_biodata_m_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_m_nat_id_num ON biodata USING btree (m_nat_id_num);


--
-- Name: ix_biodata_m_prn; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_m_prn ON biodata USING btree (m_prn);


--
-- Name: ix_biodata_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_nat_id_num ON biodata USING btree (nat_id_num);


--
-- Name: ix_biodata_nat_id_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_nat_id_serial ON biodata USING btree (nat_id_serial);


--
-- Name: ix_biodata_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_party ON biodata USING btree (party);


--
-- Name: ix_biodata_pp_no; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_pp_no ON biodata USING btree (pp_no);


--
-- Name: ix_biodata_religion; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_religion ON biodata USING btree (religion);


--
-- Name: ix_biodata_version_bc_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_bc_id ON biodata_version USING btree (bc_id);


--
-- Name: ix_biodata_version_bc_number; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_bc_number ON biodata_version USING btree (bc_number);


--
-- Name: ix_biodata_version_bc_place; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_bc_place ON biodata_version USING btree (bc_place);


--
-- Name: ix_biodata_version_bc_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_bc_serial ON biodata_version USING btree (bc_serial);


--
-- Name: ix_biodata_version_economic_class; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_economic_class ON biodata_version USING btree (economic_class);


--
-- Name: ix_biodata_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_end_transaction_id ON biodata_version USING btree (end_transaction_id);


--
-- Name: ix_biodata_version_f_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_f_nat_id_num ON biodata_version USING btree (f_nat_id_num);


--
-- Name: ix_biodata_version_f_prn; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_f_prn ON biodata_version USING btree (f_prn);


--
-- Name: ix_biodata_version_m_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_m_nat_id_num ON biodata_version USING btree (m_nat_id_num);


--
-- Name: ix_biodata_version_m_prn; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_m_prn ON biodata_version USING btree (m_prn);


--
-- Name: ix_biodata_version_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_nat_id_num ON biodata_version USING btree (nat_id_num);


--
-- Name: ix_biodata_version_nat_id_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_nat_id_serial ON biodata_version USING btree (nat_id_serial);


--
-- Name: ix_biodata_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_operation_type ON biodata_version USING btree (operation_type);


--
-- Name: ix_biodata_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_party ON biodata_version USING btree (party);


--
-- Name: ix_biodata_version_pp_no; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_pp_no ON biodata_version USING btree (pp_no);


--
-- Name: ix_biodata_version_religion; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_religion ON biodata_version USING btree (religion);


--
-- Name: ix_biodata_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_biodata_version_transaction_id ON biodata_version USING btree (transaction_id);


--
-- Name: ix_casecategory_courtcase_courtcase; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_courtcase_courtcase ON casecategory_courtcase USING btree (courtcase);


--
-- Name: ix_casecategory_courtcase_version_courtcase; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_courtcase_version_courtcase ON casecategory_courtcase_version USING btree (courtcase);


--
-- Name: ix_casecategory_courtcase_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_courtcase_version_end_transaction_id ON casecategory_courtcase_version USING btree (end_transaction_id);


--
-- Name: ix_casecategory_courtcase_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_courtcase_version_operation_type ON casecategory_courtcase_version USING btree (operation_type);


--
-- Name: ix_casecategory_courtcase_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_courtcase_version_transaction_id ON casecategory_courtcase_version USING btree (transaction_id);


--
-- Name: ix_casecategory_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_casecategory_name ON casecategory USING btree (name);


--
-- Name: ix_casecategory_subcategory; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_subcategory ON casecategory USING btree (subcategory);


--
-- Name: ix_casecategory_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_version_end_transaction_id ON casecategory_version USING btree (end_transaction_id);


--
-- Name: ix_casecategory_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_version_name ON casecategory_version USING btree (name);


--
-- Name: ix_casecategory_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_version_operation_type ON casecategory_version USING btree (operation_type);


--
-- Name: ix_casecategory_version_subcategory; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_version_subcategory ON casecategory_version USING btree (subcategory);


--
-- Name: ix_casecategory_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategory_version_transaction_id ON casecategory_version USING btree (transaction_id);


--
-- Name: ix_casecategorychecklist_case_categories; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategorychecklist_case_categories ON casecategorychecklist USING btree (case_categories);


--
-- Name: ix_casecategorychecklist_version_case_categories; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategorychecklist_version_case_categories ON casecategorychecklist_version USING btree (case_categories);


--
-- Name: ix_casecategorychecklist_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategorychecklist_version_end_transaction_id ON casecategorychecklist_version USING btree (end_transaction_id);


--
-- Name: ix_casecategorychecklist_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategorychecklist_version_operation_type ON casecategorychecklist_version USING btree (operation_type);


--
-- Name: ix_casecategorychecklist_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casecategorychecklist_version_transaction_id ON casecategorychecklist_version USING btree (transaction_id);


--
-- Name: ix_casechecklist_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casechecklist_version_end_transaction_id ON casechecklist_version USING btree (end_transaction_id);


--
-- Name: ix_casechecklist_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casechecklist_version_operation_type ON casechecklist_version USING btree (operation_type);


--
-- Name: ix_casechecklist_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_casechecklist_version_transaction_id ON casechecklist_version USING btree (transaction_id);


--
-- Name: ix_caselinktype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_caselinktype_name ON caselinktype USING btree (name);


--
-- Name: ix_caselinktype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_caselinktype_version_end_transaction_id ON caselinktype_version USING btree (end_transaction_id);


--
-- Name: ix_caselinktype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_caselinktype_version_name ON caselinktype_version USING btree (name);


--
-- Name: ix_caselinktype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_caselinktype_version_operation_type ON caselinktype_version USING btree (operation_type);


--
-- Name: ix_caselinktype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_caselinktype_version_transaction_id ON caselinktype_version USING btree (transaction_id);


--
-- Name: ix_celltype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_celltype_name ON celltype USING btree (name);


--
-- Name: ix_celltype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_celltype_version_end_transaction_id ON celltype_version USING btree (end_transaction_id);


--
-- Name: ix_celltype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_celltype_version_name ON celltype_version USING btree (name);


--
-- Name: ix_celltype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_celltype_version_operation_type ON celltype_version USING btree (operation_type);


--
-- Name: ix_celltype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_celltype_version_transaction_id ON celltype_version USING btree (transaction_id);


--
-- Name: ix_commital_cell_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_cell_type ON commital USING btree (cell_type);


--
-- Name: ix_commital_commital; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_commital ON commital USING btree (commital);


--
-- Name: ix_commital_commital_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_commital_type ON commital USING btree (commital_type);


--
-- Name: ix_commital_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_court_case ON commital USING btree (court_case);


--
-- Name: ix_commital_parties; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_parties ON commital USING btree (parties);


--
-- Name: ix_commital_police_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_police_station ON commital USING btree (police_station);


--
-- Name: ix_commital_prisons; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_prisons ON commital USING btree (prisons);


--
-- Name: ix_commital_receiving_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_receiving_officer ON commital USING btree (receiving_officer);


--
-- Name: ix_commital_release_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_release_type ON commital USING btree (release_type);


--
-- Name: ix_commital_releasing_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_releasing_officer ON commital USING btree (releasing_officer);


--
-- Name: ix_commital_version_cell_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_cell_type ON commital_version USING btree (cell_type);


--
-- Name: ix_commital_version_commital; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_commital ON commital_version USING btree (commital);


--
-- Name: ix_commital_version_commital_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_commital_type ON commital_version USING btree (commital_type);


--
-- Name: ix_commital_version_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_court_case ON commital_version USING btree (court_case);


--
-- Name: ix_commital_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_end_transaction_id ON commital_version USING btree (end_transaction_id);


--
-- Name: ix_commital_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_operation_type ON commital_version USING btree (operation_type);


--
-- Name: ix_commital_version_parties; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_parties ON commital_version USING btree (parties);


--
-- Name: ix_commital_version_police_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_police_station ON commital_version USING btree (police_station);


--
-- Name: ix_commital_version_prisons; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_prisons ON commital_version USING btree (prisons);


--
-- Name: ix_commital_version_receiving_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_receiving_officer ON commital_version USING btree (receiving_officer);


--
-- Name: ix_commital_version_release_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_release_type ON commital_version USING btree (release_type);


--
-- Name: ix_commital_version_releasing_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_releasing_officer ON commital_version USING btree (releasing_officer);


--
-- Name: ix_commital_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_transaction_id ON commital_version USING btree (transaction_id);


--
-- Name: ix_commital_version_warrant_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_version_warrant_type ON commital_version USING btree (warrant_type);


--
-- Name: ix_commital_warrant_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commital_warrant_type ON commital USING btree (warrant_type);


--
-- Name: ix_commitaltype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_commitaltype_name ON commitaltype USING btree (name);


--
-- Name: ix_commitaltype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commitaltype_version_end_transaction_id ON commitaltype_version USING btree (end_transaction_id);


--
-- Name: ix_commitaltype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commitaltype_version_name ON commitaltype_version USING btree (name);


--
-- Name: ix_commitaltype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commitaltype_version_operation_type ON commitaltype_version USING btree (operation_type);


--
-- Name: ix_commitaltype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_commitaltype_version_transaction_id ON commitaltype_version USING btree (transaction_id);


--
-- Name: ix_complaint_complaintcategory_complaintcategory; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_complaintcategory_complaintcategory ON complaint_complaintcategory USING btree (complaintcategory);


--
-- Name: ix_complaint_complaintcategory_version_complaintcategory; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_complaintcategory_version_complaintcategory ON complaint_complaintcategory_version USING btree (complaintcategory);


--
-- Name: ix_complaint_complaintcategory_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_complaintcategory_version_end_transaction_id ON complaint_complaintcategory_version USING btree (end_transaction_id);


--
-- Name: ix_complaint_complaintcategory_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_complaintcategory_version_operation_type ON complaint_complaintcategory_version USING btree (operation_type);


--
-- Name: ix_complaint_complaintcategory_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_complaintcategory_version_transaction_id ON complaint_complaintcategory_version USING btree (transaction_id);


--
-- Name: ix_complaint_courtcase_courtcase; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_courtcase_courtcase ON complaint_courtcase USING btree (courtcase);


--
-- Name: ix_complaint_courtcase_version_courtcase; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_courtcase_version_courtcase ON complaint_courtcase_version USING btree (courtcase);


--
-- Name: ix_complaint_courtcase_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_courtcase_version_end_transaction_id ON complaint_courtcase_version USING btree (end_transaction_id);


--
-- Name: ix_complaint_courtcase_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_courtcase_version_operation_type ON complaint_courtcase_version USING btree (operation_type);


--
-- Name: ix_complaint_courtcase_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_courtcase_version_transaction_id ON complaint_courtcase_version USING btree (transaction_id);


--
-- Name: ix_complaint_evaluating_prosecutor_team; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_evaluating_prosecutor_team ON complaint USING btree (evaluating_prosecutor_team);


--
-- Name: ix_complaint_police_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_police_station ON complaint USING btree (police_station);


--
-- Name: ix_complaint_reported_to_judicial_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_reported_to_judicial_officer ON complaint USING btree (reported_to_judicial_officer);


--
-- Name: ix_complaint_reportingofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_reportingofficer ON complaint USING btree (reportingofficer);


--
-- Name: ix_complaint_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_version_end_transaction_id ON complaint_version USING btree (end_transaction_id);


--
-- Name: ix_complaint_version_evaluating_prosecutor_team; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_version_evaluating_prosecutor_team ON complaint_version USING btree (evaluating_prosecutor_team);


--
-- Name: ix_complaint_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_version_operation_type ON complaint_version USING btree (operation_type);


--
-- Name: ix_complaint_version_police_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_version_police_station ON complaint_version USING btree (police_station);


--
-- Name: ix_complaint_version_reported_to_judicial_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_version_reported_to_judicial_officer ON complaint_version USING btree (reported_to_judicial_officer);


--
-- Name: ix_complaint_version_reportingofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_version_reportingofficer ON complaint_version USING btree (reportingofficer);


--
-- Name: ix_complaint_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaint_version_transaction_id ON complaint_version USING btree (transaction_id);


--
-- Name: ix_complaintcategory_complaint_category_parent; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintcategory_complaint_category_parent ON complaintcategory USING btree (complaint_category_parent);


--
-- Name: ix_complaintcategory_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_complaintcategory_name ON complaintcategory USING btree (name);


--
-- Name: ix_complaintcategory_version_complaint_category_parent; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintcategory_version_complaint_category_parent ON complaintcategory_version USING btree (complaint_category_parent);


--
-- Name: ix_complaintcategory_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintcategory_version_end_transaction_id ON complaintcategory_version USING btree (end_transaction_id);


--
-- Name: ix_complaintcategory_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintcategory_version_name ON complaintcategory_version USING btree (name);


--
-- Name: ix_complaintcategory_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintcategory_version_operation_type ON complaintcategory_version USING btree (operation_type);


--
-- Name: ix_complaintcategory_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintcategory_version_transaction_id ON complaintcategory_version USING btree (transaction_id);


--
-- Name: ix_complaintrole_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_complaintrole_name ON complaintrole USING btree (name);


--
-- Name: ix_complaintrole_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintrole_version_end_transaction_id ON complaintrole_version USING btree (end_transaction_id);


--
-- Name: ix_complaintrole_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintrole_version_name ON complaintrole_version USING btree (name);


--
-- Name: ix_complaintrole_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintrole_version_operation_type ON complaintrole_version USING btree (operation_type);


--
-- Name: ix_complaintrole_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_complaintrole_version_transaction_id ON complaintrole_version USING btree (transaction_id);


--
-- Name: ix_country_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_country_version_end_transaction_id ON country_version USING btree (end_transaction_id);


--
-- Name: ix_country_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_country_version_operation_type ON country_version USING btree (operation_type);


--
-- Name: ix_country_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_country_version_transaction_id ON country_version USING btree (transaction_id);


--
-- Name: ix_county_country; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_county_country ON county USING btree (country);


--
-- Name: ix_county_version_country; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_county_version_country ON county_version USING btree (country);


--
-- Name: ix_county_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_county_version_end_transaction_id ON county_version USING btree (end_transaction_id);


--
-- Name: ix_county_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_county_version_operation_type ON county_version USING btree (operation_type);


--
-- Name: ix_county_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_county_version_transaction_id ON county_version USING btree (transaction_id);


--
-- Name: ix_court_court_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_court_rank ON court USING btree (court_rank);


--
-- Name: ix_court_court_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_court_station ON court USING btree (court_station);


--
-- Name: ix_court_judicialofficer_judicialofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_judicialofficer_judicialofficer ON court_judicialofficer USING btree (judicialofficer);


--
-- Name: ix_court_judicialofficer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_judicialofficer_version_end_transaction_id ON court_judicialofficer_version USING btree (end_transaction_id);


--
-- Name: ix_court_judicialofficer_version_judicialofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_judicialofficer_version_judicialofficer ON court_judicialofficer_version USING btree (judicialofficer);


--
-- Name: ix_court_judicialofficer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_judicialofficer_version_operation_type ON court_judicialofficer_version USING btree (operation_type);


--
-- Name: ix_court_judicialofficer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_judicialofficer_version_transaction_id ON court_judicialofficer_version USING btree (transaction_id);


--
-- Name: ix_court_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_town ON court USING btree (town);


--
-- Name: ix_court_version_court_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_version_court_rank ON court_version USING btree (court_rank);


--
-- Name: ix_court_version_court_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_version_court_station ON court_version USING btree (court_station);


--
-- Name: ix_court_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_version_end_transaction_id ON court_version USING btree (end_transaction_id);


--
-- Name: ix_court_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_version_operation_type ON court_version USING btree (operation_type);


--
-- Name: ix_court_version_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_version_town ON court_version USING btree (town);


--
-- Name: ix_court_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_court_version_transaction_id ON court_version USING btree (transaction_id);


--
-- Name: ix_courtaccount_account__types; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtaccount_account__types ON courtaccount USING btree (account__types);


--
-- Name: ix_courtaccount_version_account__types; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtaccount_version_account__types ON courtaccount_version USING btree (account__types);


--
-- Name: ix_courtaccount_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtaccount_version_end_transaction_id ON courtaccount_version USING btree (end_transaction_id);


--
-- Name: ix_courtaccount_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtaccount_version_operation_type ON courtaccount_version USING btree (operation_type);


--
-- Name: ix_courtaccount_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtaccount_version_transaction_id ON courtaccount_version USING btree (transaction_id);


--
-- Name: ix_courtcase_case_link_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_case_link_type ON courtcase USING btree (case_link_type);


--
-- Name: ix_courtcase_filing_prosecutor; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_filing_prosecutor ON courtcase USING btree (filing_prosecutor);


--
-- Name: ix_courtcase_judicialofficer_judicialofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_judicialofficer_judicialofficer ON courtcase_judicialofficer USING btree (judicialofficer);


--
-- Name: ix_courtcase_judicialofficer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_judicialofficer_version_end_transaction_id ON courtcase_judicialofficer_version USING btree (end_transaction_id);


--
-- Name: ix_courtcase_judicialofficer_version_judicialofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_judicialofficer_version_judicialofficer ON courtcase_judicialofficer_version USING btree (judicialofficer);


--
-- Name: ix_courtcase_judicialofficer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_judicialofficer_version_operation_type ON courtcase_judicialofficer_version USING btree (operation_type);


--
-- Name: ix_courtcase_judicialofficer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_judicialofficer_version_transaction_id ON courtcase_judicialofficer_version USING btree (transaction_id);


--
-- Name: ix_courtcase_lawfirm_lawfirm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_lawfirm_lawfirm ON courtcase_lawfirm USING btree (lawfirm);


--
-- Name: ix_courtcase_lawfirm_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_lawfirm_version_end_transaction_id ON courtcase_lawfirm_version USING btree (end_transaction_id);


--
-- Name: ix_courtcase_lawfirm_version_lawfirm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_lawfirm_version_lawfirm ON courtcase_lawfirm_version USING btree (lawfirm);


--
-- Name: ix_courtcase_lawfirm_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_lawfirm_version_operation_type ON courtcase_lawfirm_version USING btree (operation_type);


--
-- Name: ix_courtcase_lawfirm_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_lawfirm_version_transaction_id ON courtcase_lawfirm_version USING btree (transaction_id);


--
-- Name: ix_courtcase_linked_cases; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_linked_cases ON courtcase USING btree (linked_cases);


--
-- Name: ix_courtcase_pretrial_registrar; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_pretrial_registrar ON courtcase USING btree (pretrial_registrar);


--
-- Name: ix_courtcase_version_case_link_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_version_case_link_type ON courtcase_version USING btree (case_link_type);


--
-- Name: ix_courtcase_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_version_end_transaction_id ON courtcase_version USING btree (end_transaction_id);


--
-- Name: ix_courtcase_version_filing_prosecutor; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_version_filing_prosecutor ON courtcase_version USING btree (filing_prosecutor);


--
-- Name: ix_courtcase_version_linked_cases; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_version_linked_cases ON courtcase_version USING btree (linked_cases);


--
-- Name: ix_courtcase_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_version_operation_type ON courtcase_version USING btree (operation_type);


--
-- Name: ix_courtcase_version_pretrial_registrar; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_version_pretrial_registrar ON courtcase_version USING btree (pretrial_registrar);


--
-- Name: ix_courtcase_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtcase_version_transaction_id ON courtcase_version USING btree (transaction_id);


--
-- Name: ix_courtrank_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_courtrank_name ON courtrank USING btree (name);


--
-- Name: ix_courtrank_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtrank_version_end_transaction_id ON courtrank_version USING btree (end_transaction_id);


--
-- Name: ix_courtrank_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtrank_version_name ON courtrank_version USING btree (name);


--
-- Name: ix_courtrank_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtrank_version_operation_type ON courtrank_version USING btree (operation_type);


--
-- Name: ix_courtrank_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtrank_version_transaction_id ON courtrank_version USING btree (transaction_id);


--
-- Name: ix_courtstation_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_courtstation_name ON courtstation USING btree (name);


--
-- Name: ix_courtstation_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtstation_version_end_transaction_id ON courtstation_version USING btree (end_transaction_id);


--
-- Name: ix_courtstation_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtstation_version_name ON courtstation_version USING btree (name);


--
-- Name: ix_courtstation_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtstation_version_operation_type ON courtstation_version USING btree (operation_type);


--
-- Name: ix_courtstation_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_courtstation_version_transaction_id ON courtstation_version USING btree (transaction_id);


--
-- Name: ix_crime_ref_law; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_crime_ref_law ON crime USING btree (ref_law);


--
-- Name: ix_crime_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_crime_version_end_transaction_id ON crime_version USING btree (end_transaction_id);


--
-- Name: ix_crime_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_crime_version_operation_type ON crime_version USING btree (operation_type);


--
-- Name: ix_crime_version_ref_law; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_crime_version_ref_law ON crime_version USING btree (ref_law);


--
-- Name: ix_crime_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_crime_version_transaction_id ON crime_version USING btree (transaction_id);


--
-- Name: ix_csi_equipment_investigationdiary_investigationdiary; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_investigationdiary_investigationdiary ON csi_equipment_investigationdiary USING btree (investigationdiary);


--
-- Name: ix_csi_equipment_investigationdiary_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_investigationdiary_version_end_transaction_id ON csi_equipment_investigationdiary_version USING btree (end_transaction_id);


--
-- Name: ix_csi_equipment_investigationdiary_version_investigationdiary; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_investigationdiary_version_investigationdiary ON csi_equipment_investigationdiary_version USING btree (investigationdiary);


--
-- Name: ix_csi_equipment_investigationdiary_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_investigationdiary_version_operation_type ON csi_equipment_investigationdiary_version USING btree (operation_type);


--
-- Name: ix_csi_equipment_investigationdiary_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_investigationdiary_version_transaction_id ON csi_equipment_investigationdiary_version USING btree (transaction_id);


--
-- Name: ix_csi_equipment_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_version_end_transaction_id ON csi_equipment_version USING btree (end_transaction_id);


--
-- Name: ix_csi_equipment_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_version_operation_type ON csi_equipment_version USING btree (operation_type);


--
-- Name: ix_csi_equipment_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_csi_equipment_version_transaction_id ON csi_equipment_version USING btree (transaction_id);


--
-- Name: ix_diagram_investigation_diary; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_diagram_investigation_diary ON diagram USING btree (investigation_diary);


--
-- Name: ix_diagram_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_diagram_version_end_transaction_id ON diagram_version USING btree (end_transaction_id);


--
-- Name: ix_diagram_version_investigation_diary; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_diagram_version_investigation_diary ON diagram_version USING btree (investigation_diary);


--
-- Name: ix_diagram_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_diagram_version_operation_type ON diagram_version USING btree (operation_type);


--
-- Name: ix_diagram_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_diagram_version_transaction_id ON diagram_version USING btree (transaction_id);


--
-- Name: ix_discipline_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_discipline_name ON discipline USING btree (name);


--
-- Name: ix_discipline_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_party ON discipline USING btree (party);


--
-- Name: ix_discipline_prison_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_prison_officer ON discipline USING btree (prison_officer);


--
-- Name: ix_discipline_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_version_end_transaction_id ON discipline_version USING btree (end_transaction_id);


--
-- Name: ix_discipline_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_version_name ON discipline_version USING btree (name);


--
-- Name: ix_discipline_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_version_operation_type ON discipline_version USING btree (operation_type);


--
-- Name: ix_discipline_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_version_party ON discipline_version USING btree (party);


--
-- Name: ix_discipline_version_prison_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_version_prison_officer ON discipline_version USING btree (prison_officer);


--
-- Name: ix_discipline_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_discipline_version_transaction_id ON discipline_version USING btree (transaction_id);


--
-- Name: ix_doctemplate_template_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_doctemplate_template_type ON doctemplate USING btree (template_type);


--
-- Name: ix_doctemplate_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_doctemplate_version_end_transaction_id ON doctemplate_version USING btree (end_transaction_id);


--
-- Name: ix_doctemplate_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_doctemplate_version_operation_type ON doctemplate_version USING btree (operation_type);


--
-- Name: ix_doctemplate_version_template_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_doctemplate_version_template_type ON doctemplate_version USING btree (template_type);


--
-- Name: ix_doctemplate_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_doctemplate_version_transaction_id ON doctemplate_version USING btree (transaction_id);


--
-- Name: ix_document_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_court_case ON document USING btree (court_case);


--
-- Name: ix_document_doc_template; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_doc_template ON document USING btree (doc_template);


--
-- Name: ix_document_documenttype_documenttype; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_documenttype_documenttype ON document_documenttype USING btree (documenttype);


--
-- Name: ix_document_documenttype_version_documenttype; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_documenttype_version_documenttype ON document_documenttype_version USING btree (documenttype);


--
-- Name: ix_document_documenttype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_documenttype_version_end_transaction_id ON document_documenttype_version USING btree (end_transaction_id);


--
-- Name: ix_document_documenttype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_documenttype_version_operation_type ON document_documenttype_version USING btree (operation_type);


--
-- Name: ix_document_documenttype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_documenttype_version_transaction_id ON document_documenttype_version USING btree (transaction_id);


--
-- Name: ix_document_issue; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_issue ON document USING btree (issue);


--
-- Name: ix_document_judicial_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_judicial_officer ON document USING btree (judicial_officer);


--
-- Name: ix_document_search_vector; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_search_vector ON document USING gin (search_vector);


--
-- Name: ix_document_version_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_court_case ON document_version USING btree (court_case);


--
-- Name: ix_document_version_doc_template; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_doc_template ON document_version USING btree (doc_template);


--
-- Name: ix_document_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_end_transaction_id ON document_version USING btree (end_transaction_id);


--
-- Name: ix_document_version_issue; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_issue ON document_version USING btree (issue);


--
-- Name: ix_document_version_judicial_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_judicial_officer ON document_version USING btree (judicial_officer);


--
-- Name: ix_document_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_operation_type ON document_version USING btree (operation_type);


--
-- Name: ix_document_version_search_vector; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_search_vector ON document_version USING gin (search_vector);


--
-- Name: ix_document_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_document_version_transaction_id ON document_version USING btree (transaction_id);


--
-- Name: ix_documenttype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_documenttype_name ON documenttype USING btree (name);


--
-- Name: ix_documenttype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_documenttype_version_end_transaction_id ON documenttype_version USING btree (end_transaction_id);


--
-- Name: ix_documenttype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_documenttype_version_name ON documenttype_version USING btree (name);


--
-- Name: ix_documenttype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_documenttype_version_operation_type ON documenttype_version USING btree (operation_type);


--
-- Name: ix_documenttype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_documenttype_version_transaction_id ON documenttype_version USING btree (transaction_id);


--
-- Name: ix_economicclass_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_economicclass_version_end_transaction_id ON economicclass_version USING btree (end_transaction_id);


--
-- Name: ix_economicclass_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_economicclass_version_operation_type ON economicclass_version USING btree (operation_type);


--
-- Name: ix_economicclass_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_economicclass_version_transaction_id ON economicclass_version USING btree (transaction_id);


--
-- Name: ix_exhibit_investigation_entry; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_investigation_entry ON exhibit USING btree (investigation_entry);


--
-- Name: ix_exhibit_search_vector; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_search_vector ON exhibit USING gin (search_vector);


--
-- Name: ix_exhibit_seizure; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_seizure ON exhibit USING btree (seizure);


--
-- Name: ix_exhibit_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_version_end_transaction_id ON exhibit_version USING btree (end_transaction_id);


--
-- Name: ix_exhibit_version_investigation_entry; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_version_investigation_entry ON exhibit_version USING btree (investigation_entry);


--
-- Name: ix_exhibit_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_version_operation_type ON exhibit_version USING btree (operation_type);


--
-- Name: ix_exhibit_version_search_vector; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_version_search_vector ON exhibit_version USING gin (search_vector);


--
-- Name: ix_exhibit_version_seizure; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_version_seizure ON exhibit_version USING btree (seizure);


--
-- Name: ix_exhibit_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_exhibit_version_transaction_id ON exhibit_version USING btree (transaction_id);


--
-- Name: ix_expert_experttype_experttype; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_experttype_experttype ON expert_experttype USING btree (experttype);


--
-- Name: ix_expert_experttype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_experttype_version_end_transaction_id ON expert_experttype_version USING btree (end_transaction_id);


--
-- Name: ix_expert_experttype_version_experttype; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_experttype_version_experttype ON expert_experttype_version USING btree (experttype);


--
-- Name: ix_expert_experttype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_experttype_version_operation_type ON expert_experttype_version USING btree (operation_type);


--
-- Name: ix_expert_experttype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_experttype_version_transaction_id ON expert_experttype_version USING btree (transaction_id);


--
-- Name: ix_expert_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_version_end_transaction_id ON expert_version USING btree (end_transaction_id);


--
-- Name: ix_expert_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_version_operation_type ON expert_version USING btree (operation_type);


--
-- Name: ix_expert_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_expert_version_transaction_id ON expert_version USING btree (transaction_id);


--
-- Name: ix_experttestimony_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_court_case ON experttestimony USING btree (court_case);


--
-- Name: ix_experttestimony_experts; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_experts ON experttestimony USING btree (experts);


--
-- Name: ix_experttestimony_requesting_police_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_requesting_police_officer ON experttestimony USING btree (requesting_police_officer);


--
-- Name: ix_experttestimony_version_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_version_court_case ON experttestimony_version USING btree (court_case);


--
-- Name: ix_experttestimony_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_version_end_transaction_id ON experttestimony_version USING btree (end_transaction_id);


--
-- Name: ix_experttestimony_version_experts; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_version_experts ON experttestimony_version USING btree (experts);


--
-- Name: ix_experttestimony_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_version_operation_type ON experttestimony_version USING btree (operation_type);


--
-- Name: ix_experttestimony_version_requesting_police_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_version_requesting_police_officer ON experttestimony_version USING btree (requesting_police_officer);


--
-- Name: ix_experttestimony_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttestimony_version_transaction_id ON experttestimony_version USING btree (transaction_id);


--
-- Name: ix_experttype_expert_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttype_expert_type ON experttype USING btree (expert_type);


--
-- Name: ix_experttype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_experttype_name ON experttype USING btree (name);


--
-- Name: ix_experttype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttype_version_end_transaction_id ON experttype_version USING btree (end_transaction_id);


--
-- Name: ix_experttype_version_expert_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttype_version_expert_type ON experttype_version USING btree (expert_type);


--
-- Name: ix_experttype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttype_version_name ON experttype_version USING btree (name);


--
-- Name: ix_experttype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttype_version_operation_type ON experttype_version USING btree (operation_type);


--
-- Name: ix_experttype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_experttype_version_transaction_id ON experttype_version USING btree (transaction_id);


--
-- Name: ix_feeclass_fee_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feeclass_fee_type ON feeclass USING btree (fee_type);


--
-- Name: ix_feeclass_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_feeclass_name ON feeclass USING btree (name);


--
-- Name: ix_feeclass_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feeclass_version_end_transaction_id ON feeclass_version USING btree (end_transaction_id);


--
-- Name: ix_feeclass_version_fee_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feeclass_version_fee_type ON feeclass_version USING btree (fee_type);


--
-- Name: ix_feeclass_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feeclass_version_name ON feeclass_version USING btree (name);


--
-- Name: ix_feeclass_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feeclass_version_operation_type ON feeclass_version USING btree (operation_type);


--
-- Name: ix_feeclass_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feeclass_version_transaction_id ON feeclass_version USING btree (transaction_id);


--
-- Name: ix_feetype_account_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_account_type ON feetype USING btree (account_type);


--
-- Name: ix_feetype_filing_fee_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_filing_fee_type ON feetype USING btree (filing_fee_type);


--
-- Name: ix_feetype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_feetype_name ON feetype USING btree (name);


--
-- Name: ix_feetype_version_account_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_version_account_type ON feetype_version USING btree (account_type);


--
-- Name: ix_feetype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_version_end_transaction_id ON feetype_version USING btree (end_transaction_id);


--
-- Name: ix_feetype_version_filing_fee_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_version_filing_fee_type ON feetype_version USING btree (filing_fee_type);


--
-- Name: ix_feetype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_version_name ON feetype_version USING btree (name);


--
-- Name: ix_feetype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_version_operation_type ON feetype_version USING btree (operation_type);


--
-- Name: ix_feetype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_feetype_version_transaction_id ON feetype_version USING btree (transaction_id);


--
-- Name: ix_healthevent_health_event_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_health_event_type ON healthevent USING btree (health_event_type);


--
-- Name: ix_healthevent_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_party ON healthevent USING btree (party);


--
-- Name: ix_healthevent_reporting_prison_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_reporting_prison_officer ON healthevent USING btree (reporting_prison_officer);


--
-- Name: ix_healthevent_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_version_end_transaction_id ON healthevent_version USING btree (end_transaction_id);


--
-- Name: ix_healthevent_version_health_event_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_version_health_event_type ON healthevent_version USING btree (health_event_type);


--
-- Name: ix_healthevent_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_version_operation_type ON healthevent_version USING btree (operation_type);


--
-- Name: ix_healthevent_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_version_party ON healthevent_version USING btree (party);


--
-- Name: ix_healthevent_version_reporting_prison_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_version_reporting_prison_officer ON healthevent_version USING btree (reporting_prison_officer);


--
-- Name: ix_healthevent_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healthevent_version_transaction_id ON healthevent_version USING btree (transaction_id);


--
-- Name: ix_healtheventtype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_healtheventtype_name ON healtheventtype USING btree (name);


--
-- Name: ix_healtheventtype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healtheventtype_version_end_transaction_id ON healtheventtype_version USING btree (end_transaction_id);


--
-- Name: ix_healtheventtype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healtheventtype_version_name ON healtheventtype_version USING btree (name);


--
-- Name: ix_healtheventtype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healtheventtype_version_operation_type ON healtheventtype_version USING btree (operation_type);


--
-- Name: ix_healtheventtype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_healtheventtype_version_transaction_id ON healtheventtype_version USING btree (transaction_id);


--
-- Name: ix_hearing_court_cases; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_court_cases ON hearing USING btree (court_cases);


--
-- Name: ix_hearing_hearing_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_hearing_type ON hearing USING btree (hearing_type);


--
-- Name: ix_hearing_issue_issue; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_issue_issue ON hearing_issue USING btree (issue);


--
-- Name: ix_hearing_issue_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_issue_version_end_transaction_id ON hearing_issue_version USING btree (end_transaction_id);


--
-- Name: ix_hearing_issue_version_issue; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_issue_version_issue ON hearing_issue_version USING btree (issue);


--
-- Name: ix_hearing_issue_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_issue_version_operation_type ON hearing_issue_version USING btree (operation_type);


--
-- Name: ix_hearing_issue_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_issue_version_transaction_id ON hearing_issue_version USING btree (transaction_id);


--
-- Name: ix_hearing_judicialofficer_judicialofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_judicialofficer_judicialofficer ON hearing_judicialofficer USING btree (judicialofficer);


--
-- Name: ix_hearing_judicialofficer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_judicialofficer_version_end_transaction_id ON hearing_judicialofficer_version USING btree (end_transaction_id);


--
-- Name: ix_hearing_judicialofficer_version_judicialofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_judicialofficer_version_judicialofficer ON hearing_judicialofficer_version USING btree (judicialofficer);


--
-- Name: ix_hearing_judicialofficer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_judicialofficer_version_operation_type ON hearing_judicialofficer_version USING btree (operation_type);


--
-- Name: ix_hearing_judicialofficer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_judicialofficer_version_transaction_id ON hearing_judicialofficer_version USING btree (transaction_id);


--
-- Name: ix_hearing_lawfirm_2_lawfirm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_2_lawfirm ON hearing_lawfirm_2 USING btree (lawfirm);


--
-- Name: ix_hearing_lawfirm_2_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_2_version_end_transaction_id ON hearing_lawfirm_2_version USING btree (end_transaction_id);


--
-- Name: ix_hearing_lawfirm_2_version_lawfirm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_2_version_lawfirm ON hearing_lawfirm_2_version USING btree (lawfirm);


--
-- Name: ix_hearing_lawfirm_2_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_2_version_operation_type ON hearing_lawfirm_2_version USING btree (operation_type);


--
-- Name: ix_hearing_lawfirm_2_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_2_version_transaction_id ON hearing_lawfirm_2_version USING btree (transaction_id);


--
-- Name: ix_hearing_lawfirm_lawfirm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_lawfirm ON hearing_lawfirm USING btree (lawfirm);


--
-- Name: ix_hearing_lawfirm_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_version_end_transaction_id ON hearing_lawfirm_version USING btree (end_transaction_id);


--
-- Name: ix_hearing_lawfirm_version_lawfirm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_version_lawfirm ON hearing_lawfirm_version USING btree (lawfirm);


--
-- Name: ix_hearing_lawfirm_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_version_operation_type ON hearing_lawfirm_version USING btree (operation_type);


--
-- Name: ix_hearing_lawfirm_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_lawfirm_version_transaction_id ON hearing_lawfirm_version USING btree (transaction_id);


--
-- Name: ix_hearing_schedule_status; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_schedule_status ON hearing USING btree (schedule_status);


--
-- Name: ix_hearing_version_court_cases; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_version_court_cases ON hearing_version USING btree (court_cases);


--
-- Name: ix_hearing_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_version_end_transaction_id ON hearing_version USING btree (end_transaction_id);


--
-- Name: ix_hearing_version_hearing_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_version_hearing_type ON hearing_version USING btree (hearing_type);


--
-- Name: ix_hearing_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_version_operation_type ON hearing_version USING btree (operation_type);


--
-- Name: ix_hearing_version_schedule_status; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_version_schedule_status ON hearing_version USING btree (schedule_status);


--
-- Name: ix_hearing_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearing_version_transaction_id ON hearing_version USING btree (transaction_id);


--
-- Name: ix_hearingtype_hearing_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearingtype_hearing_type ON hearingtype USING btree (hearing_type);


--
-- Name: ix_hearingtype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_hearingtype_name ON hearingtype USING btree (name);


--
-- Name: ix_hearingtype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearingtype_version_end_transaction_id ON hearingtype_version USING btree (end_transaction_id);


--
-- Name: ix_hearingtype_version_hearing_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearingtype_version_hearing_type ON hearingtype_version USING btree (hearing_type);


--
-- Name: ix_hearingtype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearingtype_version_name ON hearingtype_version USING btree (name);


--
-- Name: ix_hearingtype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearingtype_version_operation_type ON hearingtype_version USING btree (operation_type);


--
-- Name: ix_hearingtype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_hearingtype_version_transaction_id ON hearingtype_version USING btree (transaction_id);


--
-- Name: ix_instancecrime_crimes; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_crimes ON instancecrime USING btree (crimes);


--
-- Name: ix_instancecrime_issue_issue; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_issue_issue ON instancecrime_issue USING btree (issue);


--
-- Name: ix_instancecrime_issue_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_issue_version_end_transaction_id ON instancecrime_issue_version USING btree (end_transaction_id);


--
-- Name: ix_instancecrime_issue_version_issue; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_issue_version_issue ON instancecrime_issue_version USING btree (issue);


--
-- Name: ix_instancecrime_issue_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_issue_version_operation_type ON instancecrime_issue_version USING btree (operation_type);


--
-- Name: ix_instancecrime_issue_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_issue_version_transaction_id ON instancecrime_issue_version USING btree (transaction_id);


--
-- Name: ix_instancecrime_parties; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_parties ON instancecrime USING btree (parties);


--
-- Name: ix_instancecrime_version_crimes; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_version_crimes ON instancecrime_version USING btree (crimes);


--
-- Name: ix_instancecrime_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_version_end_transaction_id ON instancecrime_version USING btree (end_transaction_id);


--
-- Name: ix_instancecrime_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_version_operation_type ON instancecrime_version USING btree (operation_type);


--
-- Name: ix_instancecrime_version_parties; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_version_parties ON instancecrime_version USING btree (parties);


--
-- Name: ix_instancecrime_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_instancecrime_version_transaction_id ON instancecrime_version USING btree (transaction_id);


--
-- Name: ix_interview_investigation_entry; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_interview_investigation_entry ON interview USING btree (investigation_entry);


--
-- Name: ix_interview_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_interview_version_end_transaction_id ON interview_version USING btree (end_transaction_id);


--
-- Name: ix_interview_version_investigation_entry; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_interview_version_investigation_entry ON interview_version USING btree (investigation_entry);


--
-- Name: ix_interview_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_interview_version_operation_type ON interview_version USING btree (operation_type);


--
-- Name: ix_interview_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_interview_version_transaction_id ON interview_version USING btree (transaction_id);


--
-- Name: ix_investigationdiary_complaint; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_complaint ON investigationdiary USING btree (complaint);


--
-- Name: ix_investigationdiary_party_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_party_party ON investigationdiary_party USING btree (party);


--
-- Name: ix_investigationdiary_party_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_party_version_end_transaction_id ON investigationdiary_party_version USING btree (end_transaction_id);


--
-- Name: ix_investigationdiary_party_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_party_version_operation_type ON investigationdiary_party_version USING btree (operation_type);


--
-- Name: ix_investigationdiary_party_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_party_version_party ON investigationdiary_party_version USING btree (party);


--
-- Name: ix_investigationdiary_party_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_party_version_transaction_id ON investigationdiary_party_version USING btree (transaction_id);


--
-- Name: ix_investigationdiary_policeofficer_policeofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_policeofficer_policeofficer ON investigationdiary_policeofficer USING btree (policeofficer);


--
-- Name: ix_investigationdiary_policeofficer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_policeofficer_version_end_transaction_id ON investigationdiary_policeofficer_version USING btree (end_transaction_id);


--
-- Name: ix_investigationdiary_policeofficer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_policeofficer_version_operation_type ON investigationdiary_policeofficer_version USING btree (operation_type);


--
-- Name: ix_investigationdiary_policeofficer_version_policeofficer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_policeofficer_version_policeofficer ON investigationdiary_policeofficer_version USING btree (policeofficer);


--
-- Name: ix_investigationdiary_policeofficer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_policeofficer_version_transaction_id ON investigationdiary_policeofficer_version USING btree (transaction_id);


--
-- Name: ix_investigationdiary_vehicle_vehicle; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_vehicle_vehicle ON investigationdiary_vehicle USING btree (vehicle);


--
-- Name: ix_investigationdiary_vehicle_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_vehicle_version_end_transaction_id ON investigationdiary_vehicle_version USING btree (end_transaction_id);


--
-- Name: ix_investigationdiary_vehicle_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_vehicle_version_operation_type ON investigationdiary_vehicle_version USING btree (operation_type);


--
-- Name: ix_investigationdiary_vehicle_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_vehicle_version_transaction_id ON investigationdiary_vehicle_version USING btree (transaction_id);


--
-- Name: ix_investigationdiary_vehicle_version_vehicle; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_vehicle_version_vehicle ON investigationdiary_vehicle_version USING btree (vehicle);


--
-- Name: ix_investigationdiary_version_complaint; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_version_complaint ON investigationdiary_version USING btree (complaint);


--
-- Name: ix_investigationdiary_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_version_end_transaction_id ON investigationdiary_version USING btree (end_transaction_id);


--
-- Name: ix_investigationdiary_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_version_operation_type ON investigationdiary_version USING btree (operation_type);


--
-- Name: ix_investigationdiary_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_version_transaction_id ON investigationdiary_version USING btree (transaction_id);


--
-- Name: ix_investigationdiary_version_warrant_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_version_warrant_type ON investigationdiary_version USING btree (warrant_type);


--
-- Name: ix_investigationdiary_warrant_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_investigationdiary_warrant_type ON investigationdiary USING btree (warrant_type);


--
-- Name: ix_issue_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_court_case ON issue USING btree (court_case);


--
-- Name: ix_issue_defense_lawyer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_defense_lawyer ON issue USING btree (defense_lawyer);


--
-- Name: ix_issue_judicial_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_judicial_officer ON issue USING btree (judicial_officer);


--
-- Name: ix_issue_lawyer_lawyer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_lawyer_lawyer ON issue_lawyer USING btree (lawyer);


--
-- Name: ix_issue_lawyer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_lawyer_version_end_transaction_id ON issue_lawyer_version USING btree (end_transaction_id);


--
-- Name: ix_issue_lawyer_version_lawyer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_lawyer_version_lawyer ON issue_lawyer_version USING btree (lawyer);


--
-- Name: ix_issue_lawyer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_lawyer_version_operation_type ON issue_lawyer_version USING btree (operation_type);


--
-- Name: ix_issue_lawyer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_lawyer_version_transaction_id ON issue_lawyer_version USING btree (transaction_id);


--
-- Name: ix_issue_legalreference_2_legalreference; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_2_legalreference ON issue_legalreference_2 USING btree (legalreference);


--
-- Name: ix_issue_legalreference_2_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_2_version_end_transaction_id ON issue_legalreference_2_version USING btree (end_transaction_id);


--
-- Name: ix_issue_legalreference_2_version_legalreference; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_2_version_legalreference ON issue_legalreference_2_version USING btree (legalreference);


--
-- Name: ix_issue_legalreference_2_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_2_version_operation_type ON issue_legalreference_2_version USING btree (operation_type);


--
-- Name: ix_issue_legalreference_2_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_2_version_transaction_id ON issue_legalreference_2_version USING btree (transaction_id);


--
-- Name: ix_issue_legalreference_legalreference; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_legalreference ON issue_legalreference USING btree (legalreference);


--
-- Name: ix_issue_legalreference_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_version_end_transaction_id ON issue_legalreference_version USING btree (end_transaction_id);


--
-- Name: ix_issue_legalreference_version_legalreference; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_version_legalreference ON issue_legalreference_version USING btree (legalreference);


--
-- Name: ix_issue_legalreference_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_version_operation_type ON issue_legalreference_version USING btree (operation_type);


--
-- Name: ix_issue_legalreference_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_legalreference_version_transaction_id ON issue_legalreference_version USING btree (transaction_id);


--
-- Name: ix_issue_party_2_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_2_party ON issue_party_2 USING btree (party);


--
-- Name: ix_issue_party_2_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_2_version_end_transaction_id ON issue_party_2_version USING btree (end_transaction_id);


--
-- Name: ix_issue_party_2_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_2_version_operation_type ON issue_party_2_version USING btree (operation_type);


--
-- Name: ix_issue_party_2_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_2_version_party ON issue_party_2_version USING btree (party);


--
-- Name: ix_issue_party_2_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_2_version_transaction_id ON issue_party_2_version USING btree (transaction_id);


--
-- Name: ix_issue_party_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_party ON issue_party USING btree (party);


--
-- Name: ix_issue_party_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_version_end_transaction_id ON issue_party_version USING btree (end_transaction_id);


--
-- Name: ix_issue_party_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_version_operation_type ON issue_party_version USING btree (operation_type);


--
-- Name: ix_issue_party_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_version_party ON issue_party_version USING btree (party);


--
-- Name: ix_issue_party_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_party_version_transaction_id ON issue_party_version USING btree (transaction_id);


--
-- Name: ix_issue_prosecutor; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_prosecutor ON issue USING btree (prosecutor);


--
-- Name: ix_issue_version_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_version_court_case ON issue_version USING btree (court_case);


--
-- Name: ix_issue_version_defense_lawyer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_version_defense_lawyer ON issue_version USING btree (defense_lawyer);


--
-- Name: ix_issue_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_version_end_transaction_id ON issue_version USING btree (end_transaction_id);


--
-- Name: ix_issue_version_judicial_officer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_version_judicial_officer ON issue_version USING btree (judicial_officer);


--
-- Name: ix_issue_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_version_operation_type ON issue_version USING btree (operation_type);


--
-- Name: ix_issue_version_prosecutor; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_version_prosecutor ON issue_version USING btree (prosecutor);


--
-- Name: ix_issue_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_issue_version_transaction_id ON issue_version USING btree (transaction_id);


--
-- Name: ix_judicialofficer_court_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_court_station ON judicialofficer USING btree (court_station);


--
-- Name: ix_judicialofficer_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_firstname ON judicialofficer USING btree (firstname);


--
-- Name: ix_judicialofficer_judicial_role; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_judicial_role ON judicialofficer USING btree (judicial_role);


--
-- Name: ix_judicialofficer_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_othernames ON judicialofficer USING btree (othernames);


--
-- Name: ix_judicialofficer_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_rank ON judicialofficer USING btree (rank);


--
-- Name: ix_judicialofficer_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_surname ON judicialofficer USING btree (surname);


--
-- Name: ix_judicialofficer_version_court_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_court_station ON judicialofficer_version USING btree (court_station);


--
-- Name: ix_judicialofficer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_end_transaction_id ON judicialofficer_version USING btree (end_transaction_id);


--
-- Name: ix_judicialofficer_version_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_firstname ON judicialofficer_version USING btree (firstname);


--
-- Name: ix_judicialofficer_version_judicial_role; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_judicial_role ON judicialofficer_version USING btree (judicial_role);


--
-- Name: ix_judicialofficer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_operation_type ON judicialofficer_version USING btree (operation_type);


--
-- Name: ix_judicialofficer_version_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_othernames ON judicialofficer_version USING btree (othernames);


--
-- Name: ix_judicialofficer_version_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_rank ON judicialofficer_version USING btree (rank);


--
-- Name: ix_judicialofficer_version_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_surname ON judicialofficer_version USING btree (surname);


--
-- Name: ix_judicialofficer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialofficer_version_transaction_id ON judicialofficer_version USING btree (transaction_id);


--
-- Name: ix_judicialrank_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_judicialrank_name ON judicialrank USING btree (name);


--
-- Name: ix_judicialrank_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrank_version_end_transaction_id ON judicialrank_version USING btree (end_transaction_id);


--
-- Name: ix_judicialrank_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrank_version_name ON judicialrank_version USING btree (name);


--
-- Name: ix_judicialrank_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrank_version_operation_type ON judicialrank_version USING btree (operation_type);


--
-- Name: ix_judicialrank_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrank_version_transaction_id ON judicialrank_version USING btree (transaction_id);


--
-- Name: ix_judicialrole_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_judicialrole_name ON judicialrole USING btree (name);


--
-- Name: ix_judicialrole_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrole_version_end_transaction_id ON judicialrole_version USING btree (end_transaction_id);


--
-- Name: ix_judicialrole_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrole_version_name ON judicialrole_version USING btree (name);


--
-- Name: ix_judicialrole_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrole_version_operation_type ON judicialrole_version USING btree (operation_type);


--
-- Name: ix_judicialrole_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_judicialrole_version_transaction_id ON judicialrole_version USING btree (transaction_id);


--
-- Name: ix_law_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_law_version_end_transaction_id ON law_version USING btree (end_transaction_id);


--
-- Name: ix_law_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_law_version_operation_type ON law_version USING btree (operation_type);


--
-- Name: ix_law_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_law_version_transaction_id ON law_version USING btree (transaction_id);


--
-- Name: ix_lawfirm_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawfirm_mobile ON lawfirm USING btree (mobile);


--
-- Name: ix_lawfirm_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_lawfirm_name ON lawfirm USING btree (name);


--
-- Name: ix_lawfirm_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawfirm_version_end_transaction_id ON lawfirm_version USING btree (end_transaction_id);


--
-- Name: ix_lawfirm_version_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawfirm_version_mobile ON lawfirm_version USING btree (mobile);


--
-- Name: ix_lawfirm_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawfirm_version_name ON lawfirm_version USING btree (name);


--
-- Name: ix_lawfirm_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawfirm_version_operation_type ON lawfirm_version USING btree (operation_type);


--
-- Name: ix_lawfirm_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawfirm_version_transaction_id ON lawfirm_version USING btree (transaction_id);


--
-- Name: ix_lawyer_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_firstname ON lawyer USING btree (firstname);


--
-- Name: ix_lawyer_law_firm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_law_firm ON lawyer USING btree (law_firm);


--
-- Name: ix_lawyer_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_mobile ON lawyer USING btree (mobile);


--
-- Name: ix_lawyer_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_othernames ON lawyer USING btree (othernames);


--
-- Name: ix_lawyer_party_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_party_party ON lawyer_party USING btree (party);


--
-- Name: ix_lawyer_party_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_party_version_end_transaction_id ON lawyer_party_version USING btree (end_transaction_id);


--
-- Name: ix_lawyer_party_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_party_version_operation_type ON lawyer_party_version USING btree (operation_type);


--
-- Name: ix_lawyer_party_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_party_version_party ON lawyer_party_version USING btree (party);


--
-- Name: ix_lawyer_party_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_party_version_transaction_id ON lawyer_party_version USING btree (transaction_id);


--
-- Name: ix_lawyer_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_surname ON lawyer USING btree (surname);


--
-- Name: ix_lawyer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_end_transaction_id ON lawyer_version USING btree (end_transaction_id);


--
-- Name: ix_lawyer_version_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_firstname ON lawyer_version USING btree (firstname);


--
-- Name: ix_lawyer_version_law_firm; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_law_firm ON lawyer_version USING btree (law_firm);


--
-- Name: ix_lawyer_version_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_mobile ON lawyer_version USING btree (mobile);


--
-- Name: ix_lawyer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_operation_type ON lawyer_version USING btree (operation_type);


--
-- Name: ix_lawyer_version_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_othernames ON lawyer_version USING btree (othernames);


--
-- Name: ix_lawyer_version_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_surname ON lawyer_version USING btree (surname);


--
-- Name: ix_lawyer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_lawyer_version_transaction_id ON lawyer_version USING btree (transaction_id);


--
-- Name: ix_legalreference_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_legalreference_version_end_transaction_id ON legalreference_version USING btree (end_transaction_id);


--
-- Name: ix_legalreference_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_legalreference_version_operation_type ON legalreference_version USING btree (operation_type);


--
-- Name: ix_legalreference_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_legalreference_version_transaction_id ON legalreference_version USING btree (transaction_id);


--
-- Name: ix_nextofkin_bc_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_bc_id ON nextofkin USING btree (bc_id);


--
-- Name: ix_nextofkin_bc_number; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_bc_number ON nextofkin USING btree (bc_number);


--
-- Name: ix_nextofkin_bc_place; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_bc_place ON nextofkin USING btree (bc_place);


--
-- Name: ix_nextofkin_bc_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_bc_serial ON nextofkin USING btree (bc_serial);


--
-- Name: ix_nextofkin_biodata; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_biodata ON nextofkin USING btree (biodata);


--
-- Name: ix_nextofkin_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_firstname ON nextofkin USING btree (firstname);


--
-- Name: ix_nextofkin_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_mobile ON nextofkin USING btree (mobile);


--
-- Name: ix_nextofkin_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_nat_id_num ON nextofkin USING btree (nat_id_num);


--
-- Name: ix_nextofkin_nat_id_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_nat_id_serial ON nextofkin USING btree (nat_id_serial);


--
-- Name: ix_nextofkin_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_othernames ON nextofkin USING btree (othernames);


--
-- Name: ix_nextofkin_pp_no; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_pp_no ON nextofkin USING btree (pp_no);


--
-- Name: ix_nextofkin_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_surname ON nextofkin USING btree (surname);


--
-- Name: ix_nextofkin_version_bc_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_bc_id ON nextofkin_version USING btree (bc_id);


--
-- Name: ix_nextofkin_version_bc_number; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_bc_number ON nextofkin_version USING btree (bc_number);


--
-- Name: ix_nextofkin_version_bc_place; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_bc_place ON nextofkin_version USING btree (bc_place);


--
-- Name: ix_nextofkin_version_bc_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_bc_serial ON nextofkin_version USING btree (bc_serial);


--
-- Name: ix_nextofkin_version_biodata; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_biodata ON nextofkin_version USING btree (biodata);


--
-- Name: ix_nextofkin_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_end_transaction_id ON nextofkin_version USING btree (end_transaction_id);


--
-- Name: ix_nextofkin_version_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_firstname ON nextofkin_version USING btree (firstname);


--
-- Name: ix_nextofkin_version_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_mobile ON nextofkin_version USING btree (mobile);


--
-- Name: ix_nextofkin_version_nat_id_num; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_nat_id_num ON nextofkin_version USING btree (nat_id_num);


--
-- Name: ix_nextofkin_version_nat_id_serial; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_nat_id_serial ON nextofkin_version USING btree (nat_id_serial);


--
-- Name: ix_nextofkin_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_operation_type ON nextofkin_version USING btree (operation_type);


--
-- Name: ix_nextofkin_version_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_othernames ON nextofkin_version USING btree (othernames);


--
-- Name: ix_nextofkin_version_pp_no; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_pp_no ON nextofkin_version USING btree (pp_no);


--
-- Name: ix_nextofkin_version_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_surname ON nextofkin_version USING btree (surname);


--
-- Name: ix_nextofkin_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_nextofkin_version_transaction_id ON nextofkin_version USING btree (transaction_id);


--
-- Name: ix_notification_notification_register; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notification_notification_register ON notification USING btree (notification_register);


--
-- Name: ix_notification_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notification_version_end_transaction_id ON notification_version USING btree (end_transaction_id);


--
-- Name: ix_notification_version_notification_register; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notification_version_notification_register ON notification_version USING btree (notification_register);


--
-- Name: ix_notification_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notification_version_operation_type ON notification_version USING btree (operation_type);


--
-- Name: ix_notification_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notification_version_transaction_id ON notification_version USING btree (transaction_id);


--
-- Name: ix_notificationregister_complaint; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_complaint ON notificationregister USING btree (complaint);


--
-- Name: ix_notificationregister_complaint_category; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_complaint_category ON notificationregister USING btree (complaint_category);


--
-- Name: ix_notificationregister_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_court_case ON notificationregister USING btree (court_case);


--
-- Name: ix_notificationregister_document; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_document ON notificationregister USING btree (document);


--
-- Name: ix_notificationregister_health_event; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_health_event ON notificationregister USING btree (health_event);


--
-- Name: ix_notificationregister_hearing; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_hearing ON notificationregister USING btree (hearing);


--
-- Name: ix_notificationregister_notification_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_notification_type ON notificationregister USING btree (notification_type);


--
-- Name: ix_notificationregister_notify_event; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_notify_event ON notificationregister USING btree (notify_event);


--
-- Name: ix_notificationregister_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_party ON notificationregister USING btree (party);


--
-- Name: ix_notificationregister_version_complaint; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_complaint ON notificationregister_version USING btree (complaint);


--
-- Name: ix_notificationregister_version_complaint_category; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_complaint_category ON notificationregister_version USING btree (complaint_category);


--
-- Name: ix_notificationregister_version_court_case; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_court_case ON notificationregister_version USING btree (court_case);


--
-- Name: ix_notificationregister_version_document; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_document ON notificationregister_version USING btree (document);


--
-- Name: ix_notificationregister_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_end_transaction_id ON notificationregister_version USING btree (end_transaction_id);


--
-- Name: ix_notificationregister_version_health_event; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_health_event ON notificationregister_version USING btree (health_event);


--
-- Name: ix_notificationregister_version_hearing; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_hearing ON notificationregister_version USING btree (hearing);


--
-- Name: ix_notificationregister_version_notification_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_notification_type ON notificationregister_version USING btree (notification_type);


--
-- Name: ix_notificationregister_version_notify_event; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_notify_event ON notificationregister_version USING btree (notify_event);


--
-- Name: ix_notificationregister_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_operation_type ON notificationregister_version USING btree (operation_type);


--
-- Name: ix_notificationregister_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_party ON notificationregister_version USING btree (party);


--
-- Name: ix_notificationregister_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationregister_version_transaction_id ON notificationregister_version USING btree (transaction_id);


--
-- Name: ix_notificationtype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationtype_version_end_transaction_id ON notificationtype_version USING btree (end_transaction_id);


--
-- Name: ix_notificationtype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationtype_version_operation_type ON notificationtype_version USING btree (operation_type);


--
-- Name: ix_notificationtype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notificationtype_version_transaction_id ON notificationtype_version USING btree (transaction_id);


--
-- Name: ix_notifyevent_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notifyevent_version_end_transaction_id ON notifyevent_version USING btree (end_transaction_id);


--
-- Name: ix_notifyevent_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notifyevent_version_operation_type ON notifyevent_version USING btree (operation_type);


--
-- Name: ix_notifyevent_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_notifyevent_version_transaction_id ON notifyevent_version USING btree (transaction_id);


--
-- Name: ix_page_document; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_page_document ON page USING btree (document);


--
-- Name: ix_page_version_document; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_page_version_document ON page_version USING btree (document);


--
-- Name: ix_page_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_page_version_end_transaction_id ON page_version USING btree (end_transaction_id);


--
-- Name: ix_page_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_page_version_operation_type ON page_version USING btree (operation_type);


--
-- Name: ix_page_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_page_version_transaction_id ON page_version USING btree (transaction_id);


--
-- Name: ix_party_complaint_role; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_complaint_role ON party USING btree (complaint_role);


--
-- Name: ix_party_complaints; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_complaints ON party USING btree (complaints);


--
-- Name: ix_party_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_firstname ON party USING btree (firstname);


--
-- Name: ix_party_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_mobile ON party USING btree (mobile);


--
-- Name: ix_party_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_othernames ON party USING btree (othernames);


--
-- Name: ix_party_party_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_party_type ON party USING btree (party_type);


--
-- Name: ix_party_relative; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_relative ON party USING btree (relative);


--
-- Name: ix_party_settlement_settlement; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_settlement_settlement ON party_settlement USING btree (settlement);


--
-- Name: ix_party_settlement_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_settlement_version_end_transaction_id ON party_settlement_version USING btree (end_transaction_id);


--
-- Name: ix_party_settlement_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_settlement_version_operation_type ON party_settlement_version USING btree (operation_type);


--
-- Name: ix_party_settlement_version_settlement; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_settlement_version_settlement ON party_settlement_version USING btree (settlement);


--
-- Name: ix_party_settlement_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_settlement_version_transaction_id ON party_settlement_version USING btree (transaction_id);


--
-- Name: ix_party_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_surname ON party USING btree (surname);


--
-- Name: ix_party_version_complaint_role; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_complaint_role ON party_version USING btree (complaint_role);


--
-- Name: ix_party_version_complaints; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_complaints ON party_version USING btree (complaints);


--
-- Name: ix_party_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_end_transaction_id ON party_version USING btree (end_transaction_id);


--
-- Name: ix_party_version_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_firstname ON party_version USING btree (firstname);


--
-- Name: ix_party_version_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_mobile ON party_version USING btree (mobile);


--
-- Name: ix_party_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_operation_type ON party_version USING btree (operation_type);


--
-- Name: ix_party_version_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_othernames ON party_version USING btree (othernames);


--
-- Name: ix_party_version_party_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_party_type ON party_version USING btree (party_type);


--
-- Name: ix_party_version_relative; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_relative ON party_version USING btree (relative);


--
-- Name: ix_party_version_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_surname ON party_version USING btree (surname);


--
-- Name: ix_party_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_party_version_transaction_id ON party_version USING btree (transaction_id);


--
-- Name: ix_partytype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_partytype_name ON partytype USING btree (name);


--
-- Name: ix_partytype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_partytype_version_end_transaction_id ON partytype_version USING btree (end_transaction_id);


--
-- Name: ix_partytype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_partytype_version_name ON partytype_version USING btree (name);


--
-- Name: ix_partytype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_partytype_version_operation_type ON partytype_version USING btree (operation_type);


--
-- Name: ix_partytype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_partytype_version_transaction_id ON partytype_version USING btree (transaction_id);


--
-- Name: ix_payment_bill; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_payment_bill ON payment USING btree (bill);


--
-- Name: ix_payment_version_bill; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_payment_version_bill ON payment_version USING btree (bill);


--
-- Name: ix_payment_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_payment_version_end_transaction_id ON payment_version USING btree (end_transaction_id);


--
-- Name: ix_payment_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_payment_version_operation_type ON payment_version USING btree (operation_type);


--
-- Name: ix_payment_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_payment_version_transaction_id ON payment_version USING btree (transaction_id);


--
-- Name: ix_personaleffect_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffect_party ON personaleffect USING btree (party);


--
-- Name: ix_personaleffect_personal_effects_category; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffect_personal_effects_category ON personaleffect USING btree (personal_effects_category);


--
-- Name: ix_personaleffect_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffect_version_end_transaction_id ON personaleffect_version USING btree (end_transaction_id);


--
-- Name: ix_personaleffect_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffect_version_operation_type ON personaleffect_version USING btree (operation_type);


--
-- Name: ix_personaleffect_version_party; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffect_version_party ON personaleffect_version USING btree (party);


--
-- Name: ix_personaleffect_version_personal_effects_category; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffect_version_personal_effects_category ON personaleffect_version USING btree (personal_effects_category);


--
-- Name: ix_personaleffect_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffect_version_transaction_id ON personaleffect_version USING btree (transaction_id);


--
-- Name: ix_personaleffectscategory_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_personaleffectscategory_name ON personaleffectscategory USING btree (name);


--
-- Name: ix_personaleffectscategory_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffectscategory_version_end_transaction_id ON personaleffectscategory_version USING btree (end_transaction_id);


--
-- Name: ix_personaleffectscategory_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffectscategory_version_name ON personaleffectscategory_version USING btree (name);


--
-- Name: ix_personaleffectscategory_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffectscategory_version_operation_type ON personaleffectscategory_version USING btree (operation_type);


--
-- Name: ix_personaleffectscategory_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_personaleffectscategory_version_transaction_id ON personaleffectscategory_version USING btree (transaction_id);


--
-- Name: ix_policeofficer_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_firstname ON policeofficer USING btree (firstname);


--
-- Name: ix_policeofficer_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_othernames ON policeofficer USING btree (othernames);


--
-- Name: ix_policeofficer_police_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_police_rank ON policeofficer USING btree (police_rank);


--
-- Name: ix_policeofficer_policestation_policestation; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_policestation_policestation ON policeofficer_policestation USING btree (policestation);


--
-- Name: ix_policeofficer_policestation_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_policestation_version_end_transaction_id ON policeofficer_policestation_version USING btree (end_transaction_id);


--
-- Name: ix_policeofficer_policestation_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_policestation_version_operation_type ON policeofficer_policestation_version USING btree (operation_type);


--
-- Name: ix_policeofficer_policestation_version_policestation; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_policestation_version_policestation ON policeofficer_policestation_version USING btree (policestation);


--
-- Name: ix_policeofficer_policestation_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_policestation_version_transaction_id ON policeofficer_policestation_version USING btree (transaction_id);


--
-- Name: ix_policeofficer_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_surname ON policeofficer USING btree (surname);


--
-- Name: ix_policeofficer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_version_end_transaction_id ON policeofficer_version USING btree (end_transaction_id);


--
-- Name: ix_policeofficer_version_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_version_firstname ON policeofficer_version USING btree (firstname);


--
-- Name: ix_policeofficer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_version_operation_type ON policeofficer_version USING btree (operation_type);


--
-- Name: ix_policeofficer_version_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_version_othernames ON policeofficer_version USING btree (othernames);


--
-- Name: ix_policeofficer_version_police_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_version_police_rank ON policeofficer_version USING btree (police_rank);


--
-- Name: ix_policeofficer_version_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_version_surname ON policeofficer_version USING btree (surname);


--
-- Name: ix_policeofficer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficer_version_transaction_id ON policeofficer_version USING btree (transaction_id);


--
-- Name: ix_policeofficerrank_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficerrank_version_end_transaction_id ON policeofficerrank_version USING btree (end_transaction_id);


--
-- Name: ix_policeofficerrank_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficerrank_version_operation_type ON policeofficerrank_version USING btree (operation_type);


--
-- Name: ix_policeofficerrank_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policeofficerrank_version_transaction_id ON policeofficerrank_version USING btree (transaction_id);


--
-- Name: ix_policestation_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_policestation_name ON policestation USING btree (name);


--
-- Name: ix_policestation_officer_commanding; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_officer_commanding ON policestation USING btree (officer_commanding);


--
-- Name: ix_policestation_police_station_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_police_station_rank ON policestation USING btree (police_station_rank);


--
-- Name: ix_policestation_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_town ON policestation USING btree (town);


--
-- Name: ix_policestation_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_version_end_transaction_id ON policestation_version USING btree (end_transaction_id);


--
-- Name: ix_policestation_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_version_name ON policestation_version USING btree (name);


--
-- Name: ix_policestation_version_officer_commanding; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_version_officer_commanding ON policestation_version USING btree (officer_commanding);


--
-- Name: ix_policestation_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_version_operation_type ON policestation_version USING btree (operation_type);


--
-- Name: ix_policestation_version_police_station_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_version_police_station_rank ON policestation_version USING btree (police_station_rank);


--
-- Name: ix_policestation_version_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_version_town ON policestation_version USING btree (town);


--
-- Name: ix_policestation_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestation_version_transaction_id ON policestation_version USING btree (transaction_id);


--
-- Name: ix_policestationrank_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_policestationrank_name ON policestationrank USING btree (name);


--
-- Name: ix_policestationrank_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestationrank_version_end_transaction_id ON policestationrank_version USING btree (end_transaction_id);


--
-- Name: ix_policestationrank_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestationrank_version_name ON policestationrank_version USING btree (name);


--
-- Name: ix_policestationrank_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestationrank_version_operation_type ON policestationrank_version USING btree (operation_type);


--
-- Name: ix_policestationrank_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_policestationrank_version_transaction_id ON policestationrank_version USING btree (transaction_id);


--
-- Name: ix_prison_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prison_town ON prison USING btree (town);


--
-- Name: ix_prison_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prison_version_end_transaction_id ON prison_version USING btree (end_transaction_id);


--
-- Name: ix_prison_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prison_version_operation_type ON prison_version USING btree (operation_type);


--
-- Name: ix_prison_version_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prison_version_town ON prison_version USING btree (town);


--
-- Name: ix_prison_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prison_version_transaction_id ON prison_version USING btree (transaction_id);


--
-- Name: ix_prisonofficer_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_firstname ON prisonofficer USING btree (firstname);


--
-- Name: ix_prisonofficer_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_othernames ON prisonofficer USING btree (othernames);


--
-- Name: ix_prisonofficer_prison; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_prison ON prisonofficer USING btree (prison);


--
-- Name: ix_prisonofficer_prison_officer_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_prison_officer_rank ON prisonofficer USING btree (prison_officer_rank);


--
-- Name: ix_prisonofficer_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_surname ON prisonofficer USING btree (surname);


--
-- Name: ix_prisonofficer_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_end_transaction_id ON prisonofficer_version USING btree (end_transaction_id);


--
-- Name: ix_prisonofficer_version_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_firstname ON prisonofficer_version USING btree (firstname);


--
-- Name: ix_prisonofficer_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_operation_type ON prisonofficer_version USING btree (operation_type);


--
-- Name: ix_prisonofficer_version_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_othernames ON prisonofficer_version USING btree (othernames);


--
-- Name: ix_prisonofficer_version_prison; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_prison ON prisonofficer_version USING btree (prison);


--
-- Name: ix_prisonofficer_version_prison_officer_rank; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_prison_officer_rank ON prisonofficer_version USING btree (prison_officer_rank);


--
-- Name: ix_prisonofficer_version_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_surname ON prisonofficer_version USING btree (surname);


--
-- Name: ix_prisonofficer_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficer_version_transaction_id ON prisonofficer_version USING btree (transaction_id);


--
-- Name: ix_prisonofficerrank_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_prisonofficerrank_name ON prisonofficerrank USING btree (name);


--
-- Name: ix_prisonofficerrank_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficerrank_version_end_transaction_id ON prisonofficerrank_version USING btree (end_transaction_id);


--
-- Name: ix_prisonofficerrank_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficerrank_version_name ON prisonofficerrank_version USING btree (name);


--
-- Name: ix_prisonofficerrank_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficerrank_version_operation_type ON prisonofficerrank_version USING btree (operation_type);


--
-- Name: ix_prisonofficerrank_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prisonofficerrank_version_transaction_id ON prisonofficerrank_version USING btree (transaction_id);


--
-- Name: ix_prosecutor_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_firstname ON prosecutor USING btree (firstname);


--
-- Name: ix_prosecutor_lawyer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_lawyer ON prosecutor USING btree (lawyer);


--
-- Name: ix_prosecutor_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_mobile ON prosecutor USING btree (mobile);


--
-- Name: ix_prosecutor_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_othernames ON prosecutor USING btree (othernames);


--
-- Name: ix_prosecutor_prosecutor_team; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_prosecutor_team ON prosecutor USING btree (prosecutor_team);


--
-- Name: ix_prosecutor_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_surname ON prosecutor USING btree (surname);


--
-- Name: ix_prosecutor_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_end_transaction_id ON prosecutor_version USING btree (end_transaction_id);


--
-- Name: ix_prosecutor_version_firstname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_firstname ON prosecutor_version USING btree (firstname);


--
-- Name: ix_prosecutor_version_lawyer; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_lawyer ON prosecutor_version USING btree (lawyer);


--
-- Name: ix_prosecutor_version_mobile; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_mobile ON prosecutor_version USING btree (mobile);


--
-- Name: ix_prosecutor_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_operation_type ON prosecutor_version USING btree (operation_type);


--
-- Name: ix_prosecutor_version_othernames; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_othernames ON prosecutor_version USING btree (othernames);


--
-- Name: ix_prosecutor_version_prosecutor_team; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_prosecutor_team ON prosecutor_version USING btree (prosecutor_team);


--
-- Name: ix_prosecutor_version_surname; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_surname ON prosecutor_version USING btree (surname);


--
-- Name: ix_prosecutor_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutor_version_transaction_id ON prosecutor_version USING btree (transaction_id);


--
-- Name: ix_prosecutorteam_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_prosecutorteam_name ON prosecutorteam USING btree (name);


--
-- Name: ix_prosecutorteam_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutorteam_version_end_transaction_id ON prosecutorteam_version USING btree (end_transaction_id);


--
-- Name: ix_prosecutorteam_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutorteam_version_name ON prosecutorteam_version USING btree (name);


--
-- Name: ix_prosecutorteam_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutorteam_version_operation_type ON prosecutorteam_version USING btree (operation_type);


--
-- Name: ix_prosecutorteam_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_prosecutorteam_version_transaction_id ON prosecutorteam_version USING btree (transaction_id);


--
-- Name: ix_releasetype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_releasetype_name ON releasetype USING btree (name);


--
-- Name: ix_releasetype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_releasetype_version_end_transaction_id ON releasetype_version USING btree (end_transaction_id);


--
-- Name: ix_releasetype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_releasetype_version_name ON releasetype_version USING btree (name);


--
-- Name: ix_releasetype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_releasetype_version_operation_type ON releasetype_version USING btree (operation_type);


--
-- Name: ix_releasetype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_releasetype_version_transaction_id ON releasetype_version USING btree (transaction_id);


--
-- Name: ix_religion_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_religion_version_end_transaction_id ON religion_version USING btree (end_transaction_id);


--
-- Name: ix_religion_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_religion_version_operation_type ON religion_version USING btree (operation_type);


--
-- Name: ix_religion_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_religion_version_transaction_id ON religion_version USING btree (transaction_id);


--
-- Name: ix_schedulestatustype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_schedulestatustype_name ON schedulestatustype USING btree (name);


--
-- Name: ix_schedulestatustype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_schedulestatustype_version_end_transaction_id ON schedulestatustype_version USING btree (end_transaction_id);


--
-- Name: ix_schedulestatustype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_schedulestatustype_version_name ON schedulestatustype_version USING btree (name);


--
-- Name: ix_schedulestatustype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_schedulestatustype_version_operation_type ON schedulestatustype_version USING btree (operation_type);


--
-- Name: ix_schedulestatustype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_schedulestatustype_version_transaction_id ON schedulestatustype_version USING btree (transaction_id);


--
-- Name: ix_seizure_investigation_diary; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_seizure_investigation_diary ON seizure USING btree (investigation_diary);


--
-- Name: ix_seizure_recovery_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_seizure_recovery_town ON seizure USING btree (recovery_town);


--
-- Name: ix_seizure_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_seizure_version_end_transaction_id ON seizure_version USING btree (end_transaction_id);


--
-- Name: ix_seizure_version_investigation_diary; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_seizure_version_investigation_diary ON seizure_version USING btree (investigation_diary);


--
-- Name: ix_seizure_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_seizure_version_operation_type ON seizure_version USING btree (operation_type);


--
-- Name: ix_seizure_version_recovery_town; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_seizure_version_recovery_town ON seizure_version USING btree (recovery_town);


--
-- Name: ix_seizure_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_seizure_version_transaction_id ON seizure_version USING btree (transaction_id);


--
-- Name: ix_settlement_complaint; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_settlement_complaint ON settlement USING btree (complaint);


--
-- Name: ix_settlement_settlor; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_settlement_settlor ON settlement USING btree (settlor);


--
-- Name: ix_settlement_version_complaint; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_settlement_version_complaint ON settlement_version USING btree (complaint);


--
-- Name: ix_settlement_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_settlement_version_end_transaction_id ON settlement_version USING btree (end_transaction_id);


--
-- Name: ix_settlement_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_settlement_version_operation_type ON settlement_version USING btree (operation_type);


--
-- Name: ix_settlement_version_settlor; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_settlement_version_settlor ON settlement_version USING btree (settlor);


--
-- Name: ix_settlement_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_settlement_version_transaction_id ON settlement_version USING btree (transaction_id);


--
-- Name: ix_subcounty_county; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_subcounty_county ON subcounty USING btree (county);


--
-- Name: ix_subcounty_version_county; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_subcounty_version_county ON subcounty_version USING btree (county);


--
-- Name: ix_subcounty_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_subcounty_version_end_transaction_id ON subcounty_version USING btree (end_transaction_id);


--
-- Name: ix_subcounty_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_subcounty_version_operation_type ON subcounty_version USING btree (operation_type);


--
-- Name: ix_subcounty_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_subcounty_version_transaction_id ON subcounty_version USING btree (transaction_id);


--
-- Name: ix_templatetype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_templatetype_name ON templatetype USING btree (name);


--
-- Name: ix_templatetype_template_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_templatetype_template_type ON templatetype USING btree (template_type);


--
-- Name: ix_templatetype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_templatetype_version_end_transaction_id ON templatetype_version USING btree (end_transaction_id);


--
-- Name: ix_templatetype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_templatetype_version_name ON templatetype_version USING btree (name);


--
-- Name: ix_templatetype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_templatetype_version_operation_type ON templatetype_version USING btree (operation_type);


--
-- Name: ix_templatetype_version_template_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_templatetype_version_template_type ON templatetype_version USING btree (template_type);


--
-- Name: ix_templatetype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_templatetype_version_transaction_id ON templatetype_version USING btree (transaction_id);


--
-- Name: ix_town_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_version_end_transaction_id ON town_version USING btree (end_transaction_id);


--
-- Name: ix_town_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_version_operation_type ON town_version USING btree (operation_type);


--
-- Name: ix_town_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_version_transaction_id ON town_version USING btree (transaction_id);


--
-- Name: ix_town_ward_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_ward_version_end_transaction_id ON town_ward_version USING btree (end_transaction_id);


--
-- Name: ix_town_ward_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_ward_version_operation_type ON town_ward_version USING btree (operation_type);


--
-- Name: ix_town_ward_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_ward_version_transaction_id ON town_ward_version USING btree (transaction_id);


--
-- Name: ix_town_ward_version_ward; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_ward_version_ward ON town_ward_version USING btree (ward);


--
-- Name: ix_town_ward_ward; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_town_ward_ward ON town_ward USING btree (ward);


--
-- Name: ix_transaction_user_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transaction_user_id ON transaction USING btree (user_id);


--
-- Name: ix_transcript_hearing; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transcript_hearing ON transcript USING btree (hearing);


--
-- Name: ix_transcript_search_vector; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transcript_search_vector ON transcript USING gin (search_vector);


--
-- Name: ix_transcript_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transcript_version_end_transaction_id ON transcript_version USING btree (end_transaction_id);


--
-- Name: ix_transcript_version_hearing; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transcript_version_hearing ON transcript_version USING btree (hearing);


--
-- Name: ix_transcript_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transcript_version_operation_type ON transcript_version USING btree (operation_type);


--
-- Name: ix_transcript_version_search_vector; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transcript_version_search_vector ON transcript_version USING gin (search_vector);


--
-- Name: ix_transcript_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_transcript_version_transaction_id ON transcript_version USING btree (transaction_id);


--
-- Name: ix_vehicle_police_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_vehicle_police_station ON vehicle USING btree (police_station);


--
-- Name: ix_vehicle_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_vehicle_version_end_transaction_id ON vehicle_version USING btree (end_transaction_id);


--
-- Name: ix_vehicle_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_vehicle_version_operation_type ON vehicle_version USING btree (operation_type);


--
-- Name: ix_vehicle_version_police_station; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_vehicle_version_police_station ON vehicle_version USING btree (police_station);


--
-- Name: ix_vehicle_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_vehicle_version_transaction_id ON vehicle_version USING btree (transaction_id);


--
-- Name: ix_ward_subcounty; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_ward_subcounty ON ward USING btree (subcounty);


--
-- Name: ix_ward_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_ward_version_end_transaction_id ON ward_version USING btree (end_transaction_id);


--
-- Name: ix_ward_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_ward_version_operation_type ON ward_version USING btree (operation_type);


--
-- Name: ix_ward_version_subcounty; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_ward_version_subcounty ON ward_version USING btree (subcounty);


--
-- Name: ix_ward_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_ward_version_transaction_id ON ward_version USING btree (transaction_id);


--
-- Name: ix_warranttype_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE UNIQUE INDEX ix_warranttype_name ON warranttype USING btree (name);


--
-- Name: ix_warranttype_version_end_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_warranttype_version_end_transaction_id ON warranttype_version USING btree (end_transaction_id);


--
-- Name: ix_warranttype_version_name; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_warranttype_version_name ON warranttype_version USING btree (name);


--
-- Name: ix_warranttype_version_operation_type; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_warranttype_version_operation_type ON warranttype_version USING btree (operation_type);


--
-- Name: ix_warranttype_version_transaction_id; Type: INDEX; Schema: public; Owner: nyimbi
--

CREATE INDEX ix_warranttype_version_transaction_id ON warranttype_version USING btree (transaction_id);


--
-- Name: document document_search_vector_trigger; Type: TRIGGER; Schema: public; Owner: nyimbi
--

CREATE TRIGGER document_search_vector_trigger BEFORE INSERT OR UPDATE ON document FOR EACH ROW EXECUTE PROCEDURE document_search_vector_update();


--
-- Name: document_version document_version_search_vector_trigger; Type: TRIGGER; Schema: public; Owner: nyimbi
--

CREATE TRIGGER document_version_search_vector_trigger BEFORE INSERT OR UPDATE ON document_version FOR EACH ROW EXECUTE PROCEDURE document_version_search_vector_update();


--
-- Name: exhibit exhibit_search_vector_trigger; Type: TRIGGER; Schema: public; Owner: nyimbi
--

CREATE TRIGGER exhibit_search_vector_trigger BEFORE INSERT OR UPDATE ON exhibit FOR EACH ROW EXECUTE PROCEDURE exhibit_search_vector_update();


--
-- Name: exhibit_version exhibit_version_search_vector_trigger; Type: TRIGGER; Schema: public; Owner: nyimbi
--

CREATE TRIGGER exhibit_version_search_vector_trigger BEFORE INSERT OR UPDATE ON exhibit_version FOR EACH ROW EXECUTE PROCEDURE exhibit_version_search_vector_update();


--
-- Name: transcript transcript_search_vector_trigger; Type: TRIGGER; Schema: public; Owner: nyimbi
--

CREATE TRIGGER transcript_search_vector_trigger BEFORE INSERT OR UPDATE ON transcript FOR EACH ROW EXECUTE PROCEDURE transcript_search_vector_update();


--
-- Name: transcript_version transcript_version_search_vector_trigger; Type: TRIGGER; Schema: public; Owner: nyimbi
--

CREATE TRIGGER transcript_version_search_vector_trigger BEFORE INSERT OR UPDATE ON transcript_version FOR EACH ROW EXECUTE PROCEDURE transcript_version_search_vector_update();


--
-- Name: ab_permission_view ab_permission_view_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission_view
    ADD CONSTRAINT ab_permission_view_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES ab_permission(id);


--
-- Name: ab_permission_view_role ab_permission_view_role_permission_view_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission_view_role
    ADD CONSTRAINT ab_permission_view_role_permission_view_id_fkey FOREIGN KEY (permission_view_id) REFERENCES ab_permission_view(id);


--
-- Name: ab_permission_view_role ab_permission_view_role_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission_view_role
    ADD CONSTRAINT ab_permission_view_role_role_id_fkey FOREIGN KEY (role_id) REFERENCES ab_role(id);


--
-- Name: ab_permission_view ab_permission_view_view_menu_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_permission_view
    ADD CONSTRAINT ab_permission_view_view_menu_id_fkey FOREIGN KEY (view_menu_id) REFERENCES ab_view_menu(id);


--
-- Name: ab_user ab_user_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user
    ADD CONSTRAINT ab_user_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: ab_user ab_user_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user
    ADD CONSTRAINT ab_user_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: ab_user_role ab_user_role_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user_role
    ADD CONSTRAINT ab_user_role_role_id_fkey FOREIGN KEY (role_id) REFERENCES ab_role(id);


--
-- Name: ab_user_role ab_user_role_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ab_user_role
    ADD CONSTRAINT ab_user_role_user_id_fkey FOREIGN KEY (user_id) REFERENCES ab_user(id);


--
-- Name: accounttype accounttype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY accounttype
    ADD CONSTRAINT accounttype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: accounttype accounttype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY accounttype
    ADD CONSTRAINT accounttype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: bill bill_assessing_registrar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_assessing_registrar_fkey FOREIGN KEY (assessing_registrar) REFERENCES judicialofficer(id);


--
-- Name: bill bill_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: bill bill_court_account_courts_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_court_account_courts_fkey FOREIGN KEY (court_account_courts, court_account_account__types) REFERENCES courtaccount(courts, account__types);


--
-- Name: bill bill_court_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_court_fkey FOREIGN KEY (court) REFERENCES court(id);


--
-- Name: bill bill_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: bill bill_documents_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_documents_fkey FOREIGN KEY (documents) REFERENCES document(id);


--
-- Name: bill bill_lawyer_paying_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_lawyer_paying_fkey FOREIGN KEY (lawyer_paying) REFERENCES lawyer(id);


--
-- Name: bill bill_party_paying_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_party_paying_fkey FOREIGN KEY (party_paying) REFERENCES party(id);


--
-- Name: bill bill_receiving_registrar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY bill
    ADD CONSTRAINT bill_receiving_registrar_fkey FOREIGN KEY (receiving_registrar) REFERENCES judicialofficer(id);


--
-- Name: billdetail billdetail_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY billdetail
    ADD CONSTRAINT billdetail_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: billdetail billdetail_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY billdetail
    ADD CONSTRAINT billdetail_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: billdetail billdetail_feetype_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY billdetail
    ADD CONSTRAINT billdetail_feetype_fkey FOREIGN KEY (feetype) REFERENCES feetype(id);


--
-- Name: billdetail billdetail_receipt_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY billdetail
    ADD CONSTRAINT billdetail_receipt_id_fkey FOREIGN KEY (receipt_id) REFERENCES bill(id);


--
-- Name: biodata biodata_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata
    ADD CONSTRAINT biodata_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: biodata biodata_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata
    ADD CONSTRAINT biodata_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: biodata biodata_economic_class_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata
    ADD CONSTRAINT biodata_economic_class_fkey FOREIGN KEY (economic_class) REFERENCES economicclass(id);


--
-- Name: biodata biodata_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata
    ADD CONSTRAINT biodata_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: biodata biodata_religion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY biodata
    ADD CONSTRAINT biodata_religion_fkey FOREIGN KEY (religion) REFERENCES religion(id);


--
-- Name: casecategory casecategory_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory
    ADD CONSTRAINT casecategory_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: casecategory_courtcase casecategory_courtcase_casecategory_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory_courtcase
    ADD CONSTRAINT casecategory_courtcase_casecategory_fkey FOREIGN KEY (casecategory) REFERENCES casecategory(id);


--
-- Name: casecategory_courtcase casecategory_courtcase_courtcase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory_courtcase
    ADD CONSTRAINT casecategory_courtcase_courtcase_fkey FOREIGN KEY (courtcase) REFERENCES courtcase(id);


--
-- Name: casecategory casecategory_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory
    ADD CONSTRAINT casecategory_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: casecategory casecategory_subcategory_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategory
    ADD CONSTRAINT casecategory_subcategory_fkey FOREIGN KEY (subcategory) REFERENCES casecategory(id);


--
-- Name: casecategorychecklist casecategorychecklist_case_categories_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategorychecklist
    ADD CONSTRAINT casecategorychecklist_case_categories_fkey FOREIGN KEY (case_categories) REFERENCES casecategory(id);


--
-- Name: casecategorychecklist casecategorychecklist_case_checklists_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casecategorychecklist
    ADD CONSTRAINT casecategorychecklist_case_checklists_fkey FOREIGN KEY (case_checklists) REFERENCES casechecklist(id);


--
-- Name: casechecklist casechecklist_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casechecklist
    ADD CONSTRAINT casechecklist_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: casechecklist casechecklist_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY casechecklist
    ADD CONSTRAINT casechecklist_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: caselinktype caselinktype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY caselinktype
    ADD CONSTRAINT caselinktype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: caselinktype caselinktype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY caselinktype
    ADD CONSTRAINT caselinktype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: celltype celltype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY celltype
    ADD CONSTRAINT celltype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: celltype celltype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY celltype
    ADD CONSTRAINT celltype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: commital commital_cell_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_cell_type_fkey FOREIGN KEY (cell_type) REFERENCES celltype(id);


--
-- Name: commital commital_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: commital commital_commital_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_commital_fkey FOREIGN KEY (commital) REFERENCES commital(id);


--
-- Name: commital commital_commital_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_commital_type_fkey FOREIGN KEY (commital_type) REFERENCES commitaltype(id);


--
-- Name: commital commital_court_case_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_court_case_fkey FOREIGN KEY (court_case) REFERENCES courtcase(id);


--
-- Name: commital commital_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: commital commital_parties_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_parties_fkey FOREIGN KEY (parties) REFERENCES party(id);


--
-- Name: commital commital_police_station_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_police_station_fkey FOREIGN KEY (police_station) REFERENCES policestation(id);


--
-- Name: commital commital_prisons_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_prisons_fkey FOREIGN KEY (prisons) REFERENCES prison(id);


--
-- Name: commital commital_receiving_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_receiving_officer_fkey FOREIGN KEY (receiving_officer) REFERENCES prisonofficer(id);


--
-- Name: commital commital_release_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_release_type_fkey FOREIGN KEY (release_type) REFERENCES releasetype(id);


--
-- Name: commital commital_releasing_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_releasing_officer_fkey FOREIGN KEY (releasing_officer) REFERENCES prisonofficer(id);


--
-- Name: commital commital_warrant_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commital
    ADD CONSTRAINT commital_warrant_type_fkey FOREIGN KEY (warrant_type) REFERENCES warranttype(id);


--
-- Name: commitaltype commitaltype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commitaltype
    ADD CONSTRAINT commitaltype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: commitaltype commitaltype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY commitaltype
    ADD CONSTRAINT commitaltype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: complaint complaint_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint
    ADD CONSTRAINT complaint_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: complaint_complaintcategory complaint_complaintcategory_complaint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_complaintcategory
    ADD CONSTRAINT complaint_complaintcategory_complaint_fkey FOREIGN KEY (complaint) REFERENCES complaint(id);


--
-- Name: complaint_complaintcategory complaint_complaintcategory_complaintcategory_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_complaintcategory
    ADD CONSTRAINT complaint_complaintcategory_complaintcategory_fkey FOREIGN KEY (complaintcategory) REFERENCES complaintcategory(id);


--
-- Name: complaint_courtcase complaint_courtcase_complaint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_courtcase
    ADD CONSTRAINT complaint_courtcase_complaint_fkey FOREIGN KEY (complaint) REFERENCES complaint(id);


--
-- Name: complaint_courtcase complaint_courtcase_courtcase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint_courtcase
    ADD CONSTRAINT complaint_courtcase_courtcase_fkey FOREIGN KEY (courtcase) REFERENCES courtcase(id);


--
-- Name: complaint complaint_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint
    ADD CONSTRAINT complaint_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: complaint complaint_evaluating_prosecutor_team_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint
    ADD CONSTRAINT complaint_evaluating_prosecutor_team_fkey FOREIGN KEY (evaluating_prosecutor_team) REFERENCES prosecutorteam(id);


--
-- Name: complaint complaint_police_station_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint
    ADD CONSTRAINT complaint_police_station_fkey FOREIGN KEY (police_station) REFERENCES policestation(id);


--
-- Name: complaint complaint_reported_to_judicial_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint
    ADD CONSTRAINT complaint_reported_to_judicial_officer_fkey FOREIGN KEY (reported_to_judicial_officer) REFERENCES judicialofficer(id);


--
-- Name: complaint complaint_reportingofficer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaint
    ADD CONSTRAINT complaint_reportingofficer_fkey FOREIGN KEY (reportingofficer) REFERENCES policeofficer(id);


--
-- Name: complaintcategory complaintcategory_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintcategory
    ADD CONSTRAINT complaintcategory_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: complaintcategory complaintcategory_complaint_category_parent_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintcategory
    ADD CONSTRAINT complaintcategory_complaint_category_parent_fkey FOREIGN KEY (complaint_category_parent) REFERENCES complaintcategory(id);


--
-- Name: complaintcategory complaintcategory_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintcategory
    ADD CONSTRAINT complaintcategory_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: complaintrole complaintrole_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintrole
    ADD CONSTRAINT complaintrole_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: complaintrole complaintrole_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY complaintrole
    ADD CONSTRAINT complaintrole_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: country country_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: country country_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: county county_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY county
    ADD CONSTRAINT county_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: county county_country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY county
    ADD CONSTRAINT county_country_fkey FOREIGN KEY (country) REFERENCES country(id);


--
-- Name: county county_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY county
    ADD CONSTRAINT county_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: court court_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court
    ADD CONSTRAINT court_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: court court_court_rank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court
    ADD CONSTRAINT court_court_rank_fkey FOREIGN KEY (court_rank) REFERENCES courtrank(id);


--
-- Name: court court_court_station_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court
    ADD CONSTRAINT court_court_station_fkey FOREIGN KEY (court_station) REFERENCES courtstation(id);


--
-- Name: court court_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court
    ADD CONSTRAINT court_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: court_judicialofficer court_judicialofficer_court_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court_judicialofficer
    ADD CONSTRAINT court_judicialofficer_court_fkey FOREIGN KEY (court) REFERENCES court(id);


--
-- Name: court_judicialofficer court_judicialofficer_judicialofficer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court_judicialofficer
    ADD CONSTRAINT court_judicialofficer_judicialofficer_fkey FOREIGN KEY (judicialofficer) REFERENCES judicialofficer(id);


--
-- Name: court court_town_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY court
    ADD CONSTRAINT court_town_fkey FOREIGN KEY (town) REFERENCES town(id);


--
-- Name: courtaccount courtaccount_account__types_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtaccount
    ADD CONSTRAINT courtaccount_account__types_fkey FOREIGN KEY (account__types) REFERENCES accounttype(id);


--
-- Name: courtaccount courtaccount_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtaccount
    ADD CONSTRAINT courtaccount_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: courtaccount courtaccount_courts_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtaccount
    ADD CONSTRAINT courtaccount_courts_fkey FOREIGN KEY (courts) REFERENCES court(id);


--
-- Name: courtaccount courtaccount_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtaccount
    ADD CONSTRAINT courtaccount_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: courtcase courtcase_case_link_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase
    ADD CONSTRAINT courtcase_case_link_type_fkey FOREIGN KEY (case_link_type) REFERENCES caselinktype(id);


--
-- Name: courtcase courtcase_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase
    ADD CONSTRAINT courtcase_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: courtcase courtcase_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase
    ADD CONSTRAINT courtcase_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: courtcase courtcase_filing_prosecutor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase
    ADD CONSTRAINT courtcase_filing_prosecutor_fkey FOREIGN KEY (filing_prosecutor) REFERENCES prosecutor(id);


--
-- Name: courtcase_judicialofficer courtcase_judicialofficer_courtcase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_judicialofficer
    ADD CONSTRAINT courtcase_judicialofficer_courtcase_fkey FOREIGN KEY (courtcase) REFERENCES courtcase(id);


--
-- Name: courtcase_judicialofficer courtcase_judicialofficer_judicialofficer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_judicialofficer
    ADD CONSTRAINT courtcase_judicialofficer_judicialofficer_fkey FOREIGN KEY (judicialofficer) REFERENCES judicialofficer(id);


--
-- Name: courtcase_lawfirm courtcase_lawfirm_courtcase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_lawfirm
    ADD CONSTRAINT courtcase_lawfirm_courtcase_fkey FOREIGN KEY (courtcase) REFERENCES courtcase(id);


--
-- Name: courtcase_lawfirm courtcase_lawfirm_lawfirm_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase_lawfirm
    ADD CONSTRAINT courtcase_lawfirm_lawfirm_fkey FOREIGN KEY (lawfirm) REFERENCES lawfirm(id);


--
-- Name: courtcase courtcase_linked_cases_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase
    ADD CONSTRAINT courtcase_linked_cases_fkey FOREIGN KEY (linked_cases) REFERENCES courtcase(id);


--
-- Name: courtcase courtcase_pretrial_registrar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtcase
    ADD CONSTRAINT courtcase_pretrial_registrar_fkey FOREIGN KEY (pretrial_registrar) REFERENCES judicialofficer(id);


--
-- Name: courtrank courtrank_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtrank
    ADD CONSTRAINT courtrank_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: courtrank courtrank_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtrank
    ADD CONSTRAINT courtrank_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: courtstation courtstation_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtstation
    ADD CONSTRAINT courtstation_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: courtstation courtstation_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY courtstation
    ADD CONSTRAINT courtstation_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: crime crime_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY crime
    ADD CONSTRAINT crime_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: crime crime_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY crime
    ADD CONSTRAINT crime_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: crime crime_ref_law_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY crime
    ADD CONSTRAINT crime_ref_law_fkey FOREIGN KEY (ref_law) REFERENCES law(id);


--
-- Name: csi_equipment csi_equipment_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment
    ADD CONSTRAINT csi_equipment_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: csi_equipment csi_equipment_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment
    ADD CONSTRAINT csi_equipment_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: csi_equipment_investigationdiary csi_equipment_investigationdiary_csi_equipment_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment_investigationdiary
    ADD CONSTRAINT csi_equipment_investigationdiary_csi_equipment_fkey FOREIGN KEY (csi_equipment) REFERENCES csi_equipment(id);


--
-- Name: csi_equipment_investigationdiary csi_equipment_investigationdiary_investigationdiary_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY csi_equipment_investigationdiary
    ADD CONSTRAINT csi_equipment_investigationdiary_investigationdiary_fkey FOREIGN KEY (investigationdiary) REFERENCES investigationdiary(id);


--
-- Name: diagram diagram_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY diagram
    ADD CONSTRAINT diagram_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: diagram diagram_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY diagram
    ADD CONSTRAINT diagram_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: diagram diagram_investigation_diary_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY diagram
    ADD CONSTRAINT diagram_investigation_diary_fkey FOREIGN KEY (investigation_diary) REFERENCES investigationdiary(id);


--
-- Name: discipline discipline_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY discipline
    ADD CONSTRAINT discipline_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: discipline discipline_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY discipline
    ADD CONSTRAINT discipline_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: discipline discipline_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY discipline
    ADD CONSTRAINT discipline_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: discipline discipline_prison_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY discipline
    ADD CONSTRAINT discipline_prison_officer_fkey FOREIGN KEY (prison_officer) REFERENCES prisonofficer(id);


--
-- Name: doctemplate doctemplate_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY doctemplate
    ADD CONSTRAINT doctemplate_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: doctemplate doctemplate_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY doctemplate
    ADD CONSTRAINT doctemplate_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: doctemplate doctemplate_template_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY doctemplate
    ADD CONSTRAINT doctemplate_template_type_fkey FOREIGN KEY (template_type) REFERENCES templatetype(id);


--
-- Name: document document_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document
    ADD CONSTRAINT document_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: document document_court_case_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document
    ADD CONSTRAINT document_court_case_fkey FOREIGN KEY (court_case) REFERENCES courtcase(id);


--
-- Name: document document_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document
    ADD CONSTRAINT document_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: document document_doc_template_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document
    ADD CONSTRAINT document_doc_template_fkey FOREIGN KEY (doc_template) REFERENCES doctemplate(id);


--
-- Name: document_documenttype document_documenttype_document_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document_documenttype
    ADD CONSTRAINT document_documenttype_document_fkey FOREIGN KEY (document) REFERENCES document(id);


--
-- Name: document_documenttype document_documenttype_documenttype_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document_documenttype
    ADD CONSTRAINT document_documenttype_documenttype_fkey FOREIGN KEY (documenttype) REFERENCES documenttype(id);


--
-- Name: document document_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document
    ADD CONSTRAINT document_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: document document_judicial_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY document
    ADD CONSTRAINT document_judicial_officer_fkey FOREIGN KEY (judicial_officer) REFERENCES judicialofficer(id);


--
-- Name: documenttype documenttype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY documenttype
    ADD CONSTRAINT documenttype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: documenttype documenttype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY documenttype
    ADD CONSTRAINT documenttype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: economicclass economicclass_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY economicclass
    ADD CONSTRAINT economicclass_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: economicclass economicclass_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY economicclass
    ADD CONSTRAINT economicclass_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: exhibit exhibit_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY exhibit
    ADD CONSTRAINT exhibit_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: exhibit exhibit_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY exhibit
    ADD CONSTRAINT exhibit_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: exhibit exhibit_investigation_entry_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY exhibit
    ADD CONSTRAINT exhibit_investigation_entry_fkey FOREIGN KEY (investigation_entry) REFERENCES investigationdiary(id);


--
-- Name: exhibit exhibit_seizure_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY exhibit
    ADD CONSTRAINT exhibit_seizure_fkey FOREIGN KEY (seizure) REFERENCES seizure(id);


--
-- Name: expert expert_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert
    ADD CONSTRAINT expert_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: expert expert_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert
    ADD CONSTRAINT expert_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: expert_experttype expert_experttype_expert_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert_experttype
    ADD CONSTRAINT expert_experttype_expert_fkey FOREIGN KEY (expert) REFERENCES expert(id);


--
-- Name: expert_experttype expert_experttype_experttype_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY expert_experttype
    ADD CONSTRAINT expert_experttype_experttype_fkey FOREIGN KEY (experttype) REFERENCES experttype(id);


--
-- Name: experttestimony experttestimony_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony
    ADD CONSTRAINT experttestimony_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: experttestimony experttestimony_court_case_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony
    ADD CONSTRAINT experttestimony_court_case_fkey FOREIGN KEY (court_case) REFERENCES courtcase(id);


--
-- Name: experttestimony experttestimony_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony
    ADD CONSTRAINT experttestimony_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: experttestimony experttestimony_experts_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony
    ADD CONSTRAINT experttestimony_experts_fkey FOREIGN KEY (experts) REFERENCES expert(id);


--
-- Name: experttestimony experttestimony_investigation_entries_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony
    ADD CONSTRAINT experttestimony_investigation_entries_fkey FOREIGN KEY (investigation_entries) REFERENCES investigationdiary(id);


--
-- Name: experttestimony experttestimony_requesting_police_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttestimony
    ADD CONSTRAINT experttestimony_requesting_police_officer_fkey FOREIGN KEY (requesting_police_officer) REFERENCES policeofficer(id);


--
-- Name: experttype experttype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttype
    ADD CONSTRAINT experttype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: experttype experttype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttype
    ADD CONSTRAINT experttype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: experttype experttype_expert_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY experttype
    ADD CONSTRAINT experttype_expert_type_fkey FOREIGN KEY (expert_type) REFERENCES experttype(id);


--
-- Name: feeclass feeclass_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feeclass
    ADD CONSTRAINT feeclass_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: feeclass feeclass_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feeclass
    ADD CONSTRAINT feeclass_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: feeclass feeclass_fee_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feeclass
    ADD CONSTRAINT feeclass_fee_type_fkey FOREIGN KEY (fee_type) REFERENCES feeclass(id);


--
-- Name: feetype feetype_account_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feetype
    ADD CONSTRAINT feetype_account_type_fkey FOREIGN KEY (account_type) REFERENCES accounttype(id);


--
-- Name: feetype feetype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feetype
    ADD CONSTRAINT feetype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: feetype feetype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feetype
    ADD CONSTRAINT feetype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: feetype feetype_filing_fee_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY feetype
    ADD CONSTRAINT feetype_filing_fee_type_fkey FOREIGN KEY (filing_fee_type) REFERENCES feeclass(id);


--
-- Name: healthevent healthevent_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent
    ADD CONSTRAINT healthevent_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: healthevent healthevent_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent
    ADD CONSTRAINT healthevent_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: healthevent healthevent_health_event_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent
    ADD CONSTRAINT healthevent_health_event_type_fkey FOREIGN KEY (health_event_type) REFERENCES healtheventtype(id);


--
-- Name: healthevent healthevent_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent
    ADD CONSTRAINT healthevent_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: healthevent healthevent_reporting_prison_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healthevent
    ADD CONSTRAINT healthevent_reporting_prison_officer_fkey FOREIGN KEY (reporting_prison_officer) REFERENCES prisonofficer(id);


--
-- Name: healtheventtype healtheventtype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healtheventtype
    ADD CONSTRAINT healtheventtype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: healtheventtype healtheventtype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY healtheventtype
    ADD CONSTRAINT healtheventtype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: hearing hearing_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing
    ADD CONSTRAINT hearing_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: hearing hearing_court_cases_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing
    ADD CONSTRAINT hearing_court_cases_fkey FOREIGN KEY (court_cases) REFERENCES courtcase(id);


--
-- Name: hearing hearing_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing
    ADD CONSTRAINT hearing_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: hearing hearing_hearing_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing
    ADD CONSTRAINT hearing_hearing_type_fkey FOREIGN KEY (hearing_type) REFERENCES hearingtype(id);


--
-- Name: hearing_issue hearing_issue_hearing_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_issue
    ADD CONSTRAINT hearing_issue_hearing_fkey FOREIGN KEY (hearing) REFERENCES hearing(id);


--
-- Name: hearing_issue hearing_issue_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_issue
    ADD CONSTRAINT hearing_issue_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: hearing_judicialofficer hearing_judicialofficer_hearing_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_judicialofficer
    ADD CONSTRAINT hearing_judicialofficer_hearing_fkey FOREIGN KEY (hearing) REFERENCES hearing(id);


--
-- Name: hearing_judicialofficer hearing_judicialofficer_judicialofficer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_judicialofficer
    ADD CONSTRAINT hearing_judicialofficer_judicialofficer_fkey FOREIGN KEY (judicialofficer) REFERENCES judicialofficer(id);


--
-- Name: hearing_lawfirm_2 hearing_lawfirm_2_hearing_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm_2
    ADD CONSTRAINT hearing_lawfirm_2_hearing_fkey FOREIGN KEY (hearing) REFERENCES hearing(id);


--
-- Name: hearing_lawfirm_2 hearing_lawfirm_2_lawfirm_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm_2
    ADD CONSTRAINT hearing_lawfirm_2_lawfirm_fkey FOREIGN KEY (lawfirm) REFERENCES lawfirm(id);


--
-- Name: hearing_lawfirm hearing_lawfirm_hearing_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm
    ADD CONSTRAINT hearing_lawfirm_hearing_fkey FOREIGN KEY (hearing) REFERENCES hearing(id);


--
-- Name: hearing_lawfirm hearing_lawfirm_lawfirm_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing_lawfirm
    ADD CONSTRAINT hearing_lawfirm_lawfirm_fkey FOREIGN KEY (lawfirm) REFERENCES lawfirm(id);


--
-- Name: hearing hearing_schedule_status_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearing
    ADD CONSTRAINT hearing_schedule_status_fkey FOREIGN KEY (schedule_status) REFERENCES schedulestatustype(id);


--
-- Name: hearingtype hearingtype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearingtype
    ADD CONSTRAINT hearingtype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: hearingtype hearingtype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearingtype
    ADD CONSTRAINT hearingtype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: hearingtype hearingtype_hearing_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY hearingtype
    ADD CONSTRAINT hearingtype_hearing_type_fkey FOREIGN KEY (hearing_type) REFERENCES hearingtype(id);


--
-- Name: instancecrime instancecrime_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime
    ADD CONSTRAINT instancecrime_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: instancecrime instancecrime_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime
    ADD CONSTRAINT instancecrime_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: instancecrime instancecrime_crimes_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime
    ADD CONSTRAINT instancecrime_crimes_fkey FOREIGN KEY (crimes) REFERENCES crime(id);


--
-- Name: instancecrime_issue instancecrime_issue_instancecrime_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime_issue
    ADD CONSTRAINT instancecrime_issue_instancecrime_fkey FOREIGN KEY (instancecrime) REFERENCES instancecrime(id);


--
-- Name: instancecrime_issue instancecrime_issue_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime_issue
    ADD CONSTRAINT instancecrime_issue_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: instancecrime instancecrime_parties_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY instancecrime
    ADD CONSTRAINT instancecrime_parties_fkey FOREIGN KEY (parties) REFERENCES party(id);


--
-- Name: interview interview_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY interview
    ADD CONSTRAINT interview_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: interview interview_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY interview
    ADD CONSTRAINT interview_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: interview interview_investigation_entry_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY interview
    ADD CONSTRAINT interview_investigation_entry_fkey FOREIGN KEY (investigation_entry) REFERENCES investigationdiary(id);


--
-- Name: investigationdiary investigationdiary_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary
    ADD CONSTRAINT investigationdiary_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: investigationdiary investigationdiary_complaint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary
    ADD CONSTRAINT investigationdiary_complaint_fkey FOREIGN KEY (complaint) REFERENCES complaint(id);


--
-- Name: investigationdiary investigationdiary_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary
    ADD CONSTRAINT investigationdiary_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: investigationdiary_party investigationdiary_party_investigationdiary_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_party
    ADD CONSTRAINT investigationdiary_party_investigationdiary_fkey FOREIGN KEY (investigationdiary) REFERENCES investigationdiary(id);


--
-- Name: investigationdiary_party investigationdiary_party_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_party
    ADD CONSTRAINT investigationdiary_party_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: investigationdiary_policeofficer investigationdiary_policeofficer_investigationdiary_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_policeofficer
    ADD CONSTRAINT investigationdiary_policeofficer_investigationdiary_fkey FOREIGN KEY (investigationdiary) REFERENCES investigationdiary(id);


--
-- Name: investigationdiary_policeofficer investigationdiary_policeofficer_policeofficer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_policeofficer
    ADD CONSTRAINT investigationdiary_policeofficer_policeofficer_fkey FOREIGN KEY (policeofficer) REFERENCES policeofficer(id);


--
-- Name: investigationdiary_vehicle investigationdiary_vehicle_investigationdiary_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_vehicle
    ADD CONSTRAINT investigationdiary_vehicle_investigationdiary_fkey FOREIGN KEY (investigationdiary) REFERENCES investigationdiary(id);


--
-- Name: investigationdiary_vehicle investigationdiary_vehicle_vehicle_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary_vehicle
    ADD CONSTRAINT investigationdiary_vehicle_vehicle_fkey FOREIGN KEY (vehicle) REFERENCES vehicle(id);


--
-- Name: investigationdiary investigationdiary_warrant_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY investigationdiary
    ADD CONSTRAINT investigationdiary_warrant_type_fkey FOREIGN KEY (warrant_type) REFERENCES warranttype(id);


--
-- Name: issue issue_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue
    ADD CONSTRAINT issue_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: issue issue_court_case_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue
    ADD CONSTRAINT issue_court_case_fkey FOREIGN KEY (court_case) REFERENCES courtcase(id);


--
-- Name: issue issue_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue
    ADD CONSTRAINT issue_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: issue issue_defense_lawyer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue
    ADD CONSTRAINT issue_defense_lawyer_fkey FOREIGN KEY (defense_lawyer) REFERENCES lawyer(id);


--
-- Name: issue issue_judicial_officer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue
    ADD CONSTRAINT issue_judicial_officer_fkey FOREIGN KEY (judicial_officer) REFERENCES judicialofficer(id);


--
-- Name: issue_lawyer issue_lawyer_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_lawyer
    ADD CONSTRAINT issue_lawyer_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: issue_lawyer issue_lawyer_lawyer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_lawyer
    ADD CONSTRAINT issue_lawyer_lawyer_fkey FOREIGN KEY (lawyer) REFERENCES lawyer(id);


--
-- Name: issue_legalreference_2 issue_legalreference_2_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference_2
    ADD CONSTRAINT issue_legalreference_2_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: issue_legalreference_2 issue_legalreference_2_legalreference_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference_2
    ADD CONSTRAINT issue_legalreference_2_legalreference_fkey FOREIGN KEY (legalreference) REFERENCES legalreference(id);


--
-- Name: issue_legalreference issue_legalreference_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference
    ADD CONSTRAINT issue_legalreference_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: issue_legalreference issue_legalreference_legalreference_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_legalreference
    ADD CONSTRAINT issue_legalreference_legalreference_fkey FOREIGN KEY (legalreference) REFERENCES legalreference(id);


--
-- Name: issue_party_2 issue_party_2_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party_2
    ADD CONSTRAINT issue_party_2_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: issue_party_2 issue_party_2_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party_2
    ADD CONSTRAINT issue_party_2_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: issue_party issue_party_issue_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party
    ADD CONSTRAINT issue_party_issue_fkey FOREIGN KEY (issue) REFERENCES issue(id);


--
-- Name: issue_party issue_party_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue_party
    ADD CONSTRAINT issue_party_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: issue issue_prosecutor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY issue
    ADD CONSTRAINT issue_prosecutor_fkey FOREIGN KEY (prosecutor) REFERENCES prosecutor(id);


--
-- Name: judicialofficer judicialofficer_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer
    ADD CONSTRAINT judicialofficer_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: judicialofficer judicialofficer_court_station_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer
    ADD CONSTRAINT judicialofficer_court_station_fkey FOREIGN KEY (court_station) REFERENCES courtstation(id);


--
-- Name: judicialofficer judicialofficer_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer
    ADD CONSTRAINT judicialofficer_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: judicialofficer judicialofficer_judicial_role_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer
    ADD CONSTRAINT judicialofficer_judicial_role_fkey FOREIGN KEY (judicial_role) REFERENCES judicialrole(id);


--
-- Name: judicialofficer judicialofficer_rank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialofficer
    ADD CONSTRAINT judicialofficer_rank_fkey FOREIGN KEY (rank) REFERENCES judicialrank(id);


--
-- Name: judicialrank judicialrank_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrank
    ADD CONSTRAINT judicialrank_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: judicialrank judicialrank_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrank
    ADD CONSTRAINT judicialrank_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: judicialrole judicialrole_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrole
    ADD CONSTRAINT judicialrole_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: judicialrole judicialrole_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY judicialrole
    ADD CONSTRAINT judicialrole_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: law law_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY law
    ADD CONSTRAINT law_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: law law_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY law
    ADD CONSTRAINT law_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: lawfirm lawfirm_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawfirm
    ADD CONSTRAINT lawfirm_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: lawfirm lawfirm_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawfirm
    ADD CONSTRAINT lawfirm_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: lawyer lawyer_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer
    ADD CONSTRAINT lawyer_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: lawyer lawyer_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer
    ADD CONSTRAINT lawyer_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: lawyer lawyer_law_firm_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer
    ADD CONSTRAINT lawyer_law_firm_fkey FOREIGN KEY (law_firm) REFERENCES lawfirm(id);


--
-- Name: lawyer_party lawyer_party_lawyer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer_party
    ADD CONSTRAINT lawyer_party_lawyer_fkey FOREIGN KEY (lawyer) REFERENCES lawyer(id);


--
-- Name: lawyer_party lawyer_party_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY lawyer_party
    ADD CONSTRAINT lawyer_party_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: legalreference legalreference_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY legalreference
    ADD CONSTRAINT legalreference_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: legalreference legalreference_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY legalreference
    ADD CONSTRAINT legalreference_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: nextofkin nextofkin_biodata_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY nextofkin
    ADD CONSTRAINT nextofkin_biodata_fkey FOREIGN KEY (biodata) REFERENCES biodata(id);


--
-- Name: nextofkin nextofkin_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY nextofkin
    ADD CONSTRAINT nextofkin_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: nextofkin nextofkin_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY nextofkin
    ADD CONSTRAINT nextofkin_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: notification notification_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notification
    ADD CONSTRAINT notification_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: notification notification_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notification
    ADD CONSTRAINT notification_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: notification notification_notification_register_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notification
    ADD CONSTRAINT notification_notification_register_fkey FOREIGN KEY (notification_register) REFERENCES notificationregister(id);


--
-- Name: notificationregister notificationregister_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: notificationregister notificationregister_complaint_category_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_complaint_category_fkey FOREIGN KEY (complaint_category) REFERENCES complaintcategory(id);


--
-- Name: notificationregister notificationregister_complaint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_complaint_fkey FOREIGN KEY (complaint) REFERENCES complaint(id);


--
-- Name: notificationregister notificationregister_court_case_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_court_case_fkey FOREIGN KEY (court_case) REFERENCES courtcase(id);


--
-- Name: notificationregister notificationregister_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: notificationregister notificationregister_document_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_document_fkey FOREIGN KEY (document) REFERENCES document(id);


--
-- Name: notificationregister notificationregister_health_event_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_health_event_fkey FOREIGN KEY (health_event) REFERENCES healthevent(id);


--
-- Name: notificationregister notificationregister_hearing_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_hearing_fkey FOREIGN KEY (hearing) REFERENCES hearing(id);


--
-- Name: notificationregister notificationregister_notification_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_notification_type_fkey FOREIGN KEY (notification_type) REFERENCES notificationtype(id);


--
-- Name: notificationregister notificationregister_notify_event_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_notify_event_fkey FOREIGN KEY (notify_event) REFERENCES notifyevent(id);


--
-- Name: notificationregister notificationregister_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationregister
    ADD CONSTRAINT notificationregister_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: notificationtype notificationtype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationtype
    ADD CONSTRAINT notificationtype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: notificationtype notificationtype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notificationtype
    ADD CONSTRAINT notificationtype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: notifyevent notifyevent_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notifyevent
    ADD CONSTRAINT notifyevent_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: notifyevent notifyevent_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY notifyevent
    ADD CONSTRAINT notifyevent_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: page page_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY page
    ADD CONSTRAINT page_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: page page_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY page
    ADD CONSTRAINT page_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: page page_document_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY page
    ADD CONSTRAINT page_document_fkey FOREIGN KEY (document) REFERENCES document(id);


--
-- Name: party party_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party
    ADD CONSTRAINT party_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: party party_complaint_role_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party
    ADD CONSTRAINT party_complaint_role_fkey FOREIGN KEY (complaint_role) REFERENCES complaintrole(id);


--
-- Name: party party_complaints_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party
    ADD CONSTRAINT party_complaints_fkey FOREIGN KEY (complaints) REFERENCES complaint(id);


--
-- Name: party party_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party
    ADD CONSTRAINT party_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: party party_party_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party
    ADD CONSTRAINT party_party_type_fkey FOREIGN KEY (party_type) REFERENCES partytype(id);


--
-- Name: party party_relative_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party
    ADD CONSTRAINT party_relative_fkey FOREIGN KEY (relative) REFERENCES party(id);


--
-- Name: party_settlement party_settlement_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party_settlement
    ADD CONSTRAINT party_settlement_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: party_settlement party_settlement_settlement_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY party_settlement
    ADD CONSTRAINT party_settlement_settlement_fkey FOREIGN KEY (settlement) REFERENCES settlement(id);


--
-- Name: partytype partytype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY partytype
    ADD CONSTRAINT partytype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: partytype partytype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY partytype
    ADD CONSTRAINT partytype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: payment payment_bill_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY payment
    ADD CONSTRAINT payment_bill_fkey FOREIGN KEY (bill) REFERENCES bill(id);


--
-- Name: payment payment_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY payment
    ADD CONSTRAINT payment_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: payment payment_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY payment
    ADD CONSTRAINT payment_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: personaleffect personaleffect_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffect
    ADD CONSTRAINT personaleffect_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: personaleffect personaleffect_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffect
    ADD CONSTRAINT personaleffect_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: personaleffect personaleffect_party_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffect
    ADD CONSTRAINT personaleffect_party_fkey FOREIGN KEY (party) REFERENCES party(id);


--
-- Name: personaleffect personaleffect_personal_effects_category_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffect
    ADD CONSTRAINT personaleffect_personal_effects_category_fkey FOREIGN KEY (personal_effects_category) REFERENCES personaleffectscategory(id);


--
-- Name: personaleffectscategory personaleffectscategory_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffectscategory
    ADD CONSTRAINT personaleffectscategory_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: personaleffectscategory personaleffectscategory_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY personaleffectscategory
    ADD CONSTRAINT personaleffectscategory_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: policeofficer policeofficer_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer
    ADD CONSTRAINT policeofficer_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: policeofficer policeofficer_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer
    ADD CONSTRAINT policeofficer_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: policeofficer policeofficer_police_rank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer
    ADD CONSTRAINT policeofficer_police_rank_fkey FOREIGN KEY (police_rank) REFERENCES policeofficerrank(id);


--
-- Name: policeofficer_policestation policeofficer_policestation_policeofficer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer_policestation
    ADD CONSTRAINT policeofficer_policestation_policeofficer_fkey FOREIGN KEY (policeofficer) REFERENCES policeofficer(id);


--
-- Name: policeofficer_policestation policeofficer_policestation_policestation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficer_policestation
    ADD CONSTRAINT policeofficer_policestation_policestation_fkey FOREIGN KEY (policestation) REFERENCES policestation(id);


--
-- Name: policeofficerrank policeofficerrank_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficerrank
    ADD CONSTRAINT policeofficerrank_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: policeofficerrank policeofficerrank_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policeofficerrank
    ADD CONSTRAINT policeofficerrank_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: policestation policestation_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation
    ADD CONSTRAINT policestation_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: policestation policestation_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation
    ADD CONSTRAINT policestation_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: policestation policestation_officer_commanding_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation
    ADD CONSTRAINT policestation_officer_commanding_fkey FOREIGN KEY (officer_commanding) REFERENCES policeofficer(id);


--
-- Name: policestation policestation_police_station_rank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation
    ADD CONSTRAINT policestation_police_station_rank_fkey FOREIGN KEY (police_station_rank) REFERENCES policestationrank(id);


--
-- Name: policestation policestation_town_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestation
    ADD CONSTRAINT policestation_town_fkey FOREIGN KEY (town) REFERENCES town(id);


--
-- Name: policestationrank policestationrank_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestationrank
    ADD CONSTRAINT policestationrank_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: policestationrank policestationrank_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY policestationrank
    ADD CONSTRAINT policestationrank_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: prison prison_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prison
    ADD CONSTRAINT prison_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: prison prison_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prison
    ADD CONSTRAINT prison_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: prison prison_town_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prison
    ADD CONSTRAINT prison_town_fkey FOREIGN KEY (town) REFERENCES town(id);


--
-- Name: prisonofficer prisonofficer_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficer
    ADD CONSTRAINT prisonofficer_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: prisonofficer prisonofficer_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficer
    ADD CONSTRAINT prisonofficer_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: prisonofficer prisonofficer_prison_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficer
    ADD CONSTRAINT prisonofficer_prison_fkey FOREIGN KEY (prison) REFERENCES prison(id);


--
-- Name: prisonofficer prisonofficer_prison_officer_rank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficer
    ADD CONSTRAINT prisonofficer_prison_officer_rank_fkey FOREIGN KEY (prison_officer_rank) REFERENCES prisonofficerrank(id);


--
-- Name: prisonofficerrank prisonofficerrank_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficerrank
    ADD CONSTRAINT prisonofficerrank_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: prisonofficerrank prisonofficerrank_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prisonofficerrank
    ADD CONSTRAINT prisonofficerrank_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: prosecutor prosecutor_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutor
    ADD CONSTRAINT prosecutor_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: prosecutor prosecutor_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutor
    ADD CONSTRAINT prosecutor_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: prosecutor prosecutor_lawyer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutor
    ADD CONSTRAINT prosecutor_lawyer_fkey FOREIGN KEY (lawyer) REFERENCES lawyer(id);


--
-- Name: prosecutor prosecutor_prosecutor_team_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutor
    ADD CONSTRAINT prosecutor_prosecutor_team_fkey FOREIGN KEY (prosecutor_team) REFERENCES prosecutorteam(id);


--
-- Name: prosecutorteam prosecutorteam_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutorteam
    ADD CONSTRAINT prosecutorteam_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: prosecutorteam prosecutorteam_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY prosecutorteam
    ADD CONSTRAINT prosecutorteam_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: releasetype releasetype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY releasetype
    ADD CONSTRAINT releasetype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: releasetype releasetype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY releasetype
    ADD CONSTRAINT releasetype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: religion religion_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY religion
    ADD CONSTRAINT religion_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: religion religion_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY religion
    ADD CONSTRAINT religion_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: schedulestatustype schedulestatustype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY schedulestatustype
    ADD CONSTRAINT schedulestatustype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: schedulestatustype schedulestatustype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY schedulestatustype
    ADD CONSTRAINT schedulestatustype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: seizure seizure_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY seizure
    ADD CONSTRAINT seizure_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: seizure seizure_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY seizure
    ADD CONSTRAINT seizure_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: seizure seizure_investigation_diary_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY seizure
    ADD CONSTRAINT seizure_investigation_diary_fkey FOREIGN KEY (investigation_diary) REFERENCES investigationdiary(id);


--
-- Name: seizure seizure_recovery_town_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY seizure
    ADD CONSTRAINT seizure_recovery_town_fkey FOREIGN KEY (recovery_town) REFERENCES town(id);


--
-- Name: settlement settlement_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY settlement
    ADD CONSTRAINT settlement_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: settlement settlement_complaint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY settlement
    ADD CONSTRAINT settlement_complaint_fkey FOREIGN KEY (complaint) REFERENCES complaint(id);


--
-- Name: settlement settlement_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY settlement
    ADD CONSTRAINT settlement_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: settlement settlement_settlor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY settlement
    ADD CONSTRAINT settlement_settlor_fkey FOREIGN KEY (settlor) REFERENCES party(id);


--
-- Name: subcounty subcounty_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY subcounty
    ADD CONSTRAINT subcounty_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: subcounty subcounty_county_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY subcounty
    ADD CONSTRAINT subcounty_county_fkey FOREIGN KEY (county) REFERENCES county(id);


--
-- Name: subcounty subcounty_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY subcounty
    ADD CONSTRAINT subcounty_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: templatetype templatetype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY templatetype
    ADD CONSTRAINT templatetype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: templatetype templatetype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY templatetype
    ADD CONSTRAINT templatetype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: templatetype templatetype_template_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY templatetype
    ADD CONSTRAINT templatetype_template_type_fkey FOREIGN KEY (template_type) REFERENCES templatetype(id);


--
-- Name: town town_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town
    ADD CONSTRAINT town_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: town town_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town
    ADD CONSTRAINT town_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: town_ward town_ward_town_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town_ward
    ADD CONSTRAINT town_ward_town_fkey FOREIGN KEY (town) REFERENCES town(id);


--
-- Name: town_ward town_ward_ward_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY town_ward
    ADD CONSTRAINT town_ward_ward_fkey FOREIGN KEY (ward) REFERENCES ward(id);


--
-- Name: transaction transaction_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transaction
    ADD CONSTRAINT transaction_user_id_fkey FOREIGN KEY (user_id) REFERENCES ab_user(id);


--
-- Name: transcript transcript_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transcript
    ADD CONSTRAINT transcript_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: transcript transcript_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transcript
    ADD CONSTRAINT transcript_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: transcript transcript_hearing_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY transcript
    ADD CONSTRAINT transcript_hearing_fkey FOREIGN KEY (hearing) REFERENCES hearing(id);


--
-- Name: vehicle vehicle_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY vehicle
    ADD CONSTRAINT vehicle_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: vehicle vehicle_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY vehicle
    ADD CONSTRAINT vehicle_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: vehicle vehicle_police_station_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY vehicle
    ADD CONSTRAINT vehicle_police_station_fkey FOREIGN KEY (police_station) REFERENCES policestation(id);


--
-- Name: ward ward_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ward
    ADD CONSTRAINT ward_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: ward ward_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ward
    ADD CONSTRAINT ward_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- Name: ward ward_subcounty_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY ward
    ADD CONSTRAINT ward_subcounty_fkey FOREIGN KEY (subcounty) REFERENCES subcounty(id);


--
-- Name: warranttype warranttype_changed_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY warranttype
    ADD CONSTRAINT warranttype_changed_by_fk_fkey FOREIGN KEY (changed_by_fk) REFERENCES ab_user(id);


--
-- Name: warranttype warranttype_created_by_fk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nyimbi
--

ALTER TABLE ONLY warranttype
    ADD CONSTRAINT warranttype_created_by_fk_fkey FOREIGN KEY (created_by_fk) REFERENCES ab_user(id);


--
-- PostgreSQL database dump complete
--

