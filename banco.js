import 'dotenv/config';
import mysql from 'mysql2/promise';

async function main() {
  const connection = await mysql.createConnection({
    host: process.env.DB_HOST,
    port: Number(process.env.DB_PORT || 3306),
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
  });

  try {
    const [rows] = await connection.query('SELECT 1 AS ok');
    console.log(rows); // [ { ok: 1 } ]
  } finally {
    await connection.end();
  }
}

main().catch((err) => {
  console.error('Erro:', err.message || err);
  if (err.code === 'PROTOCOL_CONNECTION_LOST') {
    console.error('Failed to connect to MySQL. Check if MySQL is running and .env credentials are correct.');
  }
  process.exit(1);
});