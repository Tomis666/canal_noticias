-- Ejecutar SEGUNDO (después del DDL). Crea el usuario que usa la aplicación Python.
-- Es el mismo usuario/clave que trae el archivo .env.example

CREATE USER IF NOT EXISTS 'canal_noticias'@'localhost' IDENTIFIED BY 'canal2026';

-- Permisos SOLO sobre la base de datos del proyecto (no sobre todas)
GRANT ALL PRIVILEGES ON canal_noticias.* TO 'canal_noticias'@'localhost';

FLUSH PRIVILEGES;
