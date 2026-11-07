-- Datos de prueba. Ejecutar TERCERO (después del DDL y del CREATE_USER).
-- Usuarios de prueba para iniciar sesión:
--   admin@canal.cl   / admin123   (Administrador)
--   carlos@canal.cl  / editor123  (Editor y autor)
USE canal_noticias;

INSERT INTO roles (nombre, permisos) VALUES
    ('Administrador', 'ALL'),
    ('Editor', 'EDICION');

INSERT INTO usuarios (nombre, correo, contrasena, id_rol) VALUES
    ('Administrador del Canal', 'admin@canal.cl',  'eb901367a7047e9a318cdc37f2fd0eab$e75951d47a7a7eb55c195b78396cbc8bee54c72303de70c8e5f6272e298453d9', 1),
    ('Carlos Mendoza',          'carlos@canal.cl', 'c93d302141f9f14dfc79480c9a8ffe44$55ee0928c12b2cb5a1300ca7810139ea3d404f438b2c60d3e24d300596c264da',  2);

INSERT INTO autores (biografia, id_usuario) VALUES
    ('Reportero de investigación con 10 años de experiencia.', 2);

INSERT INTO categorias (nombre) VALUES ('Política Nacional'), ('Deportes'), ('Economía'), ('Cultura');

INSERT INTO etiquetas (nombre) VALUES ('Última hora'), ('Congreso'), ('Fútbol'), ('Mundial');

INSERT INTO estados_articulo (estado) VALUES ('Borrador'), ('Publicado'), ('Archivado');

INSERT INTO articulos (titulo, contenido, fecha_publicacion, id_autor, id_categoria, id_estado) VALUES
    ('Histórica votación en el congreso aprueba reformas clave',
     'En una jornada intensa, los parlamentarios dieron luz verde al proyecto de ley...',
     CURDATE(), 1, 1, 2),
    ('La Roja clasifica al mundial después de más de una década de espera',
     'La selección logró el cupo en un partido que se definió en los minutos finales...',
     CURDATE(), 1, 2, 2),
    ('Nuevo informe económico proyecta crecimiento para el próximo año',
     'Borrador pendiente de revisión editorial...',
     CURDATE(), 1, 3, 1);

INSERT INTO articulos_etiquetas (id_articulo, id_etiqueta) VALUES (1, 1), (1, 2), (2, 1), (2, 3), (2, 4);

INSERT INTO lectores (nombre, correo) VALUES
    ('Ana Gómez',  'ana.gomez@gmail.com'),
    ('Juan Pérez', 'juan.perez@hotmail.com');

INSERT INTO planes (nombre, precio, duracion_dias) VALUES
    ('Gratuito', 0,      3650),
    ('Mensual',  4990,   30),
    ('Anual',    49990,  365);

INSERT INTO suscripciones (id_lector, id_plan, fecha_inicio, fecha_fin, estado) VALUES
    (1, 2, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 30 DAY), 'ACTIVA');

INSERT INTO comentarios (id_lector, id_articulo, fecha, contenido) VALUES
    (1, 1, CURDATE(), 'Por fin una buena noticia para el país.');

INSERT INTO likes (id_lector, id_articulo, fecha) VALUES (1, 1, CURDATE()), (2, 2, CURDATE());
