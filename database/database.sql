PGDMP     4    "                r            movie_ticket    9.3.4    9.3.4    O	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            P	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            Q	           1262    70042    movie_ticket    DATABASE     ~   CREATE DATABASE movie_ticket WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE movie_ticket;
             django    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            R	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    5            S	           0    0    public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    5            �            3079    11793    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            T	           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    227            �            1259    70082 
   auth_group    TABLE     ^   CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.auth_group;
       public         django    false    5            �            1259    70080    auth_group_id_seq    SEQUENCE     s   CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       django    false    175    5            U	           0    0    auth_group_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;
            public       django    false    174            �            1259    70067    auth_group_permissions    TABLE     �   CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         django    false    5            �            1259    70065    auth_group_permissions_id_seq    SEQUENCE        CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       django    false    5    173            V	           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;
            public       django    false    172            �            1259    70057    auth_permission    TABLE     �   CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         django    false    5            �            1259    70055    auth_permission_id_seq    SEQUENCE     x   CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       django    false    5    171            W	           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;
            public       django    false    170            �            1259    70127 	   auth_user    TABLE     �  CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         django    false    5            �            1259    70097    auth_user_groups    TABLE     x   CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         django    false    5            �            1259    70095    auth_user_groups_id_seq    SEQUENCE     y   CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       django    false    177    5            X	           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;
            public       django    false    176            �            1259    70125    auth_user_id_seq    SEQUENCE     r   CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       django    false    5    181            Y	           0    0    auth_user_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;
            public       django    false    180            �            1259    70112    auth_user_user_permissions    TABLE     �   CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         django    false    5            �            1259    70110 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       django    false    179    5            Z	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;
            public       django    false    178            �            1259    71722    django_admin_log    TABLE     �  CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         django    false    5            �            1259    71720    django_admin_log_id_seq    SEQUENCE     y   CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       django    false    214    5            [	           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;
            public       django    false    213            �            1259    70152    django_content_type    TABLE     �   CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         django    false    5            �            1259    70150    django_content_type_id_seq    SEQUENCE     |   CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       django    false    183    5            \	           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;
            public       django    false    182            �            1259    71764    django_flatpage    TABLE     -  CREATE TABLE django_flatpage (
    id integer NOT NULL,
    url character varying(100) NOT NULL,
    title character varying(200) NOT NULL,
    content text NOT NULL,
    enable_comments boolean NOT NULL,
    template_name character varying(70) NOT NULL,
    registration_required boolean NOT NULL
);
 #   DROP TABLE public.django_flatpage;
       public         django    false    5            �            1259    71762    django_flatpage_id_seq    SEQUENCE     x   CREATE SEQUENCE django_flatpage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.django_flatpage_id_seq;
       public       django    false    220    5            ]	           0    0    django_flatpage_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE django_flatpage_id_seq OWNED BY django_flatpage.id;
            public       django    false    219            �            1259    71749    django_flatpage_sites    TABLE     �   CREATE TABLE django_flatpage_sites (
    id integer NOT NULL,
    flatpage_id integer NOT NULL,
    site_id integer NOT NULL
);
 )   DROP TABLE public.django_flatpage_sites;
       public         django    false    5            �            1259    71747    django_flatpage_sites_id_seq    SEQUENCE     ~   CREATE SEQUENCE django_flatpage_sites_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.django_flatpage_sites_id_seq;
       public       django    false    5    218            ^	           0    0    django_flatpage_sites_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE django_flatpage_sites_id_seq OWNED BY django_flatpage_sites.id;
            public       django    false    217            �            1259    70170    django_session    TABLE     �   CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         django    false    5            �            1259    71741    django_site    TABLE     �   CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);
    DROP TABLE public.django_site;
       public         django    false    5            �            1259    71739    django_site_id_seq    SEQUENCE     t   CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.django_site_id_seq;
       public       django    false    216    5            _	           0    0    django_site_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;
            public       django    false    215            �            1259    71365    facility_cinemaroom    TABLE     �   CREATE TABLE facility_cinemaroom (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    total_row integer NOT NULL,
    total_column integer NOT NULL,
    theater_id integer NOT NULL
);
 '   DROP TABLE public.facility_cinemaroom;
       public         django    false    5            �            1259    71363    facility_cinemaroom_id_seq    SEQUENCE     |   CREATE SEQUENCE facility_cinemaroom_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.facility_cinemaroom_id_seq;
       public       django    false    5    190            `	           0    0    facility_cinemaroom_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE facility_cinemaroom_id_seq OWNED BY facility_cinemaroom.id;
            public       django    false    189            �            1259    70557    facility_movietheater    TABLE     0  CREATE TABLE facility_movietheater (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    address character varying(255) NOT NULL,
    open_time time without time zone NOT NULL,
    close_time time without time zone NOT NULL,
    latitude numeric(11,6),
    longtitude numeric(11,6)
);
 )   DROP TABLE public.facility_movietheater;
       public         django    false    5            �            1259    70555    facility_movietheater_id_seq    SEQUENCE     ~   CREATE SEQUENCE facility_movietheater_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.facility_movietheater_id_seq;
       public       django    false    188    5            a	           0    0    facility_movietheater_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE facility_movietheater_id_seq OWNED BY facility_movietheater.id;
            public       django    false    187            �            1259    71441    movie_actor    TABLE     `   CREATE TABLE movie_actor (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);
    DROP TABLE public.movie_actor;
       public         django    false    5            �            1259    71439    movie_actor_id_seq    SEQUENCE     t   CREATE SEQUENCE movie_actor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.movie_actor_id_seq;
       public       django    false    5    202            b	           0    0    movie_actor_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE movie_actor_id_seq OWNED BY movie_actor.id;
            public       django    false    201            �            1259    71449    movie_company    TABLE     b   CREATE TABLE movie_company (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);
 !   DROP TABLE public.movie_company;
       public         django    false    5            �            1259    71447    movie_company_id_seq    SEQUENCE     v   CREATE SEQUENCE movie_company_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.movie_company_id_seq;
       public       django    false    204    5            c	           0    0    movie_company_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE movie_company_id_seq OWNED BY movie_company.id;
            public       django    false    203            �            1259    71385    movie_director    TABLE     c   CREATE TABLE movie_director (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);
 "   DROP TABLE public.movie_director;
       public         django    false    5            �            1259    71383    movie_director_id_seq    SEQUENCE     w   CREATE SEQUENCE movie_director_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.movie_director_id_seq;
       public       django    false    192    5            d	           0    0    movie_director_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE movie_director_id_seq OWNED BY movie_director.id;
            public       django    false    191            �            1259    71433    movie_genre    TABLE     _   CREATE TABLE movie_genre (
    id integer NOT NULL,
    name character varying(30) NOT NULL
);
    DROP TABLE public.movie_genre;
       public         django    false    5            �            1259    71431    movie_genre_id_seq    SEQUENCE     t   CREATE SEQUENCE movie_genre_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.movie_genre_id_seq;
       public       django    false    5    200            e	           0    0    movie_genre_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE movie_genre_id_seq OWNED BY movie_genre.id;
            public       django    false    199            �            1259    71412    movie_movie    TABLE     l  CREATE TABLE movie_movie (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    trailer text NOT NULL,
    poster character varying(100) NOT NULL,
    summary text NOT NULL,
    length integer NOT NULL,
    company_id integer NOT NULL,
    "MPAA_id" integer NOT NULL,
    director_id integer NOT NULL,
    slug character varying(100) NOT NULL
);
    DROP TABLE public.movie_movie;
       public         django    false    5            �            1259    72107    movie_movie_actors    TABLE     {   CREATE TABLE movie_movie_actors (
    id integer NOT NULL,
    movie_id integer NOT NULL,
    actor_id integer NOT NULL
);
 &   DROP TABLE public.movie_movie_actors;
       public         django    false    5            �            1259    72105    movie_movie_actors_id_seq    SEQUENCE     {   CREATE SEQUENCE movie_movie_actors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.movie_movie_actors_id_seq;
       public       django    false    5    226            f	           0    0    movie_movie_actors_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE movie_movie_actors_id_seq OWNED BY movie_movie_actors.id;
            public       django    false    225            �            1259    71423    movie_movie_genre    TABLE     z   CREATE TABLE movie_movie_genre (
    id integer NOT NULL,
    movie_id integer NOT NULL,
    genre_id integer NOT NULL
);
 %   DROP TABLE public.movie_movie_genre;
       public         django    false    5            �            1259    71421    movie_movie_genre_id_seq    SEQUENCE     z   CREATE SEQUENCE movie_movie_genre_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.movie_movie_genre_id_seq;
       public       django    false    5    198            g	           0    0    movie_movie_genre_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE movie_movie_genre_id_seq OWNED BY movie_movie_genre.id;
            public       django    false    197            �            1259    71410    movie_movie_id_seq    SEQUENCE     t   CREATE SEQUENCE movie_movie_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.movie_movie_id_seq;
       public       django    false    196    5            h	           0    0    movie_movie_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE movie_movie_id_seq OWNED BY movie_movie.id;
            public       django    false    195            �            1259    71393 
   movie_mpaa    TABLE     �   CREATE TABLE movie_mpaa (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    meaning text NOT NULL,
    explanation text NOT NULL
);
    DROP TABLE public.movie_mpaa;
       public         django    false    5            �            1259    71391    movie_mpaa_id_seq    SEQUENCE     s   CREATE SEQUENCE movie_mpaa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.movie_mpaa_id_seq;
       public       django    false    194    5            i	           0    0    movie_mpaa_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE movie_mpaa_id_seq OWNED BY movie_mpaa.id;
            public       django    false    193            �            1259    71457    movie_presentation    TABLE     �   CREATE TABLE movie_presentation (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    slug character varying(20) NOT NULL
);
 &   DROP TABLE public.movie_presentation;
       public         django    false    5            �            1259    71455    movie_presentation_id_seq    SEQUENCE     {   CREATE SEQUENCE movie_presentation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.movie_presentation_id_seq;
       public       django    false    5    206            j	           0    0    movie_presentation_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE movie_presentation_id_seq OWNED BY movie_presentation.id;
            public       django    false    205            �            1259    72033    movie_version    TABLE     �   CREATE TABLE movie_version (
    id integer NOT NULL,
    begin_date date NOT NULL,
    end_date date NOT NULL,
    presentation_id integer NOT NULL,
    movie_id integer NOT NULL,
    slug character varying(110) NOT NULL
);
 !   DROP TABLE public.movie_version;
       public         django    false    5            �            1259    72031    movie_version_id_seq    SEQUENCE     v   CREATE SEQUENCE movie_version_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.movie_version_id_seq;
       public       django    false    224    5            k	           0    0    movie_version_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE movie_version_id_seq OWNED BY movie_version.id;
            public       django    false    223            �            1259    71829    news_new    TABLE     �   CREATE TABLE news_new (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    text text NOT NULL,
    image character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    slug character varying(50) NOT NULL
);
    DROP TABLE public.news_new;
       public         django    false    5            �            1259    71827    news_new_id_seq    SEQUENCE     q   CREATE SEQUENCE news_new_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.news_new_id_seq;
       public       django    false    222    5            l	           0    0    news_new_id_seq    SEQUENCE OWNED BY     5   ALTER SEQUENCE news_new_id_seq OWNED BY news_new.id;
            public       django    false    221            �            1259    70180    south_migrationhistory    TABLE     �   CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 *   DROP TABLE public.south_migrationhistory;
       public         django    false    5            �            1259    70178    south_migrationhistory_id_seq    SEQUENCE        CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.south_migrationhistory_id_seq;
       public       django    false    186    5            m	           0    0    south_migrationhistory_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;
            public       django    false    185            �            1259    71571    users_customuser    TABLE       CREATE TABLE users_customuser (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    email character varying(255) NOT NULL,
    name character varying(100) NOT NULL,
    address character varying(255) NOT NULL,
    card_id character varying(20) NOT NULL,
    tel character varying(20) NOT NULL,
    date_of_birth date,
    date_joined timestamp with time zone NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL
);
 $   DROP TABLE public.users_customuser;
       public         django    false    5            �            1259    71584    users_customuser_groups    TABLE     �   CREATE TABLE users_customuser_groups (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    group_id integer NOT NULL
);
 +   DROP TABLE public.users_customuser_groups;
       public         django    false    5            �            1259    71582    users_customuser_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE users_customuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.users_customuser_groups_id_seq;
       public       django    false    5    210            n	           0    0    users_customuser_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE users_customuser_groups_id_seq OWNED BY users_customuser_groups.id;
            public       django    false    209            �            1259    71569    users_customuser_id_seq    SEQUENCE     y   CREATE SEQUENCE users_customuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.users_customuser_id_seq;
       public       django    false    208    5            o	           0    0    users_customuser_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE users_customuser_id_seq OWNED BY users_customuser.id;
            public       django    false    207            �            1259    71594 !   users_customuser_user_permissions    TABLE     �   CREATE TABLE users_customuser_user_permissions (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    permission_id integer NOT NULL
);
 5   DROP TABLE public.users_customuser_user_permissions;
       public         django    false    5            �            1259    71592 (   users_customuser_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE users_customuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ?   DROP SEQUENCE public.users_customuser_user_permissions_id_seq;
       public       django    false    212    5            p	           0    0 (   users_customuser_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE users_customuser_user_permissions_id_seq OWNED BY users_customuser_user_permissions.id;
            public       django    false    211            �           2604    70085    id    DEFAULT     `   ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       django    false    174    175    175            �           2604    70070    id    DEFAULT     x   ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       django    false    173    172    173            �           2604    70060    id    DEFAULT     j   ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       django    false    171    170    171            �           2604    70130    id    DEFAULT     ^   ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       django    false    180    181    181            �           2604    70100    id    DEFAULT     l   ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       django    false    176    177    177            �           2604    70115    id    DEFAULT     �   ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       django    false    178    179    179                       2604    71725    id    DEFAULT     l   ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       django    false    213    214    214            �           2604    70155    id    DEFAULT     r   ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       django    false    183    182    183                       2604    71767    id    DEFAULT     j   ALTER TABLE ONLY django_flatpage ALTER COLUMN id SET DEFAULT nextval('django_flatpage_id_seq'::regclass);
 A   ALTER TABLE public.django_flatpage ALTER COLUMN id DROP DEFAULT;
       public       django    false    219    220    220                       2604    71752    id    DEFAULT     v   ALTER TABLE ONLY django_flatpage_sites ALTER COLUMN id SET DEFAULT nextval('django_flatpage_sites_id_seq'::regclass);
 G   ALTER TABLE public.django_flatpage_sites ALTER COLUMN id DROP DEFAULT;
       public       django    false    218    217    218                       2604    71744    id    DEFAULT     b   ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);
 =   ALTER TABLE public.django_site ALTER COLUMN id DROP DEFAULT;
       public       django    false    215    216    216                        2604    71368    id    DEFAULT     r   ALTER TABLE ONLY facility_cinemaroom ALTER COLUMN id SET DEFAULT nextval('facility_cinemaroom_id_seq'::regclass);
 E   ALTER TABLE public.facility_cinemaroom ALTER COLUMN id DROP DEFAULT;
       public       django    false    189    190    190            �           2604    70560    id    DEFAULT     v   ALTER TABLE ONLY facility_movietheater ALTER COLUMN id SET DEFAULT nextval('facility_movietheater_id_seq'::regclass);
 G   ALTER TABLE public.facility_movietheater ALTER COLUMN id DROP DEFAULT;
       public       django    false    188    187    188                       2604    71444    id    DEFAULT     b   ALTER TABLE ONLY movie_actor ALTER COLUMN id SET DEFAULT nextval('movie_actor_id_seq'::regclass);
 =   ALTER TABLE public.movie_actor ALTER COLUMN id DROP DEFAULT;
       public       django    false    201    202    202                       2604    71452    id    DEFAULT     f   ALTER TABLE ONLY movie_company ALTER COLUMN id SET DEFAULT nextval('movie_company_id_seq'::regclass);
 ?   ALTER TABLE public.movie_company ALTER COLUMN id DROP DEFAULT;
       public       django    false    203    204    204                       2604    71388    id    DEFAULT     h   ALTER TABLE ONLY movie_director ALTER COLUMN id SET DEFAULT nextval('movie_director_id_seq'::regclass);
 @   ALTER TABLE public.movie_director ALTER COLUMN id DROP DEFAULT;
       public       django    false    192    191    192                       2604    71436    id    DEFAULT     b   ALTER TABLE ONLY movie_genre ALTER COLUMN id SET DEFAULT nextval('movie_genre_id_seq'::regclass);
 =   ALTER TABLE public.movie_genre ALTER COLUMN id DROP DEFAULT;
       public       django    false    200    199    200                       2604    71415    id    DEFAULT     b   ALTER TABLE ONLY movie_movie ALTER COLUMN id SET DEFAULT nextval('movie_movie_id_seq'::regclass);
 =   ALTER TABLE public.movie_movie ALTER COLUMN id DROP DEFAULT;
       public       django    false    196    195    196                       2604    72110    id    DEFAULT     p   ALTER TABLE ONLY movie_movie_actors ALTER COLUMN id SET DEFAULT nextval('movie_movie_actors_id_seq'::regclass);
 D   ALTER TABLE public.movie_movie_actors ALTER COLUMN id DROP DEFAULT;
       public       django    false    225    226    226                       2604    71426    id    DEFAULT     n   ALTER TABLE ONLY movie_movie_genre ALTER COLUMN id SET DEFAULT nextval('movie_movie_genre_id_seq'::regclass);
 C   ALTER TABLE public.movie_movie_genre ALTER COLUMN id DROP DEFAULT;
       public       django    false    198    197    198                       2604    71396    id    DEFAULT     `   ALTER TABLE ONLY movie_mpaa ALTER COLUMN id SET DEFAULT nextval('movie_mpaa_id_seq'::regclass);
 <   ALTER TABLE public.movie_mpaa ALTER COLUMN id DROP DEFAULT;
       public       django    false    194    193    194                       2604    71460    id    DEFAULT     p   ALTER TABLE ONLY movie_presentation ALTER COLUMN id SET DEFAULT nextval('movie_presentation_id_seq'::regclass);
 D   ALTER TABLE public.movie_presentation ALTER COLUMN id DROP DEFAULT;
       public       django    false    206    205    206                       2604    72036    id    DEFAULT     f   ALTER TABLE ONLY movie_version ALTER COLUMN id SET DEFAULT nextval('movie_version_id_seq'::regclass);
 ?   ALTER TABLE public.movie_version ALTER COLUMN id DROP DEFAULT;
       public       django    false    224    223    224                       2604    71832    id    DEFAULT     \   ALTER TABLE ONLY news_new ALTER COLUMN id SET DEFAULT nextval('news_new_id_seq'::regclass);
 :   ALTER TABLE public.news_new ALTER COLUMN id DROP DEFAULT;
       public       django    false    221    222    222            �           2604    70183    id    DEFAULT     x   ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);
 H   ALTER TABLE public.south_migrationhistory ALTER COLUMN id DROP DEFAULT;
       public       django    false    186    185    186            	           2604    71574    id    DEFAULT     l   ALTER TABLE ONLY users_customuser ALTER COLUMN id SET DEFAULT nextval('users_customuser_id_seq'::regclass);
 B   ALTER TABLE public.users_customuser ALTER COLUMN id DROP DEFAULT;
       public       django    false    208    207    208            
           2604    71587    id    DEFAULT     z   ALTER TABLE ONLY users_customuser_groups ALTER COLUMN id SET DEFAULT nextval('users_customuser_groups_id_seq'::regclass);
 I   ALTER TABLE public.users_customuser_groups ALTER COLUMN id DROP DEFAULT;
       public       django    false    209    210    210                       2604    71597    id    DEFAULT     �   ALTER TABLE ONLY users_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('users_customuser_user_permissions_id_seq'::regclass);
 S   ALTER TABLE public.users_customuser_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       django    false    211    212    212            	          0    70082 
   auth_group 
   TABLE DATA               '   COPY auth_group (id, name) FROM stdin;
    public       django    false    175   O      q	           0    0    auth_group_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('auth_group_id_seq', 1, false);
            public       django    false    174            	          0    70067    auth_group_permissions 
   TABLE DATA               F   COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       django    false    173   2O      r	           0    0    auth_group_permissions_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);
            public       django    false    172            	          0    70057    auth_permission 
   TABLE DATA               G   COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       django    false    171   OO      s	           0    0    auth_permission_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_permission_id_seq', 72, true);
            public       django    false    170            	          0    70127 	   auth_user 
   TABLE DATA               �   COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       django    false    181   =R      	          0    70097    auth_user_groups 
   TABLE DATA               :   COPY auth_user_groups (id, user_id, group_id) FROM stdin;
    public       django    false    177   �R      t	           0    0    auth_user_groups_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);
            public       django    false    176            u	           0    0    auth_user_id_seq    SEQUENCE SET     7   SELECT pg_catalog.setval('auth_user_id_seq', 1, true);
            public       django    false    180            	          0    70112    auth_user_user_permissions 
   TABLE DATA               I   COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       django    false    179   S      v	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);
            public       django    false    178            @	          0    71722    django_admin_log 
   TABLE DATA               �   COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
    public       django    false    214   3S      w	           0    0    django_admin_log_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('django_admin_log_id_seq', 86, true);
            public       django    false    213            !	          0    70152    django_content_type 
   TABLE DATA               B   COPY django_content_type (id, name, app_label, model) FROM stdin;
    public       django    false    183    Z      x	           0    0    django_content_type_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('django_content_type_id_seq', 24, true);
            public       django    false    182            F	          0    71764    django_flatpage 
   TABLE DATA               r   COPY django_flatpage (id, url, title, content, enable_comments, template_name, registration_required) FROM stdin;
    public       django    false    220   �[      y	           0    0    django_flatpage_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('django_flatpage_id_seq', 2, true);
            public       django    false    219            D	          0    71749    django_flatpage_sites 
   TABLE DATA               B   COPY django_flatpage_sites (id, flatpage_id, site_id) FROM stdin;
    public       django    false    218   (\      z	           0    0    django_flatpage_sites_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('django_flatpage_sites_id_seq', 4, true);
            public       django    false    217            "	          0    70170    django_session 
   TABLE DATA               I   COPY django_session (session_key, session_data, expire_date) FROM stdin;
    public       django    false    184   O\      B	          0    71741    django_site 
   TABLE DATA               0   COPY django_site (id, domain, name) FROM stdin;
    public       django    false    216   ^      {	           0    0    django_site_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('django_site_id_seq', 1, true);
            public       django    false    215            (	          0    71365    facility_cinemaroom 
   TABLE DATA               U   COPY facility_cinemaroom (id, name, total_row, total_column, theater_id) FROM stdin;
    public       django    false    190   <^      |	           0    0    facility_cinemaroom_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('facility_cinemaroom_id_seq', 1, false);
            public       django    false    189            &	          0    70557    facility_movietheater 
   TABLE DATA               h   COPY facility_movietheater (id, name, address, open_time, close_time, latitude, longtitude) FROM stdin;
    public       django    false    188   Y^      }	           0    0    facility_movietheater_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('facility_movietheater_id_seq', 3, true);
            public       django    false    187            4	          0    71441    movie_actor 
   TABLE DATA               (   COPY movie_actor (id, name) FROM stdin;
    public       django    false    202   �^      ~	           0    0    movie_actor_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('movie_actor_id_seq', 6, true);
            public       django    false    201            6	          0    71449    movie_company 
   TABLE DATA               *   COPY movie_company (id, name) FROM stdin;
    public       django    false    204   7_      	           0    0    movie_company_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('movie_company_id_seq', 1, true);
            public       django    false    203            *	          0    71385    movie_director 
   TABLE DATA               +   COPY movie_director (id, name) FROM stdin;
    public       django    false    192   ]_      �	           0    0    movie_director_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('movie_director_id_seq', 2, true);
            public       django    false    191            2	          0    71433    movie_genre 
   TABLE DATA               (   COPY movie_genre (id, name) FROM stdin;
    public       django    false    200   �_      �	           0    0    movie_genre_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('movie_genre_id_seq', 14, true);
            public       django    false    199            .	          0    71412    movie_movie 
   TABLE DATA               t   COPY movie_movie (id, name, trailer, poster, summary, length, company_id, "MPAA_id", director_id, slug) FROM stdin;
    public       django    false    196   k`      L	          0    72107    movie_movie_actors 
   TABLE DATA               =   COPY movie_movie_actors (id, movie_id, actor_id) FROM stdin;
    public       django    false    226   �a      �	           0    0    movie_movie_actors_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('movie_movie_actors_id_seq', 12, true);
            public       django    false    225            0	          0    71423    movie_movie_genre 
   TABLE DATA               <   COPY movie_movie_genre (id, movie_id, genre_id) FROM stdin;
    public       django    false    198   �a      �	           0    0    movie_movie_genre_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('movie_movie_genre_id_seq', 18, true);
            public       django    false    197            �	           0    0    movie_movie_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('movie_movie_id_seq', 2, true);
            public       django    false    195            ,	          0    71393 
   movie_mpaa 
   TABLE DATA               =   COPY movie_mpaa (id, name, meaning, explanation) FROM stdin;
    public       django    false    194   7b      �	           0    0    movie_mpaa_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('movie_mpaa_id_seq', 5, true);
            public       django    false    193            8	          0    71457    movie_presentation 
   TABLE DATA               5   COPY movie_presentation (id, name, slug) FROM stdin;
    public       django    false    206   �c      �	           0    0    movie_presentation_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('movie_presentation_id_seq', 2, true);
            public       django    false    205            J	          0    72033    movie_version 
   TABLE DATA               [   COPY movie_version (id, begin_date, end_date, presentation_id, movie_id, slug) FROM stdin;
    public       django    false    224   #d      �	           0    0    movie_version_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('movie_version_id_seq', 9, true);
            public       django    false    223            H	          0    71829    news_new 
   TABLE DATA               E   COPY news_new (id, title, text, image, created_at, slug) FROM stdin;
    public       django    false    222   �d      �	           0    0    news_new_id_seq    SEQUENCE SET     6   SELECT pg_catalog.setval('news_new_id_seq', 2, true);
            public       django    false    221            $	          0    70180    south_migrationhistory 
   TABLE DATA               K   COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
    public       django    false    186   �e      �	           0    0    south_migrationhistory_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('south_migrationhistory_id_seq', 27, true);
            public       django    false    185            :	          0    71571    users_customuser 
   TABLE DATA               �   COPY users_customuser (id, password, last_login, is_superuser, email, name, address, card_id, tel, date_of_birth, date_joined, is_staff, is_active) FROM stdin;
    public       django    false    208   Jh      <	          0    71584    users_customuser_groups 
   TABLE DATA               G   COPY users_customuser_groups (id, customuser_id, group_id) FROM stdin;
    public       django    false    210    i      �	           0    0    users_customuser_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('users_customuser_groups_id_seq', 1, false);
            public       django    false    209            �	           0    0    users_customuser_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('users_customuser_id_seq', 7, true);
            public       django    false    207            >	          0    71594 !   users_customuser_user_permissions 
   TABLE DATA               V   COPY users_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
    public       django    false    212   i      �	           0    0 (   users_customuser_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('users_customuser_user_permissions_id_seq', 1, false);
            public       django    false    211                        2606    70089    auth_group_name_key 
   CONSTRAINT     R   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         django    false    175    175                       2606    70074 1   auth_group_permissions_group_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);
 r   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_key;
       public         django    false    173    173    173                       2606    70072    auth_group_permissions_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         django    false    173    173            #           2606    70087    auth_group_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         django    false    175    175                       2606    70064 ,   auth_permission_content_type_id_codename_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);
 f   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_key;
       public         django    false    171    171    171                       2606    70062    auth_permission_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         django    false    171    171            &           2606    70102    auth_user_groups_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         django    false    177    177            )           2606    70104 %   auth_user_groups_user_id_group_id_key 
   CONSTRAINT     w   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);
 `   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_key;
       public         django    false    177    177    177            1           2606    70132    auth_user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         django    false    181    181            ,           2606    70117    auth_user_user_permissions_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         django    false    179    179            /           2606    70119 4   auth_user_user_permissions_user_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);
 y   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_key;
       public         django    false    179    179    179            3           2606    70134    auth_user_username_key 
   CONSTRAINT     X   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         django    false    181    181            q           2606    71731    django_admin_log_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         django    false    214    214            6           2606    70159 '   django_content_type_app_label_model_key 
   CONSTRAINT     {   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);
 e   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_key;
       public         django    false    183    183    183            8           2606    70157    django_content_type_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         django    false    183    183            |           2606    71772    django_flatpage_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY django_flatpage
    ADD CONSTRAINT django_flatpage_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.django_flatpage DROP CONSTRAINT django_flatpage_pkey;
       public         django    false    220    220            w           2606    71756 -   django_flatpage_sites_flatpage_id_site_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_flatpage_id_site_id_key UNIQUE (flatpage_id, site_id);
 m   ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT django_flatpage_sites_flatpage_id_site_id_key;
       public         django    false    218    218    218            y           2606    71754    django_flatpage_sites_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT django_flatpage_sites_pkey;
       public         django    false    218    218            ;           2606    70177    django_session_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         django    false    184    184            t           2606    71746    django_site_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.django_site DROP CONSTRAINT django_site_pkey;
       public         django    false    216    216            B           2606    71370    facility_cinemaroom_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY facility_cinemaroom
    ADD CONSTRAINT facility_cinemaroom_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.facility_cinemaroom DROP CONSTRAINT facility_cinemaroom_pkey;
       public         django    false    190    190            @           2606    70562    facility_movietheater_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY facility_movietheater
    ADD CONSTRAINT facility_movietheater_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.facility_movietheater DROP CONSTRAINT facility_movietheater_pkey;
       public         django    false    188    188            W           2606    71446    movie_actor_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY movie_actor
    ADD CONSTRAINT movie_actor_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.movie_actor DROP CONSTRAINT movie_actor_pkey;
       public         django    false    202    202            Y           2606    71454    movie_company_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY movie_company
    ADD CONSTRAINT movie_company_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.movie_company DROP CONSTRAINT movie_company_pkey;
       public         django    false    204    204            E           2606    71390    movie_director_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY movie_director
    ADD CONSTRAINT movie_director_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.movie_director DROP CONSTRAINT movie_director_pkey;
       public         django    false    192    192            U           2606    71438    movie_genre_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY movie_genre
    ADD CONSTRAINT movie_genre_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.movie_genre DROP CONSTRAINT movie_genre_pkey;
       public         django    false    200    200            �           2606    72114 1   movie_movie_actors_movie_id_2a1d75460d4477cd_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY movie_movie_actors
    ADD CONSTRAINT movie_movie_actors_movie_id_2a1d75460d4477cd_uniq UNIQUE (movie_id, actor_id);
 n   ALTER TABLE ONLY public.movie_movie_actors DROP CONSTRAINT movie_movie_actors_movie_id_2a1d75460d4477cd_uniq;
       public         django    false    226    226    226            �           2606    72112    movie_movie_actors_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY movie_movie_actors
    ADD CONSTRAINT movie_movie_actors_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.movie_movie_actors DROP CONSTRAINT movie_movie_actors_pkey;
       public         django    false    226    226            Q           2606    71430 0   movie_movie_genre_movie_id_4ddaa796d0e56877_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY movie_movie_genre
    ADD CONSTRAINT movie_movie_genre_movie_id_4ddaa796d0e56877_uniq UNIQUE (movie_id, genre_id);
 l   ALTER TABLE ONLY public.movie_movie_genre DROP CONSTRAINT movie_movie_genre_movie_id_4ddaa796d0e56877_uniq;
       public         django    false    198    198    198            S           2606    71428    movie_movie_genre_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY movie_movie_genre
    ADD CONSTRAINT movie_movie_genre_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.movie_movie_genre DROP CONSTRAINT movie_movie_genre_pkey;
       public         django    false    198    198            L           2606    71420    movie_movie_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY movie_movie
    ADD CONSTRAINT movie_movie_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.movie_movie DROP CONSTRAINT movie_movie_pkey;
       public         django    false    196    196            G           2606    71401    movie_mpaa_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY movie_mpaa
    ADD CONSTRAINT movie_mpaa_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.movie_mpaa DROP CONSTRAINT movie_mpaa_pkey;
       public         django    false    194    194            [           2606    71462    movie_presentation_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY movie_presentation
    ADD CONSTRAINT movie_presentation_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.movie_presentation DROP CONSTRAINT movie_presentation_pkey;
       public         django    false    206    206            �           2606    72038    movie_version_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY movie_version
    ADD CONSTRAINT movie_version_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.movie_version DROP CONSTRAINT movie_version_pkey;
       public         django    false    224    224            �           2606    72180    movie_version_slug_key 
   CONSTRAINT     X   ALTER TABLE ONLY movie_version
    ADD CONSTRAINT movie_version_slug_key UNIQUE (slug);
 N   ALTER TABLE ONLY public.movie_version DROP CONSTRAINT movie_version_slug_key;
       public         django    false    224    224            �           2606    71837    news_new_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY news_new
    ADD CONSTRAINT news_new_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.news_new DROP CONSTRAINT news_new_pkey;
       public         django    false    222    222            �           2606    71839    news_new_slug_key 
   CONSTRAINT     N   ALTER TABLE ONLY news_new
    ADD CONSTRAINT news_new_slug_key UNIQUE (slug);
 D   ALTER TABLE ONLY public.news_new DROP CONSTRAINT news_new_slug_key;
       public         django    false    222    222            >           2606    70188    south_migrationhistory_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.south_migrationhistory DROP CONSTRAINT south_migrationhistory_pkey;
       public         django    false    186    186            _           2606    71796    users_customuser_email_key 
   CONSTRAINT     `   ALTER TABLE ONLY users_customuser
    ADD CONSTRAINT users_customuser_email_key UNIQUE (email);
 U   ALTER TABLE ONLY public.users_customuser DROP CONSTRAINT users_customuser_email_key;
       public         django    false    208    208            e           2606    71591 ;   users_customuser_groups_customuser_id_3f6d7b3193d4318d_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_customuser_id_3f6d7b3193d4318d_uniq UNIQUE (customuser_id, group_id);
 }   ALTER TABLE ONLY public.users_customuser_groups DROP CONSTRAINT users_customuser_groups_customuser_id_3f6d7b3193d4318d_uniq;
       public         django    false    210    210    210            h           2606    71589    users_customuser_groups_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.users_customuser_groups DROP CONSTRAINT users_customuser_groups_pkey;
       public         django    false    210    210            b           2606    71579    users_customuser_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY users_customuser
    ADD CONSTRAINT users_customuser_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.users_customuser DROP CONSTRAINT users_customuser_pkey;
       public         django    false    208    208            j           2606    71601 ?   users_customuser_user_permi_customuser_id_36c9a899473ffb58_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_user_permi_customuser_id_36c9a899473ffb58_uniq UNIQUE (customuser_id, permission_id);
 �   ALTER TABLE ONLY public.users_customuser_user_permissions DROP CONSTRAINT users_customuser_user_permi_customuser_id_36c9a899473ffb58_uniq;
       public         django    false    212    212    212            n           2606    71599 &   users_customuser_user_permissions_pkey 
   CONSTRAINT        ALTER TABLE ONLY users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_user_permissions_pkey PRIMARY KEY (id);
 r   ALTER TABLE ONLY public.users_customuser_user_permissions DROP CONSTRAINT users_customuser_user_permissions_pkey;
       public         django    false    212    212            !           1259    70194    auth_group_name_like    INDEX     X   CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);
 (   DROP INDEX public.auth_group_name_like;
       public         django    false    175                       1259    70192    auth_group_permissions_group_id    INDEX     _   CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);
 3   DROP INDEX public.auth_group_permissions_group_id;
       public         django    false    173                       1259    70193 $   auth_group_permissions_permission_id    INDEX     i   CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);
 8   DROP INDEX public.auth_group_permissions_permission_id;
       public         django    false    173                       1259    70191    auth_permission_content_type_id    INDEX     _   CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);
 3   DROP INDEX public.auth_permission_content_type_id;
       public         django    false    171            $           1259    70196    auth_user_groups_group_id    INDEX     S   CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);
 -   DROP INDEX public.auth_user_groups_group_id;
       public         django    false    177            '           1259    70195    auth_user_groups_user_id    INDEX     Q   CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);
 ,   DROP INDEX public.auth_user_groups_user_id;
       public         django    false    177            *           1259    70198 (   auth_user_user_permissions_permission_id    INDEX     q   CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);
 <   DROP INDEX public.auth_user_user_permissions_permission_id;
       public         django    false    179            -           1259    70197 "   auth_user_user_permissions_user_id    INDEX     e   CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);
 6   DROP INDEX public.auth_user_user_permissions_user_id;
       public         django    false    179            4           1259    70199    auth_user_username_like    INDEX     ^   CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);
 +   DROP INDEX public.auth_user_username_like;
       public         django    false    181            o           1259    71738     django_admin_log_content_type_id    INDEX     a   CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);
 4   DROP INDEX public.django_admin_log_content_type_id;
       public         django    false    214            r           1259    71737    django_admin_log_user_id    INDEX     Q   CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);
 ,   DROP INDEX public.django_admin_log_user_id;
       public         django    false    214            u           1259    71778 !   django_flatpage_sites_flatpage_id    INDEX     c   CREATE INDEX django_flatpage_sites_flatpage_id ON django_flatpage_sites USING btree (flatpage_id);
 5   DROP INDEX public.django_flatpage_sites_flatpage_id;
       public         django    false    218            z           1259    71779    django_flatpage_sites_site_id    INDEX     [   CREATE INDEX django_flatpage_sites_site_id ON django_flatpage_sites USING btree (site_id);
 1   DROP INDEX public.django_flatpage_sites_site_id;
       public         django    false    218            }           1259    71780    django_flatpage_url    INDEX     G   CREATE INDEX django_flatpage_url ON django_flatpage USING btree (url);
 '   DROP INDEX public.django_flatpage_url;
       public         django    false    220            ~           1259    71781    django_flatpage_url_like    INDEX     `   CREATE INDEX django_flatpage_url_like ON django_flatpage USING btree (url varchar_pattern_ops);
 ,   DROP INDEX public.django_flatpage_url_like;
       public         django    false    220            9           1259    70201    django_session_expire_date    INDEX     U   CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);
 .   DROP INDEX public.django_session_expire_date;
       public         django    false    184            <           1259    70200    django_session_session_key_like    INDEX     n   CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);
 3   DROP INDEX public.django_session_session_key_like;
       public         django    false    184            C           1259    71376    facility_cinemaroom_theater_id    INDEX     ]   CREATE INDEX facility_cinemaroom_theater_id ON facility_cinemaroom USING btree (theater_id);
 2   DROP INDEX public.facility_cinemaroom_theater_id;
       public         django    false    190            H           1259    71486    movie_movie_MPAA_id    INDEX     K   CREATE INDEX "movie_movie_MPAA_id" ON movie_movie USING btree ("MPAA_id");
 )   DROP INDEX public."movie_movie_MPAA_id";
       public         django    false    196            �           1259    72132    movie_movie_actors_actor_id    INDEX     W   CREATE INDEX movie_movie_actors_actor_id ON movie_movie_actors USING btree (actor_id);
 /   DROP INDEX public.movie_movie_actors_actor_id;
       public         django    false    226            �           1259    72126    movie_movie_actors_movie_id    INDEX     W   CREATE INDEX movie_movie_actors_movie_id ON movie_movie_actors USING btree (movie_id);
 /   DROP INDEX public.movie_movie_actors_movie_id;
       public         django    false    226            I           1259    71480    movie_movie_company_id    INDEX     M   CREATE INDEX movie_movie_company_id ON movie_movie USING btree (company_id);
 *   DROP INDEX public.movie_movie_company_id;
       public         django    false    196            J           1259    72120    movie_movie_director_id    INDEX     O   CREATE INDEX movie_movie_director_id ON movie_movie USING btree (director_id);
 +   DROP INDEX public.movie_movie_director_id;
       public         django    false    196            N           1259    71498    movie_movie_genre_genre_id    INDEX     U   CREATE INDEX movie_movie_genre_genre_id ON movie_movie_genre USING btree (genre_id);
 .   DROP INDEX public.movie_movie_genre_genre_id;
       public         django    false    198            O           1259    71492    movie_movie_genre_movie_id    INDEX     U   CREATE INDEX movie_movie_genre_movie_id ON movie_movie_genre USING btree (movie_id);
 .   DROP INDEX public.movie_movie_genre_movie_id;
       public         django    false    198            M           1259    72160    movie_movie_slug_like    INDEX     Z   CREATE INDEX movie_movie_slug_like ON movie_movie USING btree (slug varchar_pattern_ops);
 )   DROP INDEX public.movie_movie_slug_like;
       public         django    false    196            \           1259    72161    movie_presentation_slug    INDEX     O   CREATE INDEX movie_presentation_slug ON movie_presentation USING btree (slug);
 +   DROP INDEX public.movie_presentation_slug;
       public         django    false    206            ]           1259    72162    movie_presentation_slug_like    INDEX     h   CREATE INDEX movie_presentation_slug_like ON movie_presentation USING btree (slug varchar_pattern_ops);
 0   DROP INDEX public.movie_presentation_slug_like;
       public         django    false    206            �           1259    72050    movie_version_movie_id    INDEX     M   CREATE INDEX movie_version_movie_id ON movie_version USING btree (movie_id);
 *   DROP INDEX public.movie_version_movie_id;
       public         django    false    224            �           1259    72044    movie_version_presentation_id    INDEX     [   CREATE INDEX movie_version_presentation_id ON movie_version USING btree (presentation_id);
 1   DROP INDEX public.movie_version_presentation_id;
       public         django    false    224            �           1259    72181    movie_version_slug_like    INDEX     ^   CREATE INDEX movie_version_slug_like ON movie_version USING btree (slug varchar_pattern_ops);
 +   DROP INDEX public.movie_version_slug_like;
       public         django    false    224            �           1259    71840    news_new_slug_like    INDEX     T   CREATE INDEX news_new_slug_like ON news_new USING btree (slug varchar_pattern_ops);
 &   DROP INDEX public.news_new_slug_like;
       public         django    false    222            `           1259    71797    users_customuser_email_like    INDEX     f   CREATE INDEX users_customuser_email_like ON users_customuser USING btree (email varchar_pattern_ops);
 /   DROP INDEX public.users_customuser_email_like;
       public         django    false    208            c           1259    71614 %   users_customuser_groups_customuser_id    INDEX     k   CREATE INDEX users_customuser_groups_customuser_id ON users_customuser_groups USING btree (customuser_id);
 9   DROP INDEX public.users_customuser_groups_customuser_id;
       public         django    false    210            f           1259    71620     users_customuser_groups_group_id    INDEX     a   CREATE INDEX users_customuser_groups_group_id ON users_customuser_groups USING btree (group_id);
 4   DROP INDEX public.users_customuser_groups_group_id;
       public         django    false    210            k           1259    71626 /   users_customuser_user_permissions_customuser_id    INDEX        CREATE INDEX users_customuser_user_permissions_customuser_id ON users_customuser_user_permissions USING btree (customuser_id);
 C   DROP INDEX public.users_customuser_user_permissions_customuser_id;
       public         django    false    212            l           1259    71632 /   users_customuser_user_permissions_permission_id    INDEX        CREATE INDEX users_customuser_user_permissions_permission_id ON users_customuser_user_permissions USING btree (permission_id);
 C   DROP INDEX public.users_customuser_user_permissions_permission_id;
       public         django    false    212            �           2606    71481    MPAA_id_refs_id_f8806c2b    FK CONSTRAINT     �   ALTER TABLE ONLY movie_movie
    ADD CONSTRAINT "MPAA_id_refs_id_f8806c2b" FOREIGN KEY ("MPAA_id") REFERENCES movie_mpaa(id) DEFERRABLE INITIALLY DEFERRED;
 P   ALTER TABLE ONLY public.movie_movie DROP CONSTRAINT "MPAA_id_refs_id_f8806c2b";
       public       django    false    194    2119    196            �           2606    72127    actor_id_refs_id_b0eb962b    FK CONSTRAINT     �   ALTER TABLE ONLY movie_movie_actors
    ADD CONSTRAINT actor_id_refs_id_b0eb962b FOREIGN KEY (actor_id) REFERENCES movie_actor(id) DEFERRABLE INITIALLY DEFERRED;
 V   ALTER TABLE ONLY public.movie_movie_actors DROP CONSTRAINT actor_id_refs_id_b0eb962b;
       public       django    false    2135    226    202            �           2606    70075 )   auth_group_permissions_permission_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_permission_id_fkey;
       public       django    false    2072    171    173            �           2606    70105    auth_user_groups_group_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 Y   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_fkey;
       public       django    false    2083    175    177            �           2606    70120 -   auth_user_user_permissions_permission_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_permission_id_fkey;
       public       django    false    2072    179    171            �           2606    71475    company_id_refs_id_e48999ad    FK CONSTRAINT     �   ALTER TABLE ONLY movie_movie
    ADD CONSTRAINT company_id_refs_id_e48999ad FOREIGN KEY (company_id) REFERENCES movie_company(id) DEFERRABLE INITIALLY DEFERRED;
 Q   ALTER TABLE ONLY public.movie_movie DROP CONSTRAINT company_id_refs_id_e48999ad;
       public       django    false    204    2137    196            �           2606    70165     content_type_id_refs_id_d043b34a    FK CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 Z   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT content_type_id_refs_id_d043b34a;
       public       django    false    171    2104    183            �           2606    71621    customuser_id_refs_id_55fe159d    FK CONSTRAINT     �   ALTER TABLE ONLY users_customuser_user_permissions
    ADD CONSTRAINT customuser_id_refs_id_55fe159d FOREIGN KEY (customuser_id) REFERENCES users_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.users_customuser_user_permissions DROP CONSTRAINT customuser_id_refs_id_55fe159d;
       public       django    false    212    2146    208            �           2606    71609    customuser_id_refs_id_87477e43    FK CONSTRAINT     �   ALTER TABLE ONLY users_customuser_groups
    ADD CONSTRAINT customuser_id_refs_id_87477e43 FOREIGN KEY (customuser_id) REFERENCES users_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 `   ALTER TABLE ONLY public.users_customuser_groups DROP CONSTRAINT customuser_id_refs_id_87477e43;
       public       django    false    210    208    2146            �           2606    72115    director_id_refs_id_ed31528e    FK CONSTRAINT     �   ALTER TABLE ONLY movie_movie
    ADD CONSTRAINT director_id_refs_id_ed31528e FOREIGN KEY (director_id) REFERENCES movie_director(id) DEFERRABLE INITIALLY DEFERRED;
 R   ALTER TABLE ONLY public.movie_movie DROP CONSTRAINT director_id_refs_id_ed31528e;
       public       django    false    196    192    2117            �           2606    71732 %   django_admin_log_content_type_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 `   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_fkey;
       public       django    false    2104    214    183            �           2606    71757 "   django_flatpage_sites_site_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_site_id_fkey FOREIGN KEY (site_id) REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED;
 b   ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT django_flatpage_sites_site_id_fkey;
       public       django    false    218    2164    216            �           2606    71773    flatpage_id_refs_id_83cd0023    FK CONSTRAINT     �   ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT flatpage_id_refs_id_83cd0023 FOREIGN KEY (flatpage_id) REFERENCES django_flatpage(id) DEFERRABLE INITIALLY DEFERRED;
 \   ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT flatpage_id_refs_id_83cd0023;
       public       django    false    2172    220    218            �           2606    71493    genre_id_refs_id_9e1ad564    FK CONSTRAINT     �   ALTER TABLE ONLY movie_movie_genre
    ADD CONSTRAINT genre_id_refs_id_9e1ad564 FOREIGN KEY (genre_id) REFERENCES movie_genre(id) DEFERRABLE INITIALLY DEFERRED;
 U   ALTER TABLE ONLY public.movie_movie_genre DROP CONSTRAINT genre_id_refs_id_9e1ad564;
       public       django    false    198    2133    200            �           2606    71615    group_id_refs_id_6eb7a9ad    FK CONSTRAINT     �   ALTER TABLE ONLY users_customuser_groups
    ADD CONSTRAINT group_id_refs_id_6eb7a9ad FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 [   ALTER TABLE ONLY public.users_customuser_groups DROP CONSTRAINT group_id_refs_id_6eb7a9ad;
       public       django    false    210    2083    175            �           2606    70090    group_id_refs_id_f4b32aac    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 Z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT group_id_refs_id_f4b32aac;
       public       django    false    2083    173    175            �           2606    72121    movie_id_refs_id_95d7c7a5    FK CONSTRAINT     �   ALTER TABLE ONLY movie_movie_actors
    ADD CONSTRAINT movie_id_refs_id_95d7c7a5 FOREIGN KEY (movie_id) REFERENCES movie_movie(id) DEFERRABLE INITIALLY DEFERRED;
 V   ALTER TABLE ONLY public.movie_movie_actors DROP CONSTRAINT movie_id_refs_id_95d7c7a5;
       public       django    false    226    196    2124            �           2606    71487    movie_id_refs_id_e0cba9f0    FK CONSTRAINT     �   ALTER TABLE ONLY movie_movie_genre
    ADD CONSTRAINT movie_id_refs_id_e0cba9f0 FOREIGN KEY (movie_id) REFERENCES movie_movie(id) DEFERRABLE INITIALLY DEFERRED;
 U   ALTER TABLE ONLY public.movie_movie_genre DROP CONSTRAINT movie_id_refs_id_e0cba9f0;
       public       django    false    198    2124    196            �           2606    72045    movie_id_refs_id_f737606f    FK CONSTRAINT     �   ALTER TABLE ONLY movie_version
    ADD CONSTRAINT movie_id_refs_id_f737606f FOREIGN KEY (movie_id) REFERENCES movie_movie(id) DEFERRABLE INITIALLY DEFERRED;
 Q   ALTER TABLE ONLY public.movie_version DROP CONSTRAINT movie_id_refs_id_f737606f;
       public       django    false    196    2124    224            �           2606    71627    permission_id_refs_id_26b8f05c    FK CONSTRAINT     �   ALTER TABLE ONLY users_customuser_user_permissions
    ADD CONSTRAINT permission_id_refs_id_26b8f05c FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.users_customuser_user_permissions DROP CONSTRAINT permission_id_refs_id_26b8f05c;
       public       django    false    2072    171    212            �           2606    72039     presentation_id_refs_id_db905b69    FK CONSTRAINT     �   ALTER TABLE ONLY movie_version
    ADD CONSTRAINT presentation_id_refs_id_db905b69 FOREIGN KEY (presentation_id) REFERENCES movie_presentation(id) DEFERRABLE INITIALLY DEFERRED;
 X   ALTER TABLE ONLY public.movie_version DROP CONSTRAINT presentation_id_refs_id_db905b69;
       public       django    false    2139    206    224            �           2606    71371    theater_id_refs_id_19b90acf    FK CONSTRAINT     �   ALTER TABLE ONLY facility_cinemaroom
    ADD CONSTRAINT theater_id_refs_id_19b90acf FOREIGN KEY (theater_id) REFERENCES facility_movietheater(id) DEFERRABLE INITIALLY DEFERRED;
 Y   ALTER TABLE ONLY public.facility_cinemaroom DROP CONSTRAINT theater_id_refs_id_19b90acf;
       public       django    false    190    188    2112            �           2606    70140    user_id_refs_id_40c41112    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 S   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT user_id_refs_id_40c41112;
       public       django    false    181    177    2097            �           2606    70145    user_id_refs_id_4dc23c39    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ]   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT user_id_refs_id_4dc23c39;
       public       django    false    179    181    2097            	      x������ � �      	      x������ � �      	   �  x�u�=��0�k�<A`�׮7H�e�@���E	��d� }��ҤN�-Rl.⛄"������7xciޓ%{h�hv;q��B�ixb���'{vG�9d{h�^ʗ�;p��j��/%����Z=��3,s���K�K@Fl��	ڈ���~�N=˝���k�n��'6X) �	�G�mg&�����+V:(�.,��A��%_�0�8ɨ���p��$�#�ƺ	Ɉm�\��C3٢8�q���N8̳֡��^�r�)�P�:a���,�ٝ��A5����8נĳ�̷��l�� s-:�L��L��j1t]�6~_\e.�"�Bа-��ɲ:�
