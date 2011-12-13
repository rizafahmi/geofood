--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Name: maps_foodlocation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('maps_foodlocation_id_seq', 6, true);


--
-- Data for Name: maps_foodlocation; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO maps_foodlocation VALUES (3, 'resto-lantai-1', '', 'Mall Central Park, Jakarta Barat, jakarta, indonesia', 'Jakarta Barat, Jakarta Capital Region, Indonesia', '', '', -6.15849720000000023, 106.747053600000001, '0101000020E6100000730E9E094DA218C0259694BBCFAF5A40');
INSERT INTO maps_foodlocation VALUES (4, 'lumut-cafe-and-gallery', '', 'Jalan Danau Tamblingan 166, Sanur, Bali', 'Jalan Danau Tamblingan, Denpasar, Indonesia', '', '', -8.69581559999999953, 115.2636526, '0101000020E61000002C11A8FE416421C0821FD5B0DFD05C40');
INSERT INTO maps_foodlocation VALUES (6, 'santap-rendang-hitam-lezat-di-bali', 'http://www.okefood.com/read/2011/11/14/301/529044/santap-rendang-hitam-lezat-di-bali', 'Jalan Danau Tamblingan 166, Sanur, Bali', 'Jalan Danau Tamblingan, Denpasar, Indonesia', '', '', -8.69581559999999953, 115.2636526, '0101000020E61000002C11A8FE416421C0821FD5B0DFD05C40');
INSERT INTO maps_foodlocation VALUES (1, 'roti-bakar-edi', '', 'Jalan Raden Patah, Kebayoran Baru, Jakarta', 'Jalan Raden Patah, Jakarta Capital Region 12120', '', '', -6.23779699999999959, 106.8001, '0101000020E6100000FF58880E81F318C0E561A1D634B35A40');


--
-- PostgreSQL database dump complete
--