��q���������\yw(3(�m� K.�ġ�
�/����(������B��z�i�����kbR�sھ16fH ���]$���.��U����g���0�Ӫ�څ�9I�%s J�j��8�)�����;�3�k��AZ7,�'�$�3D�X���=X}��=���[f̥��F:�e�����k
	N�2�����4'})o�Kk��A;_�$l�l����6uDJ�n�*�/H���8xA�3 8x��I�Bۓ��4�|(I�@�mĐԙ��ɈI��X�=_�X;�߁����>�HF�|l&�7{�x�΅��+�^ZB�e	
�	M>}�FL�-˼E���+bP��c�3R��oU򤲾����]����qg5��1�fp�5q�@)r�Q���}|�9���v�      	   �   x�-��
�@ ���-܅vg�W!��R� ����2M�i���?)n��1Q�{�S�R�9��'n�pܙmtj��r��S=�9��_�\���2�&2���
��P(�hY�z�GʱIK��>x�ő���<ʔ��L��Qz��}��_��-I=��y��	�_all�0>�T1^      	      x������ � �      	      x������ � �      @	   �  x����n�D��%�SuN]�e�A\F��`�4r:&mᶣ��MlX �K�7!$�H�f7Y��&��n��r'P�������uꯈ��\Ʉȸ�@�J!8�
7	& ��ɏ���;8`�/�`���ْ����_s�(ח_ՉHf�ϔN�0$׫�۪a������]����8��&$���>-N�ŪJgr�/3�2�t�r�G)����8���Q�ʐܙ7u����7˫?jF�_���^����TK%��J �{X|̚���� S��C@ ڏ�`�(��h9��<*k��a���(�P����� �J�=C�؏m��3m��AL����e@�4F �;�Ti�BN ߃�hR)�q�^�������d�R˥3�:  =D�@��`��ݴq;�Mf`&]&d�8e{ vz�#@�!I  ��nM��{/�v{Z���Cr�<-ۼ
'���Rn����Dv�kW?��������� �)(0���V=��:����E�`��۹�ʹ#3^��d�Փ���A�v�_�{�y]| &a�n	E�~Z����#E��;��T�:_����Jgс���3m-uJn]u��H� �{�3��1B
����[O��I�����dB_��'@�T8kL�a������fI���x�ȄJiC��w�]Z���s�zS���a����N���'!�_U{5��r�6�-@��b���k��"_Um���j��� ��L�kկ:�E$��l��������Ů NPՔF������.W�J	&����^ �@=��7J:S'�˯ۃ I� 5��<Zy�]\����$ڻ�j�M�֗O�*3�ΔJ�zF���hr�}3g�侬Y���͞ȉ���S�T���������s�!Mt���>����aO�P?����:_?�5�UN�c�e����A�ZC=�l�� N�c3.S)A��j%��Q�J�T]԰��e���r�2fB�$؃5��۲�8)X^�GS�n>)�詤�������AYT'�l�'�H��j�H��OicD��aQ����������8:m\W�G�-f�x$	��9A?�?%��3~b�"�qN�N����oK�"+�m.c����Ee]W�45|+���yQ���1���9�(�*	��^�{/T�P�Pf������j���i����]�J]�?ؒa��i�N����-��U���)tru{��[ͤ�*��۫���O~��ؾP�b~�:Og��Dh�C�ڊ.���ՠp^]�/�<]aN�k�6�MP�P���P�fW]�~�[	�%6���xp;��&=6�پ�=�Mn�Q�!�In�����KN���ǽ����E�S4c{�{�S�"��Vw�	�{{u1j�EQ�7�ԫ�S4�\b�U��Ո���,n@}��
�m�8�x]m�}1x�8-��'y���E}>ҙٱ�*D�<J'�t9����9���|�w�ҩw�j��+������њ>�����dE��*ܒ�S��Gz!��R��_�s�v/wA�Υ`"�!���|YR�m>�$P6�(<��]X͇�E����)s-|�	�͸)
!�)
Y����3J���<)Vo�5�9{x�#�%��,jv=�?��ᚳ��>�ӻ�v�{��I��*dc;��>�`,Nu׏����#Tt���O��|
��@Ṭ���)��CEsVԏ�r;�y՜�4�M����o���麟��_~d�`      !	   _  x�MQ;R�0�wO�0��!�p ��4G�wƒ<�p��s�CCM��"�	���4��ޮvWOS1���Al���Zi9GF��|}�q�5];�	�J�}��|��3��]\��S�|�3�[PTY�f59o�V��=˸e�$������N�Ԑ�'9�x%i��ƨ��I��l����3��C��J��Oߺ
bn>4{�����ҨV�y4�4���K�(Þ�����M%9�%+��"�8�5+k����5�\�Z�i��ȗ�����
��SD�蜴��.�"�b��w%h��b�b��L����]#<kE%��]ť����j�01��Jf�t���-�n      F	   �   x�3��OL�/-��{��Q!/���\�����7&+dd>�ݞ�ydB��y
!Eww�e��޼t ]
$uuuL��M8�89Ӹ�8����J�����d^�� 4���1% VIQ~^����Cznbf�^r~.��=... ��A�      D	      x�3�4�4�2�4�1z\\\ I      "	   �  x���ˎ�@E����@��/��l2�c�n�ж�`�n�yL}L���+�����9:�7��+
��l����@Zs.�=��N٦fRH�$��ij�N�y+G���2�ϙ^YQ	�2�O"�~�'�cB�.K�����,��#�Q�8���Of��Ц���z��p�|�~�&�~���#��iVE�L��+vy������=��� L�0y�"@^ b!ʿ!�g�ڃ=G���Ŷ�;�<���|�0��eFRNm
)Q�+=&N��S����t7�:�X>T�l��3'���D_���9��`/�S�2{��T�n�OC����7!�Χ*f�)���e��1(�(g:"��,�5�t�F��)��Y�s7��c��000"�=�����Y]!/���5�F�m��W8�U}t���qw~i�Q@`����װ������n      B	      x�3�L�H�-�I�K��Efs��qqq �<	�      (	      x������ � �      &	   Z   x�3�t��K�MT0�L)NK,NI+�40�20 "N0	b��[���r��ZXZ�s��q��APqZ
6���������� #�      4	   d   x�˱
�P�9�+��m�.b��]��K�C���z��R����n������Xq�y��{��ngX�~�)�m�:K��ŝ&)v�<� �A      6	      x�3�t�,�K������ �Y      *	   *   x�3��OJ-*Q.)���ҹ�8}���S���b���� ��
�      2	   �   x�U�;
AD��S�	���wA�Md{p? ��@��Pt5D��	G���Ğа��^���;gL����l��q�����&��R���!���=jl�\JE�����6��f�n��2��]�b��>E����)��;M+)�3*�$�U��ߕ��@4�R2�!���U�����j��U�R�	�C�आ�?a^L      .	   G  x�u�Mj�@���)t�ڮ���E)9@HH�H�Ŗm����8�9}�Z(t1�'���S��PQ�5���8��d�8\(��.H_�)��_��h��k�zz)��Q(��|(�OJ���O�%[��i��|%h����"D��`Ӣ��<��B k�4xB�7���=�4NpY�!k�^�$�S��8��y��I%�w��J�Ĺ�xc���qC>ۉ����\�ꈫw�Y��ޞv��@���K�L�/��`���h=�6�C �wh&؇�z�L`p��`[���++�,y��%B��X�rT!�垊[�-�3�J���,,�MV�y��ߵ}�N      L	   -   x���  ��w<"�e���|Β[��X�x�V�q�Wry�z�t      0	   (   x�34�B.C# e�eh�i�).Cτ+F��� qzW      ,	   �  x���Mo�0��� |�)�t(�[�CNk���B[�LԒ\Yj�?ʊ��f@��z��$�j�v�(� �I3��&��c��@�1�٧A�?��i1���|�w�s�j/��<h�T_�~��s�w�5
��"iU﯄i��܍�s}���w��(;��%�)�-2,�>��~�YU�\|e���>���߳����ߠ>�ô�-�Z�)q�v(�RW1�Zo�b��wf��Sd���'�?��%ij�cWI��q~�X,m�@�H��P�>m�&jq �i
���սzQ/���ݼ�m�T�:�7�������z�a�S�u�x�"┣_�}\�9�9c���GQ� ����]��e� ފT�0hF��W��]����Q&��m�=j˱���eq�����l0� ^+o�;`��4,�Eձ���q�)N      8	   "   x�3�t�L�,I��L��\���.��)\1z\\\ �N�      J	   d   x�M�A
� E��]&-����4P�r����y��#�$�(T���(H$�³�.6��t�שN;�
�۠����n��m�'�����5Ψ`� �1�$!      H	   �   x�e�Ak�0���W�[�7����C)l�,�"��1f�L���7.m��<x���Qt+�����6Ajh��d�Uh|1AB�Q�"���<�<}�%�yD�� �My<|`��NX��u�4������rz{��g��)����7\7�a��|.B2�V5u���X���֒��$� ݨj�FQ��M�'9�)˲X���p_Z�Z��Xb>q/���f��!&7Ki[߁�d����7e���>�[U�7k�h      $	   �  x����n�0��g����Fvb��,+!v�S$Z�ڷ�$�C2���J\ ����1�;�]� �������I@zzF~B��<�К��?����>t}7���� ���R�JV�2�UU7M��_�zn��>pe�b�* *���=��8�.�"�tHE�a����o�C�M�a�ό��z}{��s;��܍Cf)��Ƕ�=;�JX`�T.�E�J��z�^�������;?�|B�Y{���RA��ީ����`�r²5���s;��5,�Kƭ��&��T���y��<��{љ<ZaH1وB(r�W����yBOJ�5Φ��Μ��\��ux� �v5�崚L�:	��0��k�z���H��H�DS[Qn���	�j|�~u���A9��P ��R��i��w�0�]��Є�<����%~mV�X��0��B�#�K�¡Sr�H���FsQȻ
��q�cg���n���\��P�𥀆��⭖�J�aEW�v7mΗLՇ �Ҵ���1)��g�v��@�&,������Ƹ���7Q��@��`P�����'���@��&E�[�����]���r�@a��t5*�&T����2�<�g�B�d��t��̯Qw"8ipEm��ҺkT��͇�֬����C�l��f���Vm��н/m���:�̀ -��b�����G/      :	   �   x�3�,H�NI3�/�H425S14200P�v�q��*��J�R	/���sJ�w�M�6	�7w,�)/�2�q�tN2tɊ�0�)�̶t��4204�50�52T04�21�20�3�4144�60�,�,)*�Kw �z����! '�4!1AfZ��YYB������� �1      <	      x������ � �      >	      x������ � �     